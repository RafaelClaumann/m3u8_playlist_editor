def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().split('\n')
    return lines

def save_file(file_path, lines):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("\n".join(lines))
