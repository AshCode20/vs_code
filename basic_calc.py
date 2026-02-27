#input numbers
input_data = input("Enter the numbers with space in between:")
converted = []
numbers = input_data.split()

#convert the numbers into float
for value in numbers:
    converted.append(float(value))
print(converted)

if len(converted) == 0:
    print ("Your list is empty. ")


#calculating mean
def mean_calc(converted): 
    value = 0 
    total=0
    while(value <= len(converted)):
        total = value + total
        value += 1
        
    mean = total / len(converted)
    return mean

print(mean_calc(converted))