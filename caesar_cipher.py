def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

print("🔐 Caesar Cipher Tool 🔐")
choice = input("Type 'encrypt' or 'decrypt': ").strip().lower()
message = input("Enter the message: ")
shift = int(input("Enter the shift number (key): "))

if choice == "encrypt":
    print("Encrypted Text:", encrypt(message, shift))
elif choice == "decrypt":
    print("Decrypted Text:", decrypt(message, shift))
else:
    print("Invalid choice!")
