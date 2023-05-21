#!/bin/bash

python3 rsa_encrypt.py &
echo $! > rsa_encrypt.pid

python3 rsa_decrypt.py &
echo $! > rsa_decrypt.pid