#age_categories
age=int(input("enter the age:"))
if age<=6:
    print("Kid")
elif age<=12:
    print("Child")
elif age<=17:
    print("Teenager")
else:
    print("Adult")


#vote_eligibility
age=int(input("enter the age :"))
if age>=18:
    print("Eligible for voting")
else:
    print("Not Eligible for voting")

 #swapping_two_nos_
num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
num1,num2=num2,num1
print("Before swapping first number is:",num1,"second number is:",num2)
print("After swapping first number is:",num2,"second number is:",num1)

 #sum_of_natural_nos
num=int(input("enter the number upto which you want to find the sum:"))
sum=0
for i in range(1,num+1):
    sum=sum+i
print("sum of first",num,"numbers is:",sum)





