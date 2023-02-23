from tkinter import *
import subprocess
import win32api

janela = Tk()
janela.title("Energy Mananger")
janela.geometry("350x250")

def economia():
    # Define o plano de energia para Economia
    
    subprocess.run(["powercfg", "/setactive", "a6230e07-0388-4a44-a49f-0389adfe16e6"])   
    labelAtual["text"] = "Modo de energia agora é: Economia"


def altodesempenho():
    # Define o plano de energia para Alto Desempenho
    
    subprocess.run(["powercfg", "/setactive", "fed2c136-42f5-4a5b-a02a-6e9d961aa6cd"])
    labelAtual["text"] = "Modo de energia agora é: Alto Desempenho"

def check_idle_time():
    return win32api.GetTickCount() - win32api.GetLastInputInfo()


def iniciar():
    janela.after(1000, check_idle)

def check_idle():
    idle_time = check_idle_time()

    if idle_time >= 600 * 1000: # Se o tempo de inatividade for igual ou superior a 5 segundos
        labelAtual.config(text="Modo Economia ativado")
        subprocess.run(["powercfg", "/setactive", "a6230e07-0388-4a44-a49f-0389adfe16e6"])                  
        #labelInfo["text"] = subprocess.run(["powercfg", "/getactivescheme"])
        
    else:        
        labelAtual.config(text="Modo Alto Desempenho ativado")
        subprocess.run(["powercfg", "/setactive", "fed2c136-42f5-4a5b-a02a-6e9d961aa6cd"])
        #labelInfo["text"] = subprocess.run(["powercfg", "/getactivescheme"])
    
    if not stop:
        janela.after(1000, check_idle)

def parar():
    global stop
    stop = True
    
stop = False    

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

janela.mainloop()