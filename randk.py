
import random
import time
from ecdsa import SECP256k1, SigningKey
from sympy import mod_inverse

# Prime number for secp256k1 curve
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
curve = SECP256k1  # SECP256k1 curve

# Given constant values
s = int("15509729875763924304053419655647994379903175655107184284998698212653288468986", 16)
z = int("104030932347129662709396011011259297327760920087649791561008864660756158512260", 16)
r = int("90653255469745952335985143920649543885181555095025199315947044135806663628368", 16)
target_pub_key_hex = "02145d2611c823a396ef6712ce0f712f09b9b4f3135e3e0aa3230fb9b6d08d1e16"

# Calculate the modular inverse of r
r_inv = mod_inverse(r, n)

# Target range
min_d = int("4000000000000000000000000000000000", 16)
max_d = int("7fffffffffffffffffffffffffffffffff", 16)

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
