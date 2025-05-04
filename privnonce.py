
from sympy import mod_inverse

# Prime number for secp256k1 curve
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

# Given values
k = "1, 16)  # Known k value 
s = 15017469962149945200885750723848273514585811077818809131821534176221677769123", 16)  # Signature's s value
z = 114127494999609483589900034258620576750389929574496287636294793597914174465998", 16)  # Message digest (z)
r = 103156088317849197759996882435181365194174551366286995120913712587868633841000", 16)  # Signature's r value

# Calculate the modular inverse of r
r_inv = mod_inverse(r, n)

# Calculate the value of d
d = (r_inv * (s * k - z)) % n

print("Calculated d value:", hex(d))
