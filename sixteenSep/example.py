age = int(input("AGE:"))
id = input("enter Id(yes/no)")

if age >= 18:
    if id == "yes":
        print("You can vote")
    else:
        print("You need an ID")
else:
    print("You are too young")


# Nested loops

for row in range(1,4):
    for column in range(1,5):
        print(f"{row} X {column} = {row*column}")
    print("-----------------------------")

# while nested loop
row = 1
while row < 6:
    column = 1
    while column < 5:
        print(f"{row} X {column} = {row*column}")
        column+=1
    print("+++++++++++++++++++++++++++++")
    row+=1


# Branching statements 


