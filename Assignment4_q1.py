#Program for read file and manage exception if file not found.

try:
    file = open('sample.txt', 'r')
    file_content = file.read()
    print(file_content)
except FileNotFoundError:
    print("sample.txt file not found.")
