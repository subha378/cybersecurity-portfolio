"""
SHA-256 Proof-of-Work Demo — Educational Only
Finds a nonce so SHA-256(data + nonce) starts with a chosen prefix.
"""
import hashlib

def find_nonce(data: str, prefix: str = "0000") -> tuple[int, str]:
    nonce = 0
    while True:
        digest = hashlib.sha256(f"{data}{nonce}".encode()).hexdigest()
        if digest.startswith(prefix):
            return nonce, digest
        nonce += 1

def main() -> None:
    data = "portfolio proof of work demo"
    prefix = "0000"
    nonce, digest = find_nonce(data, prefix)
    print("SHA-256 Proof-of-Work Demo")
    print(f"Data:        {data}")
    print(f"Target:      hash starts with {prefix}")
    print(f"Nonce found: {nonce}")
    print(f"Hash:        {digest}")

if __name__ == "__main__":
    main()
