def caesar_encrypt(plaintext, k):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            ciphertext += chr((ord(char) - shift + k) % 26 + shift)
        else:
            ciphertext += char
    return ciphertext

k = 2
plaintext = "BuiNgocDiep"

ciphertext = caesar_encrypt(plaintext, k)
print("Plaintext: ", plaintext)
print("Ciphertext: ", ciphertext)