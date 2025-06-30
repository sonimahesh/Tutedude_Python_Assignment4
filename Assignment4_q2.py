#Program for write to get uer input, write and append text to output.txt

try:
    mainText = input("Enter text to write to the file : ")
    file = open('output.txt', 'w')
    file.write(mainText)
    file.close()
    print("Data successfully written to output.txt")


    appendText = input("Enter text to append : ")
    file = open('output.txt', 'a')
    file.write("\n" + appendText)
    file.close()
    print('Data successfully append')

    file = open('output.txt', 'r')
    final_content = file.read()
    file.close()
    print(final_content)
except FileNotFoundError:
    print("output.txt not found.")