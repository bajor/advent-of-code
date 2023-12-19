file_path = 'day_10_drawing.txt'

def count_occurrences(file_path, characters):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            occurrences = {char: content.count(char) for char in characters}
            return occurrences
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

characters_to_count = ['X', 'A']

occurrences = count_occurrences(file_path, characters_to_count)

if occurrences:
    for char, count in occurrences.items():
        print(f"Occurrences of '{char}': {count}")