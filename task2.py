from PIL import Image

def encrypt_image(image_path, output_path, key):
    """Encrypt an image by modifying pixel values."""
    image = Image.open(image_path)
    encrypted_image = Image.new(image.mode, image.size)
    pixels = image.load()
    encrypted_pixels = encrypted_image.load()
    
    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]
            encrypted_pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
    
    encrypted_image.save(output_path)

def decrypt_image(image_path, output_path, key):
    """Decrypt an image by reversing the modification of pixel values."""
    image = Image.open(image_path)
    decrypted_image = Image.new(image.mode, image.size)
    pixels = image.load()
    decrypted_pixels = decrypted_image.load()
    
    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]
            decrypted_pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)
    
    decrypted_image.save(output_path)

def main():
    print("Image Encryption/Decryption Tool")
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt an image? (E/D): ").upper()
        if choice in ['E', 'D']:
            image_path = input("Enter the path of the image: ")
            output_path = input("Enter the output path for the processed image: ")
            key = int(input("Enter the key (integer value): "))
            
            if choice == 'E':
                encrypt_image(image_path, output_path, key)
                print(f"Image encrypted and saved to {output_path}")
            else:
                decrypt_image(image_path, output_path, key)
                print(f"Image decrypted and saved to {output_path}")
        else:
            print("Invalid choice. Please choose 'E' for encryption or 'D' for decryption.")
        
        continue_choice = input("Do you want to perform another operation? (Y/N): ").upper()
        if continue_choice != 'Y':
            break

if __name__ == "__main__":
    main()
