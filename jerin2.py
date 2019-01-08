
def smallest(lst): 
      for i,n in enumerate(lst):  
    if n != '0':  
        tmp = lst.pop(i) 
        break
   return str(tmp) + ''.join(lst)  
 if name == 'main': 
    lst = list(str(570107)) 
    lst.sort() 
  print smallest(lst) 
      
