"""
Assignment-02 .py File

Description: Prompts a user to enter 10 integers. If the 
user enters anything other than integers, remind her that only 
integers are allowed and let her retry. Don't allow the user 
to enter more than 10 or less than 10 integers. Display the 10 
integers back to the user at the end. Calculate the following statistics 
from the 10 integers entered:

- Minimum
- Maximum
- Range
- Mean
- Variance
- Standard Deviation
"""

# Ask the users for x number of integers
############################################################

i = 1
x = 10 # the number of integers you want, can be easily changed

list_int = [] # empty list to hold integers after being verified

print("Enter " + str(x) + " integers:\n--------------------")

# Only want x number of integers
while i <= x:
    # Ask user for input
    value = input("\nPlease enter an integer:\n")
    try:
      value = int(value)
      i += 1
      list_int.append(value)
    # Only catch the error of a non-int
    except ValueError as e:
      print("The value you entered is not an integer.")



# Display numbers the user entered
############################################################
# Display the integers back to the user
print("\nYou entered the following integers:\n-------------------------------------")

for i in list_int:
  print(i)




# Caluculate Statistcs
############################################################

# Minimum, Maximum, Sum, Length
min = list_int[0]
max = list_int[0]
s = 0    # s will be used for sum
l = 0    # l will be used for length

for i in list_int:
  # assign new minimum if value is less than current min
  if i < min:
    min = i

  # assign new max if value is greater than current max  
  if i > max:
    max = i
  
  # add all of the values together in preperation for mean
  s = s + i

  l = l + 1



# Variance
# Pass through the list of values, sum of values within the list, and the length of the list
def variance(list_name,sum_val, len_val):
  # calculate average to be used later
  average = sum_val/len_val

  # prepare to calculate variance
  a=[]
  for i in list_name:
    a.append((i-average)**2)

  # get the sum and length of the new list that is being used for variance
  len_a = 0
  sum_a = 0
  for i in a:
    len_a = len_a + 1
    sum_a = sum_a + i

  # return the variance
  return sum_a/len_a


# Standard Deviation
# Pass through the list of values, sum of values within the list, and the length of the list
def std_dev(list_name, sum_val, len_name):
  # calculate average of list to be used later
  average = sum_val/len_name

  # if there is less/only one value, the standart dev will be 0
  if len_name <= 1:
    return 0.0
  
  

  # Calculate Standard Deviation
  top_half = 0.0

  for i in list_name:
    top_half += (i-average)**2
  sd = (top_half/len_name)**(1/2)

  # return the standard deviation
  return sd


# Display the Statistcs
############################################################
print("\nCalculated Statistics:\n------------------------")

print("Minimum:", min)
print("Maximum:", max)
print("Range:", max-min)
print("Mean:", s/l)
print("Variance:", variance(list_int,s,l))
print("Standard Deviation:", std_dev(list_int,s,l))

