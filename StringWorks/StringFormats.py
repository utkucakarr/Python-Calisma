# string concat
name = "Utku"
surname = "Çakar"
age = 26
message = "My name is: " + name + " " + surname + " I'm " + str(age) + "years old."
print(message)

#string format

message1 = "My name {0} {1}. I am {2} years old.".format(name, surname, age)
print(message1)

# f-string

message1 = f"My name {name} {surname}. I am {age} years old."

