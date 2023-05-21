#!/bin/bash

kill $(cat rsa_encrypt.pid)
rm -rf rsa_encrypt.pid

kill $(cat rsa_decrypt.pid)
rm -rf rsa_decrypt.pid