# Simple Directory Enumerator

A basic Python tool to perform directory brute-forcing on a target web server using a wordlist.

## Features

- Reads target domain/IP from command-line
- Uses a custom wordlist (`wordlist.txt`) for directory guessing
- Detects valid directories via HTTP status codes
- Simple and lightweight

## Requirements

- Python 3.x
- `requests` library  
  Install it using:
  ```bash  
    'pip install requests'
