import tkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
import subprocess
import time
from threading import Timer
import pyautogui
import mouse
import os
import ctypes
from ctypes import *
import win32api

pyautogui.position()

INACTIVE_TIME = 20

janela = Tk()
janela.title("Energy Mananger")
janela.geometry("350x250")



def economia():
    # Define o plano de energia para Economia
    
    subprocess.run(["powercfg", "/setactive", "a1841308-3541-4fab-bc81-f71556f20b4a"])   
    labelInfo["text"] = "Modo de energia agora é: Economia"


def altodesempenho():
    # Define o plano de energia para Alto Desempenho
    
    subprocess.run(["powercfg", "/setactive", "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"])
    labelInfo["text"] = "Modo de energia agora é: Alto Desempenho"

def check_idle_time():
    return win32api.GetTickCount() - win32api.GetLastInputInfo()




def iniciar():
    idle_time = 0
    while True:
        time.sleep(1)
        idle_time = check_idle_time()
        
        if idle_time >= 5 * 1000: # Se o tempo de inatividade for igual ou superior a 5 segundos
            subprocess.run(["powercfg", "/setactive", "a1841308-3541-4fab-bc81-f71556f20b4a"])                  
            labelInfo["text"] = subprocess.run(["powercfg", "/getactivescheme"])
        else:        
            subprocess.run(["powercfg", "/setactive", "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"])
            labelInfo["text"] = subprocess.run(["powercfg", "/getactivescheme"])
    

    


btntroca1 = Button(width=10, text="Economia", command=economia)
btntroca1.place(x=100, y=40)

btntroca3 = Button(width=20, text="Alto desempenho", command=altodesempenho )
btntroca3.place(x=100, y=70)

btnIniciar = Button(width=10, text="Iniciar", command=iniciar )
btnIniciar.place(x=100, y=170)

btnParar = Button(width=10, text="Parar" )
btnParar.place(x=190, y=170)

labelAtual = Label(text="Modo de energia atual:")
labelAtual.place(x=100, y=10)






labelInfo = Label(text="Modo de energia que irá mudar:")
labelInfo.place(x=100, y=220)


janela.mainloop()