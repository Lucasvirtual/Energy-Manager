import winreg as rg
from tkinter import *
from tkinter import ttk
import winreg

def modoEnergia():
    rg.CreateKeyEx(rg.HKEY_LOCAL_MACHINE,r"SOFTWARE\Microsoft\Windows\CurrentVersion\explorer\ControlPanel\NameSpace\{6bff0ef8-7e5f-4252-a2fc-061dbb1a8571}")

print
    

janela = Tk()
janela.title("Energy Manager")
text_orientacao = Label(janela, text="Energy Manager")
janela.geometry("320x320")

listEnergia=["Economia","Alto desempenho"]

lb_energia=Label(text="Modo de energia atual")
lb_energia.pack()

cb_energia=ttk.Combobox(values=listEnergia)
cb_energia.set("")
cb_energia.pack()

path = winreg.HKEY_CURRENT_USER

software = winreg.OpenKeyEx(path, r"SOFTWARE\\")
new_key = winreg.CreateKey(software, "NeuralNine")


#--------------------------------------------#
listTempo=["1min","3min","5min","10min","15min","30min"]

lb_energia=Label(text="Tempo para mudar")
lb_energia.pack()

cb_energia=ttk.Combobox(values=listTempo)
cb_energia.set("1min")
cb_energia.pack()



#--------------------------------------------#
lb_energia=Label(text="Modo de Energia que irá mudar")
lb_energia.pack()

cb_energia=ttk.Combobox(values=listEnergia)
cb_energia.set("Economia")
cb_energia.pack()

#-----------------------------------------#

btnIniciar = Button(text = "Iniciar",command=modoEnergia) .place(x=130,y=140)




janela.mainloop()