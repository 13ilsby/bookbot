def main():

    file_path = "books/frankenstein.txt"
    file_contents = get_file_contents(file_path)
    print(file_contents)

def get_file_contents(file_path):
    with open(file_path) as f:
        return f.read()

main()


