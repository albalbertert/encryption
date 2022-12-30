# pip install pyAesCrypt
import pyAesCrypt


def encrypt_decrypt(path_input, path_output, psw=None, method='encrypt'):
    if method == 'encrypt':
        password = input("Enter the password for encryption of the file: ")
        pyAesCrypt.encryptFile(path_input, path_output, password)
        print('File successfully encrypted.')
    elif method == 'decrypt' and psw:
        pyAesCrypt.decryptFile(path_input, path_output, psw)
        print('File successfully decrypted.')
    else:
        print('Incorrect parameter(s).')


if __name__ == '__main__':
    encrypt_decrypt('data.txt', 'data.aes')
    # encrypt_decrypt('data.aes', 'data_new.txt', psw='123', method='decrypt')
