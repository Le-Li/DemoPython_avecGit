#exercise 1: Character Input
##########################################################################
print"%s, you will turn 100 in %s" %(raw_input("What is your name? "),
2116-int(raw_input("What is your age? ")))

#exercise 2: Odd or Even 
##########################################################################
# extra 2
num=int(raw_input("Enter a number to check (num): "))
check=int(raw_input("Enter a number to divide by (check): "))
if num % check == 0: print(str(check)+" divides evenly into "+str(num)) 
else: print(str(check)+" does not divide evenly into "+str(num))

