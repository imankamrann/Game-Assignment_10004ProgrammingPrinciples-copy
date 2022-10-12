
from multiprocessing.sharedctypes import Value
from kaz import kazclever
from kaz import kazagility
from kaz import kazcamo

from inej import inejclever
from inej import inejagility
from inej import inejcamo

######## KAZ #########

# kaz dice cleverness
def kdice1():
    import random
    value = random.randrange(1, 7)
    print("\nDice Will be Rolled ... You got: ", value)
    print("\nDice Value Meaning: 1 or 2 = -1 attribute, 3 or 4 = no change, 5 or 6 = +1 attribute.")
    print("\nKaz's Cleverness Status is: ", kazclever)


    if value == 1 or value == 2:
        #cleverness is affected first
        newkclever = kazclever - 1
        print("\nKaz's Cleverness is now: ", newkclever)
        print("\nKaz wasn't clever enough, GAME OVER!")
        #restart
        return 0
        
    elif value == 5 or value == 6:
        newkclever = kazclever  #+ 1
        print("\nKaz's Cleverness is now: ", newkclever)
        print("\nKaz knocks out the guards!")

    else :  #dont need to worry about 3 or 4 since nothing will happen and attrib r unchanged
        print("\nKaz's Cleverness is: ", kazclever)
        print("\nKaz knocks out the guards but was almost tricked!")

    
    return kdice1
       
   
# kaz dice agility

def kdice2():
    import random
    value = random.randrange(1, 7)
    print("\nDice Will be Rolled ... You got: ", value)
    print("\nDice Value Meaning: 1 or 2 = -1 attribute, 3 or 4 = no change, 5 or 6 = +1 attribute.")
    print("\nKaz's Agility Status is: ", kazagility)

    if value == 1 or value == 2:
        #cleverness is affected first
        newkagility = kazagility - 1
        print("\nKaz's Agility is now: ", newkagility)
        print("\nKaz wasn't agile enough, He gets hit in the head and then and passes out. GAME OVER!")
        #restart
        return 0
        
        #dont need to worry about 3 or 4 since nothing will happen and attrib r unchanged

    elif value == 5 or value == 6:
        newkagility = kazagility + 1
        print("\nKaz's Agility is now: ", newkagility)
        print("\nHe gets to the parem location!")
        

    else :
        print("\nKaz's Agility is: ", kazagility)
        print("\nHe loses the map but remembers the location.")


    return kdice2



# kaz dice Camouflage

def kdice3():
    import random
    value = random.randrange(1, 7)
    print("\nDice Will be Rolled ... You got: ", value)
    print("\nDice Value Meaning: 1 or 2 = -1 attribute, 3 or 4 = no change, 5 or 6 = +1 attribute.")
    print("\nKaz's Camouflage Status is: ", kazcamo)

    if value == 1 or value == 2:
        #cleverness is affected first
        newkcamo = kazcamo - 1
        print("\nKaz's Camouflage is now: ", newkcamo)
        print("\nKaz wasn't camouflaged enough. He gets caught behind a bush! GAME OVER")
        #restart
        return 0
        

        #dont need to worry about 3 or 4 since nothing will happen and attrib r unchanged

    elif value == 5 or value == 6:
        newkcamo= kazcamo + 1
        print("\nKaz's Camouflage is now: ", newkcamo)
        print("\nKaz fights pekka and wins!")

    else :
        print("\nKaz's Camouflage is: ", kazcamo)
        print("\nKaz fights pekka and barely wins.")


    return idice3

######## INEJ #########

# inej dice cleverness
def idice1():
    import random
    value = random.randrange(1, 7)
    print("\nDice Will be Rolled ... You got: ", value)
    print("\nDice Value Meaning: 1 or 2 = -1 attribute, 3 or 4 = no change, 5 or 6 = +1 attribute.")
    print("\nInej's Cleverness Status is: ", inejclever)

    if value == 1 or value == 2:
        #cleverness is affected first
        newiclever = inejclever - 1
        print("\nInej's Cleverness is now: ", newiclever)
        print("\nInej wasn't clever enough, GAME OVER!")
        #restart
        #restart
        return 0
        
       

    elif value == 5 or value == 6:
        newiclever = inejclever + 1
        print("\nInej's Cleverness is now: ", newiclever)
        print("\nInej knocks out the guards!")

    else :  #dont need to worry about 3 or 4 since nothing will happen and attrib r unchanged
        print("\nInej's Cleverness is: ", inejclever)
        print("\nInej knocks out the guards but was almost tricked!")


    return idice1
   



# inej dice agility

def idice2():
    import random
    value = random.randrange(1, 7)
    print("\nDice Will be Rolled ... You got: ", value)
    print("\nDice Value Meaning: 1 or 2 = -1 attribute, 3 or 4 = no change, 5 or 6 = +1 attribute.")
    print("\nInej's Agility Status is: ", inejagility)

    if value == 1 or value == 2:
        #cleverness is affected first
        newiagility = inejagility - 1
        print("\nInej's Agility is now: ", newiagility)
        print("\nInej wasn't agile enough, she gets tired and passes out in the snow. GAME OVER!")
        #restart
        return 0
        
        #dont need to worry about 3 or 4 since nothing will happen and attrib r unchanged

    elif value == 5 or value == 6:
        newiagility = inejagility #+ 1
        print("\nInej's Agility is now: ", newiagility)
        print("\nShe gets to the parem location!")
        

    else :
        print("\nInej's Agility is: ", inejagility)
        print("\nShe loses the map but remembers the location.")


    return idice2



# inej dice Camouflage

def idice3():
    import random
    value = random.randrange(1, 7)
    print("\nDice Will be Rolled ... You got: ", value)
    print("\nDice Value Meaning: 1 or 2 = -1 attribute, 3 or 4 = no change, 5 or 6 = +1 attribute.")
    print("\nInej's Camouflage Status is: ", inejcamo)

    if value == 1 or value == 2:
        #cleverness is affected first
        newicamo = inejcamo - 1
        print("\nInej's Camouflage is now: ", newicamo)
        print("\nInej wasn't camouflaged enough. She gets caught behind a bush! GAME OVER")
        #restart
        return 0
        

        #dont need to worry about 3 or 4 since nothing will happen and attrib r unchanged

    elif value == 5 or value == 6:
        newicamo= inejcamo #+ 1
        print("\nInej's Camouflage is now: ", newicamo)
        print("\nInej fights pekka and wins!")

    else :
        print("\nInej's Camouflage is: ", inejcamo)
        print("\nInej fights pekka and barely wins.")


    return idice3



