#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import encdec

key = 0b101111100011
enc = encdec.encrypt("hello", key)
print(enc)

dec = encdec.decrypt(enc, key)
print(''.join(dec))
