"""
ElGamal Secure Voting Demo — Portfolio Safe Version

This simplified example demonstrates the idea of encrypted voting
and homomorphic aggregation. It is educational only.
"""

def main() -> None:
    # Small educational prime and generator
    p = 467
    g = 2

    # Election/private key
    x = 127
    h = pow(g, x, p)

    # Vote vector: 1 = Yes, 0 = No
    votes = [0, 1, 1, 0, 0]
    nonces = [53, 71, 89, 107, 131]

    c1_values = []
    c2_values = []

    for vote, nonce in zip(votes, nonces):
        c1 = pow(g, nonce, p)
        c2 = (pow(g, vote, p) * pow(h, nonce, p)) % p
        c1_values.append(c1)
        c2_values.append(c2)

    prod1 = 1
    prod2 = 1

    for c1, c2 in zip(c1_values, c2_values):
        prod1 = (prod1 * c1) % p
        prod2 = (prod2 * c2) % p

    # Decrypt aggregate: prod2 * prod1^(-x) mod p = g^(sum of votes)
    aggregate_encoded = (prod2 * pow(pow(prod1, x, p), -1, p)) % p

    # Since there are only 5 voters, brute-force the small discrete log
    total_yes = None
    for possible_total in range(len(votes) + 1):
        if pow(g, possible_total, p) == aggregate_encoded:
            total_yes = possible_total
            break

    print("ElGamal Secure Voting Demo")
    print(f"Votes:            {votes}")
    print(f"Encrypted c1:     {c1_values}")
    print(f"Encrypted c2:     {c2_values}")
    print(f"Aggregate value:  {aggregate_encoded}")
    print(f"Recovered total:  {total_yes}")
    print(f"Expected total:   {sum(votes)}")


if __name__ == "__main__":
    main()
