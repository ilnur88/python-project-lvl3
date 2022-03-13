import os


def save(data, path, filename):
    with open(os.path.join(path, filename), 'wb') as write_file:
        write_file.write(data)


def mkdir(path):
    os.makedirs(path)
