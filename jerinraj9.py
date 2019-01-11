using System; 
  public class GFG { 
       static public void printString(string str, 
                           char ch, int count) 
    { 
        int occ = 0, i; 
      if (count == 0) { 
            Console.WriteLine(str); 
            return; 
        } 
      
        
        for (i = 0; i < str.Length; i++) 
        { 
      if (str[i] == ch) 
                occ++; 
      if (occ == count) 
                break; 
        } 
      if (i < str.Length - 1) 
            Console.WriteLine(str.Substring(i + 1)); 
    else
            Console.WriteLine("Empty string"); 
    } 
     static public void Main() 
    { 
        string str = "geeks for geeks"; 
        printString(str, 'e', 2); 
    } 
} 
  

