import math 

#input numbers
input_data = input("Enter the numbers with space in between:")
converted = []
numbers = input_data.split()

#convert the numbers into float
for value in numbers:
    converted.append(float(value))


if len(converted) == 0:
    print ("Your list is empty. ")


#calculating mean
def mean_calc(converted,): 
    value = 0 
    total=0
    for value in converted:
        total = value + total
        value += 1
        
    mean = total / len(converted)
    return mean


print("The mean of the numbers are:",mean_calc(converted))
mean_value=mean_calc(converted )

#calculating sample variance
def sample_variance(converted, mean_value):
    total = 0
    for value in converted:
        var = (value-mean_value)**2
        total = var + total
    return total
loop_var = sample_variance(converted, mean_value)
if len(converted) <= 1:
    print("sample variance not defined for samples with size less than 2")
else:
    variance = (1/(len(converted)-1))*loop_var
    print("The sample variance of the numbers are: " ,variance)

#calculate standard deviation
def std_dev(converted, variance):
    standard_deviation = math.sqrt(variance)
    return standard_deviation
print("The standard deviation of the numbers is: " ,std_dev(converted, variance))

#calculate median
def median(converted):
    sorted_list = sorted(converted)

    n = len(sorted_list)
    if n%2 == 0:
        first_value = n//2
        second_value = n//2 - 1
        median_value = (sorted_list[first_value] + sorted_list[second_value]) / 2
    else:
        value = n//2 
        median_value = sorted_list[value]
    return median_value
print("The median of the numbers is: ",median(converted))

#calculating range
def range(converted):
    maximum = (max(converted))
    minimum = (min(converted))
    range_value = maximum - minimum
    return range_value
print("The range of the numbers are:", range(converted))

#calculating mode
def mode(converted):
    frequency = {}
    for value in converted:
        if value in frequency:
            print(value)
            frequency[value] += 1
        else:
            frequency[value] = 1
    max_frequency = max(frequency.values())
    modes = []
    for key, count in frequency.items():
        if count == max_frequency:
            modes.append(key)
    if max_frequency == 1:
        return "No mode (all value occur once)"
    return modes

print("The mode of the data is: ", mode(converted))

