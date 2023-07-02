#Display the contents of the file
# $cat > geekfile.txt
def load_file(filename):
    file=open(filename,'r')
    return file.readlines()

path="C:\\Local Disk D\\DSAAT CP\\demo.txt"
print(load_file(path))

# Searching for the word in a text file
# $grep -i "UNix" geekfile.txt
def search_word(filename,word):
    for lines in load_file(filename):
        for word_lines in lines.split():
            if(word_lines==word):
                print("Word is present")
                print("Word=",word)
                return True

search_word(path,"to")
        
# $grep -c "unix" geekfile.txt
# Count the no of occurances of the word
def count_word(filename,word):
    count=0
    for lines in load_file(filename):
        for word_lines in lines.split():
            if(word_lines==word):
                count+=1
    print("Number of occurances:",count)

count_word(path,"to")

# # grep "string" FILE_PATH
def check_line(filename,string):
    for lines in load_file(filename):
        if string in lines:
            print("Yes given string is present")
            break

check_line(path,"This file")

# Searching for the word in a text file case insensitive
def search_word_case_insenstive(filename,word):
    for lines in load_file(filename):
        for word_lines in lines.split():
            if(word_lines.lower()==word.lower()):
                print("Word is present")
                print("Word=",word)
                return True

search_word_case_insenstive(path,"To")

#  Show line number while displaying the output using grep -n
# $ grep -n "unix" geekfile.txt
def line_no_of_word(filename,word):
    count_line_number=0
    for lines in load_file(filename):
        count_line_number+=1
        if word in lines:
            print(count_line_number,lines)

line_no_of_word(path,"to")

# Inverting the pattern match-
# $ grep -v "unix" geekfile.txt
def inverting_the_pattern_match(filename,word):
    for lines in load_file(filename):
        if word not in lines:
            print(lines)

inverting_the_pattern_match(path,"to")

# Matching the lines that end with a string
# $ grep "os$" geekfile.txt
def string_in_line_end(filename,word):
    for lines in load_file(filename):
        count=0
        for word_lines in lines.split()[::-1]:
            count+=1
            if(word_lines.lower()==word.lower()):
                print(lines)
            if(count==1):
                break

string_in_line_end(path,"es")

# grep -v "unix" geekfile.txt
def reverse_word(filename,word):
    for lines in load_file(filename):
        if word in lines.split():
            word=word[::-1]
    print(word)

reverse_word(path,"for")

# $grep -A[NumberOfLines(n)] [search] [file]   i.e $grep -A1 learn geekfile.txt
def n_lines_after_searched_sent(filename,word,count):
    lines_count=0
    flag=0
    for lines in load_file(filename):
        lines_count+=1
        if word in lines.split():
            break
    lines_count2=0
    while(count>=0):
        for line in load_file(filename):
            lines_count2+=1
            if((lines_count2>=lines_count) and ((lines_count2-lines_count)<=count)):
                print(line)
                count-=1


n_lines_after_searched_sent(path,"to",2)

# grep "^unix" geekfile.txt
# Starting word of sentence if matches with given word then print the sentence
def match_start(filename,word):
    for lines in load_file(filename):
        s=lines.split()
        if word in s[0]:
           print(lines)
           return

# match_start(path,"Hello!")


