# Secure File Hasher

A lightweight command-line tool to generate and verify cryptographic file hashes.
Useful for verifying file integrity, detecting tampering, and secure file distribution.

## Features
- Generate SHA-256 hashes
- Save hashes to `.hash` files
- Verify files against hash records
- Simple command-line usage
- No external dependencies beyond Python standard library

## Installation
```bash
pip install .
```

## Usage
Generate a hash:
```bash
secure-hasher hash example.zip
```

Verify file integrity:
```bash
secure-hasher verify example.zip
```

## Sponsor
If this tool helps you, please consider supporting development through GitHub Sponsors.
