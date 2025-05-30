import hashlib

usuarios = {}

def cadastrar():
    nome = input("Nome: ")
    senha = input("Senha: ")
    hash_senha = hashlib.sha256(senha.encode()).hexdigest()
    usuarios[nome] = hash_senha

def login():
    nome = input("Nome: ")
    senha = input("Senha: ")
    hash_senha = hashlib.sha256(senha.encode()).hexdigest()
    if usuarios.get(nome) == hash_senha:
        print("Login bem-sucedido!")
    else:
        print("Falha no login.")

cadastrar()
login()