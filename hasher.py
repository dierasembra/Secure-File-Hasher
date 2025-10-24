import hashlib
import os

def generate_hash(filepath):
    h = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            h.update(chunk)
    return h.hexdigest()

def save_hash(filepath, file_hash):
    with open(filepath + '.hash', 'w') as f:
        f.write(file_hash)

def verify_hash(filepath):
    hash_path = filepath + '.hash'
    if not os.path.exists(hash_path):
        print("Hash file not found.")
        return False

    with open(hash_path, 'r') as f:
        stored_hash = f.read().strip()

    current_hash = generate_hash(filepath)
    return stored_hash == current_hash
