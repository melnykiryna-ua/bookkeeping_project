def encrypt(user_message, key):

    encrypted_message = ""
    range = 26

    for char in user_message:
        if char.isalpha():
            is_upper = char.isupper()
            char_code = ord(char)
            new_char_code = char_code + key
        
            if is_upper:
                if new_char_code > ord("Z"):
                    new_char_code -= range
            else:
                if new_char_code > ord("z"):
                    new_char_code -= range

            new_char = chr(new_char_code)
            encrypted_message += new_char
        else:
            encrypted_message += char
    return encrypted_message


key = int(input("Enter key: "))
user_message = input("Enter message: ")
result = encrypt(user_message, key)
print("Encrypted message:", result)