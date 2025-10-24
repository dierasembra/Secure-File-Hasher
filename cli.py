import argparse
from .hasher import generate_hash, save_hash, verify_hash

def main():
    parser = argparse.ArgumentParser(description='Secure File Hasher')
    parser.add_argument('command', choices=['hash', 'verify'])
    parser.add_argument('file', help='File to process')
    args = parser.parse_args()

    if args.command == 'hash':
        file_hash = generate_hash(args.file)
        save_hash(args.file, file_hash)
        print(f"Hash generated and saved: {file_hash}")
    elif args.command == 'verify':
        valid = verify_hash(args.file)
        if valid:
            print("✅ File integrity verified.")
        else:
            print("❌ File has been modified or corrupted.")
