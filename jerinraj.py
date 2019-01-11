def print_factors(x):
 print("The factors of",x,"are:")
  for i in range(1, x + 1):
       if x % i == 0:
           print(i)
num = 320
print_factors(num)
# uncomment the following line to take input from the user
9
#num = int(input("Enter a number: "))
