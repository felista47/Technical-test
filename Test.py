#Write a query that will display the results below (Note: some columns might be renamed but use the column names above). 
#It should only show 2020 data and order by driver points.

# SELECT 
#     grid, 
#     position, 
#     fastest_lap, 
#     points, 
#     driver_name, 
#     race_name, 
#     time, 
#     year, 
#     team_name, 
#     race_date AS date
# FROM results
# JOIN drivers ON results.driver_id = drivers.driver_id
# JOIN races ON results.race_id = races.race_id
# JOIN constructors ON results.constructor_id = constructors.constructor_id
# WHERE year = 2020
# ORDER BY points DESC;


#.Write a Python function that checks whether a word or phrase is palindrome or not.
def palindrome(string):
  return string == string[::-1]
palindrome("madam")


#Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)


import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())
ispangram("The quick brown fox jumps over the lazy dog0909777!")


#Write a program that takes an integer as input and returns an integer with reversed digit ordering.


def reverse_int(integer):
    if integer >= 0:
        return int(str(integer)[::-1])
    else:
        return int('-' + str(integer)[1:][::-1])

reverse_int(-51)


#Write a program that accepts a string as input, capitalizes the first letter of each word in the string, and then returns the result string.

def caitalizer(string):
  return string.title()
caitalizer("Pangrams are words or sentences containing every letter of the alphabet at least once")