values = []

print("Hey, I can find all the numbers that are devisible by 3.")
a = input("Enter Values: ").split()

print()



for i in a:
    values.append(int(i))


#Shortcut for all the above code
# values= [int(i) for i in input("Enter Values: ").split()]

final_list = []

for i in values:
    if (i%3==0):
        final_list.append(int(i))
    

print(final_list)
print()