import sys

for filename in sys.argv[1:]:
    if "secret" in filename:
        sys.exit(1)

