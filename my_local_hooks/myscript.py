import sys
import re
import os

if not os.path.exists(".bad"):
    print("Nothing to do. Add patterns to '.bad' to check for leaks")
    sys.exit(0)

with open(".bad", 'r') as f:
    patterns = [l.rstrip() for l in f]

print("Excluding files matching these patterns:")
for p in patterns:
    print(f"\t{p}")

for fn in sys.argv[1:]:
    with open(fn, 'r') as f:
        for i, l in enumerate(f):
            for p in patterns:
                if re.search(p, l):
                    print(f"Naughty file ({fn}) contained a match to pattern ({p}) on line {i + 1}")
                    sys.exit(1)
    print(f"Good file ({fn})")

