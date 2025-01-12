def decrypt(text, k):
    result = []
    for char in text:
        if 'А' <= char <= 'Я':  
            new_char = chr((ord(char) - ord('А') - k) % 32 + ord('А'))
        elif 'а' <= char <= 'я':  
            new_char = chr((ord(char) - ord('а') - k) % 32 + ord('а'))
        else:
            new_char = char 
        result.append(new_char)
    return ''.join(result)

def encrypt(text, k):
    result = []
    for char in text:
        if 'А' <= char <= 'Я':  
            new_char = chr((ord(char) - ord('А') + k) % 32 + ord('А'))
        elif 'а' <= char <= 'я':  
            new_char = chr((ord(char) - ord('а') + k) % 32 + ord('а'))
        else:
            new_char = char  
        result.append(new_char)
    return ''.join(result)

k = int(input("k = ",))
text = input("Ввежите строку ",)
encrypted_text = encrypt(text, k)
print(f"Зашифрованный текст: {encrypted_text}")
decrypted_text = decrypt(encrypted_text, k)
print (decrypted_text)
