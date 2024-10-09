# Find File Script
> This script contains a function called find_file, which recursively searches a Windows filesystem for a file starting at a given directory.

### *function: find_file*
    @param: file_name: string to find specific file
            path: (string) start path to begin search
    @return: path: string name of path found file is in

This script is currently set to find a file called 'FindMe.txt'.

## Prerequisities
This script is guaranteed to run on your machine if it has:
* Windows 10 and up
* Python 3.10.0 (although it will likely run with older versions)
> Ensure the **os module** is included in your Python version

## Usage
Edit the start path to begin in a user folder.
> ```Note: the script may not work starting in 'C:\\' if your machine does not have long paths enabled.```

Add 'FindMe.txt' to an *accessible* directory  
Run the command in the terminal based on which version (or alias) of 
Python you have on your machine.

```sh
python find_file.py
```
or
```sh
python3 find_file.py
```

## Version
* v1.0 - Oct. 2024
    * first (and likely final) version

## Author
Rafaela Lomboy
GitHub: [@rlom721](https://github.com/rlom721)
