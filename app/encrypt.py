from cryptography.fernet import Fernet
import pathlib
import os
from dotenv import load_dotenv

load_dotenv()

def generate_key():
    return Fernet.generate_key().decode("utf-8")

ENCRYPTION_KEY = os.environ.get("ENCRYPTION_KEY")

def encrypt_dir(input_dir, output_dir):
    key = ENCRYPTION_KEY
    if not key:
        raise Exception("ENCRYPTION_KEY is not found")
    fer = Fernet(key) # f"{}:"
    input_dir = pathlib.Path(input_dir)
    output_dir = pathlib.Path(output_dir)
    output_dir.mkdir(exist_ok=True, parents=True)
    for path in input_dir.glob("*"):
        __path_bytes = path.read_bytes()
        data = fer.encrypt(__path_bytes)
        rel_path = path.relative_to(input_dir)
        dest_path = output_dir / rel_path
        dest_path.write_bytes(data)

def decrypt_dir(input_dir, output_dir):
    key = ENCRYPTION_KEY
    if not key:
        raise Exception("ENCRYPTION_KEY is not found")
    fer = Fernet(key) # f"{}:"
    input_dir = pathlib.Path(input_dir)
    output_dir = pathlib.Path(output_dir)
    output_dir.mkdir(exist_ok=True, parents=True)
    for path in input_dir.glob("*"):
        __path_bytes = path.read_bytes()
        data = fer.decrypt(__path_bytes)
        rel_path = path.relative_to(input_dir)
        dest_path = output_dir / rel_path
        dest_path.write_bytes(data)