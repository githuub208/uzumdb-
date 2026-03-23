from passlib.context import CryptContext

encryption = CryptContext(schemes=["argon2"], deprecated="auto")

def hashed_password(password):
    return encryption.hash(password)

def verify_password(plain_text, hash_password):
    return encryption.verify(plain_text, hash_password)

# print(hashed_password("abduqodir"))
print(verify_password("abduqodir","$argon2id$v=19$m=65536,t=3,p=4$yvm/d875vxdCCEEo5fzfuw$QkwxP1CJmF9Egx5IB/V2EGfzRr3+qJ3/Vt2na8RATaI"))