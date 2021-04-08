import time
import random
import sys

def Start():
  print("Welcome to my horror game.")
  Player.name = input("What is your name? "'\n')
  time.sleep(0.2)
  print("Hello,", Player.name)
  time.sleep(0.2)
  Player.hp = 10
  Player.dmg_min = 1
  Player.dmg_max = 2
  Player.defe = 1
  Player.coins = 0
  Player.bandage = False
  Player.combat = False
  Player.lvl = 1.0
  print("You are starting with {} health, ( {} - {} ) damage, {} defense, {} coins.".format(Player.hp, Player.dmg_min, Player.dmg_max, Player.defe, Player.coins))
  time.sleep(0.2)
  ans = input("Ready to start? (yes/no)"'\n')
  if ans == "yes":
    RandomLoot()
    time.sleep(0.2)
    ActOne()
    time.sleep(1)
    ActTwo()
  else:
    print("Pussy...")

def End():
  time.sleep(6)
  print("YOU DIED")
  time.sleep(1)
  ans = input("Wanna try again? (yes/no)"'\n')
  if ans == "yes":
    Start()
  else:
    print("Pussy...)")
    sys.exit()

class Player():
  hp = 10
  dmg_min = 1
  dmg_max = 2
  defe = 1
  lvl = 1

  ### INVENTORY ###
  coins = 0
  bandage = False
  combat = False
  
class Enemy:
   def __init__(self, hp, dmg, defe):
    self.hp = hp 
    self.dmg = dmg
    self.defe = defe

def Combat(hp, dmg_min, dmg_max, defe):
  Enemy.hp = hp
  Enemy.dmg_min = dmg_min
  Enemy.dmg_max = dmg_max
  Enemy.defe = defe
  Player.combat = True
  time.sleep(2)
  print("The combat begins!")
  time.sleep(0.5)
  print("Your stats: {} health, ( {} - {} ) damage, {} defense.".format(Player.hp, Player.dmg_min, Player.dmg_max, Player.defe))
  time.sleep(0.5)
  print("Enemy's stats: {} health, ( {} - {} ) damage, {} defense.".format(Enemy.hp, Enemy.dmg_min, Enemy.dmg_max, Enemy.defe))
  time.sleep(3)
  while Enemy.hp > 0 and Player.hp > 0:
    player_hit = max(0, random.randint(Player.dmg_min, Player.dmg_max) - Enemy.defe)
    enemy_hit = max(0, random.randint(Enemy.dmg_min, Enemy.dmg_max) - Player.defe)
    Enemy.hp -= player_hit
    print("Your turn. You are hitting it for {} damage. The creature's HP is {}.".format(player_hit, Enemy.hp))
    if Enemy.hp <= 0:
      print("You have finally defeated it. It was a hard fight. You survived with {} health.".format(Player.hp))
      time.sleep(1)
      break
    time.sleep(2)
    Player.hp -= enemy_hit
    print("The beast is hitting you for {} damage. Your HP is {}.".format(enemy_hit, Player.hp))
    if Player.hp <= 0:
      time.sleep(1)
      print("YOU DIED...")
      time.sleep(1)
      ans = input("...would you like another try? (yes/no) "'\n')
      if ans == "yes":
        Start()
      else:
        print("Pussy...")
        sys.exit()
    time.sleep(2)
  if Player.bandage == True:
    Player.hp += 3
    print("You use the bandage your have in your bag. Your heal yourself by 3, you now have {} health.".format(Player.hp))
  print("You continue on your journey...")
  time.sleep(2)

def Tavern():
  leave = False
  while leave == False:  
    ans = input("You stand in the middle of the tavern. You can go buy some stuff, go gamble with a group of men, go speak with the tavernkeeper, leave the tavern. (shop/gamble/talk/leave)"'\n')
    if ans == "shop":
      Shop()
    elif ans == "gamble":
      Gamble()
    elif ans == "talk":
      Talk()
    else:
      leave = True

