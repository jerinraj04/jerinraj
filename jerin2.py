# Function to find the smallest number 
def smallest(lst): 
      
    # Here i is index and n is the number of the list 
    for i,n in enumerate(lst):  
          
        # Checking for the first non-zero digit in the sorted list 
        if n != '0':  
              
            # Remove and store the digit from the lst 
            tmp = lst.pop(i) 
            break
      
    # Place the first non-zero digit at the starting 
    # and return the final number 
    return str(tmp) + ''.join(lst)  
  
  
# Driver program 
if __name__ == '__main__': 
      
    # Converting the given numbers into string to form a list 
    lst = list(str(570107)) 
    lst.sort() 
      
    # Calling the function using the above list 
    print smallest(lst) 
      
# This code is contributed by Mahendra Yadav 
