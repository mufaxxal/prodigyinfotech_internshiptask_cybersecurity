
print(" Welcome to my Task 1 of Internship\n ")
print(" Created by: Muffadal Ali\n")


def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

print("Choose an option:")
print("e - Encrypt a message")
print("d - Decrypt a message")
choice = input("Enter e or d: ")

msg = input("\nEnter your message: ")
shift = int(input("Enter shift value: "))

if choice == "e":
    print("\nEncrypted Message:", encrypt(msg, shift))
elif choice == "d":
    print("\nDecrypted Message:", decrypt(msg, shift))
else:
    print("\nInvalid choice! Please restart the program.")

print("\nThank you for using my Caesar Cipher Program!")
