n = int(input('Enter a starting value: ')) #Taking n as an integer input


lst = [] #Creating an empty list to store values after every iteration

def SplitBinary(n): #Devining function named Splitbinary
    B = bin(n) #Converting integer n into binary
    B = list(B) #Converting binary number into list
    decimal_val = B.pop(0) and B.pop(0) #Removing 0 and b from the list so that we can operate with remaining numbers
    B = list(reversed(B)) #Reversing the list
    length = len(B) #Finding the length of the list
    middle_index = length//2 #Finding the quotient to get the middle index of the list
    S = B[:middle_index] #Slicing the list from 0 to the middle index
    S = list(reversed(S)) #Reversing the list for correct form
    F = B[middle_index:] #Slicing the list from middle index to the last index
    F = list(reversed(F)) #Reversing the list for correct form
    S = list(S)
    F = list(F)

    
    stri_S = "" #Creating an empty string to add elements from list S
    stri_F = "" #Creating an empty string to add elements from list F

    for i in S: #Checking through every element in S
        stri_S += str(i)

    new_S = list(stri_S)

    total_S = 0 #Creating a variable with value 0

    #Decimal to integer conversion for S:

    Len_S = len(new_S)
    for i in range(Len_S):
        last_element = new_S.pop()
        if last_element == "1":
            total_S += pow(2,i) 

    for i in F: #Checking through every element in F
        stri_F += str(i)

    new_F = list(stri_F)

    total_F = 0 #Creating a variable with value 0

    #Decimal to integer conversion for F:

    Len_F = len(new_F)
    for i in range(Len_F):
        last_element = new_F.pop()
        if last_element == "1":
            total_F += pow(2,i)

    SplitBinary_Sequense = (total_F + 1)*(total_S + 1)

    return SplitBinary_Sequense
    
while (n not in lst):
     lst.append(n) #Storing values in the empty list
     n = SplitBinary(n) #Updating value after every iteration
lst.append(n)


for i in lst: #Going through every element in the list
    print(i)  #Printing all elements from the list
print("Duplicate Found!") #Duplicate found message when duplicate is detected