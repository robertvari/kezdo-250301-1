username = "csaba"
password = "testpas123"

print("-"*50, "Wellcome to our webshop", "-"*50)
print("Please log in to continue")

input_username = input("Username: ")
input_password = input("Password: ")

#            True                          True
if username == input_username and password == input_password:
    print("You are logged in :)))")
else:
    print("Username or Password is not correct :(")