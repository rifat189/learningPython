
def ceaser_cipher(start_text, shift_amount, cipher_direction):
    end_text = ""
    for i in start_text:
        end_text += chr((ord(i) + (shift_amount*cipher_direction) - 97) % 26 + 97)
    print(f"Decrypted text:{end_text}")

cont = True
while cont:
    choice = input("What do you want to do? (Decrypt/Encrypt): ").lower()

    if choice == 'decrypt':
        encrypted_text = input("Enter text to decrypt: ").lower()
        shift = int(input("Enter Shift Amount: "))
        ceaser_cipher(encrypted_text, shift, -1)
    elif choice == 'encrypt':
        normal_text = input("Enter text to encrypt: ").lower()
        shift = int(input("Enter Shift Amount: "))
        ceaser_cipher(normal_text, shift, 1)
    else:
        print("Invalid input")

    st = input("Do you want to continue? (y/n): ").lower()
    if st == 'n':
        cont = False
