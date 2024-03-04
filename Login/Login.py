from tkinter import *
import csv

def salvar():
    with open('usuarios.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([entry_usuario.get(), entry_senha.get()])

def login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    with open('usuarios.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == usuario and row[1] == senha:
                print("Login realizado com sucesso!")
                return
        print("Usuário ou senha incorretos!")

root = Tk()
root.title("Login | Cássio Estevão")

root.configure(bg='#f0f0f0')

largura_janela = 600
altura_janela = 200
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
posicao_x = (largura_tela - largura_janela) // 2
posicao_y = (altura_tela - altura_janela) // 2

root.geometry(f'{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}')


background_image = PhotoImage(file='background.png')
background_label = Label(root, 
                         image=background_image
                         )
background_label.place(relwidth=1, 
                       relheight=1
                       )

label_usuario = Label(root, 
                      text="Usuário:", 
                      bg='#f0f0f0', 
                      fg='#333333', 
                      font=('Helvetica', 12)
                      )
label_usuario.place(relx=0.6, rely=0.6)
entry_usuario = Entry(root, 
                      bg='#ffffff', 
                      fg='#333333', 
                      font=('Times New Roman', 12)
                      )
entry_usuario.place(relx=0.7, rely=0.6)

label_senha = Label(root, 
                    text="Senha:", 
                    bg='#f0f0f0', 
                    fg='#333333', 
                    font=('Times New Roman', 12)
                    )
label_senha.place(relx=0.6, rely=0.7)
entry_senha = Entry(root, 
                    show="*", 
                    bg='#ffffff', 
                    fg='#333333', 
                    font=('Times New Roman', 12)
                    )
entry_senha.place(relx=0.7, rely=0.7)

botao_login = Button(root, 
                     text="Login", 
                     command=login, 
                     bg='#333333', 
                     fg='#ffffff', 
                     font=('Times New Roman', 12)
                     )
botao_login.place(relx=0.7, rely=0.84)

botao_cadastro = Button(root, 
                        text="Cadastrar", 
                        command=salvar, 
                        bg='#333333', 
                        fg='#ffffff', 
                        font=('Times New Roman', 12)
                        )
botao_cadastro.place(relx=0.85, rely=0.84)

root.mainloop()
