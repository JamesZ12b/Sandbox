MIN_LENGTH = 6
password = input("Enter the password: ")
length = len(password)
while (length < MIN_LENGTH):
    print("Invaild length")
    password = input("Enter the password: ")
    length = len(password)
print('*' * length)