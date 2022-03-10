import ceaserCipher

isContinue = True
while isContinue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    shift = shift % 26
    ceaserCipher.caesar(start_text=text, shift_amount= shift, cipher_direction=direction)

    result = input("Do you want to play again? 'yes' to continue, otherwise 'no'\n").lower()
    if result == "no":
        isContinue = False
        print("Bye")