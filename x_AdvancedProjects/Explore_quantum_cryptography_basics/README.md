# Caesar Cipher & Modular Arithmetic in Python

Here you will find cryptography study codes, from the basics to quantum cryptography.

This project consists of two educational Jupyter Notebooks:

1. CAESAR_CIPHER_IMPLEMENTATION.ipynb – Implements the classic Caesar Cipher encryption.
2. Modular_Arithmetic.ipynb – Demonstrates modular arithmetic and prime number testing using both basic and probabilistic methods.

-----------------------------------------------------
1. Caesar Cipher Implementation

The Caesar Cipher is one of the earliest known and simplest ciphers. It works by shifting the letters of the alphabet by a fixed number (KEY) using modular arithmetic.

Features

- Custom alphabet including the space character (' ABCDEFGHIJKLMNOPQRSTUVWXYZ').
- Case-insensitive encryption.
- Fully functional Caesar cipher encryption function.
- Clean and easy-to-understand implementation.

Example

ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY = 3

Input:
HELLO WORLD

Encrypted Output:
KHOORCZRUOG

-----------------------------------------------------
2. Modular Arithmetic & Prime Testing

This notebook focuses on the fundamental mathematical concept of modular arithmetic, particularly in the context of primality testing.

Features

- Prime checking using trial division.
- Prime checking using Fermat’s Primality Test (a probabilistic algorithm).
- Utility functions to work with large integers efficiently.
- Modular exponentiation with pow(a, n-1, n).

Example

is_prime(99194853094755497)  # Output: True or False depending on the method

Fermat’s test performs k iterations (default k=10) and returns True if the number is likely to be prime.

-----------------------------------------------------
Getting Started

Prerequisites

- Python 3.6+
- Jupyter Notebook or JupyterLab

Installation

1. Clone the repository:
   git clone https://github.com/yourusername/caesar-modular-arithmetic.git
   cd caesar-modular-arithmetic

2. Install Jupyter (if not already installed):
   pip install notebook

3. Launch the notebooks:
   jupyter notebook


Educational Value

These notebooks are designed to teach:

- The fundamentals of classical encryption methods.
- How modular arithmetic is used in cryptography.
- Basic vs. probabilistic approaches to prime checking.
- Python coding best practices in a notebook format.

-----------------------------------------------------
License

This project is licensed under the MIT License. See the LICENSE file for details.

-----------------------------------------------------
Acknowledgments

- Inspired by classical cryptography.
- Built using Python and Jupyter Notebooks.
