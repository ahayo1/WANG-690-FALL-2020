"""
Prompts a user to enter 10 integers. If the user enters anything other than integers, 
remind her that only integers are allowed and let her retry. Don't allow the user to enter more 
than 10 or less than 10 integers. Display the 10 integers back to the user at the end. 
Calculate the following statistics from the 10 integers entered:

Minimum
Maximum
Range
Mean
Variance
Standard Deviation
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
    # Store value in list
    list_int.append(value)
  # Only catch the error of a non-int
  except ValueError as e:
    print("The value you entered is not an integer.")



# Display numbers the user entered
############################################################
print("\nYou entered the following integers:\n-------------------------------------")

# Loop through each value in the list and display it
for i in range(len(list_int)):
  print(list_int[i])




# Caluculate Statistcs
############################################################

import numpy as np

print("\nCalculated Statistics:\n------------------------")

# Use predefined functions for the statitics
print("Minimum:", min(list_int))
print("Maximum:", max(list_int))
print("Range:", max(list_int)-min(list_int))
print("Mean:", sum(list_int)/len(list_int))
print("Variance:", np.var(list_int))
print("Standard Deviation:", np.std(list_int))
