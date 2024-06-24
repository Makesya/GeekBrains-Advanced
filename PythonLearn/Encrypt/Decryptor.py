import pyAesCrypt
import os
import customtkinter as ctk
from customtkinter import filedialog

app = ctk.CTk()
app.title("Encryptor by Makesya")
app.geometry("400x270")
app.resizable(False, False)


def encrypt(file, password: str):
    pyAesCrypt.encryptFile(str(file), str(file) + ".aes", password)
    os.remove(file)
    print(f"Файл [{file}] зашифрован")


def decrypt(file, password: str):
    pyAesCrypt.decryptFile(str(file), str(file)[:-4], password)
    os.remove(file)
    print(f"Файл [{file}] расшифрован")


def all_encrypt(dir, password: str):
    """
    Программа рекурсивно проходит по директории и зашифровывает все файлы в ней и вложенных папках
    """
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            encrypt(path, password)
            status_bar.configure(
                text=f"Файл [{path.split('/')[-1]}] зашифрован")
        else:
            all_encrypt(path, password)
    print("Все файлы зашифрованы")
    status_bar.configure(text="Все файлы зашифрованы")


def all_decrypt(dir, password: str):

    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            decrypt(path, password)
            status_bar.configure(
                text=f"Файл [{path.split('/')[-1]}] расшифрован")
        else:
            all_decrypt(path, password)
    print("Все файлы расшифрованы")
    status_bar.configure(text="Все файлы расшифрованы")


def select_directory():
    folder_path = filedialog.askdirectory()
    inputPathFolder.delete(0, 'end')
    inputPathFolder.insert(0, folder_path)


inputPathFolder = ctk.CTkEntry(
    app, placeholder_text="Путь до папки", width=250)
inputPathFolder.pack_configure(pady=5, ipady=5, padx=5)
inputPathFolder.pack(side=ctk.TOP, fill=ctk.X)

buttonSelectDirectory = ctk.CTkButton(
    app, text="...", command=select_directory)
buttonSelectDirectory.pack_configure(side=ctk.LEFT, padx=5, ipady=1)
buttonSelectDirectory.pack(side=ctk.LEFT)

inputPassword = ctk.CTkEntry(app, placeholder_text="Пароль", width=200)
inputPassword.pack_configure(pady=5, ipady=5, padx=5)
inputPassword.pack(side=ctk.TOP, fill=ctk.X)

buttonEncrypt = ctk.CTkButton(app, text="Зашифровать", command=lambda: all_encrypt(
    inputPathFolder.get(), inputPassword.get()))
buttonEncrypt.pack_configure(pady=5, ipady=1, padx=5)
buttonEncrypt.pack(side=ctk.TOP, fill=ctk.X)

buttonDecrypt = ctk.CTkButton(app, text="Расшифровать", command=lambda: all_decrypt(
    inputPathFolder.get(), inputPassword.get()))
buttonDecrypt.pack_configure(pady=5, ipady=1, padx=5)
buttonDecrypt.pack(side=ctk.TOP, fill=ctk.X)

status_bar = ctk.CTkLabel(app, text="Made by Makesya")
status_bar.pack_configure(pady=5, ipady=5, padx=5)
status_bar.pack(side=ctk.TOP, fill=ctk.X)

app.mainloop()
