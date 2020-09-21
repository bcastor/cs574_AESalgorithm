from aes import AES

def main():
    cryptography = AES()
    mode = True
    while mode:
        prompt = input("Do you want to encrypt or decrypt your message? enter q to quit")

        if prompt == "encrypt":

            key = input("enter a key 16 characters long ONLY")
            file = input("choose a file to encrypt")
            cryptography.encrypt_File(file,key)
            print("File " + file + " has been encrypted")
        elif prompt == "decrypt":
            key = input("enter a key 16 characters long ONLY")
            file = input("choose a file to decrypt")
            cryptography.decrypt_File(file, key)
            print("File " + file + " has been decrypted")

        elif prompt == 'q':
            mode = False
        else:
            print("that wasn't an option try again please")


if __name__ == '__main__':
    main()