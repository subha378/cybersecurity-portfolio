"""
RSA Demo — Educational Only
This is a simplified RSA demonstration using small numbers.
It is NOT production-safe and should only be used for learning.
"""
from math import gcd

def mod_inverse(e: int, phi: int) -> int:
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    raise ValueError("No modular inverse found")

def main() -> None:
    p, q = 61, 53
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17
    if gcd(e, phi) != 1:
        raise ValueError("e must be coprime with phi")
    d = mod_inverse(e, phi)
    message = 42
    ciphertext = pow(message, e, n)
    decrypted = pow(ciphertext, d, n)
    print("RSA Demo")
    print(f"Public key:  (e={e}, n={n})")
    print(f"Private key: (d={d}, n={n})")
    print(f"Message:     {message}")
    print(f"Ciphertext:  {ciphertext}")
    print(f"Decrypted:   {decrypted}")

if __name__ == "__main__":
    main()
