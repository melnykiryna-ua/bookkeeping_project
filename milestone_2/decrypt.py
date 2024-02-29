def decrypt(encrypted_message, key):

    decrypted_message = ""
    range = 26

    for char in encrypted_message:
        if char.isalpha():
            is_upper = char.isupper()
            char_code = ord(char)
            new_char_code = char_code - key
        
            if is_upper:
                if new_char_code < ord('A'):
                    new_char_code += range
            else:
                if new_char_code < ord('a'):
                    new_char_code += range
                
            new_char = chr(new_char_code)
            decrypted_message += new_char
        else:
            decrypted_message += char
    return decrypted_message


key = int(input("Enter key: "))
decrypted_message = input("Enter message: ")
result = decrypt(decrypted_message, key)
print("Decrypted message:", result)