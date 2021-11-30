import string


class FileReader:

    def read(self, path: string) -> string:
        with open(path, 'r') as f:
            data = f.read()
        return data
