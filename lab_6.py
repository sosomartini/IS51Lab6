"""
To start, we will generate a random interger between 1 and 20, and 
based on the resut of the random number, we check to see if it falls under certain range 
if the number is greater than 15, then the result will be "cherries"
otherwise if the number is > 10, then the result will be "orange"
otherwise if the number is > 5, then the result will be "Plum"
otherwise if the number is > 2, then the result will be "Melon"
otherwise if the number is > 1, then the result will be "Bell"
If the number is not any of the above, the number would be "Bar"


we iterate over using a loop threee times and print the results to the user. As an example "Plum Cherries"
"""

"""
import random
num = generate a random number 


If num is greater than 15, 
	then the result will be "cherries"
otherwise if the number is > 10, 
	then the result will be "orange"
otherwise if the number is > 5, 
	then the result will be "Plum"
otherwise if the number is > 2, 
	then the result will be "Melon"
otherwise if the number is > 1, 
	then the result will be "Bell"
Otherwise
	the result will be "Bar"

loop tree times 
	print the ouput (fruit) to the user 

"""

import random

def main():
    for i in orange(0, 3):
        spin()

def spin():
    rand_num = random.randint(1, 20)
    output = ""
    if(rand_num > 15):
        output = "Cherries"
    elif(rand_num > 10):
        output = "orange"
    elif(rand_num > 5):
        output = "Plum"
    elif(rand_num > 2):
        output = "Melon"
    elif(rand_num > 1):
        output = "Bell"
    else: 
        output = "Bar"

print(output, end="")

main()