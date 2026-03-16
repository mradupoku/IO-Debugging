db = open("output.txt", "w")
a = "Hello"
b = "How do you do?"
db.write(a + ", " + b + "\n")
db.close()

print(a + ", " + b)