def Shop():
  leave = False
  print("You are in front of a man selling his wares. 'I have wares if you have coins', he says. 'How can I help you?'")
  while leave == False:
    if Player.lvl == 1:
      time.sleep(0.5)
      print("You see weapons and a shield.")
      time.sleep(0.5)
      print("Shortsword: 2 - 3 Damage, 4 coins.")
      time.sleep(0.5)
      print("Longsword: 3 - 6 Damage, 7 coins.")
      time.sleep(0.5)
      print("Wooden shield: 1 Defense, 3 coins.")
      time.sleep(0.5)
      print("Your coins: {}.".format(Player.coins))
      time.sleep(0.5)
      ans = input("What will you choose? (Shortsword, Longsword, Shield, leave)"'\n').lower()
      time.sleep(0.3)
      if ans == "shortsword":
        if Player.coins >= 4:
          Player.dmg_min, Player.dmg_max = 2, 3
          Player.coins -= 4
          print("You bought the Shortsword!"'\n'"Your damage is now {} - {}.".format(Player.dmg_min, Player.dmg_max))
          print("You loose 4 coins. You now have {} coins.".format(Player.coins))
        else:
          print("You don't have enough coins!")
      elif ans == "longsword":
        if Player.coins >= 7:
          Player.dmg_min, Player.dmg_max = 3, 6
          Player.coins -= 7
          print("You bought the Longsword!"'\n'"Your damage is now {} - {}.".format(Player.dmg_min, Player.dmg_max))
          print("You loose 7 coins. You now have {} coins.".format(Player.coins))
        else:
          print("You don't have enough coins!")
      elif ans == "shield":
        if Player.coins >= 3:
          Player.defe += 1
          Player.coins -= 3
          print("You bought the Shield!"'\n'"Your defense is now {}.".format(Player.defe))
          print("You loose 3 coins. You now have {} coins.".format(Player.coins))
        else:
          print("You don't have enough coins!")
      else:
        leave = True
    else: #PLAYER LVL 2
      print("You see") #NEW WEAPONS AND ARMOR
  
def Gamble():
  leave = False
  print("You approach the group of men. They look at you and give you a seat. They are playing dice with coins.")
  while leave == False:
    ans = input("Do you want to bet? (yes/no)"'\n')
    time.sleep(0.3)
    if ans == "yes":
      print("You are taking a seat to play a game.")
      time.sleep(0.2)
      print("The rules are simple: You throw 3 dice and get points. Number 1-6 on die gives you 10-60 points respectively. Who gets 500 or more points, wins.")
      time.sleep(0.2)
      bet = int(input("You have {} coins. how much would you like to bet?"'\n'.format(Player.coins)))
      time.sleep(0.2)
      if bet <= Player.coins: 
        Player.coins -= bet
        price = round(bet * 1.4)
        playing = True
        print("You are betting {}. You can win {} coins.".format(bet, price-bet))
        player_sum = 0
        oponent_sum = 0
        time.sleep(0.7)
        while playing == True:
          player_throw = random.randrange(30, 180, 10)
          player_sum += player_throw
          oponent_throw = random.randrange(30, 180, 10)
          oponent_sum += oponent_throw
          print("You are throwing {} points. You now have {} points.".format(player_throw, player_sum))
          time.sleep(0.7)
          if player_sum >= 500:
            Player.coins += price
            print("You won! You earn {} coins. Now you have {} coins!".format(price-bet, Player.coins))
            playing == False
            break
          print("Oponent is throwing {} points. He has {} points.".format(oponent_throw, oponent_sum))
          time.sleep(0.7)
          if oponent_sum >= 500:
            print("You lost! Better luck next time...")
            time.sleep(0.2)
            print("You loose {} coins, unfortunate...".format(bet))
            playing = False
            break
      else:
        print("You don't have that much!")
    else:
      leave = True

def RandomLoot():
  loot_list = ["Whetstone", "Chainmail", "Axe", "Shield"]
  loot = random.choice(loot_list)
  if loot == loot_list[0]:
    Player.dmg_min+= 1 
    Player.dmg_max += 1
    print("You found a {}. With that, your damage is increased by 1! You now have {} - {} damage.".format(loot, Player.dmg_min, Player.dmg_max))
  elif loot == loot_list[1]:
    Player.defe += 1
    print("You found a {}, your defense is increased by 1! You now have {} defense.".format(loot, Player.defe))
  elif loot == loot_list[2]:
    axe_min = 2
    axe_max = 4
    if Player.dmg_min < axe_min and Player.dmg_max < axe_max:
      Player.dmg_min = axe_min
      Player.dmg_max = axe_max
      print("You found an {}! It looks stronger than your current weapon. You now have {} - {} damage.".format(loot, Player.dmg_min, Player.dmg_max))
  elif loot == loot_list[3]:
    Player.defe += 1
    print("You found a {}! It looks sturdy. Your defense is increased by 1. You now have {} defense.".format(loot, Player.defe))

