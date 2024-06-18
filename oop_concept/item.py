"""In python programming each data_type is an object that is instantiated from some class .now we want to create our
own class and we give it a name(Item)  """
#__init__"""every time we create the object of a class the python run this __init__ method  atuomatically:"""
import csv #responsible to read any csv 
class Item:
    #class attribute
    pay_rate=0.8 #pay rate after the 20% disscount
    all=[]
    def __init__(self,name:str,price:float,quantity=0):

        #run validation to the recieved argument
        assert price>=0 , f"price {price} is not greater than or equal zero:"
        assert quantity>=0 , f"quantity {quantity} is not greater than or equal zero:"
        
        #Assign to self object that are unique to every instance(object)
        self.name=name
        self.__price =price
        self.quantity=quantity
        
        #action to excute
        Item.all.append(self)
    
    @property
    def price(self):#restric the value of price attribute
        return self.__price
    def apply_disscount(self):
        self.__price=self.__price*self.pay_rate ##overriding the value of self.price #change Item=self
    def apply_increment(self,increment_value):
        self.__price=self.__price + self.__price * increment_value
    def calculate_total_price(self):
        return self.__price*self.quantity
    
    
    @classmethod
    def instantiate_from_csv(cls):
        with open("data.csv",'r') as f:
            reader=csv.DictReader(f)
            items=list(reader)
        for item in items:
            Item(   #instantiatiing our objects
                  name=item.get('name') , 
                  price=float(item.get('price')),  
                  quantity=int(item.get('quantity'))  
                    )
    @staticmethod
    def is_integer(num):
        #we wil count out the float that are point zero 
        #5.0,10.0 
        if  isinstance(num,float):#it is built in function to check that the (num) is instance or int or float
            #count out the float that are point zero 
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False
    def __repr__(self):#magic method to represent the object and self.__class__.__name__ magic attribute to identify
        #the class name 
        return f"{self.__class__.__name__}('{self.name},{self.price}',{self.quantity})"
          
        

 #lets say we create two object from Item class we will see 2time the print statment of "iam created!"
#so the most important thing is __init__ method is call every time we create our object 

"""Now another concept of class attribute is that which is shared amonge all the instances.Its global attribute
but we can also access this class attribute at instance level as well FOR_EXAMPLE : WE WANT TO APPLY THE DISCOUNT
IN OUR SHOP FOR ITEMS SEE ABOVE THE CLASS ATTRIBUTE  print(Item.pay_rate) we can directly access it by call our class
also we can access it with instance level print(item1.pay_rate) 
BY using print(Item.__dict__) #check attribute at class level
BY using print(item1.__dict__) #check attribute at instance level 
where (__dict__) is magic_attribute 
"""

"""Now the whole concept of instance attribute with example: now what if we want to apply some disscount on 
our item 2 which is laptop suppose we want to apply 30%disscount on it in order to do that we also know another way of 
assigning the instance attribute which is this [item2.apply_disscount()] [item2.pay_rate=0.7] but when we run this still we 
got 80% disscount instead of 70% disccount to over come this problem we have to write self in apply_discoutn()mthod
instead of Item_class so when we want to apply disscount on any other object item and python will look at it firstly 
at instance level and it will find it and apply the disscount and for the item1 object  it will not find the attribute
at instance level so it will move to class attribute :"""

"""Now another thing we should do is that to store our instances every time we create them in organized manner
to do this we can create the class attribute all=[] and now we want to store our all the objects that we want to 
create in that class attribute list to over come this problem we know that every time we create our object the __init__
mehtod is called out for every instance so we can write the code in it so every time we create our item object 
it would store in all=[]   for better representation of objects we use __repr__ magic method """

# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)


"""
Now another thing we can do is we can import our objects from a external source lets say csv.file so all our 
object are stored there and we just make a method to instantiated it from there also we use class_mehtod in order
to execute our method because we can directly call our method see method above 
so the main difference between class_method and static_method is that class_method are sending the first argument
as class reference  (Item) and in static method we never send the first argument object itself that why it works
as isolated function  """

"""Now we will talk about decorator means adding more functionality to a function i will just only got the 
concept of decorator but i will not write it in code @property decorator (read_only_attribute)(__private sign)
@name.setter """


#*********************      OOP FOUR KEY PRINCIPLES *************************************************
#1) ENCAPSULATION    2)ABSTRACTION   3)INHERITANCE      4)POLYMORPHISM

#1)ENCAPSULATION:
""" Refer to a mechanism of restricting the direct access to some of our attribute in a program:now forexample:
see price attribute first we set @property attribute  which is read_only_attribute we can change directly our 
value """
# item1=Item("MyItem",750)
# item1.price=900 #after we private the attribute we cannot directly apply value to item1.price
#insted we will make methods to apply changes like apply_increment
# item1.apply_increment(0.2)
# print(item1.price)

