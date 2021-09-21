# ----------------------------
# PRIMITIVE TYPES + VARIABLES

firstname = "ian" #string
lastname = "nguyen"
myname = firstname + lastname #string concatenation
print(myname)

number = 50 #integers
boolean = True #boolean. Needs to be capilaized apparently
floatingNum = 0.5 #floating point number

calc= 1+10-2*3/2 #basic calculations
print('Python calculation =', calc)

modulo=8%2 #python's modulo calc. returns a number value that is evenly divided by 2
print("modulo", modulo)

expo=8**3
print("exponential", expo)

# ------------------------------------------------
# FUNCTION
def my_func(param): 
    return param + 1

print("printing function return value", my_func(2))

#-----------------------------
# Statements

#elif statement. can insert different avaluation cases in each statement. Not like ethe else statement which only eval the case in if statement. 
myPet = 'dog'

if myPet == 'fish':
    print('nah')
elif myPet == 'cat':
    print(False)
elif myPet == 'god':
    print('maybe misspelling, maybe true')
elif myPet == 'dog':
    print('my pet is a dog',True)

# --------------------------------
# WHITE SPACE IN PYTHON
y = 12 #this variable is in global scope

def value(z = 10):
    return z + y
    print(z) # indentation after a statement, function will create a block scope.


# print(z) # this line is not in the function value() block scope. Will return undefined.
print(value()) # returns 22.




