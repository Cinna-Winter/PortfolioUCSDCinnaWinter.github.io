#A text-based escape room game

#Variables in the game

player_has_key = False
player_has_seeds = False
player_has_water_in_vase= False
player_has_vase = False
player_has_flower = False
window_is_open = False
vase_is_back = False
current_weather = "sunny"
current_location = "center"
inventory = []

#Functions in the game.
  
def game_door():
  global player_has_key
  global current_location
  global inventory
  
  print("You are at the door.")
  print("You see a door. It is a pretty normal door for your perspective. There is a keyhole in the door.")
  print("You can try 'look at door', 'open door', or 'use key'.")
  print("You can also go back to the center of  the room by typing 'go back'.")
  current_location = "door"
  while True:
    game_state()
    print("What do you do?")
    player_input = input(">")
    if player_input == "look at door":
      print("Again, it is a pretty normal door for your perspective.")
    elif player_input == "use key":
      if player_has_key == True:
        print("You open the door.")
        game_won()
      else:
        print("You do have a key yet.")
    elif player_input == "open door":
      print("You try to open the door, but it's locked.")
    elif player_input == "go back":
      game_room()
    else:
      print("That command doesn't work here. Try something else.")
    game_state()    
     
def game_drawer():
  global player_has_key
  global player_has_vase
  global vase_is_back 
  global player_has_flower
  global player_has_water_in_vase
  global current_location
  global inventory
  
  print("You are at the drawer.")
  print("Do you want to take a closer look at the drawer?")
  print("You can also go back to the center of the room by typing 'go back'.")
  current_location = "drawer"
  while True:
    game_state()
    print("What do you do?")
    player_input = input(">")
    if player_input == "look at drawer":
      print("You examine the drawer. There's three drawers. There is also a vase on top of the drawer.")
    elif player_input == "look at vase":
      print("You look at the vase. It's a pretty vase. It's empty.")
    elif player_input == "take vase":
      print("You take the vase.")
      print("Maybe you can fill it up with something.")
      player_has_vase = True
    elif player_input == "place vase back":
      print("You place the vase back with water.")
    elif player_input == "place flower in vase":
        if player_has_flower == True and player_has_vase == False and player_has_water_in_vase == True:
          print("You also place the flower in the vase.")
          print("You hear a click sound.")
          player_has_flower = False
          player_has_water_in_vase = False
          vase_is_back = True 
          
    elif player_input == "open drawer":
      if vase_is_back == True:
        print("You open the drawer.")
        print("You see a key in the drawer.")
        print("You take the key.")
        player_has_key = True 
    elif player_input == "go back":
      game_room()
    else:
      print("That command doesn't work here. Try something else.")
    
         
def game_clock():
  global current_weather
  global current_location
  global inventory
  
  print("You are at the clock.")
  print("It is a pretty clock. It is look like a grandfather clock.")
  print("Hold on, something doesn't seem right.")
  print("Want to take a closer look?")
  print("You can also go back to the center of the room by typing 'go back'.")
  current_location = "clock"
  while True:
    game_state()
    print("What do you do?")
    player_input = input(">")
    if player_input == "look at clock":
      print("You take a closer look at the clock.")
      print("You see that the clock isn't normal. It doesn't tell time")
      print("It has a face with symbols of a sun, teardrop, and a cloud on it.")
      print("There is knob on the side of the clock. Maybe you can turn it?")
    elif player_input == "turn knob to sun":
      print("You turn the knob to the sun.")
      print("The clock makes a sound and the sun symbol lights up.")
      current_weather = "sunny"
    elif player_input == "turn knob to teardrop":
      print("You turn the knob to the teardrop.")
      print("The clock makes a sound and the teardrop symbol lights up.")
      current_weather = "rainy"
    elif player_input == "turn knob to cloud":
      print("You turn the knob to the cloud.")
      print("The clock makes a sound and the cloud symbol lights up.")
      current_weather = "cloudy"
    elif player_input == "go back":
      game_room()
    else:
      print("That command doesn't work here. Try something else.")
    
  
