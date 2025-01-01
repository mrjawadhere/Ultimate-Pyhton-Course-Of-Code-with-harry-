p1 = "Make a lot of money"
p2 = "Click here"
p3 = "buy now" 
p4 = ("Subscribe this channel")

a = input("Enter a Comment:")

if((p1 in a) or (p2 in a) or (p3 in a) or (p4 in a)):
    print("This comment is a Spam!")
else:
    print("This Comment is not a spam")