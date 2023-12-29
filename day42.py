#Implement a context manager for file handling.
print ("\nWilson - Day 42 of #100DaysOfCode\n") 
print("\nImplement a context manager for file handling.\n")

class Filemanager:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.file_path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

file_path = 'day42.txt'
with Filemanager(file_path, 'w') as file:
    file.write('im wilson')
with Filemanager(file_path, 'r') as file:
    content = file.read()
    print(content)
