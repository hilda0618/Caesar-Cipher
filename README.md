# 🔐 Caesar Cipher Program

**Author:** Hilda Liu  
**Class:** 7th Grade Computer Science  
**Project:** Caesar Cipher Program  
**Date:** [TODAY'S DATE]  

---

## 🎯 Project Overview

This Python program allows users to **encrypt or decrypt messages** using a Caesar Cipher. A Caesar Cipher is a type of substitution cipher where each letter in the plaintext is shifted by a fixed number of positions in the alphabet.

---

## 🛠️ Features

- Supports both **encryption** and **decryption**
- Accepts a **shift key from 1 to 25**
- Automatically **wraps around** the alphabet using `% 26`
- Handles **uppercase and lowercase** letters correctly
- Leaves **symbols, numbers, and spaces unchanged**
- Runs in a loop until the user types `"quit"`
- Displays helpful error messages for invalid input

---

## 🧪 Example Usage

```plaintext
Type 'encrypt', 'decrypt', or 'quit': encrypt
Enter shift amount (1–25): 5
Enter your message: Hello, World!
Encrypted message: Mjqqt, Btwqi!

Type 'encrypt', 'decrypt', or 'quit': decrypt
Enter shift amount (1–25): 5
Enter your message: Mjqqt, Btwqi!
Decrypted message: Hello, World!
