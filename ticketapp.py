TICKET_PRICE = 10

tickets_remaining = 100  

while tickets_remaining>=1:
     print("There are {} tickets reamaining".format(tickets_remaining))
     name=input("what's your name?:  ")
     try:
       num_tickets=int(input("Hi,{} how many tickets do you want? : ".format(name)))
        if num_tickets>tickets_remaining:
          raise ValueError("Sorry not possible")
     except ValueError as err:
      print("No way {}".format(err))
    else:
        
       amount_due=num_tickets*TICKET_PRICE
       print(amount_due)
       proceed=input("Do you want to proceed? Y/N : ")
       if proceed.lower()=='y':
  
           tickets_remaining-=num_tickets
       else:
            print("thanks anyways{}".format(name))
         
print("sorry tickets sold out")
     