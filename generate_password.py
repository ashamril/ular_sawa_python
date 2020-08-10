#!/usr/bin/python3

import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
#symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
symbols = "@#%&_+-=,.?"

all = lower + upper + numbers + symbols
length = 15

for i in range(1, 6):
  gen_password = "".join(random.sample(all, length))
  print("Generated Password No", i, ":", gen_password)
