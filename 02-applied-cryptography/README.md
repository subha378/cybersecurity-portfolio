# Applied Cryptography — Fundamentals of Cryptosystems

A practical cryptography assignment covering classical ciphers, symmetric encryption, and cryptographic hash functions. Implemented in Python (Jupyter Notebook) with hands-on cryptanalysis, mode comparison, and hash collision experiments.

---

## Tools & Libraries
- **Python** — Jupyter Notebook
- **cryptography** library (AES-CBC, AES-CTR, Fernet, SHA3-256)
- **egcd** — Extended Euclidean Algorithm package
- **MD5 / SHA-3** — hash function analysis

## Skills Demonstrated
- Classical cipher implementation and cryptanalysis (Affine cipher)
- Frequency analysis and known-plaintext attack
- AES symmetric encryption (CBC and CTR modes)
- Padding analysis (PKCS7)
- Avalanche effect measurement (bit-level diffusion analysis)
- Fernet encryption/decryption with key derivation
- Birthday attack implementation and statistical analysis
- Second preimage attack (hash collision forgery)
- SHA3-256 digest comparison and bit-difference calculation

---

## Project Structure

```
applied-cryptography-fundamentals/
├── README.md
├── Task_A_Affine_Cipher.ipynb       ← Affine cipher implementation & cryptanalysis
├── Task_B_Symmetric_Cipher.ipynb    ← AES-CBC, AES-CTR, Fernet encryption
├── Task_C_Hash_Functions.ipynb      ← Birthday attack, second preimage, SHA3-256
├── plaintext.txt                    ← Decrypted Fernet output (CC Attribution 4.0 text)
└── ciphertext.txt                   ← Re-encrypted with personal key
```

---

## Task A — Affine Cipher (Extended Alphabet)

Extended Affine cipher operating over 95 printable ASCII characters (space to `~`).

### Key Findings

**A.1 — Key Space Analysis**
- Alphabet size N = 95 (= 5 × 19)
- φ(95) = (5−1)(19−1) = 72 valid `key_a` values (coprime to 95)
- Probability of a random value being a valid key_a: 72/95 ≈ 75.79%
- Student ID mod 95 = 41 → gcd(41, 95) = 1 → valid key_a (probability = 1)

**A.2 — Encryption**
- Key pair: `key_a = 41`, `key_b = 10`
- Plaintext: `"Hello everyone, welcome to Applied Cryptography!"`
- Ciphertext: `Ctvv3*t5tOQ3it;*^tv"3@t*B3*A\vvZtK*4OQ\B3gO/\1QS`

**A.3 — Cryptanalysis (Unknown Key)**
- Brute-force (Option 1): worst case 72 × 95 = 6,840 key pairs; found correct key after 104 attempts
- Frequency analysis (Option 2): identified `'('` as cipher for `' '` (21 occurrences), `'S'` for `'e'` (9 occurrences)
- System of equations derived: `key_a = 2`, `key_b = 8`
- Deciphered plaintext revealed the key for Task B.3

---

## Task B — Symmetric Encryption (AES)

**B.1 — AES-CBC: Padding & Avalanche Effect**
- Plaintext: `"Hellow World! Welcome to COMP2300/6300!"` (39 bytes)
- PKCS7 padded to 48 bytes (9 padding bytes of value `0x09`)
- 1-bit change in plaintext (`'H'` → `'I'`): **48.96% of ciphertext bits flipped**
- Block-by-block: Block 1 → 61/128, Block 2 → 69/128, Block 3 → 58/128 bits changed
- Ciphertext modification: corrupts the entire modified block; next block loses only 1 bit (CBC error propagation)

**B.2 — AES-CTR: Mode Comparison**
- Same 1-bit plaintext change in CTR mode: only **0.32% of ciphertext bits changed** (1 bit out of 312)
- CTR keystream is independent of plaintext — no diffusion between positions
- Stark contrast to CBC's ~49%: CTR lacks the avalanche effect by design

**B.3 — Fernet Encryption/Decryption**
- Decrypted a Fernet-encrypted file using a key derived from a string discovered via Task A cryptanalysis
- Re-encrypted the plaintext using a personal student ID as the key string
- Key derivation: string padded to 32 bytes → Base64 encoded → Fernet key

---

## Task C — Cryptographic Hash Functions

**C.1 — Birthday Attack on TruncatedMD5 (8-bit)**
- Hash space: n = 2⁸ = 256 possible values
- Message space: 305 messages (lines from decrypted CC license text)
- 100 rounds of birthday attack
- Empirical average collisions: **23.43** (std dev: 10.01)
- Theoretical value: √(π/2 × 256) = **20.5**
- Difference (~3.38) within 1 standard deviation — explained by finite message space without replacement
- At 16-bit (n = 65,536): theoretical threshold ~320.85 exceeds message pool (305) → birthday attack fails

**C.2 — Second Preimage Attack**
- Target message selected by index: `studentID mod 97 = 14`
- Target: `"original works of authorship and other material subject to copyright"`
- Digest (TruncatedMD5, 8-bit): `59` (hex)
- Forged message: `"original works of aulhorship and other material subject to copyright"` (position 20: `'t'` → `'l'`)
- Both messages produce digest `59` — collision confirmed

**C.3 — SHA3-256 Avalanche Effect**
- Applied SHA3-256 to original and forged messages (1-character difference)
- Two digests are completely different (as expected from a secure hash function)
- Bit-level difference measured to demonstrate SHA3-256's strong avalanche property

---

## Key Concepts Demonstrated

| Concept | Where Applied |
|---|---|
| Extended Euclidean Algorithm | Affine cipher key validation & decryption |
| Frequency Analysis | Task A.3 cryptanalysis |
| PKCS7 Padding | AES-CBC block alignment |
| Avalanche Effect | AES-CBC vs CTR comparison, SHA3-256 |
| CBC Error Propagation | Task B.1.5 ciphertext modification |
| Key Derivation | Fernet string-to-key generation |
| Birthday Paradox | TruncatedMD5 collision experiment |
| Second Preimage Attack | Hash forgery via character substitution |

---

## Important Note
Notebooks contain personal student ID references which have been retained as they are integral to the cryptographic operations (key derivation, index selection). No university assessment materials, private keys, or restricted data are included beyond what is demonstrated in the notebooks themselves.
