from setuptools import setup, find_packages

setup(
    name='secure-file-hasher',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'secure-hasher=secure_file_hasher.cli:main',
        ],
    },
    description='A secure file hashing and integrity verification tool',
)
