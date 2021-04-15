##Password check program
##original password of the user
OriginalPassword = "topsecret"
x = -1#loop exit condition

#setting the number of attempts equal to three
for i in range(3,0,x):
    InputPassword = str(input("Enter the password : "))
    #if the entered password is correct login the user and exit the loop
    if(OriginalPassword == InputPassword):
        print("You have been logged in successfully!")
        break##loop exit condition
    #if the entered password ask the user to try again for 3 attempts
    else:
        j = i-1
        print("Oops " +str(j) + " attempts left!!")
       
