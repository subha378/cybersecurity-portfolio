"""
SHA-256 Proof-of-Work Expected Value Demo

This demonstrates why four leading hexadecimal zeros has an expected
search cost of approximately 16^4 = 65,536 attempts.
"""

import hashlib
import random


def find_nonce(data: str, prefix: str = "0000") -> tuple[int, str]:
    nonce = 0
    while True:
        candidate = f"{data}{nonce}"
        digest = hashlib.sha256(candidate.encode()).hexdigest()
        if digest.startswith(prefix):
            return nonce, digest
        nonce += 1


def main() -> None:
    prefix = "0000"
    theoretical_expected_attempts = 16 ** len(prefix)

    data = "portfolio proof of work demo"
    nonce, digest = find_nonce(data, prefix)

    print("SHA-256 Proof-of-Work Demo")
    print(f"Target prefix: {prefix}")
    print(f"Theoretical expected attempts: {theoretical_expected_attempts}")
    print(f"Nonce found in this run: {nonce}")
    print(f"Hash: {digest}")


if __name__ == "__main__":
    main()
