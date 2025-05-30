import tkinter as tk
from tkinter import filedialog

def salvar():
    with open(filedialog.asksaveasfilename(defaultextension=".txt"), 'w') as f:
        f.write(text.get("1.0", tk.END))

janela = tk.Tk()
janela.title("Editor de Texto")
text = tk.Text(janela)
text.pack()
tk.Button(janela, text="Salvar", command=salvar).pack()
janela.mainloop()