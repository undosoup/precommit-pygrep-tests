import sys

for filename in sys.argv[1:]:
    # Do whatever you want here!
    if "secret" in filename:
        sys.exit(1)

