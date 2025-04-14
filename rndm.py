import math

def rsa(e, n, m):
    return f"C = {(m**e) % n}"

def decrypt(e, n, d=38597):
    c = [16560, 15475, 43198, 36141]
    decrypted_vals = []

    for i in c:
        decrypted_vals.append((i**d) % n)
    return decrypted_vals

if __name__ == "__main__":
    print(decrypt(13,72217))