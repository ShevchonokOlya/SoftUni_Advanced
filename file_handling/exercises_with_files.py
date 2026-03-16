
from fileinput import close
import os

def create_file_text():
    path = os.path.join(path_dir, "files", "text.txt")
    with open(path, 'w') as file:
        file.write("This is some random line\nThis is the second line\nAnd this is the third one")

def first_task():
    path = os.path.join(path_dir, "files", "text.txt")

    try:
        with open(path, 'r') as file:
            file.seek(0)
            print("File found")
            print(file.read())

    except FileNotFoundError:
        print("File not found")
    finally:
        print("File is closed= ", file.closed)

# create_file_text()
# first_task()


def create_file_numbers():
    path = os.path.join(path_dir, "files", "numbers.txt")
    with open(path, 'w') as file:
        file.write("1\n2\n3\n4\n5\n5")


def file_reader_by_lines():
    path = os.path.join(path_dir, "files", "numbers.txt")
    result = []
    result2 = 0
    with open(path) as file:
        result = [int(line) for line in file if line]
        file.seek(0)
        for line in file:
            result2 += int(line)
    print(f"\nSum of numbers = {sum(result)}")
    print(f"Sum of numbers = {result2}")

# create_file_numbers()
# file_reader_by_lines()

def create_file_my_first_file():
    path = os.path.join(path_dir, "files", "my_first_file.txt")
    with open(path, 'w') as file:
        file.write('I just created my first file!')

# create_file_my_first_file()

def file_deleting():
    path = os.path.join(path_dir, "files", "my_first_file.txt")
    if os.path.exists(path):
        os.remove(path)
        print("File removed")
    else:
        print("File already deleted!")

def create_file_list_of_words():
    path = os.path.join(path_dir, "files", "words.txt")
    with open(path, 'w') as file:
        file.write('quick is fault')

    path2 = os.path.join(path_dir, "files", "text.txt")
    with open(path2, 'w') as file:
        file.write("-I was quick to judge him, but it wasn't his fault.\n-Is this some kind of joke?! Is it?\n-Quick, hide here…It is safer.")

def word_counter_in_file():
    import re

    words = []
    result = {}

    search_file = os.path.join(path_dir, "files", "words.txt")
    with open(search_file) as search:
        for word in search:
            words.extend(word.split())

    target_file = os.path.join(path_dir, "files", "text.txt")
    with open(target_file) as target:

        for word in words:
            target.seek(0)
            pattern =  fr'\b{word}\b'
            matches = re.findall(pattern,  target.read(), re.IGNORECASE)
            result[word] = len(matches)


    path_resulting_file = os.path.join(path_dir, "files", "output.txt")
    with open(path_resulting_file, 'w') as file:
        for word in sorted(result.items(), key= lambda x : -x[1]):
            file.write(f'{word[0]} - { word[1]}\n')

# create_file_list_of_words()
# word_counter_in_file()


def even_lines():

    from costants import path_dir
    import os
    path2 = os.path.join(path_dir, "files", "text_even.txt")
    with open(path2, 'r') as file:
        for index, line in enumerate(file):
            if index % 2 == 0:
                for ch in "-,.!?":
                    line = line.replace(ch, "@")
                print(" ".join(reversed(line.split())))

# even_lines()

def line_numbers():
    from costants import path_dir
    from string import punctuation
    import os
    path_read = os.path.join(path_dir, "files", "text_even.txt")
    path_out = os.path.join(path_dir, "files", "output_even.txt")
    with open(path_read, 'r') as file_in, open(path_out, 'w') as file_out:
        for index, line in enumerate(file_in):
            punctuation_count = 0
            letters = 0
            for ch in line:
                if ch in punctuation:
                    punctuation_count += 1
                elif ch.isalpha():
                    letters += 1

            file_out.write(f'Line {index+1}: {line.strip()} ({letters})({punctuation_count})\n')

from costants import path_dir
path_task = os.path.join(path_dir, "files")

def create_file(full_file_name: str):
    with open(full_file_name, 'w'): close()

def add_file(full_file_name: str, content: str):
    with open(full_file_name, 'a') as file_to_append:
        file_to_append.write(content + '\n')

def replace_file(full_file_name: str, *args):
    old_string = args[0]
    new_string = args[1]
    try:
        with open(full_file_name, 'r+') as file:
            line = file.read()
            file.seek(0)
            file.truncate(0)
            line = line.replace(old_string, new_string)
            file.write(line)
    except FileNotFoundError:
        print("An error occurred")


def delete_file(full_file_name: str):
    try:
        os.remove(full_file_name)
    except FileNotFoundError:
        print("An error occurred")

def file_manipulator():

    command_mapper = {
        "Create": create_file,
        "Replace": replace_file,
        "Delete": delete_file,
        "Add": add_file
    }
    while True:
        command_line = input()
        if command_line == "End":
            break
        command, file_name, *args = command_line.split("-")
        path_to_create = os.path.join(path_task, file_name)
        command_mapper[command](path_to_create, *args)

# file_manipulator()

def directory_traversal():
    import os
    files = {}
    directory = "../"
    #directory = '/Volumes/Extreme SSD/Olya/Food/[NAN] Я Нутрициолог 2.0 (Татьяна Забалуева, Елена Малиновская) 2'
    path_dir_task = os.path.join(directory)
    for element in os.listdir(path_dir_task):
        f = os.path.join(path_dir_task, element)

        if os.path.isfile(f):
            extension = element.split(".")[-1]
            if extension not in files:
                files[extension] = []
            files[extension].append(f)

        else:
            for folder_element in os.listdir(f):
                file_name = os.path.join(f, folder_element)

                if os.path.isfile(file_name):
                    extension = folder_element.split(".")[-1]
                    if extension not in files:
                        files[extension] = []
                    files[extension].append(folder_element)

    with open(os.path.join(directory, "report.txt"), 'w') as output_file:
        for extension, file_names in sorted(files.items()):
            output_file.write(f'{extension}\n')
            for file_name in sorted(file_names):
                output_file.write(f'---{file_name}\n')


def directory_traversal_recursive():
    import os
    import shutil

    files = {".pdf": []}
    directory = '/Volumes/Extreme SSD/Olya/Food/[NAN] Я Нутрициолог 2.0 (Забалуева,Малиновская)'
    target_folder = os.path.join(directory, "pdf_files")
    os.makedirs(target_folder, exist_ok=True)


    def get_files(folder, level = 1):
        if level == -1:
            return

        for element in os.listdir(folder):
            if element.startswith('.'):
                continue

            f = os.path.join(folder, element)

            if os.path.isfile(f):
                extension = os.path.splitext(element)[1]
                if extension == ".pdf":
                    files[extension].append(f)
            else:
                get_files(f, level - 1)

    get_files(directory, -2)

    print(f"Found PDF-files: {len(files['.pdf'])}")
    print("Started coping...")

    for original_path in files[".pdf"]:
        file_name = os.path.basename(original_path)
        destination_path = os.path.join(target_folder, file_name)

        if os.path.exists(destination_path):
            base_name, ext = os.path.splitext(file_name)
            counter = 1

            while os.path.exists(destination_path):
                new_name = f"{base_name}_{counter}{ext}"
                destination_path = os.path.join(target_folder, new_name)
                counter += 1

        shutil.copy(original_path, destination_path)
    print("Done.")


