
import hashlib
import requests
from bitcoin.core import CTransaction
from bitcoin.core import lx
from ecdsa.util import sigdecode_der
from ecdsa import SECP256k1

def fetch_transaction_hex(tx_id):
    url = f"https://blockchain.info/rawtx/{tx_id}?format=hex"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to fetch transaction hex")
        return None

def calculate_z(transaction_hash):
    return int(hashlib.sha256(transaction_hash).hexdigest(), 16)

def decode_signature(signature):
    r, s = sigdecode_der(signature, SECP256k1.order)
    return r, s

def decode_transaction(tx_id):
    tx_hex = fetch_transaction_hex(tx_id)
    if not tx_hex:
        return

    tx = CTransaction.deserialize(bytes.fromhex(tx_hex))
    
    for i, txin in enumerate(tx.vin):
        print(f"Input #{i + 1}")
        
        script_sig = txin.scriptSig

        try:
            # Extract the signature and public key from scriptSig
            script_elems = list(script_sig)
            if len(script_elems) < 2:
                print("Error: Not enough elements in script to extract signature and public key.")
                continue

            signature_bytes = script_elems[0]
            public_key_bytes = script_elems[1]

            signature_hex = signature_bytes.hex()
            public_key_hex = public_key_bytes.hex()

            # Decode r, s from signature
            signature_without_hash_type = signature_bytes[:-1]  # Exclude the hash type byte
            r, s = decode_signature(signature_without_hash_type)
            z = calculate_z(tx.GetHash())

            # Display results
            print("Signature:", signature_hex)
            print("Signature R:", r)
            print("Signature S:", s)
            print("Z value:", z)
            print("Public Key:", public_key_hex)
            
            # Compute Public Key Hash
            pubkey_hash = hashlib.new('ripemd160', hashlib.sha256(public_key_bytes).digest()).hexdigest()
            print("Public Key Hash:", pubkey_hash)

        except Exception as e:
            print(f"Error processing input {i+1}: {e}")

# Example transaction ID
tx_id = "5d45587cfd1d5b0fb826805541da7d94c61fe432259e68ee26f4a04544384164"
decode_transaction(tx_id)
