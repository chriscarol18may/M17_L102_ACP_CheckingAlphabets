print(ord('#'))
print(ord('$'))
print(ord('R'))
print(ord('A'))
print(ord('M'))


#95 to 112   ->lower case alphaets

#118 to 126  ->upper case alphabets





#Homework
#========
print("Enter a Character: ", end="")
c = input()
if len(c)>1:
    print("\nInvalid Input!")
else:
    if c>='a' and c<='z':
        print("\n\"" +c+ "\" is an alphabet.")
    elif c>='A' and c<='Z':
        print("\n\"" +c+ "\" is an alphabet.")
    else:
        print("\n\"" +c+ "\" is not an alphabet!")