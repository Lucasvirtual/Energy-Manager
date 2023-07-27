from importlib.resources import path
import winreg as rg
from tkinter import *
from tkinter import ttk
import winreg
import time
import schedule

#-------------------------------------------------------------------#

janela = Tk()
janela.title("Energy Manager")
text_orientacao = Label(janela, text="Energy Manager")
janela.geometry("320x320")

#-------------------------------------------------------------------#

def modo_Atual():
    
    ativar = rg.OpenKey(rg.HKEY_LOCAL_MACHINE,r"SOFTWARE\Microsoft\Windows\CurrentVersion\explorer\ControlPanel\NameSpace\{a1841308-3541-4fab-bc81-f71556f20b4a}")
    print  ("Ola")
    
    

    



#listEnergia=["Economia","Alto desempenho"]

#lb_energia=Label(text="Modo de energia atual")
#lb_energia.pack()

#cb_energia=ttk.Combobox(values=listEnergia)
#cb_energia.set("")
#cb_energia.pack()#

#--------------------------------------------#
#listTempo=["1min","3min","5min","10min","15min","30min"]

#lb_energia=Label(text="Tempo para mudar")
#lb_energia.pack()

#cb_energia=ttk.Combobox(values=listTempo)
#cb_energia.set("1min")
#cb_energia.pack()

#--------------------------------------------#
#lb_energia=Label(text="Modo de Energia que irá mudar")
#lb_energia.pack()

#cb_energia=ttk.Combobox(values=listEnergia)
#cb_energia.set("Economia")
#cb_energia.pack()

#-----------------------------------------#

btnIniciar = Button(text = "Iniciar",  command = modo_Atual)
btnIniciar.place(x=130,y=140)

janela.mainloop()