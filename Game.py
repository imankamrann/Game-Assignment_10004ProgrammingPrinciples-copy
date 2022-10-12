
import welcome
import dice
import kaz
import inej

#resources
def kazresources1():
  kaz.kc1()
  return dice.kdice1()

def kazresources2():
  kaz.kc2()
  return dice.kdice2()

def kazresources3():
  kaz.kc3()
  return dice.kdice3()
  

def inejresources1():
   inej.ic1()
   return dice.idice1()

def inejresources2():
   inej.ic2()
   return dice.idice2()

def inejresources3():
   inej.ic3()
   return dice.idice3()

#Challenges
def challenge1():
  print("\nYour 1st Challenge: Break into Pekkas high security building and find the map that has the location of the Parem which Pekka intends to retrieve")


def challenge2():
  print("\nYour 2nd Challenge: Follow the map to the Parem and destroy it, fighting anyone on the way.")


def challenge3():
  print("\nYour 3rd Challenge: Put pekka in his place since he will want revenge")

def win():
  print("\n------ Congrats! You Defeated Pekka! ------- ")

def lose():
  print("\n-------- Better Luck Next Time! --------")   

# create a loop here to restart the game
x=1
while (x==1):
  print("*******************************")

  #Character
  character = input("\nEnter kaz or inej: ")
  print("\nYou Chose: ", character)

  if character == 'kaz': 
      challenge1()
      if(kazresources1()==0):
        lose()
        continue
      challenge2()
      if(kazresources2()==0):
        lose()
        continue
      challenge3()
      if(kazresources3()==0):
        lose()
        continue
      win()
      break
      

  if character == 'inej':

      challenge1()
      if(inejresources1()==0):
        lose()
        continue
      challenge2()
      if(inejresources2()==0):
        lose()
        continue
      challenge3()
      if(inejresources3()==0):
        lose()
        continue
      win()
      break
      


