# https://github.com/valeria-aynbinder-edu/fs-7732-3/tree/main/lesson18    # שיעור 18

# os.path.isfile("../a.txt")
# os.path.isdir("../my_dir")
# os.path.abspath("../")
# os.path.getsize("../my_text.txt.txt")
# os.path.split("/some/path")
# os.path.splitext(full_path)

import os
# root: Prints out directories only from what you specified.
# dirs: Prints out sub-directories from the root.
# files: Prints out all files from root and directories.

# iterate over files in
# that directory
for root, dirs, files in os.walk(directory):
    for filename in files:
        print(root, dirs, filename)
        # print(os.path.join(root, filename))