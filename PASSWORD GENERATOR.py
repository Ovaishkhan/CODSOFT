import random, string

user_length=int(input("Enter length of the password: "))
def generate_pass():
    global password
    letters= string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(letters) for _ in range(user_length))
    print(f"Generated Password: {password}")

# Get the desired password length from the user
if user_length < 4:
    print("Password length should be at least 4 characters for complexity.")
else:
    # Generate and display the password
    generate_pass()
  
    



     