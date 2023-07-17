# Password Generator and Storage

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

This is a simple Python script that generates random passwords and securely stores them using the `simplecrypt` and `pycryptodome` library. The script allows you to generate strong passwords of customizable length and complexity and stores them in an encrypted file for later use.

## Features

- Generates random passwords with customizable length and complexity.
- Utilizes the `simplecrypt` and `pycryptodome` libraries for secure encryption and decryption.
- Stores encrypted passwords in a file for easy retrieval.
- Retrieves encrypted passwords into clipboard for immediate use. (`pbcopy` for mac, `xclip` for linux)
- Provides a simple command-line interface for password generation and retrieval.

## Prerequisites

Make sure you have the following installed before running the script:

- Python 3.x
- `simplecrypt` library (install using `pip install simple-crypt`)
- `pycryptodome` (install using `pip install pycryptodome`)

## Usage

1. Clone the repository:

```bash
git clone https://github.com/ademz/my-password-storage.git
```

2. Change into the project directory:
   
```bash
cd my-password-storage
```

3. Run the script:
```bash
python passwdstorage.py set new_password
```


## Acknowledgments

This script was inspired by the need for a secure and convenient way to generate and store passwords. It utilizes the simplecrypt and pycryptodome library, which provides a straightforward encryption solution.

## Disclaimer
This script is provided as-is without any warranty. Use it at your own risk.

## Contributing
Contributions are welcome! If you have any suggestions or improvements, please submit a pull request.

If you find any issues or bugs, please open an issue on the GitHub repository.

## Contact
If you have any questions or suggestions, feel free to contact me at adem@oztas.net.
