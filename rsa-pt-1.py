import math

def rsa(e, n, m):
    """
    simulating the rsa encryption
    """
    return f"C = {(m**e) % n}"

def decrypt(n=239867394157913, d= 92256678147157):
    "decrypting the original encryption"
    c = [145211848999400,
         227222064321977,
         39598222912650,
         191763979974614,
         219576934403262,
         117169554031523,
         168500484359777,
         38123838523268,
         30644753213699,
         226826181481017,
         65649234045392,
         63007712434340,
         49848375180474,
         47222405287028,
         13850107387430,
         88452639299251,
         144564351057224,
         206595123002906,
         219364678594453,
         157011015407561,
         34522712143931,
         67065160666261,
         132007183329974,
         13850107387430,
         215735794076967,
         221134475240962,
         192182683094731,
         8182780553165,
         110370733643200,
         120277394498613,
         30949600993003

         ]
        #EM     #ER    #AL    #DX
    decrypted_vals = []

    for i in c:
        decrypted_vals.append((i**d) % n)
    return decrypted_vals
"""
def find_d(e, n):
    p, q = 0, 0

    for i in range(9999999, int(math.sqrt(n)) + 1):
        if n % i == 0:
            p , q = i, n // i 
            prime_result = ((p-1) * (q-1))
    


    return f"P = {p}\nQ = {q}\nprime_result = {prime_result}\nd = {d}"
"""
if __name__ == "__main__":
    print(decrypt())