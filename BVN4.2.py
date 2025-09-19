def encrypt_with_stt(plaintext):
    plaintext = plaintext.upper()  # Chuyển hết sang chữ hoa
    ciphertext = ""
    for i, ch in enumerate(plaintext, start=1):
        if ch.isalpha():
            p = ord(ch) - ord('A')
            c = (p + i) % 26
            ciphertext += chr(c + ord('A'))
        else:
            ciphertext += ch
    return ciphertext

def decrypt_with_stt(ciphertext):
    plaintext = ""
    for i, ch in enumerate(ciphertext, start=1):
        if ch.isalpha():
            c = ord(ch) - ord('A')
            p = (c - i) % 26
            plaintext += chr(p + ord('A'))
        else:
            plaintext += ch
    return plaintext


P = "BuiNgocDiep"
C = encrypt_with_stt(P)
print("Plaintext :", P.upper())
print("Ciphertext:", C)
print("Giải mã lại:", decrypt_with_stt(C))