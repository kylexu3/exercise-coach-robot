import threading
from threading import *
from pruebas_1214 import *
from fin_movimientos_sportcoach import *
import time
from naoqi import ALProxy


def medir_hr():    
    main_hr()    

def movimientos():    
    global fase
    if(fase==1):
        lateralqnees()
    if(fase==2):
        lateralqnees()
    if(fase==3):
        lateralqnees()

def bloque_bm():
    medir_hr()
    t0=time.time()    
    t1=time.time()    
    while t1-t0 < 30:
        basicmarching()
        t1=time.time()

def bloque_su():
    medir_hr()
    t0=time.time()    
    t1=time.time()    
    while t1-t0 < 30:
        stepup()
        t1=time.time()

def bloque_lk():
    medir_hr()
    t0=time.time()    
    t1=time.time()    
    while t1-t0 < 30:
        lateralqnees()
        t1=time.time()

def bloque_baf():
    medir_hr()
    t0=time.time()    
    t1=time.time()    
    while t1-t0 < 30:
        botharms_forward()
        t1=time.time()

#FASE CALENTAMIENTO 
def f_calentamiento():    
    bloque_bm()
    bloque_bm()

    bloque_su()
    bloque_su()

#FASE ACONDICIONAMIENTO
def f_acondicionamiento():    
    bloque_bm()
    bloque_bm()

    bloque_lk()
    bloque_lk() 

    bloque_bm()
    bloque_bm()

    bloque_baf()
    bloque_baf()

    bloque_bm()
    bloque_bm()

    bloque_lk()
    bloque_lk() 

    bloque_bm()
    bloque_bm()

def f_enfriamiento():
    bloque_su()
    bloque_su()

    bloque_bm()
    bloque_bm()


def main(fase):
    if(fase==1):
        tts = ALProxy("ALTextToSpeech", "192.168.1.100", 9559) # cambiar el ip adress
        tts.say("Fase de calentamiento")
        print("CALENTAMIENTOOO**")
        f_calentamiento()
    if(fase==2):
        
        tts = ALProxy("ALTextToSpeech", "192.168.1.100", 9559) # cambiar el ip adress
        tts.say("Fase de acondicionamiento")
        print("ACONDICIONAMIENTO**")
        f_acondicionamiento()

    if(fase==3):
        
        tts = ALProxy("ALTextToSpeech", "192.168.1.100", 9559) # cambiar el ip adress
        tts.say("Fase de enfriamiento")
        print("ENFRIAMIENTO**")
        f_enfriamiento()
#for x in range(3):
main(3)



