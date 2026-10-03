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

x=("1","2", "3","4", "5","6", "7", "8", "9", "10")
greater=8
for i in x:
    num=int(i)
    print("current num is",i)
    if num>greater:
        print("this is greater")
    