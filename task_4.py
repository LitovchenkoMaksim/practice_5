import random             
def main():                         
    c=int(0)
    y=int(0)                        
    d = { "Russia" : "moscow",      
        "USA" : "washington",       
        "Canada": "ottawa",         
        "Germany": "berlin", }      
    dl = list(d.keys())             
    random.shuffle(dl)             
    for i in dl :                  
      y+=1                         
      print (*dl[y-1], sep='')     
      x = str(input())             
      if x.lower()==d[i].lower():   
        c +=1                       
        print("C=",c)               
      else:print("-")               
    print ("close C=", c)           
main()                            