def Quest(item, location, reward):
  item = item
  location = location
  reward = reward
  have_item = False
  ans = input("Greetings, traveller. If you want to earn some coin, I have something for ya. I lost {} at the {} narby. Bring it to me, and I will give you {} coins. It may be dangerous... Would you like to help me? (yes/no)"'\n'.format(item, location, reward))
  time.sleep(0.2)
  if ans == "yes":
    print("Great! I will show you the way...")
    time.sleep(0.3)
    leave = False
    while leave == False:
      if location == "farm":
        ans = input("You stand in front of a farm. It looks abandoned. You can either go in or check around. (in/around)"'\n')
        if ans == "in":
          ans = input("You are opening the front door. When you walk in, you see a big mess. Windows are broken, furniture is all around the floor. Something is behind you. You turn around. It jumps on you. You unsheet your weapon and get ready for combat...")
          Combat(7,2,3,2)
          input("After the fight you see the {} tavernkeeper asked you to bring him back on him. You quickly take it.")
          have_item = True
          ans = input("You can either leave or check the farm. (check/leave)"'\n')
          if ans == "check":
            print("While scavenging the farm, you find a pouch with 3 coins!")
            time.sleep(1)
            ans = input("You can continue searching or leave. Sun sets soon... (continue/leave)"'\n')
            if ans == "continue":
              print("Outside is already dark... but the search was worth it. You found ")
            else:
              print("You are walking away. You have your reward, let's not push your luck...")
          else:
            print("You are walking away. You have your reward, let's not push your luck...")
            time.sleep(2)
            leave = True
      elif location == "cave": 
        leave_loc = False
        ans = input("You stand in front of a cave. You see blood trails leading into the cave. It is certain that something will be there... Will you take the risk? (yes/no)"'\n')
        if ans == "yes":
          print("You walk in... Blood is all over the floor and walls. Guts are making you sick.")
          went_right = False
          while leave_loc == False:
            ans = input("You see two ways. The left way leads to a bigger room with dim light. The right way leads is dark and seems lifeless. But who knows what is hiding in there... You can still go away. (left/right/away)"'\n')
            if ans == "left":
              ans = input("You go to the left. The sounds are getting louder and louder. You see a creature eating something at a fireplace. You see the {} tavernkeeper asked you to bring him back... Fortunately, the creature hasn't noticed you. You can fight it or go back. (fight, back)"'\n'.format(item))
              if ans == "fight":
                print("You are approaching the creature. It stops eating and grunts. Prepare for the battle...")
                Combat(7, 1, 3, 2)
                have_item = True
                print("After you the defeated creature, you see what it was eating. A human. Better take that {} and go away...".format(item))
                leave = True
                leave_loc = True
              else:
                print("You are going back to the entrance.")
            elif ans == "right":
              if went_right == False:
                Player.hp -= 1
                print("You are going right. For a while you see nothing. As your eyes get used to the darkness, you see bones and pickaxes. Looks like this cave was a mine. You are searching the ground and find 2 coins! Unfortunately, a rat bite you and you loose 1 health. You now have {} health.".format(Player.hp))
                went_right = True
              else:
                print("You alredy went there...")
            else:
              print("You are leaving the cave.")
              leave = True
              leave_loc = True
        else:
          print("You are leaving this place. Maybe only death awaits you there...")
          leave = True
      else: #GRAVEYARD
        print("")
    if have_item == True:
      print("You get back to the tavern. Tavernkeeper is surprised you cambe back in one piece. You give him the {} and he gives you {} coins. Maybe you can buy new gear...".format(item, reward))
      Player.coins += reward
      Player.lvl = 2
    else:
      print("You ran away? Can't really blame you... Come again later, I will always have something for you.")

  else:
    print("Ok, I guess you can't be bothered...")
    
def Talk():
  leave = False
  while leave == False:
    print("You go to the tavernkeeper. Maybe he has something to say...")
    Quest("necklace", "cave", 6)
    leave = True

