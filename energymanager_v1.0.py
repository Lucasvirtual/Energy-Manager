from tkinter import *
import subprocess
import win32api

janela = Tk()
janela.title("Energy Mananger")
janela.geometry("350x250")

def economia():
    # Define o plano de energia para Economia
    
    subprocess.run(["powercfg", "/setactive", "a1841308-3541-4fab-bc81-f71556f20b4a"])   
    labelAtual["text"] = "Modo de energia agora é: Economia"


def altodesempenho():
    # Define o plano de energia para Alto Desempenho
    
    subprocess.run(["powercfg", "/setactive", "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"])
    labelAtual["text"] = "Modo de energia agora é: Alto Desempenho"

def check_idle_time():
    return win32api.GetTickCount() - win32api.GetLastInputInfo()


def iniciar():
    janela.after(1000, check_idle)

def check_idle():
    idle_time = check_idle_time()

    if idle_time >= 5 * 1000: # Se o tempo de inatividade for igual ou superior a 5 segundos
        labelAtual.config(text="Modo Economia ativado")
        subprocess.run(["powercfg", "/setactive", "a1841308-3541-4fab-bc81-f71556f20b4a"])                  
        #labelInfo["text"] = subprocess.run(["powercfg", "/getactivescheme"])
        
    else:        
        labelAtual.config(text="Modo Alto Desempenho ativado")
        subprocess.run(["powercfg", "/setactive", "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"])
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
