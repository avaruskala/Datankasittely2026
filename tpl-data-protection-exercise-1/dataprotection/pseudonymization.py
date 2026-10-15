from cryptography.fernet import Fernet

"""
TODO:
- Generate a key once and reuse it for both pseudonymization and restoration. In a real system, this key would be securely stored.
"""

key = Fernet.generate_key()
f = Fernet(key)


def pseudonymize_names(names):
    """
    TODO: Encrypt each name with Fernet symmetric encryption.
    - return list of encrypted names
    """

    names = [f.encrypt(name.encode("utf-8")) for name in names]

    return names


def restore_names(encrypted):
    """
    TODO: Decrypt previously pseudonymized names.
    - return list of decrypted names
    """
    names = [f.decrypt(name.decode()).decode() for name in encrypted]

    return names

