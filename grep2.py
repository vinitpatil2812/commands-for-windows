# Display the contents of the file
# $cat > geekfile.txt
def load_file(filename):
    file = open(filename, 'r')
    return file.readlines()


# Searching for the word in a text file
# $grep -i "UNix" geekfile.txt
def search_word(filename, word):
    for lines in load_file(filename):
        for word_lines in lines.split():
            if (word_lines == word):
                print("Word is present")
                print("Word=", word)
                return True



# $grep -c "unix" geekfile.txt
# Count the no of occurances of the word
def count_word(filename, word):
    count = 0
    for lines in load_file(filename):
        for word_lines in lines.split():
            if (word_lines == word):
                count += 1
    print("Number of occurances:", count)


# # grep "string" FILE_PATH
def check_line(filename, string):
    for lines in load_file(filename):
        if string in lines:
            print("Yes given string is present")
            break
        else:
            print("Not present")


# Searching for the word in a text file case insensitive
def search_word_case_insenstive(filename, word):
    for lines in load_file(filename):
        for word_lines in lines.split():
            if (word_lines.lower() == word.lower()):
                print("Word is present")
                print("Word=", word)
                return True



#  Show line number while displaying the output using grep -n
# $ grep -n "unix" geekfile.txt
def line_no_of_word(filename, word):
    count_line_number = 0
    for lines in load_file(filename):
        count_line_number += 1
        if word in lines:
            print(count_line_number, lines)


# Inverting the pattern match-
# $ grep -v "unix" geekfile.txt
def inverting_the_pattern_match(filename, word):
    for lines in load_file(filename):
        if word not in lines:
            print(lines)


# Matching the lines that end with a string
# $ grep "os$" geekfile.txt
def string_in_line_end(filename, word):
    for lines in load_file(filename):
        count = 0
        for word_lines in lines.split()[::-1]:
            count += 1
            if (word_lines.lower() == word.lower()):
                print(lines)
            if (count == 1):
                break



# grep -v "unix" geekfile.txt
def reverse_word(filename, word):
    for lines in load_file(filename):
        if word in lines.split():
            word = word[::-1]
    print(word)

# $grep -A[NumberOfLines(n)] [search] [file]   i.e $grep -A1 learn geekfile.txt
def n_lines_after_searched_sent(filename, word, count):
    lines_count = 0
    flag = 0
    for lines in load_file(filename):
        lines_count += 1
        if word in lines.split():
            break
    lines_count2 = 0
    while (count >= 0):
        for line in load_file(filename):
            lines_count2 += 1
            if ((lines_count2 >= lines_count) and ((lines_count2 - lines_count) <= count)):
                print(line)
                count -= 1




# grep "^unix" geekfile.txt
# Starting word of sentence if matches with given word then print the sentence
def match_start(filename, word):
    for lines in load_file(filename):
        s = lines.split()
        if word in s[0]:
            print(lines)
            return

print("\n1. Enter 1 for loading the file \n 2. Enter 2 for searching a word in the text file \n 3. Enter 3 for Counting the number of occurences of the word \n 4. Enter 4 for checking if the string is present or not \n 5. Enter 5 for searching word in a text file(CASE SENSITIVE) \n 6. Enter 6 for Showing the line number while displaying the output \n 7. Enter 7 for inverting the word if matched \n  Enter 8 to check if the text ends with the given string \n 9. Enter 9 for reversing the word \n 10. Enter 10 for printing the lines after given word\n 11. Enter 11 for checking if the text starts with the given word")

n=21
while(n != 0):
    n = int(input("Enter the choice: "))
    if (n == 1):
        path = input("Enter the file path: ")
        load_file(path)

    if(n==2):
        path = input("Enter the file path: ")
        string=input("Enter the word for  search")

        search_word(path,string)
    if(n==3):
        path = input("Enter the file path: ")
        string = input("Enter the word for checking number of occurences: ")

        count_word(path, string)

    if(n==4):
        path = input("Enter the file path: ")
        string = input("Enter the string: ")

        check_line(path, string)

    if(n==5):
        path = input("Enter the file path: ")
        string = input("Enter the word for search (CASE INSENSITIVE): ")

        search_word_case_insenstive(path, string)

    if(n==6):
        path = input("Enter the file path: ")
        string = input("Enter the word: ")

        line_no_of_word(path,string)

    if(n==7):
        path = input("Enter the file path: ")
        string = input("Enter the word: ")
        inverting_the_pattern_match(path,string)
    if(n==8):
        path = input("Enter the file path: ")
        string = input("Enter the word: ")

        string_in_line_end(path,string)

    if(n==9):
        path = input("Enter the file path: ")
        string = input("Enter the word: ")
        reverse_word(path,string)
    if(n==10):
        path = input("Enter the file path: ")
        string = input("Enter the word: ")
        count=int(input("Enter the count"))

        n_lines_after_searched_sent(path,string,count)

    if(n==11):
        path = input("Enter the file path: ")
        string = input("Enter the word: ")

        match_start(path,string)