# Corrections Notes

This file explains the corrections made in the portfolio-safe version.

## 1. RSA Session Key Generation Correction

### Issue
The original assessed work used a 256-bit random value, but feedback indicated that the required random key range should ensure the key is selected from:

```text
[2^255 + 1, 2^256]
```

This guarantees a 256-bit key rather than allowing smaller values.

### Corrected idea
A corrected 256-bit key generation method should use a lower bound above 2^255.

In Python demonstration form:

```python
import secrets

k = secrets.randbelow(2**256 - (2**255 + 1)) + (2**255 + 1)
```

This produces a value in the intended 256-bit range.

## 2. RSA Ciphertext Correction

### Issue
Because the session key `k` was generated using the wrong range, the RSA ciphertext `c = k^e mod n` was also marked incorrect.

### Corrected idea
Once the corrected key `k` is generated, ciphertext must be recomputed:

```text
c = k^e mod n
```

Then decryption verifies:

```text
k' = c^d mod n
k' == k
```

## 3. SHA-256 Expected Value Correction

### Issue
The average proof-of-work value was marked incorrect. The expected value should be close to:

```text
2^16
```

or equivalently:

```text
16^4 = 65,536
```

### Why
Each hexadecimal character has 16 possible values. Requiring four leading hexadecimal zeros means:

```text
Probability = (1/16)^4 = 1/65,536
```

So the expected number of attempts is approximately:

```text
65,536
```

## 4. Safe GitHub Correction

The original files are not uploaded because they contain assessment material and student-specific data. This corrected public version uses:
- cleaned README
- correction notes
- safe demonstration code
- no raw assessment notebooks
- no plaintext/ciphertext assessment files
- no student identifiers
