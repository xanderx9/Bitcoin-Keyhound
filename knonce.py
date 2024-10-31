
from sympy import mod_inverse

# Prime number for secp256k1 curve
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

# Given values
d = int("35c0d7234df7deb0f20cf706244", 16)  # Private key (d)
s = int("23142018875421668674805744145115366215102447136300717062570926532185873127405", 16)  # Signature's s value
z = int("104030932347129662709396011011259297327760920087649791561008864660756158512260", 16)  # Message digest (z)
r = int("20312125620252617190628581189119353303634619175788989653674318123623043938400", 16)  # Signature's r value

# Calculate the modular inverse of s
s_inv = mod_inverse(s, n)

# Calculate the k value
k = (s_inv * (z + r * d)) % n

print("Calculated k value:", hex(k))
