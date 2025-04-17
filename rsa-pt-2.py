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
        bn = bin(self.n)
        bn =  bn[2:]
        self.power = self.base % self.mod
        self.x = 1
        #Slice the oringial binary by 2 to get rid of leading 0b
        # issue, not checking from right to left, reverse the binary string
        for i in bn[::-1]:
            if i == '1':
                self.x = (self.x * self.power) % self.mod
            self.power = (self.power * self.power) % self.mod
            print(f"Binary Digit: {i}")
            print(f"X: {self.x}")
            print(f"Power: {self.power}")
    # do not use int conversion, Happens already in the loop
        print(f"correct output: {pow(self.base, self.n, self.mod)}")
        return self.x


if __name__ == "__main__":
    r1 = RSAEncryption()
    print(r1.modular_exponentiation())

    """
Integer Base (b): 3257106254
Enter Exponent (n): 102567813
Enter Modulus (m): 503421789 
    """
    