def ActOne():
    print("You are starting with {} health, ( {} - {} ) damage, {} defense, {} coins.".format(Player.hp, Player.dmg_min, Player.dmg_max, Player.defe, Player.coins))

    ans = input("You find yourself in the middle of a forest. You are disoriented and your head hurts. How did you get here? You can see human footsteps and a lake in a distance. What are you going to do? (steps/lake) "'\n')
    time.sleep(0.2)
    if ans == "lake":
      ans = input("Good, you follow the path and reach the lake... Do you swim across or go around (across/around)? "'\n')
      time.sleep(0.2)
      if ans == "across":
        ans = input("You are testing the waters... The water is cold and muddy. You can't see your submerged legs. You have a long journey ahead... Some time later, you feel something under you. It felt small, but dangerous. You can try to swim faster OR hold the tempo and swim calmly (faster/slowly). "'\n')
        time.sleep(0.2)
        if ans == "faster":
          print("Your swimming attracted piranhas. They bite you and you loose 2 HP.")
          Player.hp -= 2
          End()
          time.sleep(0.2)
          print("Your health is {}.".format(Player.hp))
        else: #CALM
          print("You keep calm and swim safely to the shore. You see an old fishing shack.")
      else: #AROUND
        print("You went to the left around the lake. Even though the route around is longer, you feel relieved. The lake is looking suspicious. The forest on your left is looking scary. Better hurry. To that old fishing shack.")
      

      ans = input("You are approaching the shack. It looks abandoned, but who knows what can be hiding in there. You can go inside, look around or go away to the forest. What is your decision? (inside/around/away) "'\n')
      time.sleep(0.2)
      if ans == "inside":
        ans = input("You open the front door. Rusty sound is piercing through quiet, dim interior. Disgusting, metal smell is making your eyes wet. You are looking around, noone to be seen. You can see a blood trail heading outside through a broken window. You can search around, maybe find something of use, or go away. (search/away) "'\n')
        time.sleep(0.2)
        if ans == "search":
          print("After a while, you find a rusty knife. It's not great, but better than bare hands...")
          Player.dmg_max += 1
          print("Your damage was increased by 1! You now have ( {} - {} ) damage!".format(Player.dmg_min, Player.dmg_max))
          ans = input("With a weapon in your hand, you can go check the blood trail or go away. (check/away) "'\n')
          time.sleep(0.2)
          if ans == "check":
            ans = input("You go outside, following the trail. You come to some basement door. Will you open the door or go away? (open/away) "'\n')
            time.sleep(0.2)

            if ans == "open":
              ans == input("As you are opening the door, you freeze in panic. You see a human-like creature eating a poor man. An urge to puke is bigger with every second looking at the massacre. The creature sees you. Turns around quickly. Blood is dripping from it's mouth. You can now see the creature more clearly. It's lifeless eyes are piecing through you as it's coming towards you. You probably won't run away, with your rusty knife in your hand, you either run towards it and attack first, or you wait for it to come closer and try to wait for a good opportunity. (attack/wait) "'\n')
              time.sleep(0.2)
              if ans == "attack":
                print("You plunge onto it. Taking the creature by surprise (creature's defense decreased by 1).")
                Combat(6,1,3,0)

              else:
                print("You are waiting and preparing for the right moment, increasing your defense by 1.")
                Player.defe += 1
                Combat(6,1,3,1)
              
            else: #AWAY
              print("You move away from the shack. Who knows what's hiding in there. You are heading towards the forest, leaving the shack far behind you...")
              time.sleep(0.2)
          else: #AWAY
            print("You are quickly going away. Who knows what can surprise you.")
            time.sleep(0.2)
          

      elif ans == "around":
        ans = input("You are scouting the outside of the shack. You see a blood trail heading through a window to the back of the shack. When you are following the trail, you stand in front of some basement door. Will you open the door or go away? (open/away)"'\n')
        time.sleep(0.2)
        if ans == "open":
          ans = input("As you are opening the door, you freeze in panic. You see a human-like creature eating a poor man. An urge to puke is bigger with every second looking at the massacre. The creature sees you. Turns around quickly. Blood is dripping from it's mouth. You can now see the creature more clearly. It's lifeless eyes are piecing through you as it's coming towards you. You probably won't run away, with your rusty knife in your hand, you either run towards it and attack first, or you wait for it to come closer and try to wait for a good opportunity. (attack/wait) "'\n')
          time.sleep(0.2)
          if ans == "attack":
            print("You plunge onto it. Taking the creature by surprise (creature's defense decreased by 1).")
            Combat(6,1,3,0)
            
          else:
            print("You are waiting and preparing for the right moment, increasing your defense by 1.")
            Player.defe += 1
            Combat(6,1,3,1)
        else:
          print("You move away from the shack. Who knows what's hiding in there. You are heading towards the forest, leaving the shack far behind you...")
      else: #AWAY
	      print("You move away from the shack. Who knows what's hiding in there. You are heading towards the forest, leaving the shack far behind you...")

      ans = input("In the middle of the forest you see an abandoned camp. Smoke is coming from the fireplace, somebody was here not so long ago. You see a leather bag with a bandage and some coins. As the sun sets and darkness is rising, you can either stay in the camp, or take the bag and continue. (stay/continue) "'\n') 
      time.sleep(0.2)
      Player.coins += 5
      if ans == "stay":
        time.sleep(0.2)
        if Player.combat == True:
          print("You are trying to light up the fireplace. You finally feel the warmth. The fight worned you. You are grabing the bandage and try to bandage yourself. Luckily, wounds aren't so bad. It looked like the creature was young, not so experienced. Bleeding wounds are finally sealed.")
          time.sleep(0.5)
          Player.hp += 3
          print("The bandage heals you for 3 health. Your health is now: {}.".format(Player.hp))
          time.sleep(0.2)
          print("You see 5 coins in a leather pouch. Maybe it will come handy. You now have {} coins."'\n'"As you are falling asleep, you are trying to remember, why the hell are you here. Let's hope that you will survive until morning...".format(Player.coins))
        else:
          time.sleep(0.2)
          print("You are trying to light up the fireplace. You finally feel the warmth. You see 5 coins in a leather pouch. Maybe it will come handy. You now have {} coins."'\n'"As you are falling asleep, you are trying to remember, why the hell are you here. Let's hope that you will survive until morning...".format(Player.coins))
          Player.bandage = True
          time.sleep(0.2)
        print("You are waking up. Luckily nothing found you here sleeping. As soon as possible, you continue walking. Better not push your luck again.")

      else: #CONTINUE
        print("You are grabbing the bag and continue walking. Though it may be dangerous, sleeping in the forest may be worse...")
        if Player.combat == True:
          time.sleep(0.2)
          print("As you are walking, you take a look inside the bag, you see a bandage. Walking and bandaging is hard, but you finally did it. The wounds are sealed.")
          Player.hp += 2
          time.sleep(0.2)
          print("The bandage heals you for 2 health. Your health is now: {}.".format(Player.hp))
          time.sleep(0.2)
          print("You see 5 coins in a leather pouch. Maybe it will come handy. You now have {} coins."'\n'"As you are walking along the path, you are trying to remember, why the hell are you here...".format(Player.coins))
          time.sleep(0.2)
        else:
          Player.defe -= 1
          time.sleep(0.2)
          print("As you are walking, you take a look inside the bag, you see a bandage. It may come handy.You see 5 coins in a leather pouch. Maybe it will come handy. You now have {} coins."'\n' "As you are walking along the path, you are trying to remember, why the hell are you here... Sun rises and you are very tired. You loose 1 defense. Better be tired than being dead at the camp you passed." '\n' "You now have {} defense.".format(Player.coins, Player.defe))
          Player.bandage = True
          time.sleep(0.2)
    
    else:
      print("You follow the footsteps through the forest. Scary sounds are echoing around you. You feel an urge to look back. When you turn around to look behing you, your body freezes as you look into the red and lifeless eyes. Sudden pain strikes through your body, you can no longer move. You see the world spin around. Your detached head is landing on the ground... The horror is over.")
      End()

def ActTwo():
  print("After a few hours you stand in front of a tavern. The tavern sits on a crossroad. It doesn't look like the shack you saw. You hear... voices? You come in. The place is full of people, four, to be exact. Normal people. A tavernkeeper looks at you. The other three men are not paying any attention to you. They are just playing something. You are finally asked by the tavernkeeper.")
  time.sleep(3)
  print("'Who are you?', he asked. 'My name is {}, I woke up in the forest nearby and don't know how I got here... Tell me, what is happening here?'. The taverkeeper stares at you and answers: 'Interesting. This town is haunted. Dunno if you encountered it, but we are plagued by cursed creatures. It was maybe a month ago. The sky turned green and some people... just begun changing. They were screaming, disgusting to hear. Their bodies were changing... Ever since, we are hiding over here. For some reason they can't go away from that forest. Because of that incident, we are forbidden from ot her towns. They think we are cursed and attack us on sight...'".format(Player.name))
  time.sleep(5)
  print("Now that he is talking about that, you remember a green sky and roars. Unfortunately, nothing else...")
  Tavern()

Start()

