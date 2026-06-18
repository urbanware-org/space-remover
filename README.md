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

> [!NOTE]
> This project was **officially discontinued** as of June 2026 and is **no longer maintained**.

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

As mentioned above, this project was discontinued. For this reason, no new features will be implemented, existing features will not be enhanced and remaining bugs will not be fixed either.

However, if you have questions about it, you can contact me by sending an email to <dev@urbanware.org>.

[Top](#space-remover)
