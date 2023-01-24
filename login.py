import tkinter as tk

def check_password():
    if password_var.get() == "123":
        print("Senha correta")
        print("Senha incorreta")

root = tk.Tk()
root.title("Banco de Dados")

username_label = tk.Label(root, text="Usuário:")
username_label.grid(row=0, column=0)

username_var = tk.StringVar()
username_entry = tk.Entry(root, textvariable=username_var)
username_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = tk.Label(root, text="Senha:")
password_label.grid(row=1, column=0, padx=10, pady=10)

password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

login_button = tk.Button(root, text="Login", command=check_password)
login_button.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()