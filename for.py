
# find all numbers > 10 and count the occurances
print("-----")

listOfNumbers = [1,3,5,6,10,234,44,55,66,77]
limit = 10 # limit of the for
count = 0 # occurances
sum = 0 # value of the occurances

for n in listOfNumbers:
    if  n > limit:
        count += 1
        sum += n
        
print("count = ", count)
print("sum = ", sum)
print("-----")


# sum all the possibile combination

prevValue = 0

for n in listOfNumbers:
    prevValue += n

print(prevValue)


