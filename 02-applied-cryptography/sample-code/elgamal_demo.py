"""
ElGamal Demo — Educational Only
This simplified example demonstrates ElGamal-style encryption.
It is NOT production-safe.
"""
def main() -> None:
    p = 467
    g = 2
    x = 127
    y = pow(g, x, p)
    message = 25
    k = 53
    c1 = pow(g, k, p)
    shared_secret = pow(y, k, p)
    c2 = (message * shared_secret) % p
    recovered_secret = pow(c1, x, p)
    decrypted = (c2 * pow(recovered_secret, -1, p)) % p
    print("ElGamal Demo")
    print(f"Public parameters: p={p}, g={g}")
    print(f"Public key y:      {y}")
    print(f"Message:           {message}")
    print(f"Ciphertext:        (c1={c1}, c2={c2})")
    print(f"Decrypted:         {decrypted}")

if __name__ == "__main__":
    main()
