def decrypt_string(encrypted):
 
    length = len(encrypted)
    

    chet = encrypted[:length//2]
    nechet = encrypted[length//2:][::-1]
    

    decrypted = []
    for i in range(length):
        if i % 2 == 0:
            decrypted.append(nechet[i//2])
        else:
            decrypted.append(chet[i//2])
    
    return ''.join(decrypted)

s = "ргамамроП"
d_s = decrypt_string(s)
print(d_s) 
