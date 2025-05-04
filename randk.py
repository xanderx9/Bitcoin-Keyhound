
import random
import time
from ecdsa import SECP256k1, SigningKey
from sympy import mod_inverse

# Prime number for secp256k1 curve
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
curve = SECP256k1  # SECP256k1 curve

# Given constant values
s = 9322106992035102879135399198935471517312480572852046969272153240755838405632", 16)
z = 10042653713903670780376663601754538074851657618494896283759920590720077315696", 16)
r = 88766593257285807869272031906434371360037348660523351971529391117947056431080", 16)
target_pub_key_hex = "0296516a8f65774275278d0d7420a88df0ac44bd64c7bae07c3fe397c5b3300b23"

# Calculate the modular inverse of r
r_inv = mod_inverse(r, n)

# Target range
min_d = int("40", 16)
max_d = int("7f", 16)

# File to write results
output_file = "find.txt"

def generate_random_k():
    return random.randint(1, n - 1)

def calculate_private_key(k):
    d = (r_inv * (s * k - z)) % n
    return d

def get_public_key_hex(d):
    signing_key = SigningKey.from_secret_exponent(d, curve=curve)
    verifying_key = signing_key.get_verifying_key()
    return verifying_key.to_string("compressed").hex()

def main():
    start_time = time.time()  # Start time of the loop
    attempts = 0
    
    while True:
        k = generate_random_k()
        d = calculate_private_key(k)

        # Check if within specified range
        if min_d <= d <= max_d:
            pub_key_hex = get_public_key_hex(d)

            # Check for match with target public key
            if pub_key_hex == target_pub_key_hex:
                print(f"Found suitable d! d: {hex(d)}")
                with open(output_file, "a") as file:
                    file.write(f"Found suitable d! d: {hex(d)}\n")
                break
        
        attempts += 1

        # Print speed information every 1000 attempts
        if attempts % 1000 == 0:
            elapsed_time = time.time() + 1 - start_time  # Calculate total elapsed time
            speed = attempts / elapsed_time  # Speed per attempt
            print(f"{attempts} attempts, elapsed time: {elapsed_time:.2f} seconds, speed: {speed:.2f} attempts/second")

if __name__ == "__main__":
    main()
