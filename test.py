# users = {
# 	"alice": "password123",
# 	"bob": "securepass456",
# }

# username = input("Enter your username: ")


# if username in users:
#     password = input("Enter your password: ")
#     if password==users[username]:
#         print("logged in")
#     else:
#         print("incor")
    
# else:
#     print("nope")
    
    
# people={"name": "Alice", "age": 25, "contact": "alice@example.com"},
# print (people['name'])

# x=("1","2", "3","4", "5","6", "7", "8", "9", "10")
# greater=8
# for i in x:
#     num=int(i)
#     print("current num is",i)
#     if num>greater:
# #         print("this is greater")
    
# try:
#     # Code that may raise exceptions
#     num = int(input("Enter a positive number: "))
#     if num <= 0:
#         raise ValueError("Number must be positive!")
#     result = 10 / num
# except Exception as e:
#     # Handles value conversion errors or custom raised ValueError
#     print(f"Error type: {type(e).__name__}")
#     print(f"Error message: {e}")
# finally:
#     # Executes regardless of whether an exception occurred or not
#     print("Execution completed.")
    
name=None   

def print_details(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_details(Name="Alice", Age=25, Role="Developer")

my_dict = {"name": "Alice", "age": 25, "city": "New York"}