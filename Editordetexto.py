import tkinter as tk
from tkinter import filedialog

def abrir():
    caminho = filedialog.askopenfilename()
    with open(caminho, 'r') as file:
        texto.delete("1.0", tk.END)
        texto.insert(tk.END, file.read())

def salvar():
    caminho = filedialog.asksaveasfilename(defaultextension=".txt")
    with open(caminho, 'w') as file:
        file.write(texto.get("1.0", tk.END))

janela = tk.Tk()
texto = tk.Text(janela)
texto.pack()
tk.Button(janela, text="Abrir", command=abrir).pack()
tk.Button(janela, text="Salvar", command=salvar).pack()
janela.mainloop()