print("Enter two numbers ")
num1=int(input("1st number: "))
num2=int(input("2nd number: "))
#nums=2^num1
#print(nums)
choice=['+','-','*','/','%']


print(choice)
user_choice=input("Enter a operator to perform your desired operation: ")
if user_choice=='+':
    sum=num1+num2
    print("sum of two numbers: ",+sum)
    
elif user_choice=='-':
    sub=num1-num2
    print(" subtraction: ",+sub)

elif user_choice=='*':
    mul=num1*num2
    print(" Multiplications: ",+mul)

elif user_choice=='/':
    div=num1/num2
    print(" Devision: ",+div)


elif user_choice=='%':
    mod=num1%num2
    print(" mod: ",+mod)

else:
    print("input unidentified")

