# precommit-tests

A simplest-possible example of using a local pre-commit system hook.

The example uses a system hook, meaning it simply calls a system executable, in this case `python my_local_hooks/myscript.py`. I wanted to show something working and not-completely-useless with the least possible effort, therefore the example is somewhat terrible. For starters, it re-invents a bad version of pygrep, and for another thing it doesn't use pre-commit's many excellent features including support for a variety of programming languages. Pre-commit is at its best when hooks are re-used by many projects (e.g. enforcing organisation-wide style guides) but a local hook is a convenient way to get started.

The example python script loads regular expressions from a secret file called `.bad` and checks that no committed files match any of these patterns. For example, if you want to protect yourself from accidentally revealing that you are batman, you can do the following:

```bash
cd path/to/repo
pre-commit install
echo batman > .bad 
```

You will then be protected from this oopsie:

```bash
echo "I am batman" > confession
git add confession
git commit -a
```

