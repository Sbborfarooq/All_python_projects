from item import Item # type: ignore
class Phone(Item):
    def __init__(self,name:str,price:float,quantity=0,broken_phones=0):
     #calling super function to havinh the full access of parent class (Item) attribute / method   
        super().__init__(
            name,price,quantity
        )
        #run validation to the recieved argument
        assert broken_phones>=0 , f"broken_phones {broken_phones} is not greater than or equal zero:"
        
        #Assign to self object that are unique to every instance(object)
        self.broken_phones=broken_phones
        
        

