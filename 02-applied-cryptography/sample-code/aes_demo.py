"""
AES Demo — Educational Only
Uses the Python cryptography library if available:
pip install cryptography
"""
def main() -> None:
    try:
        from cryptography.fernet import Fernet
    except ImportError:
        print("cryptography library not installed.")
        print("Install it with: pip install cryptography")
        return
    key = Fernet.generate_key()
    cipher = Fernet(key)
    message = b"This is a confidential demo message."
    encrypted = cipher.encrypt(message)
    decrypted = cipher.decrypt(encrypted)
    print("AES/Fernet Symmetric Encryption Demo")
    print(f"Original message:  {message.decode()}")
    print(f"Encrypted token:   {encrypted.decode()[:60]}...")
    print(f"Decrypted message: {decrypted.decode()}")

if __name__ == "__main__":
    main()
