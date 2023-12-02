# PRUEBAS - SPORT coach
import sys
import serial
import struct
import time
import threading
import sensors
import logging
from naoqi import ALProxy
from fin_movimientos_sportcoach import *

logging.basicConfig(level = logging.DEBUG, format = '[%(levelname)s] (%(threadName)-9s) %(message)s',)

# VERIFICANDO QUE LEA ECG:
# frec_cardiac = print("YO SOLITO", ecg.get_data())
edad_ingresada = 18
#FRECUENCIAS CARDIACAS MAXIMAS
#frec_cardiac = 90

#frec_cardiac_max = 208- (0.7*edad_ingresada)+35
frec_cardiac_max = 208- (0.7*edad_ingresada)
frec_cardiac_40 = (0.5*frec_cardiac_max)
frec_cardiac_70 = 0.7*frec_cardiac_max

tts = ALProxy("ALTextToSpeech", "192.168.1.100", 9559) # cambiar el ip adress
tts.say("Hola laura, bienvenida a la prueba")
#tts.say("Se que lo haras muy bien")
tts.say("3")
tts.say("2")
tts.say("1")
tts.say("ya!")
print("se que lo haras muy bien")
print("3")
print("2")
print("1")
print("ya!")

## PRUBAS ECG

class EcgSensor(sensors.sensor):
    def __init__(self, port = "/dev/rfcomm0",name_csv = "Ecg_Data.csv",sample = 1):
        super(EcgSensor, self).__init__(sample_time = sample,name = "Ecg-thread",header_file ="fid, fiv, hid, hiv, batt, hr, hbn, hbts1, hbts2, hbts3, hbts4, hbts5, hbts6, hbts7, hbts8, hbts9, hbts10, hbts11, hbts12, hbts13, hbts14, hbts15, distance, speed, strides",file_name = name_csv)
        #defining the serial port that will be used.
        self.__ser=serial.Serial(port, 115200, timeout=1)
        #Flag used to check the synchronization.
        self.__async=False
        #Variables used in the zephyr's serial protocol.
        self.__stx = struct.pack("<B", 0x02)
        self.__etx = struct.pack("<B", 0x02)
        self.__rate = struct.pack("<B", 0x26)
        self.__dlc_byte = struct.pack("<B", 55)
        #Array where the EKG data will be saved.
        self.__data_temp=[]
        #Flag that is used in case of pause.
        self.__pause=True
        self.sample_time=sample
        self.lock = threading.Lock()
        """
        *********************************************************************************************
        *********************************************************************************************
        *** Override of the [sensor]'s process method, in this case [process] is a controlled and ***
        *** infinite loop which interacts with the serial port that is assigned after linking the ***
        *** bluetooth devices.                                                                    ***
        *********************************************************************************************
        *********************************************************************************************
        """
    def process(self):
        while self.go_on:
            if not self.__pause:
                try:
                    d = self.__ser.read()
                    print(str(d))
                    if d != self.__stx:
                        if not self.__async:
                            print >>sys.stderr, "Not synched"
                            self.__async = True
                        continue

                    self.__async = False
                    type = self.__ser.read()    # Msg ID
                    if type != self.__rate:
                        print >>sys.stderr, "Unknown message type"
                    dlc = self.__ser.read()    # DLC
                    len, = struct.unpack("<B", dlc)
                    if len != 55:
                        print >>sys.stderr, "Bad DLC"
                    payload = self.__ser.read(len)
                    crc, = struct.unpack("<B", self.__ser.read())
                    end, = struct.unpack("<B", self.__ser.read())
                    sum = 0
                    #print "L: " + str(len)

                    for i in xrange(len):
                        b, = struct.unpack("<B", payload[i])
                        #print "Data: 0x%02x" % b
                        sum = (sum ^ b) & 0xff
                        for j in xrange(8):
                            if sum & 0x01:
                                sum = (sum >> 1) ^ 0x8c
                            else:
                                sum = (sum >> 1)
                    #print "CRC:  0x%02x" % crc
                    if crc != sum:
                        print >>sys.stderr, "Bad CRC: " + str(sum) + " is not " + str(crc)
                    else:
                        pass #print "CRC validated!"
                    if end != 0x03:
                        print >>sys.stderr, "Bad ETX"

                    #Saving data into the backup file.
                    with self.lock:
                        self.__data_temp=list(struct.unpack("<H2sH2sBBB15H6xHHB3x", payload))

                    self.val=reduce(lambda a,b:str(a)+','+str(b),self.__data_temp)+'\n'
                    self.load_data(self.val)
                    time.sleep(self.sample_time)
                except:
                    print("problems with ECG acquisition ")
                    pass
            else:
                time.sleep(1)
        """
        *********************************************************************************************
        *********************************************************************************************
        *** The [pause] method changes the [__pause] flag, which means that the thread will be    ***
        *** paused until the flag is changed to a False value.                                    ***
        *********************************************************************************************
        *********************************************************************************************
        """
    def pause(self):
        self.__pause=True
        """
        *********************************************************************************************
        *********************************************************************************************
        *** The [play] method changes the [__pause] flag, which means that the thread will run    ***
        *** until the flag is changed to a True value.
        *********************************************************************************************
        *********************************************************************************************
        """
    def play(self):
        self.__pause=False
        """
        *********************************************************************************************
        *********************************************************************************************
        *** The [close] method is used to close the serial port that is being used.               ***
        *********************************************************************************************
        *********************************************************************************************
        """
    def close(self):
        self.shutdown()
        self.__ser.close()
        """
        *********************************************************************************************
        *********************************************************************************************
        *** The [get_data] method is used to return the data collected by the Zephyr sensor.      ***
        *********************************************************************************************
        *********************************************************************************************
        """
    def get_data(self):
        return self.__data_temp

    def Sleep(self):
        self.pause()

    def WakeUp(self):
        self.play()
  


