#!/usr/bin/python3
if __name__ == "__main__":
import sys
def main():
    num_arg = len(sys.argv) - 1
    arguments = sys.argv[1:]
    if numArgs == 0:
        print("0 arguments.")
    elif numArgs == 1:
        print("1 argument:")
    else:
        print(f"{numArgs} arguments:")
    for i in range(numArgs):
        print(f"{i + 1}: {sys.argv[i + 1]}")
        