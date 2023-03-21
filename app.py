import tkinter as tk
import hashlib

users = {'user1': 'password1', 'user2': 'password2', 'user3': 'password3'}
failed_logins = {}

def login(username, password):
    if username not in users:
        return False, 'Usuário inválido'
    
    if username in failed_logins:
        if time.time() - failed_logins[username]['time'] < 300: # 5 minutos
            return False, 'Conta bloqueada. Tente novamente mais tarde.'
        else:
            del failed_logins[username]
    
    password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    
    if password == users[username]:
        return True, 'Login bem-sucedido'
    else:
        if username not in failed_logins:
            failed_logins[username] = {'attempts': 1, 'time': time.time()}
        else:
            failed_logins[username]['attempts'] += 1
            if failed_logins[username]['attempts'] >= 3:
                failed_logins[username]['time'] = time.time()
                return False, 'Conta bloqueada. Tente novamente mais tarde.'
        return False, 'Senha inválida'

def submit_login():
    username = entry_username.get()
    password = entry_password.get()
    success, message = login(username, password)
    if success:
        label_status.config(text='Login bem-sucedido')
    else:
        label_status.config(text=message)

# cria a janela principal
root = tk.Tk()
root.title('Painel de Login')

# cria os widgets
label_username = tk.Label(root, text='Nome de usuário:')
entry_username = tk.Entry(root)
label_password = tk.Label(root, text='Senha:')
entry_password = tk.Entry(root, show='*')
button_login = tk.Button(root, text='Entrar', command=submit_login)
label_status = tk.Label(root, text='')

# posiciona os widgets na janela
label_username.grid(row=0, column=0)
entry_username.grid(row=0, column=1)
label_password.grid(row=1, column=0)
entry_password.grid(row=1, column=1)
button_login.grid(row=2, column=1)
label_status.grid(row=3, column=0, columnspan=2)

# inicia a janela principal
root.mainloop()
