import os

def find(path, dir):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            if item == dir:
                print(os.path.abspath(item_path))
            find(item_path, dir)

path = "./tree"
dir = "python"
find(path, dir)
