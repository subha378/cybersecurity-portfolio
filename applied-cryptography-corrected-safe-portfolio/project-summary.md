# Project Summary — Applied Cryptography Corrected Version

## Purpose
This project demonstrates practical cryptographic concepts in a safe and professional GitHub format. It translates university cryptography work into portfolio evidence without publishing restricted assessment files.

## Main Components
1. **RSA Key Exchange Concepts**
   - Demonstrates public/private key generation ideas
   - Shows how a symmetric session key can be encrypted with a public key and recovered with a private key
   - Includes corrected 256-bit key generation logic

2. **ElGamal Secure Voting**
   - Demonstrates how encrypted votes can be aggregated
   - Shows the idea behind privacy-preserving vote tallying
   - Explains why individual votes should remain hidden while the final total can be recovered

3. **SHA-256 Proof-of-Work**
   - Demonstrates nonce searching
   - Explains hash-prefix difficulty
   - Includes corrected expected-value reasoning

4. **Encryption Ethics**
   - Summarises arguments against mandatory backdoors in end-to-end encrypted systems

## Corrected Learning Points
- A 256-bit session key should be sampled from a range that guarantees the key has 256-bit length when required.
- In RSA key exchange, if the session key changes, the encrypted ciphertext changes too.
- For a SHA-256 hash target requiring four leading hexadecimal zeros, the expected number of trials is about 16^4 = 65,536.
- Public GitHub portfolios should demonstrate skill without exposing raw assessment files.

## Skills Demonstrated
- Cryptographic reasoning
- Python implementation
- Modular arithmetic
- Secure voting concepts
- Hashing and probability
- Security ethics
- Technical communication
