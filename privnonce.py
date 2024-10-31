
from sympy import mod_inverse

# Prime number for secp256k1 curve
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

# Given values
k = int("6d67c3521c7e2841f9f47705e2e79d73183c8782da1f621d85a46bb8701d7fbd", 16)  # Known k value
s = int("15509729875763924304053419655647994379903175655107184284998698212653288468986", 16)  # Signature's s value
z = int("104030932347129662709396011011259297327760920087649791561008864660756158512260", 16)  # Message digest (z)
r = int("90653255469745952335985143920649543885181555095025199315947044135806663628368", 16)  # Signature's r value

# Calculate the modular inverse of r
r_inv = mod_inverse(r, n)

# Calculate the value of d
d = (r_inv * (s * k - z)) % n

print("Calculated d value:", hex(d))
