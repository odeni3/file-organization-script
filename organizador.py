import os

# Change the current working directory to the desired path
cwd = os.chdir("")

all_files = os.listdir()

files_list = [i for i in all_files if os.path.isfile(i) and '.py' not in i]

types = list(set([i.split('.')[-1] for i in files_list]))

def create_folders():
    for file_type in types:
        if not os.path.exists(file_type):
            os.mkdir(file_type)

def organize():
    create_folders()
    for file in files_list:
        ext = file.split('.')[-1]
        os.replace(file, os.path.join(ext, file))

organize()
