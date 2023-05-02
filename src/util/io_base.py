import os

def write_text(text: str, file_path: str):
    directory = os.path.dirname(file_path)

    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(file_path, 'w') as file:
        file.write(text)