# CLinica medica
import tkinter as tk
from tkinter import messagebox

class Pessoa:
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

class Paciente(Pessoa):
    def __init__(self, nome, cpf, telefone):
        super().__init__(nome, cpf, telefone)

class Medico(Pessoa):
    def __init__(self, nome, cpf, telefone):
        super().__init__(nome, cpf, telefone)

class Consulta:
    def __init__(self, medico, paciente, data, horario):
        self.medico = medico
        self.paciente = paciente
        self.data = data
        self.horario = horario

class Clinica:
    def __init__(self):
        self.medicos = {}
        self.pacientes = {}
        self.consultas = []

    def cadastrar_medico(self, medico):
        self.medicos[medico.cpf] = medico

    def cadastrar_paciente(self, paciente):
        self.pacientes[paciente.cpf] = paciente

    def agendar_consulta(self, cpf_medico, cpf_paciente, data, horario):
        if cpf_medico in self.medicos and cpf_paciente in self.pacientes:
            medico = self.medicos[cpf_medico]
            paciente = self.pacientes[cpf_paciente]
            consulta = Consulta(medico, paciente, data, horario)
            self.consultas.append(consulta)
            return True
        return False

# ---------------- GUI ----------------
clinica = Clinica()
root = tk.Tk()
root.title("Sistema da Clínica Médica")
root.geometry("400x400")

def cadastrar_medico():
    nome = entrada_medico_nome.get()
    cpf = entrada_medico_cpf.get()
    telefone = entrada_medico_telefone.get()
    if nome and cpf:
        clinica.cadastrar_medico(Medico(nome, cpf, telefone))
        messagebox.showinfo("Sucesso", "Médico cadastrado com sucesso!")
    else:
        messagebox.showwarning("Erro", "Nome e CPF são obrigatórios.")

def cadastrar_paciente():
    nome = entrada_paciente_nome.get()
    cpf = entrada_paciente_cpf.get()
    telefone = entrada_paciente_telefone.get()
    if nome and cpf:
        clinica.cadastrar_paciente(Paciente(nome, cpf, telefone))
        messagebox.showinfo("Sucesso", "Paciente cadastrado com sucesso!")
    else:
        messagebox.showwarning("Erro", "Nome e CPF são obrigatórios.")

def agendar_consulta():
    cpf_medico = entrada_consulta_medico.get()
    cpf_paciente = entrada_consulta_paciente.get()
    data = entrada_consulta_data.get()
    horario = entrada_consulta_horario.get()
    if clinica.agendar_consulta(cpf_medico, cpf_paciente, data, horario):
        messagebox.showinfo("Sucesso", "Consulta agendada com sucesso!")
    else:
        messagebox.showwarning("Erro", "Médico ou paciente não encontrado.")

def visualizar_consultas():
    janela_consultas = tk.Toplevel(root)
    janela_consultas.title("Consultas Agendadas")
    for consulta in clinica.consultas:
        tk.Label(
            janela_consultas,
            text=f"{consulta.data} {consulta.horario} - {consulta.paciente.nome} com {consulta.medico.nome}"
        ).pack()

# ---------------- Cadastro de Médicos ----------------
tk.Label(root, text="Cadastrar Médico").pack()
entrada_medico_nome = tk.Entry(root); entrada_medico_nome.pack(); entrada_medico_nome.insert(0,"Nome")
entrada_medico_cpf = tk.Entry(root); entrada_medico_cpf.pack(); entrada_medico_cpf.insert(0,"CPF")
entrada_medico_telefone = tk.Entry(root); entrada_medico_telefone.pack(); entrada_medico_telefone.insert(0,"Telefone")
tk.Button(root, text="Cadastrar Médico", command=cadastrar_medico).pack(pady=5)

# ---------------- Cadastro de Pacientes ----------------
tk.Label(root, text="Cadastrar Paciente").pack()
entrada_paciente_nome = tk.Entry(root); entrada_paciente_nome.pack(); entrada_paciente_nome.insert(0,"Nome")
entrada_paciente_cpf = tk.Entry(root); entrada_paciente_cpf.pack(); entrada_paciente_cpf.insert(0,"CPF")
entrada_paciente_telefone = tk.Entry(root); entrada_paciente_telefone.pack(); entrada_paciente_telefone.insert(0,"Telefone")
tk.Button(root, text="Cadastrar Paciente", command=cadastrar_paciente).pack(pady=5)

# ---------------- Agendamento de Consultas ----------------
tk.Label(root, text="Agendar Consulta").pack()
entrada_consulta_medico = tk.Entry(root); entrada_consulta_medico.pack(); entrada_consulta_medico.insert(0,"CPF do Médico")
entrada_consulta_paciente = tk.Entry(root); entrada_consulta_paciente.pack(); entrada_consulta_paciente.insert(0,"CPF do Paciente")
entrada_consulta_data = tk.Entry(root); entrada_consulta_data.pack(); entrada_consulta_data.insert(0,"Data AAAA-MM-DD")
entrada_consulta_horario = tk.Entry(root); entrada_consulta_horario.pack(); entrada_consulta_horario.insert(0,"Horário HH:MM")
tk.Button(root, text="Agendar Consulta", command=agendar_consulta).pack(pady=5)

# ---------------- Visualizar Consultas ----------------
tk.Button(root, text="Visualizar Consultas", command=visualizar_consultas).pack(pady=10)

root.mainloop()
