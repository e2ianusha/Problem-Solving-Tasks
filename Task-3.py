Task-3:

'''

Program that takes list and returns two lists having the odd and even numbers in the list

'''



# Python code to split into even and odd lists 

# Funtion to split 

def splitevenodd(A): 

   evenlist = [] 

   oddlist = [] 

   for i in A: 

      if (i % 2 == 0): 

         evenlist.append(i) 

      else: 

         oddlist.append(i) 

   print("Even lists:", evenlist) 

   print("Odd lists:", oddlist) 

  

# Driver Code 

A=list()

n=int(input("Enter the size of the First List ::"))

print("Enter the Elements of First  List ::")

for i in range(int(n)):

   k=int(input(""))

   A.append(k)

splitevenodd(A) 





Output:

Enter the size of the First List ::8

Enter the Elements of First  List ::

10

501

22

37

100

99

87

351

Even lists: [10, 22, 100]

Odd lists: [501, 37, 99, 87, 351]









'''



Pyhton program that takes list and returns prime numbers in list



'''



# Given number list

numberList = [10, 501, 22, 37, 100, 99, 87, 351]

 

# Empty list

ansList = []

 

# Iterate through each number 

# form the list

for num in numberList :

     

    # 0 and 1 is not a 

    # prime number

    # so skip this number

    if num == 0 or num == 1 :

        continue

         

    # loop from 2 to half of the

    # given number

    for i in range(2, num // 2 + 1) :

 

        # If number is divisible by any

        # number (i) then it is not

        # a prime number

        if num % i == 0 :

            break

 

    # If not divisible then it is

    # a prime number

    else :

         

        # if number is prime

        # then append to the list

        ansList.append(num)

 

# If list is non-empty then

# print th elements

if len(ansList) :

     

    print("Prime Number : ",end = "-> ")

     

    # printing the prime number

    # from the ansList

    for ans in ansList :

        print(ans, end = “[, ]”)

     

else :

    print("No any number from the given list is Prime")



Output:

Prime Number : -> 37,



'''

Python program to find out happy numbers in the given list

'''



#Initialise an array

a=[10, 501, 22, 37, 100, 99, 87, 351]



#Empty array to hold the happy numbers

b = []



#Define happy numbers function

def is_happy(a):

    for i in range (len(a)):

        sum = a[i]

        while sum!=1 and sum !=4:

            tempsum = 0

            for digit in str(sum):

                tempsum += int(digit) ** 2   

            sum = tempsum

        if sum == 1:

            b.append(a[i])

    return b

print("Happy numbers are:",is_happy(a))



print("The count of happy numbers in the list are:" +str(len(b)))





 Output:

Happy numbers are: [10, 100]

The count of happy numbers in the list are:2







'''



Python program to find sum of first and last digit of an integer



'''



# We have a number.

number = 1247

 

# Assigning last digit of the number in res

# variable.

res = number % 10

 

# Now, continue a loop until

# the number becomes less than 9.

while number > 9:

 

    # integer division of the number and reassigning

    # it.

    number = number // 10

 

# Here, our number only contain one digit.

# So, add this number in res variable.

res += number

 

# Now, display our output

print('Addition of first and last digit of number is', res)





Output:

Addition of first and last digit of number is 8


# Python program to print duplicates from a list of integers

lis1 = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
lis2 = [2,5,6,5,9,2]
lis3 = [7,3,9,7]

uniqueList1 = []
uniqueList2 = []
uniqueList3 = []
duplicateList1 = []
duplicateList2 = []
duplicateList3 = []

for i in lis1:
	if i not in uniqueList1:
		uniqueList1.append(i)
	elif i not in duplicateList1:
		duplicateList1.append(i)

print(duplicateList1)

for i in lis2:
	if i not in uniqueList2:
		uniqueList2.append(i)
	elif i not in duplicateList2:
		duplicateList2.append(i)

print(duplicateList2)


for i in lis3:
	if i not in uniqueList3:
		uniqueList3.append(i)
	elif i not in duplicateList3:
		duplicateList3.append(i)

print(duplicateList3)



output:
[1, 2, 5, 9]
[5, 2]
[7]



'''
Python program to find the first non-repeated numbers in the list of given integers
'''


# Define a function to find the first non-repeated element in a list
def first_non_repeated_el(lst):
    # Create a dictionary 'ctr' to count the occurrences of each element
    ctr = {}
    # Iterate through the elements in the list
    for i in lst:
        # If the element is already in the dictionary, increment its count
        if i in ctr:
            ctr[i] += 1
        # If the element is not in the dictionary, add it with a count of 1
        else:
            ctr[i] = 1
    # Iterate through the elements in the list again
    for i in lst:
        # Find the first element with a count of 1 (non-repeated)
        if ctr[i] == 1:
            return i
    # If no non-repeated element is found, return None

# Create a list of numbers
nums =  [1, 2, 3, 4, 5, 6, 7, 8]

# Print the original list of numbers
print("Original list:")
print(nums)

# Call the first_non_repeated_el function with the list and store the result in 'result'
result = first_non_repeated_el(nums)

# Print the result, which is the first non-repeated element in the list
print("First non-repeated element in the said list:")
print(result)

# Create another list of numbers with some repeated elements
nums =  [1, 2, 3, 1, 2, 4, 5, 6, 7, 8]

# Print the original list of numbers
print("\nOriginal list:")
print(nums)

# Call the first_non_repeated_el function with the second list and store the result in 'result'
result = first_non_repeated_el(nums)

# Print the result, which is the first non-repeated element in the list
print("First non-repeated element in the said list:")
print(result)

# Create another list of numbers with more repeated elements
nums =  [1, 1, 2, 3, 1, 2, 3, 8, 8]

# Print the original list of numbers
print("\nOriginal list:")
print(nums)

# Call the first_non_repeated_el function with the third list and store the result in 'result'
result = first_non_repeated_el(nums)

# Print the result, which is the first non-repeated element in the list
print("First non-repeated element in the said list:")
print(result) 

output:
Original list:
[1, 2, 3, 4, 5, 6, 7, 8]
First non-repeated element in the said list:
1

Original list:
[1, 2, 3, 1, 2, 4, 5, 6, 7, 8]
First non-repeated element in the said list:
3

Original list:
[1, 1, 2, 3, 1, 2, 3, 8, 8]
First non-repeated element in the said list:
None




# python3 code  to implement the approach
 
def findMin(arr, N):
     
    min_ele = arr[0];
 
    # Traversing over array to
    # find minimum element
    for i in range(N) :
        if arr[i] < min_ele :
            min_ele = arr[i]
 
    return min_ele;
 
# Driver program
arr = [5, 6, 1, 2, 3, 4]
N = len(arr)
 
print(findMin(arr,N))

output:
1



# Python3 program to Find total number of triplets in a temp_list with given k
 
def findTriplets(lst, k):
    triplet_count = 0
    final_temp_list =[]
     
    for i in range(0, len(lst)-1): 
         
        s = set() 
        temp_list = []
 
        # Adding first element
        temp_list.append(lst[i])
 
        curr_k = k - lst[i] 
         
        for j in range(i + 1, len(lst)): 
             
            if (curr_k - lst[j]) in s: 
                triplet_count += 1
                 
                # Adding second element
                temp_list.append(lst[j])
 
                # Adding third element
                temp_list.append(curr_k - lst[j])
                 
                # Appending tuple to the final list
                final_temp_list.append(tuple(temp_list))
                temp_list.pop(2)
                temp_list.pop(1)
            s.add(lst[j])
             
    return final_temp_list
     
# Driver Code
lst = [10,20,30,9]
k = 59
print(findTriplets(lst, k))

output:
[(20, 9, 30)]


#Python program to find if there is sublist whose sum is zero
def subArrayExists(arr, n):
    for i in range(n):
        # Starting point of the subarray and
        # sum is initialized with the first element of subarray
        sum = arr[i]
        if sum == 0:
            return True
        for j in range(i + 1, n):
            # We are finding the sum till the jth index
            # starting from the ith index
            sum += arr[j]
            if sum == 0:
                return True
    return False
 
# Driver's code
if __name__ == "__main__":
    arr = [4, 2, -3, 1, 6]
    N = len(arr)
 
    # Function call
    if subArrayExists(arr, N):
        print("Found a subarray with 0 sum")
    else:
        print("No Such Sub Array Exists!")

output:
Found a subarray with 0 sum




