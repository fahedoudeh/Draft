def greet_user(name):
    print(f"Welcome {name} at Codezilla Python Course Enjoy your Learning Journey")

user_input = input("Enter your name: ")    

greet_user(user_input)

def reverse_text(text):
    return text[::-1].lower()

print(reverse_text(user_input))