marks1 = int(input("Enter Your Marks 1:"))
marks2 = int(input("Enter Your Marks 2:"))
marks3= int(input("Enter Your Marks 3:"))

# Check for total Percentage
total_percentaage = (100*(marks1+marks2+marks3))/300
if(total_percentaage>=40 and marks1>33 and marks2>33 and marks3>33):
    print("You are passed Sucessfully!")
else:
    print("You are Failed , And your Total Percentage is ->", total_percentaage)
 