from numpy import sum, array, random, mean

# sum 0 - 100
print(sum(array(range(100))))

# sum 0 - x
x = int(input("Input x, please:"))
print(sum(array(range(x))))

# average among 100 random numbers
random_array = random.randint(99, size= 100)
print("Mean =", mean(random_array))
