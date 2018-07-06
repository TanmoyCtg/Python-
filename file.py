with open("text.txt", "w") as f:
    print (f.write("hello, Python\n"))


f=open("text.txt","a")
print (f.write("hello,joy"))
f.close()
