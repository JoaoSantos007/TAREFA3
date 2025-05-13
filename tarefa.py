import tkinter as tk
from tkinter import messagebox


def fechar_janela():
    janela.quit()

janela = tk.Tk()
janela.geometry("500x500")
janela.title("Novalynx")
janela.config(bg='gray20')

menu = tk.Menu(janela)
janela.config(menu=menu)

menu_arquivo = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Cadastro", menu=menu_arquivo)
menu_arquivo.add_command(label="Sair", command=fechar_janela)

cadastro = tk.Label(janela, text="Cadastro de usuários", font=("Arial", 20), bg='gray20', fg='white')
cadastro.pack(pady=5)

n = tk.Label(janela, text="Nome completo:", font=("Arial", 10), bg='gray20', fg='white')
n.pack(pady=5)

nome_cadastro = tk.Entry(janela, width=30)
nome_cadastro.pack(pady=5)

e = tk.Label(janela, text="Email:", font=("Arial", 10), bg='gray20', fg='white')
e.pack(pady=5)

email_cadastro = tk.Entry(janela, width=30)
email_cadastro.pack(pady=5)

frame_botoes = tk.Frame(janela, bg='gray20')
frame_botoes.pack(pady=20)

btn_cds = tk.Button(frame_botoes, text="Cadastrar", font=("Arial", 12))
btn_cds.grid(row=0, column=0, padx=10)

btn_edt = tk.Button(frame_botoes, text="Editar", font=("Arial", 12))
btn_edt.grid(row=0, column=1, padx=10)

btn_exc = tk.Button(frame_botoes, text="Excluir", font=("Arial", 12))
btn_exc.grid(row=0, column=2, padx=10)

listbox = tk.Listbox(janela, width=50, height=10, relief=tk.SUNKEN)
listbox.pack(pady=10)

janela.mainloop()