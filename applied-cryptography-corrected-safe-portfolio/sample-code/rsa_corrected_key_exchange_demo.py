"""
Corrected RSA Key Exchange Demo — Portfolio Safe Version

This is a simplified educational demonstration.
It is NOT production-safe and should not be used for real cryptographic security.
"""

import math
import secrets


def egcd(a: int, b: int) -> tuple[int, int, int]:
    if a == 0:
        return b, 0, 1
    g, y, x = egcd(b % a, a)
    return g, x - (b // a) * y, y


def mod_inverse(a: int, m: int) -> int:
    g, x, _ = egcd(a, m)
    if g != 1:
        raise ValueError("Modular inverse does not exist")
    return x % m


def generate_256_bit_session_key() -> int:
    """
    Generate a session key in the corrected required range:
    [2^255 + 1, 2^256)
    """
    lower = 2**255 + 1
    upper = 2**256
    return secrets.randbelow(upper - lower) + lower


def main() -> None:
    # Small demo primes only. Real RSA requires secure large primes.
    p = 3557
    q = 2579
    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = 65537
    if math.gcd(e, phi_n) != 1:
        raise ValueError("e must be coprime with phi(n)")

    d = mod_inverse(e, phi_n)

    # For this small demo modulus, we reduce the key so encryption works.
    # The full 256-bit key-generation function above demonstrates the corrected range.
    k_demo = 123456
    c = pow(k_demo, e, n)
    k_recovered = pow(c, d, n)

    print("Corrected RSA Key Exchange Demo")
    print(f"Public key:  (e={e}, n={n})")
    print(f"Private key: (d={d}, n={n})")
    print(f"Demo session key: {k_demo}")
    print(f"Ciphertext:       {c}")
    print(f"Recovered key:    {k_recovered}")
    print(f"Verification:     {k_demo == k_recovered}")

    example_256_bit_key = generate_256_bit_session_key()
    print("\nCorrected 256-bit key range demo:")
    print(f"Bit length: {example_256_bit_key.bit_length()}")


if __name__ == "__main__":
    main()