def verificar_hr():
    ecg = EcgSensor(port='COM10')    
    ecg.start() 
    ecg.play()
    datos = ecg.get_data()

    while len(datos)== 0:
        datos = ecg.get_data()

    #logging.debug(ecg.get_data())
    #datos = ecg.get_data()
    print("longitud", len(datos))
    frec_cardiac = datos[5]
    print("Frecuencia cardiaca:", frec_cardiac)
    ecg.shutdown()
    return frec_cardiac

def main_hr():
      
    frec_cardiac=verificar_hr()


    if (frec_cardiac < frec_cardiac_40):
        print("La actual", frec_cardiac)
        tts = ALProxy("ALTextToSpeech", "192.168.1.100", 9559) # cambiar el ip adress
        tts.say("Vamos a subir el ritmo")
        leds = ALProxy("ALLeds","192.168.1.100",9559)
        #leds = ALProxy("ALLeds","192.168.0.102",9559)
        leds.on("AllLedsBlue")

        
    elif (frec_cardiac > frec_cardiac_70):
        print("La actual", frec_cardiac)
        tts = ALProxy("ALTextToSpeech", "192.168.1.100", 9559) # cambiar el ip adress
        tts.say("Reduce el ritmo")
        leds = ALProxy("ALLeds","192.168.1.100",9559)
        #leds = ALProxy("ALLeds","192.168.0.102",9559)
        leds.off("AllLeds")

        #tts = ALProxy("ALTextToSpeech", "192.168.0.102", 9559) # cambiar el ip adress
        
        leds = ALProxy("ALLeds","192.168.1.100",9559)
        #leds = ALProxy("ALLeds","192.168.0.102",9559)
        leds.on("AllLedsRed")

        #try:
          #motion = ALProxy("ALMotion", "192.168.1.100", 9559)
          #motion = ALProxy("ALMotion", "192.168.0.102", 9559)
          #motion.angleInterpolation(names, keys, times, True)
        #  leds.on("AllLedsRed")
        #except BaseException, err:
        #  print err
        # --------------------------------------------------------------------------------------------------------
    else:
        print("La actual", frec_cardiac)
        tts = ALProxy("ALTextToSpeech", "192.168.1.100", 9559) # cambiar el ip adress
        tts.say("Continua asi, ZONA DE EJERCICIO")
        leds = ALProxy("ALLeds","192.168.1.100",9559)
        #leds = ALProxy("ALLeds","192.168.0.102",9559)
        leds.off("AllLeds")
        #tts = ALProxy("ALTextToSpeech", "192.168.1.100", 9559) # cambiar el ip adress
        #tts = ALProxy("ALTextToSpeech", "192.168.0.102", 9559) # cambiar el ip adress
        #tts.say("ZONA DE EJERCICIO")    
        leds = ALProxy("ALLeds","192.168.1.100",9559)
        #leds = ALProxy("ALLeds","192.168.0.102",9559)
        leds.on("AllLedsGreen")
        #leds.off()


