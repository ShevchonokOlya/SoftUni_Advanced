import re

from costants import path_dir
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

create_file_list_of_words()
word_counter_in_file()