#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Filename: find_file.py
    Author: Rafaela Lomboy
    Date: 2024-10-09
    Version: 1.0
    Description: This script contains a function recursively searches a Windows
    filesystem for a file starting at a given directory.
"""

import os

def find_file(file_name, path):
    """ find_file recursively searches for file starting at a given directory.

        @param: file_name: string to find specific file
                path: (string) start path to begin search
        @return: path: string name of path found file is in
    """
    try:
        os.chdir(path)
        items = os.listdir(path)
    except PermissionError:
        # skip directories we don't have permission to access
        return None

    # print("current directory: " + os.getcwd())
    
    for item in items:
        item_path = os.path.join(path, item)

        if os.path.isfile(item_path) and item == file_name and item[0] != '.':
            return path
        elif os.path.isdir(item_path) and item[0] != '.':
            found = find_file(file_name, item_path)
            if found:
                return found

    return None


if __name__ == '__main__':
    file_name = "FindMe.txt"
    start_path = "C:\\Users\\"
    
    result = find_file(file_name, start_path)
    if result:
        print("File found in: " + result)
    else:
        print("File not found.")