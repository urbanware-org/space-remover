# *space-remover*

**Table of contents**
*   [Definition](#definition)
*   [Details](#details)
*   [Usage](#usage)
*   [Contact](#contact)

----

## Definition

Simple *Python* script to remove trailing spaces and tabs from files.

[Top](#space-remover)

## Details

There often are code or config files that contain trailing spaces and tabs at the end of lines as well as in blank lines. This script will remove them without removing any blank lines themselves.

The code was written on *Linux* and has only been tested on that platform, yet.

[Top](#space-remover)

## Usage

Please backup the data before using this script.

So, to remove all unnecessary spaces inside all *Python* files inside the directory `/tmp/project` as well as its sub-directories, type:

```bash
$ find /tmp/project -type f | grep "\.py$" > /tmp/foobar.tmp
$ while read line; do
      ./space-remover.py "$line"
$ done < /tmp/foobar.tmp
$ rm -f /tmp/foobar.tmp
```

[Top](#space-remover)

## Contact

Any suggestions, questions, bugs to report or feedback to give?

You can contact me by sending an email to [dev@urbanware.org](mailto:dev@urbanware.org) or by opening a *GitHub* issue (which I would prefer if you have a *GitHub* account).

[Top](#space-remover)
