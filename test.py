class bottle:
    
    capacity=500
    material="metal"
    filled=0


    def drinkwater():
        if(bottle.filled==0):
            print("Bottle empty\n")
        else:
            print("Drink water from bottle(-100)\n")
            bottle.filled=bottle.filled-100
    
    def refillwater():
        print("Refilled water in the bottle (+100)\n")
        if (bottle.filled<bottle.capacity):
            bottle.filled=bottle.filled+100
        else:
            print("Bottle full!\n")
    
    def emptybottle():
        print("Emptied the bottle\n")
        bottle.filled=0
    
    def specifications():
        print("\nSpecifications of the bottle:")
        print("Material:", bottle.material) 
        print("capacity:", bottle.capacity) 
        print("\n")


b=bottle
while(1):
    print("------------------------Waterbottle------------------------")
    print("1=Fill,2=drink,3=empty,4=specificiations")
    ch = int(input("Enter choice: "))
    if(ch==1):
        b.refillwater()
        
    elif(ch==2):
        b.drinkwater()
        
    elif(ch==3):
        b.emptybottle()
        
    else:
        b.specifications()

    
