#My Functions

import random
import math

def test_function(a,b):

    summed_up = a*b

    print ("Your value is {}".format(summed_up))


#Calculations based on our new function

print("12 x 96 =", summed_up(12, 96))

print("48 x 17 =", summed_up(48, 17))

print("196523 x 87323 =", summed_up(196523, 87323))



#fruit colour code

picked_fruit = random.choice(['orange', 'strawberry', 'banana'])

choice = picked_fruit


if choice == 'orange':
    print ('orange')
elif choice == 'strawberry':
    print('red')
elif choice == 'banana':
    print ('yellow') 



#i conditional

i = random.randint(0, 100)

if i < 50:
    print ("50 is greater than i ")
elif i > 50:
    print ("i is greater than 50")
elif i == 50:
    print ("i is equal to 50")




#print pi math equation
print ("The value of pi is equal to {} and pi is also a {}".format (pi, type(pi)))