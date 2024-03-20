import customtkinter




#----------------------------------tela de login ------------------------------------------------

customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("dark-blue") 

#paramentros
rootlogin = customtkinter.CTk()
rootlogin.geometry('600x300')
rootlogin.title('Gerenciamento | Vendas e Entradas')
rootlogin.resizable(False,False)

#funções
def acess():
    print('login feito com sucesso!')
    pass

def registro():
    print('Registro feito com Sucesso!')
    pass



#Label Introdução
intro = customtkinter.CTkLabel(rootlogin,text='Login')
intro.pack(padx=10, pady=10)

# entradas
user_label  = customtkinter.CTkEntry(rootlogin,placeholder_text='Digite o seu usuário')
user_label.pack(padx=10, pady=10)

passw_label = customtkinter.CTkEntry(rootlogin, placeholder_text='Digite a sua senha',show="*")
passw_label.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(rootlogin,text='Lembrar Senha')
checkbox.pack(anchor='center')

# Botões
login = customtkinter.CTkButton(rootlogin, text='Acessar', command= acess)
login.pack(padx=10, pady=10)

regist = customtkinter.CTkButton(rootlogin, text='Registrar', command= registro)
regist.pack(padx=10, pady=10)

# --------------------- sistema ----------------









# -----------------------------------------------
rootlogin.mainloop()
