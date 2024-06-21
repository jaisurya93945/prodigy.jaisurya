def caesar_cipher_encrypt(text, shift):
    """Encrypts text using Caesar Cipher."""
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    """Decrypts text using Caesar Cipher."""
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Caesar Cipher Program")
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? (E/D): ").upper()
        if choice in ['E', 'D']:
            message = input("Enter the message: ")
            shift = int(input("Enter the shift value: "))
            if choice == 'E':
                result = caesar_cipher_encrypt(message, shift)
                print(f"Encrypted message: {result}")
            else:
                result = caesar_cipher_decrypt(message, shift)
                print(f"Decrypted message: {result}")
        else:
            print("Invalid choice. Please choose 'E' for encryption or 'D' for decryption.")
        
        continue_choice = input("Do you want to perform another operation? (Y/N): ").upper()
        if continue_choice != 'Y':
            break

if __name__ == "__main__":
    main()
