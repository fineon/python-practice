# ----------------------------
# PRIMITIVE TYPES + VARIABLES DECLARATION

firstname = 'ian' #string
lastname = 'nguyen' #string
myname = firstname + lastname #string concatenation
print('my name is', myname)

number = 50 #integers
boolean = True #boolean. Needs to be capitalized
floatingNum = 0.5 #floating point number

null = None #the null object in python
print(null)

# -------------------------------
# BASIC PYTHON OBJECTS (DICTIONARY) AND ITERABLE DATA (LISTS)
li = ['orange',True, False, 250] # Python list
print('the value at index 0 is: ',li[0]) # list index starts at 0

tup=(1,2,3) #tuple - iterable like list, but immutable
print('a tuple list', tup)

obj = {'key': 'value pair', 'number': 12, 'boolean': True, 'list': [True, False, 'cucumber'], 2: True,}
print(obj)

# EVALUATION AND ARITHMETIC OPERATORS
calc= 1+10-2*3/2 #basic calculations
print('Python calculation =', calc)

modulo=8%2 #python's modulo calc. returns a number value that is evenly divided by 2
print("modulo", modulo)

expo=8**3
print("exponential", expo)

# ------------------------------------------------
# FUNCTION && CLASS
def my_func(param): 
    return param + 1
print("function invocation return the value of", my_func(2))

class myClass: 
    classVar = 'returned string value in a class'
    def classFunc(self):
        return True #invoke this method will return the boolean value True
        #return self # return <__main__.myClass object at 0x7f6c2e9bfa90>

    # class methods if inited by a variable should accept 1 parameter before invocation
    def funcMethod(self):
        print('class method invoked')
    #Python's __init__() func can create a new object in a class, which can be referenced in other places
    def __init__(self, obj): 
        self.obj = obj 
    def printObj(self):
        #print(self.obj)
        return self.obj
initClass= myClass('a class object') #init class and passing an object value declared inside the class
print(initClass.classVar)
print(initClass.classFunc()) 
print(initClass.funcMethod())
print(initClass.printObj())
# Python method that prints all available methods inside a class
print(dir(myClass))

#-----------------------------
# STATEMENTS	

myPet = 'dog'
print(type(myPet)) #printing type of variable

#elif statement. can insert different avaluation cases in each statement. Not like ethe else statement which only eval the case in if statement. 
if myPet == 'fish':
    print('nah')
elif myPet == 'cat':
    print(False)
elif myPet == 'god':
    print('maybe a misspelling, maybe true')
elif myPet == 'dog':
    print('my pet is a dog', True)

#if else
if myPet == 'cat':
    print("is my pet a cat?", False)
else: 
    print("is my pet a dog?", True)

# rewriting if..else statements into a tuernary statement
# souce: https://stackoverflow.com/questions/394809/does-python-have-a-ternary-conditional-operator
print('---ternary statement---')
print("is my pet a cat?", False) if myPet == 'cat' else print("is my pet a dog?", True)

# for..in loop
for n in [1,2,3,4,5]: 
    print("the for loop returning", n+1)

# while loop
i = 0
while i < 10:
    i += 1
    print(i)
    
    

# --------------------------------
# WHITE SPACE IN PYTHON
y = 12 #this variable is in global scope

def value(z = 10):
    return z + y
    print(z) # indentation after a statement, function will create a block scope.


# print(z) # this line is not in the function value() block scope. Will return undefined.
print(value()) # returns 22.




