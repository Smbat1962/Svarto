def create_file(filename):
    try:
        with open(filename, 'w') as f:
            f.write('3 + 5 = ')
        print("File " + filename + " created successfully.")
    except IOError:
        print("Error: could not create file " + filename)
 
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            contents = f.read()
            print(contents)
    except IOError:
        print("Error: could not read file " + filename)
 
def append_file(filename, text):
    try:
        with open(filename, 'a') as f:
            f.write(text)
        print("After appended solution ")
    except IOError:
        print("Error: could not append to file " + filename)

if __name__ == '__main__':
    filename = "example.txt"
 
    create_file(filename)
    read_file(filename)
    append_file(filename,'8')
    read_file(filename)


f = open("example.txt", "w")
f.write("15 + 27 = ")
f = open("example.txt", "r")
print (f.read())
f= open("example.txt","a")
f.write("42")
f = open("example.txt", "r")
print (f.read())
    