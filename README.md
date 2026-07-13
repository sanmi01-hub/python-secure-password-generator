# Secure Password Generator

## Overview

This is a command-line Secure Password Generator built with Python.

The program allows users to generate strong passwords by choosing the password length and the types of characters to include, such as uppercase letters, lowercase letters, numbers, and symbols.

Unlike basic password generators that use Python's `random` module, this project uses the `secrets` module, which is designed for generating cryptographically secure random values suitable for passwords and other security-related applications.

---

## Features

- Custom password length (8–30 characters)
- Choose whether to include:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Symbols
- Ensures every selected character type appears at least once
- Input validation
- Generates secure passwords using Python's `secrets` module

---

## Technologies Used

- Python 3
- secrets
- string
- random

---

## How to Run

1. Clone this repository

```bash
git clone https://github.com/yourusername/secure-password-generator.git
```

2. Navigate into the project folder

```bash
cd secure-password-generator
```

3. Run the program

```bash
python password_generator.py
```

---

## Example Output

```
========================================
Secure Password Generator
========================================

Enter your preferred password length (8-30): 16

Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): y

Generated Password:
9&TaVx!2B#rQm7Lp
```

---

## What I Learned

Building this project helped me improve my understanding of:

- Python functions
- Lists and strings
- User input validation
- Exception handling using `try` and `except`
- Secure random number generation using the `secrets` module
- Writing simple cybersecurity-related Python applications

---

## Future Improvements

- Password strength rating
- Copy password to clipboard
- Save generated passwords securely
- Graphical user interface (GUI)

---

## Author

Ayodeji Sanmi
