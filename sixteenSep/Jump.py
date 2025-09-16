
for num in range(1,5):
    print(num)

print("_______________________")

# break (Exists/Break the loop)
for num in range(1,5):
    if num == 3:
        break
    print(num)

print("+++++++++++++++++++++++++")
# Continue: skips current iterarion
for num in range(1,5):
    if num == 3:
        continue
    print(num)


print("-------------------------------------")

#pass: acts as a placeholder

emp_salary = 10000
if emp_salary > 10000:
    pass 
