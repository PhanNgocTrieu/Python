import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 
'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 
'x', 'y', 'z']

print(logo.logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if (cipher_direction == "decode"):
            shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += letter

    print(f"The {cipher_direction}d text is: {end_text}")


###### For First Way #######
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        # using index method
        # return the first index found
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letter
    
    print(f"The encoded text is: {cipher_text}")
    return cipher_text
    

def decrypt(encrypted_text, shift_amount):
    decrypt_text = ""
    for letter in encrypted_text:
        # using index method
        # return the first index found
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            decrypt_text += alphabet[new_position]
        else:
            decrypt_text += letter    
    print(f"The decrypted text is: {decrypt_text}")
    return decrypt_text


# Case 1:
if direction == "encode":
    encrypt(plain_text = text, shift_amount = shift)
elif direction == "decode":
    decrypt(encrypted_text = text, shift_amount = shift)
else:
    print("Not a option!")


# Case 2:
caesar(start_text=text, shift_amount=shift,cipher_direction=direction)

