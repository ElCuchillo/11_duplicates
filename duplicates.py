import os
import sys
import collections


def file_tree_scan(path):
    file_tree = []

    for root, dirs, files in os.walk(path):
        sys.stdout.write('\r \r{:.<60}'.format(root[:60]))
        sys.stdout.flush()

        for current_file in files:
            file_path = os.path.join(root, current_file)
            if os.path.isfile(file_path):
                file_tree.append((current_file, os.path.getsize(file_path),
                                  file_path))
    sys.stdout.write('\r \r\n')
    return file_tree


def doubles_searching(file_tree):

    filename_list = [(name, size) for name, size, path in file_tree]

    filename_doubles = ([filename for filename, frequency in
                         collections.Counter(filename_list).most_common()
                         if frequency > 1])

    duplicates = [(name, size, path) for name, size, path in file_tree
                  if (name, size) in filename_doubles]

    return sorted(duplicates)


if __name__ == '__main__':
    if len(sys.argv) > 1:

        file_tree = file_tree_scan(sys.argv[1])
        duplicates = doubles_searching(file_tree)

        if duplicates:
            print('{:*<60}\n Duplicates of files as following \n'
                  ' (filename, filesize, path to file):\n{:*<60}'
                  .format('', ''))
            for name, size, path in duplicates:
                print('{} [{:.2f}kB]\n{}\n{:.<60}'
                      .format(name, size / 1024, path, ''))

        else:
            print('There are no doubles in you directory ', sys.argv[1])
    else:
        print("Launch: $python3 lang_frequency.py <path_to_file>")
