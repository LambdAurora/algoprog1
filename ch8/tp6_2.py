# Search in file tree.
import os
import os.path


def is_directory(path):
    return os.path.isdir(path)


def list_directory(path):
    if is_directory(path):
        result = []
        for entry in os.listdir(path):
            result += list_directory(path + "/" + entry)
        return result
    else:
        return [path]


def search_in_tree(path, search):
    files = list_directory(path)
    if len(files) == 0:
        return []
    result = []
    for f in files:
        if f.endswith(search):
            result += [f]
    return result


print(list_directory(os.path.abspath("..")))
print(search_in_tree("..", "graph.py"))
