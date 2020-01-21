#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import encdec

key = 0b101111100011
enc = encdec.encrypt("hello", key)
encdec.show_encrypted_codepoints(enc)

dec = encdec.decrypt(enc, key)
encdec.show_decrypted_letters(dec)
