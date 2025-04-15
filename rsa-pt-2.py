import math

class RSAEncryption:
    def __init__(self):
        """
        Declare b, n, and m
        """
        self.base = int(input("Integer Base (b): "))
        self.n = int(input("Enter Exponent (n): "))
        self.mod = int(input("Enter Modulus (m): "))
        self.power = None
        self.x = None

    """
    then implement algo 5 
    """
    
    def modular_exponentiation(self):
        # convert the exponent to binary
        self.n = bin(self.n)

        self.power = self.base % self.mod
        self.x = 1
        # Since the binary representation starts with 0b, we subtract 2 from the range
        # and add 2 to each iteration index to handle that properly
        # this way when i am handling the data in the last the conversion back to an integer works correctly

        for i in range(len(self.n) - 2):
            if self.n[i+2] == '1':
                self.x = (self.x * self.power) % self.mod
                self.power = (self.power * self.power) % self.mod

        self.x = (self.base**int(self.n, base=2)) % self.mod
        return self.x

if __name__ == "__main__":
    r1 = RSAEncryption()
    print(r1.modular_exponentiation())
    
