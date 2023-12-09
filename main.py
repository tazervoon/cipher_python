def vigenere_cipher(message, key):
    alphabet = [chr(i) for i in range(97, 123)]
    encrypted_message = ''
    key_long = (key * (len(message) // len(key))) + key[:len(message) % len(key)]

    for i in range(len(message)):
        if message[i].isalpha():
            shift = alphabet.index(key_long[i].lower())
            if message[i].isupper():
                encrypted_message += alphabet[(alphabet.index(message[i].lower()) + shift) % 26].upper()
            else:
                encrypted_message += alphabet[(alphabet.index(message[i]) + shift) % 26]
        else:
            encrypted_message += message[i]
    return encrypted_message

message = input('Введи сообщение, которое желаешь зашифровать: ')
key = input('Введи сдвиг, при помощи которого будет осуществлена зашифровка: ')
print(vigenere_cipher(message, key))