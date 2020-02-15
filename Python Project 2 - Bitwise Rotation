#Created by Ruma Ikram 10/08/2019


''' Function Definition '''
def decimal_to_binary(dec):  # Function to convert decimal to binary
    a = bin(dec).replace("0b","")
    return str(a).zfill(16)


def binary_rotation(binaryNumber, direction, step):#Function to perform the bitwise rotation
    if direction == "L":
        l_rem = (binaryNumber[step:]) # left rotation removes first step nums  and gives the remaining
        first = (binaryNumber[:step])# gives the first step nums
        left_rot = l_rem + first # concatenate the remaining with the first step nums
        return left_rot
    else:
        f_rem = (binaryNumber[:-step])#right rotation removes the last step and gives the first remaining
        last = (binaryNumber[-step:]) # gives the last step
        right_rot = last + f_rem # concatenate the last step with the first remaining
        return right_rot

def binary_to_decimal(n): #Function to convert binary to decimal
    return int(n,2)     


'''Script'''
inFile = open('inFile.txt') #reading the input file
outFile = open('outFile.txt', 'w') # reading the output File
lines = inFile.readlines() #reading each line from input File
for line in lines:
    line = line.split() # converting the white spaces into lists
    if len(line) > 1:
        originalDecimal = int(line[0]) # instantiating the object
        direction = line[1]
        step = int(line[2]) % 16
        originalBinary = decimal_to_binary(originalDecimal) # function calling
        resultBinary = binary_rotation(originalBinary, direction, step)
        resultDecimal = binary_to_decimal(resultBinary)
        outFile.write('%d\n' % resultDecimal) #writing to output File

inFile.close() # closing the input file
outFile.close() # closing the output File










  
# def binary_rotation(binaryNumber, direction, steps):
#     return (binaryNumber << steps)|(binaryNumber >> (INT_BITS - steps)) 
# 
