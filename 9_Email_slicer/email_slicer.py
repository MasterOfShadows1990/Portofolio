email = input("Enter your email: ")

index = email.index("@")

username = email[:index]
domain = email[index + 1 :]

print(f"Your username is {username} and domain is {domain}")

f_name = input("Enter your first name: ")
s_name = input("Enter your second name: ")

print(f"Nice to meet you {f_name} {s_name}")

bank_account = 0
 
while bank_account <= 0:
    bank_account = float(input("Enter how much money you want to draw: "))
    if bank_account <= 0:
        print("The amount can't be less than or equal to zero!")
print(f"There it is the amount you ask for: {bank_account} $")