def cipherMessage(message, key, decrypt): 
    encrypted = '' 
  
    if decrypt == True: 
        key = -key 
    for char in message: 
        if char.isalpha(): 
            num = ord(char) 
            num += key 
            if char.isupper(): 
                if num > ord('Z'): 
                    num -= 26 
                elif num < ord('A'): 
                    num += 26 
            elif char.islower(): 
                if num > ord('z'): 
                    num -= 26 
                elif num < ord('a'): 
                    num += 26 
            encrypted += chr(num) 
        else: 
            encrypted += char
    print (encrypted)

cipherMessage("david is gay",1,True)