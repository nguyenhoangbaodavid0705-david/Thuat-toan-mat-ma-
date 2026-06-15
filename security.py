from cryptography.fernet import Fernet
import hashlib
import base64

def derive_key(master_password:str)-> bytes:
    #Chuyen doi mat khau thanh khoa ma hoa 32 bytes
    #Bam mat khau chinh de lay khoa ,dam bao do dai yeu cau Fernet
    hash_obj= hashlib.sha256(master_password.encode())
    return base64.urlsafe_b64encode(hash_obj.digest())

def encrypt(data:str, master_password:str)->bytes:
    key=derive_key(master_password)
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

#Ham gia ma du lieu
def decrypt(encrypted_data: bytes,master_password:str)->str:
    try:
        key=derive_key(master_password)
        fernet = Fernet(key)
        return fernet.decrypt(encrypted_data).decode()
    except Exception as e:
        return None 
    
if __name__ == "__main__":
    master_password = "my_secret_password"
    original_data = "This is a secret message."
    
    encrypted_data = encrypt(original_data, master_password)
    print(f"Encrypted: {encrypted_data}")
    
    decrypted_data = decrypt(encrypted_data, master_password)
    print(f"Decrypted: {decrypted_data}")