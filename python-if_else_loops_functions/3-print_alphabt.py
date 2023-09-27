#!/usr/bin/python3
for alpha_letters in range(ord('a'), ord('z')+1):
    if alpha_letters == ord('e') or alpha_letters == ord('q'):
        continue
        print(f"{chr(alpha_letters)}", end="")