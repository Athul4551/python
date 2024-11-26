def read():
    f=open("exa.txt")
    print(f.read())
    f.close
def write(content):    
    f=open("exa.txt",'w')
    f.write(content)
    f.close()
def append(content):    
    f=open("exa.txt",'a')
    f.write(content)
    f.close()
def creat_file(file_name1):
    f=open(file_name1,'x')    

# content="hello ibru"
# write(content)
# read()
# file_name1="sim.txt"
# creat_file(file_name1)
todo_list=[{"task":"read from the file","function":read}
           {"task":"write to the file","function":write}
           {"task":"append to the file","function":append}
           {"task":"create a file","function":creat_file}]

