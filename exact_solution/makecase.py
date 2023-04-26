"""
    name:  Nick Spokes & Abdallah Derbala
    
    Autogenerate test cases
"""
import random
import sys


def main():
    outfile, size = None, None

    # Read in args and check for invalid input
    args = sys.argv[1:]
    if len(args) < 1:
        raise Exception("Case size must be passed as argument with command")
    for item in args:
        if item.isdigit():
            size = int(item)
    if not size:
        raise Exception("No size found in arguments")
    if '-f' in args:
        outfile = open(f"test_cases/{size}.txt", 'w')
        sys.stdout = outfile

    # Create test case
    print(f"{size} {size * (size - 1) // 2}")
    visited = {}
    for i in range(size):
        for j in range(size):
            if i != j and (j, i) not in visited:
                ending = '\n'
                if sys.stdout == outfile and i == size - 2:
                    ending = ''
                visited[(i, j)] = True
                print(f"{chr(97 + i)} {chr(97 + j)} {random.randint(0, 10000)}", end=ending)
    if outfile:
        outfile.close()


if __name__ == "__main__":
    main()
