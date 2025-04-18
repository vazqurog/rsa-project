import math

class RSAEncryption:
    def __init__(self):
        """
        Declare b, n, and m
        """
        self.base = [145211848999400,
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
         120277394408613,
         30949600993003

        ]
        self.n = 92256678147157
        self.mod = 239867394157913
        self.power = None
        self.x = None

    """
    then implement algo 5 
    """
    
    def modular_exponentiation(self):
        # convert the exponent to binary
        bn = bin(self.n)
        bn =  bn[2:]

        for i in range(len(self.base)):
            self.power = self.base[i] % self.mod
            self.x = 1
            #Slice the oringial binary by 2 to get rid of leading 0b
            # issue, not checking from right to left, reverse the binary string


            for j in bn[::-1]:
                if j == '1':
                    self.x = (self.x * self.power) % self.mod
                self.power = (self.power * self.power) % self.mod
        # do not use int conversion, Happens already in the loop
            print(f"correct output: {pow(self.base[i], self.n, self.mod)}")
            print(self.x)


if __name__ == "__main__":
    r1 = RSAEncryption()
    print(r1.modular_exponentiation())

    """
Integer Base (b): 3257106254
Enter Exponent (n): 102567813
Enter Modulus (m): 503421789 
    """
