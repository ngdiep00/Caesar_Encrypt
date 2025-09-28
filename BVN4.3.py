def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    d_old, d = 0, 1
    r_old, r = phi, e
    while r != 0:
        q = r_old // r
        r_old, r = r, r_old - q * r
        d_old, d = d, d_old - q * d
    if d_old < 0:
        d_old += phi
    return d_old

# Tham số RSA
p, q, e = 17, 23, 5
n = p * q
phi = (p - 1) * (q - 1)
d = mod_inverse(e, phi)

print(f"Khóa công khai: (n={n}, e={e})")
print(f"Khóa bí mật: (n={n}, d={d})")

# Mã hóa thông điệp
message = "BuiNgocDiep"
# Chuyển từng ký tự thành mã ASCII
ascii_values = [ord(c) for c in message]
print("ASCII:", ascii_values)

# Mã hóa: c = m^e mod n
cipher = [pow(m, e, n) for m in ascii_values]
print("Bản mã:", cipher)

# Giải mã: m = c^d mod n
decrypted = "".join([chr(pow(c, d, n)) for c in cipher])
print("Giải mã:", decrypted)