CLI application to parse data from API https://rdb.altlinux.org/api/ with different options:
1. packages which present in p10 branch but absent in sisyphus branch
2. packages which present in sisyphus branch but absent in p10 branch
3. packages which present in both p10 and sisyphus branches
4. packages which present in both p10 and sisyphus branches with "version" newer in sisyphus branch

Example of using:
<a href="https://asciinema.org/a/fJGqrNkvnIAGl7HAD7sUzLOEt" target="_blank"><img src="https://asciinema.org/a/fJGqrNkvnIAGl7HAD7sUzLOEt.svg" /></a>

Example of result data.json:
```
[
    {
        "name": "0ad-data",
        "epoch": 1,
        "version": "0.0.26",
        "release": "alt0_3_alpha",
        "arch": "noarch",
        "disttag": "sisyphus+307413.100.1.1",
        "buildtime": 1664219864,
        "source": "0ad-data"
    },
    ...
    {
        "name": "3dprinter-udev-rules",
        "epoch": 0,
        "version": "0.3",
        "release": "alt1_2",
        "arch": "noarch",
        "disttag": "sisyphus+315942.100.1.1",
        "buildtime": 1677531353,
        "source": "3dprinter-udev-rules"
    }
]
```

To install application, first install Poetry package:
```
curl -sSL https://install.python-poetry.org | python3 -
```

then clone, build and install application:
```commandline
git clone git@github.com:al-ov73/altlinux-branch-diff.git
cd altlinux-branch-diff
make start
```
then start application and check result:
```commandline
gendiff
```