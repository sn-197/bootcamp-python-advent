import os


def find_txt_file(folder_path: str) -> str:
    """Returns the first .txt file found in the folder."""
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            return os.path.join(folder_path, file_name)
    return ""


def count_file_stats(file_path: str) -> dict:
    line_count = 0
    word_count = 0
    char_count = 0

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line_count += 1
            word_count += len(line.split())
            char_count += len(line)

    return {
        "lines": line_count,
        "words": word_count,
        "characters": char_count
    }


if __name__ == "__main__":
    folder_path = input("Enter folder path: ").strip()

    txt_file = find_txt_file(folder_path)

    if not txt_file:
        print("No .txt file found in the folder.")
    else:
        print(f"Reading file: {txt_file}")
        stats = count_file_stats(txt_file)

        print("\nFile Statistics:")
        print(f"Lines: {stats['lines']}")
        print(f"Words: {stats['words']}")
        print(f"Characters: {stats['characters']}")