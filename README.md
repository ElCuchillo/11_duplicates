# Anti-Duplicator

The script accepts the folder name, then checks the specified folder and all subfolders for duplicate files. Duplicates are files having the same name and size. 
As a result, the script outputs to the console a list of duplicates containing the file name, file size and the full path to the file.

# Quickstart

Example of script launch on Linux, Python 3.5:

```bash

$ python3 duplicates.py <path to folder>
```

Output example as following:

```
Duplicates of files:

<301894_900__900x597.jpg, 62.20kB>
 - /home/ElCuchillo/Рабочий стол/301894.jpg
 - /home/ElCuchillo/Рабочий стол/test/301894.jpg

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
