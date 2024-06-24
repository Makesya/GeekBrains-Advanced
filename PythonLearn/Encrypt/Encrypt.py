import pyAesCrypt
import os
from pathlib import Path


def encrypt(file, password: str):
    pyAesCrypt.encryptFile(str(file), str(file) + ".aes", password)
    os.remove(file)


def all_encrypt(path, password: str):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".aes"):
                path = os.path.join(root, file)
                encrypt(path, password)


def decrypt(file, password: str):
    pyAesCrypt.decryptFile(str(file), str(file)[:-4], password)
    os.remove(file)


def all_decrypt(path, password: str):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".aes"):
                path = os.path.join(root, file)
                decrypt(path, password)


if __name__ == "__main__":
    pass
