from fastapi import FastAPI
from pydantic import BaseModel
from src.quantum.ccakem import kem_decaps768, kem_keygen768, kem_encaps768

class EncryptBody(BaseModel):
    message: str
    pubkey: list    
    
class DecryptBody(BaseModel):
    ciphertext: list
    privkey: list    

# APP definition
app = FastAPI(title="Crystals-Kyber"
              description="Implementation of Crystals-Kyber")


@app.get("/generate-pair")
def generate_key_pair():
    """Generates pair of keys for security level 768"""
    key_pair = kem_keygen768()

    return {"private_key": key_pair[0],
            "public_key": key_pair[1]}


@app.post("/encrypt")
def encrypt_message(body: EncryptBody):
    """Encrypt Message"""
    shared_secret, encripted_message = kem_encaps768(body.pubkey, body.message)
    return {"shared_secret": shared_secret,
            "ciphertext": encripted_message}
    

@app.post("/decrypt")
def decrypt_message(body: DecryptBody):
    response = kem_decaps768(body.privkey, body.ciphertext)
    return response