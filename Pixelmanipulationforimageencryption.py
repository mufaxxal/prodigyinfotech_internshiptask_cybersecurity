from PIL import Image
import numpy as np

print("Simple Image Encryption Tool")

def encrypt_image(img_path, key):
    img = Image.open(img_path)
    arr = np.array(img)
    enc_arr = (arr * key) // (key + 1)
    enc_img = Image.fromarray(np.uint8(enc_arr))
    enc_img.save("encrypted.png")
    print("Image encrypted and saved as 'encrypted.png'.")

def decrypt_image(img_path, key):
    img = Image.open(img_path)
    arr = np.array(img)
    dec_arr = (arr * (key + 1)) // key
    dec_arr = np.clip(dec_arr, 0, 255)
    dec_img = Image.fromarray(np.uint8(dec_arr))
    dec_img.save("decrypted.png")
    print("Image decrypted and saved as 'decrypted.png'.")

def encrypt_mode():
    key = int(input("Enter encryption key: "))
    path = input("Enter image path: ")
    try:
        encrypt_image(path, key)
    except FileNotFoundError:
        print("Image not found.")

def decrypt_mode():
    key = int(input("Enter decryption key: "))
    path = input("Enter encrypted image path: ")
    try:
        decrypt_image(path, key)
    except FileNotFoundError:
        print("Image not found.")

def main():
    while True:
        choice = input("Encrypt (e), Decrypt (d), Quit (q): ").lower()
        if choice == 'e':
            encrypt_mode()
        elif choice == 'd':
            decrypt_mode()
        elif choice == 'q':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
