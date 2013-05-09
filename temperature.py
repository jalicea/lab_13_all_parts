"""
temperature.py
=====
Write a program that calculates celsius to fahrenheit based on user input.
1. Create a file called temperature.py
2. The program should ask for the temperature
3. Find the formula for this conversion here:   
4. Implement it in your program
5. The program should output: c degrees celsius is f degrees fahrenheit
6. (obvs with f and c substituted with the appropriate calculated values)
7. Note that the outputs are floats!
8. You don't have to account for non-numeric input (at least... not yet!)

Example Output - Everything after the greater than sign (>) is user input:

Please enter a temperature in celsius
> 37
37.0 degrees celsius is 98.6 degrees fahrenheit
"""

print("Please enter a temperature in celsius")
c = raw_input(">")
f = (9 * float(c))/5+32
print(c + " degrees celsius is " + str(f) + " degrees fahrenheit")