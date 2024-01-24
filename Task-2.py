Task-2



'''


Program to print pyramid of numbers from 1 to 20 using for loop


'''

rows = int(input("Enter number of rows: "))


k = 0


for i in range(1, rows+1):

    for space in range(1, (rows-i)+1):

        print(end="  ")

   

    while k!=(2*i-1):

        print(i, end="")

        k += 1

   
    k = 0

    print( )


Output :



Enter number of rows: 20

                                       1

                                      222

                                     33333

                                    4444444

                                   555555555

                                  66666666666

                                 7777777777777

                                888888888888888

                               99999999999999999

                    10101010101010101010101010101010101010

                  111111111111111111111111111111111111111111

                1212121212121212121212121212121212121212121212

              13131313131313131313131313131313131313131313131313

            141414141414141414141414141414141414141414141414141414

          1515151515151515151515151515151515151515151515151515151515

        16161616161616161616161616161616161616161616161616161616161616

      171717171717171717171717171717171717171717171717171717171717171717

    1818181818181818181818181818181818181818181818181818181818181818181818

  19191919191919191919191919191919191919191919191919191919191919191919191919

202020202020202020202020202020202020202020202020202020202020202020202020202020







'''


Program to calculate total number of vowels and count of each individual vowel A,E,I,O,U in the string 'Guvi Geeks Network Private Limited'


'''

# to calculate total number of vowels in the given string

data = input("Enter a string : ")

count = 0

# iterate over the string

for data in data:

    if data == 'a' or data == 'e' or data == 'i' or data == 'o' or data == 'u':

        count = count + 1

# print the total vowels in a string

print("Number of vowels in the string : ", count)



# Program to count the number of each vowels


# string of vowels

vowels = 'aeiou'



ip_str = 'Guvi Geeks Network Private Limited'



# make it suitable for caseless comparisions

ip_str = ip_str.casefold()



# make a dictionary with each vowel a key and value 0

count = {}.fromkeys(vowels,0)



# count the vowels

for char in ip_str:

   if char in count:

       count[char] += 1



print(count)





Output:

Enter a string : Guvi Geeks Network Private Limited

Number of vowels in the string :  12

{'a': 1, 'e': 5, 'i': 4, 'o': 1, 'u': 1}





'''

Program that takes string and returns string with all the vowels removed


'''

string = input("Enter any string: ")



newstr = string;



print("\nRemoving vowels from the given string");



vowels = ('a', 'e', 'i', 'o', 'u');



for x in string.lower():

    

    if x in vowels:

        

        newstr = newstr.replace(x,"");



print("New string after successfully removed all the vowels:");



print(newstr);





Output:

Enter any string: Hello I am Anusha

Removing vowels from the given string

New string after successfully removed all the vowels:

Hll I m Ansh







'''

Program that takes string and returns number of unique characters in it



'''

def countDis(str):

    # Create an empty dictionary to store the frequency of each character

    freq = {}

 

    # Iterate over each character in the string

    for char in str:

        # Increment the frequency count for the character in the dictionary

        freq[char] = freq.get(char, 0) + 1

 

    # Return the number of distinct characters in the string

    return len(freq)

 

 

# Driver Code

if __name__ == "__main__":

    # Given string S

    S = "geeksforgeeks"

    # Call the countDis function and print the result

    print(countDis(S))





Output :

7





'''

Program that takes string and returns true if its palindrome, false otherwise



'''





# function which return reverse of a string

 

def isPalindrome(s):

    return s == s[::-1]

 

 

# Driver code

s = "malayalam"

ans = isPalindrome(s)

 

if ans:

    print("True")

else:

    print("False")





Output:

True





'''

Program that takes string and returns common longest substring between them



'''



# Import SequenceMatcher from difflib

from difflib import SequenceMatcher



# Function to find longest common substring

def longest_Substring(s1,s2):



  # Create sequence matcher object

  seq_match = SequenceMatcher(None,s1,s2) 

  

  # Find longest matching substring

  match = seq_match.find_longest_match(0, len(s1), 0, len(s2))



  # If match found, return substring

  if (match.size!=0):  

    return (s1[match.a: match.a + match.size])

  

  # Else no match found

  else:

    return ('Longest common sub-string not present')



# Test strings  

s1 = 'abcdefgh'

s2 = 'xswerabcdwd'



# Print original strings 

print("Original Substrings:\n",s1+"\n",s2)



# Print message  

print("\nCommon longest sub_string:")



# Print longest common substring

print(longest_Substring(s1,s2)) 





Output :

Original Substrings:

 abcdefgh

 xswerabcdwd



Common longest sub_string:

abcd







'''

Program that takes string and returns most frequent character in it



'''



import string



def find_max_letter_count(word):



# enter the string in lowercase

    alphabet = string.ascii_lowercase

    dictionary = {}



    for letters in alphabet:

        dictionary[letters] = 0



    for letters in word:

        dictionary[letters] += 1



    dictionary = sorted(dictionary.items(), 

                        reverse=True, 

                        key=lambda x: x[1])



    for position in range(0, 26):

        print (dictionary[position])

        if position != len(dictionary) - 1:

            if dictionary[position + 1][1] < dictionary[position][1]:

                break



find_max_letter_count("dakshika")



Output:

('a', 2)

('k', 2)





'''

Program that takes string and returns true if its anagram of another string, false otherwise



'''



# function to check if two strings are

# anagram or not 

def check(s1, s2):

     

    # the sorted strings are checked 

    if(sorted(s1)== sorted(s2)):

        print("True") 

    else:

        print("False")         

         

# driver code  

s1 ="listen"

s2 ="silent"

check(s1, s2)





Output:

True





'''

Program that takes string and returns number of words in it

'''



# Python3 code to demonstrate

# to count words in string

# using split()

 

# initializing string

test_string = "Guvi is best online learning Portal"

 

 

# printing original string

print("The original string is : " + test_string)

 

# using split()

# to count words in string

res = len(test_string.split())

 

# printing result

print("The number of words in string are : " + str(res))

print("The number of words in string are : ", len(test_string))



Output:

The original string is : Guvi is best online learning Portal

The number of words in string are : 6

The number of words in string are :  35