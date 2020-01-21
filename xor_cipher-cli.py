#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import xor_cipher as xc

key = 0b101111100011
enc = xc.encrypt("hello", key)
xc.show_encrypted_codepoints(enc)

dec = xc.decrypt(enc, key)
xc.show_decrypted_letters(dec)
