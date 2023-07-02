def load_file(filename):
    file=open(filename,'r')
    return file.readlines()

# $grep -c "unix" geekfile.txt
# Count the no of occurances of the word
def count_word(filename,word):
    count=0
    for lines in load_file(filename):
        for word_lines in lines.split():
            if(word_lines==word):
                count+=1
    print("Number of occurances:",count)

path=input("Enter the file path:")
word=input("Enter the word:")
count_word(path,word)

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
