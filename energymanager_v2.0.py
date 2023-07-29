import subprocess
import tkinter as tk
from tkinter import ttk
import win32api
import os
from bs4 import BeautifulSoup


janela = tk.Tk()
janela.title("Energy Manager")
janela.geometry("350x220")

def economia():
    subprocess.run(["powercfg", "/s", "a1841308-3541-4fab-bc81-f71556f20b4a"])
    labelAtual.config(text="Modo de energia agora é: Economia")

def altodesempenho():
    subprocess.run(["powercfg", "/s", "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"])
    labelAtual.config(text="Modo de energia agora é: Alto Desempenho")

def equilibrado():
    subprocess.run(["powercfg", "/s", "381b4222-f694-41f0-9685-ff5bb260df2e"])
    labelAtual.config(text="Modo de energia agora é: Equilibrado")

def check_idle_time():
    return win32api.GetTickCount() - win32api.GetLastInputInfo()

def iniciar():
    global stop
    stop = False
    janela.after(1000, check_idle)

def gerar_relatorio():
    # Obter o caminho da pasta "Downloads"
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

    # Gerar o caminho completo do arquivo HTML
    output_path = os.path.join(downloads_folder, "Relatorio de bateria.html")

    # Executar o comando powercfg para gerar o relatório em um arquivo HTML
    os.system(f'powercfg /batteryreport /output "{output_path}"')

    # Analisar o arquivo HTML gerado e obter as informações da bateria
    with open(output_path, "r") as file:
        content = file.read()
        soup = BeautifulSoup(content, "html.parser")

        # Encontrar a seção de informações da bateria no arquivo HTML
        battery_info = soup.find("div", {"id": "battery-report"})

def check_idle():
    if not stop:
        tempo_selecionado = tempos_combobox.get()  # Obter o tempo selecionado na combobox
        tempo_selecionado = int(tempo_selecionado.split()[0]) * 60 * 1000  # Converter minutos para milissegundos

        idle_time = check_idle_time()

        if idle_time >= tempo_selecionado:
            economia()
        else:
            altodesempenho()

        janela.after(1000, check_idle)

def parar():
    global stop
    stop = True

stop = False

btntroca1 = tk.Button(width=10, text="Economia", command=economia)
btntroca1.place(x=10, y=30)

btntroca3 = tk.Button(width=15, text="Alto desempenho", command=altodesempenho)
btntroca3.place(x=100, y=30)

btntroca4 = tk.Button(width=15, text="Equilibrado", command=equilibrado)
btntroca4.place(x=220, y=30)

btnIniciar = tk.Button(width=10, text="Iniciar", command=iniciar)
btnIniciar.place(x=90, y=150)

btnParar = tk.Button(width=10, text="Parar", command=parar)
btnParar.place(x=180, y=150)

btnParar = tk.Button( text="Relatório de bateria", command=gerar_relatorio)
btnParar.place(x=120, y=180)

# Label informativo
labelinfo = tk.Label(text="Sistema automático de troca de modo de energia \nModo desempenho para Economia")
labelinfo.place(x=40, y=80)

# Label topo
labelAtual = tk.Label(text="")
labelAtual.place(x=60, y=5)

# Combobox para escolher o tempo de ociosidade
tempos_combobox = ttk.Combobox(janela, values=["1 minuto", "5 minutos", "10 minutos"])
tempos_combobox.set("Selecione o tempo")
tempos_combobox.pack(pady=10)
tempos_combobox.place(x=100, y=120)

janela.mainloop()
