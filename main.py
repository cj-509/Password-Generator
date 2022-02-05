import secrets
import string


upper = string.ascii_uppercase
lower = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation

#add together all uppercase, lowercase, numbers(digits), and the symbols(*/-&^%$) together to the 'res' var
res = upper + lower + digits + symbols
char = int(input("Enter the number of characters for your password: ")) #getting the charcther lenght from the user
while True:
    if char < 8: # character leght cannot be < (less than) 8 
        print("Sorry, the lenght of your password cannot be less than 8 character :(")
        break
    else:
        #joinning together the character that's equals to the number of the lenght of the password
        result = ''.join(secrets.choice(res) for i in range(char))
        print("=" *30 + '\n')
        print(f'Your password is: {result} \n')
        print("=" *30 + '\n')
        break