import os
f= open("today.txt","a")
f.write("Hello")
print (os.path.exists("today.txt"))
f.close()
if os.path.exists("today.txt"):
    os.remove("deep.txt")
    print ("file removed")
else:
    print ("file not found")