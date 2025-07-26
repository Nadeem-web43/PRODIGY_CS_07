from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    img = img.convert('RGB')  # Ensure RGB mode

    width, height = img.size
    encrypted_img = Image.new('RGB', (width, height))

    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            r, g, b = pixel[:3]
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            encrypted_img.putpixel((x, y), (r, g, b))

    encrypted_img.save("encrypted.png")
    print("✅ Image encrypted and saved as 'encrypted.png'")

def decrypt_image(image_path, key):
    img = Image.open(image_path)
    img = img.convert('RGB')  # Ensure RGB mode

    width, height = img.size
    decrypted_img = Image.new('RGB', (width, height))

    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            r, g, b = pixel[:3]
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            decrypted_img.putpixel((x, y), (r, g, b))

    decrypted_img.save("decrypted.png")
    print("✅ Image decrypted and saved as 'decrypted.png'")

if __name__ == "__main__":
    print("🔐 Image Encryption/Decryption Tool")
    choice = input("Do you want to encrypt or decrypt? (e/d): ")
    key = int(input("Enter encryption key (example: 5): "))

    if choice == 'e':
        encrypt_image("original.png", key)
    elif choice == 'd':
        decrypt_image("encrypted.png", key)
    else:
        print("❌ Invalid choice")
