# precommit-tests

A simplest-possible example of using a local pre-commit system hook.

The example uses a system hook, meaning it simply calls a system executable, in this case `python my_local_hooks/myscript.py`. This has an implicit python dependency; it would be better to use the proper pre-commit language (python in this case) but I wanted to get something running with the least effort possible, and demonstrate the flexibility.

The example python script errors out if you attempt to commit any file with "secret" in the name. The script can do anything you like though, e.g. checking the file contents against a list of forbidden patterns.

To show it working, make sure `pre-commit` is installed and clone the repository, then do:

```bash
cd path/to/repo
pre-commit install
touch oops_secret
git add *
git commit -a
```

