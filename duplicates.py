import os
import sys
import collections
from itertools import groupby


def file_tree_scan(path):
    file_tree = []

    for root, dirs, files in os.walk(path):
        for current_file in files:
            file_path = os.path.join(root, current_file)
            if os.path.isfile(file_path):
                file_tree.append((current_file, os.path.getsize(file_path),
                                  file_path))
    return file_tree


def doubles_searching(file_tree):

    filename_list = [(name, size) for name, size, path in file_tree]

    filename_doubles = [filename for filename, frequency in
                         collections.Counter(filename_list).most_common()
                         if frequency > 1]

    duplicates = [((name, size), path) for name, size, path in file_tree
                  if (name, size) in filename_doubles]
    return duplicates


def print_duplicates(duplicates_list):
    print('\nDuplicates of files:\n'.format(''))

    for file in groupby(sorted(duplicates_list), key=lambda x: x[0]):
        print('<{}, {:.2f}kB>'.format(file[0][0], file[0][1]/1024))

        for path in file[1]:
            print(' - '+ path[1])
        print('\n'.format(''))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_tree = file_tree_scan(sys.argv[1])
        duplicates = doubles_searching(file_tree)
        if duplicates:
            print_duplicates(duplicates)
        else:
            print('There are no doubles in you directory ', sys.argv[1])
    else:
        print("Launch: $python3 lang_frequency.py <path_to_file>")