def game_window():
  global current_weather
  global player_has_vase
  global player_has_water_in_vase
  global player_has_flower
  global player_has_seeds
  global window_is_open
  global current_location
  global inventory
  
  print("You are at the window.")
  current_location = "window"
  if current_weather == "cloudy":
    print("It is cloudy outside. There is a tree outside the window.")
  elif current_weather == "rainy":
    print("It is raining outside. There is a tree outside the window.")
  elif current_weather == "sunny":
    print("It is sunny outside. There is a tree outside the window. A bird is sitting on a branch.")
  print("Do you want to look around the window?") 
  print("You can also go back to the center of the room by typing 'go back'.")
  while True:
    game_state()
    print("What do you do?")
    player_input = input(">")
    if player_input == "look at window":
      print("You look at the window.")
      print("You notice a pot of soil on the window sill with packets of seeds.")
    elif player_input == "take seeds":
      print("You take the packet of seeds. Maybe you can give it to the bird?")
      player_has_seeds = True
    elif player_input == "open window":
      print("You open the window.")
      if current_weather == "cloudy":
          print("Clouds are rolling by.")
      elif current_weather == "rainy":
          print("Rain is coming down.")
      elif current_weather == "sunny":
          print("It's nice to feel the rays.")
      window_is_open = True     
    elif player_input == "close window":
      print("You close the window.")
      window_is_open = False
    elif player_input =="give seeds to bird":
        if player_has_seeds == True and window_is_open== True and current_weather == "sunny":
          print("You give the seeds to the bird.")
          print("The bird takes the seeds and flies away.")
          print("After a while, the bird comes back with a flower.")
          print("You have a flower now.")
          player_has_flower = True
          player_has_seeds = False
        elif player_has_seeds == False:
          print("You don't have seeds.")
        elif window_is_open == False:
            print("The window is closed.")
        elif current_weather != "sunny":
          print("It's not sunny.")
        else:
          print("This doesn't make sense.")
    elif player_input == "collect rain with vase":
        if window_is_open == True and current_weather == "rainy" and player_has_vase == True:
          print("The rain comes in through the window.")
          print("You hold the vase to collect the rain.")
          print("You have water in the vase now.")
          player_has_water_in_vase = True
          player_has_vase = False
        elif window_is_open == False:
          print("The window is closed.")
        elif current_weather != "rainy":
          print("It's not raining.")
        elif player_has_vase == False:
          print("You don't have a vase.")
        else:
          print("This doesn't make sense.")
    elif player_input == "go back":
      game_room()
    else:
      print("That command doesn't work here. Try something else.")
  
  
def game_room():
  global current_location
  global inventory
  current_location = "center"
  
  print("You look around the space you're in. There's a door, a window, a clock, and a drawer.")
  print("You can go up to a location by typing 'go to' and then the location or you can 'do nothing'. You won't pick 'do nothing' will you?")
  game_state()
  while True:
    print("So what do you do?")
    player_input = input(">")
    if player_input == "go to door":
        game_door()
    elif player_input == "go to window":
        game_window()
    elif player_input == "go to clock":
        game_clock()
    elif player_input == "go to drawer":
          game_drawer()
    elif player_input == "do nothing":
        print("You do nothing.")
        print("You remain still for the remainder of time.")
        print("Is this really how you want to spend your time?")
    else:
        print("That command doesn't work here. Try something else.")
   
        
def game_state():
  
  global player_has_key
  global player_has_seeds
  global player_has_water_in_vase
  global player_has_vase
  global player_has_flower
  global window_is_open
  global vase_is_back
  global current_location
  global inventory
  
  inventory = []
  if player_has_key == True:
        inventory.append("key")
  if player_has_seeds == True:
        inventory.append("seeds")
  if player_has_water_in_vase == True:
        inventory.append("vase with water")
  if player_has_vase == True:
        inventory.append("vase")
  if player_has_flower == True:
        inventory.append("flower")

  print("Inventory: " + str(inventory))
  
  if current_location == "center":
    print("Location: The center of the room")
  elif current_location == "door":
    print("Location: The door")
  elif current_location == "window":  
    print("Location: The window")
  elif current_location == "clock":
    print("Location: The clock")
  elif current_location == "drawer":
    print("Location: The drawer")
  
def game_won():
  print("You exited through the door.")
  print("You have escape the program.")
  print("Well done.")
  print("Do you want to play again?")
  print("Type 'yes' or 'no'.")
  player_input = input(">")
  if player_input == "yes":
    game_start()
  elif player_input == "no":
    print("Thank you for playing.")
  else:
    print("That command doesn't work here. Try something else.") 
    
     
def game_start():
  print("Hey! Wake up! Wake up!")
  print("What? Where am I? Who are you?")
  print("My name? Oh, it's not important. What is important is that you get out of here.")
  print("You got mixed up with the program and now you're stuck here. You have to get out before the game ends or you'll be stuck here forever.")
  print("I'll help you as much as I can, but I can't do much. I'm just ??? from the beyond.")
  print("Now, let's get started.")
  player_input = input("Press enter to continue.")
  if player_input == "":
    game_room() 
  else:
    print("That command doesn't work here. Try something else.")

game_start()

