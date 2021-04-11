import time
import random
import sys

def PlayerRestart():
  Player.hp = 10
  Player.dmg_min = 1
  Player.dmg_max = 2
  Player.defe = 1
  Player.coins = 0
  Player.bandage = False
  Player.combat = False
  Player.lvl = 1.0

def Start():
  print("Welcome to my horror game.")
  Player.name = input("What is your name? "'\n')
  time.sleep(0.2)
  PlayerRestart()
  print("Hello,", Player.name)
  time.sleep(0.2)
  print("You are starting with {} health, ( {} - {} ) damage, {} defense, {} coins.".format(Player.hp, Player.dmg_min, Player.dmg_max, Player.defe, Player.coins))
  time.sleep(0.2)
  ans = input("Ready to start? (yes/no)"'\n')
  if ans == "yes":
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

def Save():
  pass

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

def Combat(enemy, hp, dmg_min, dmg_max, defe):
  enemy = enemy
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
    print("Your turn. You are hitting it for {} damage. The {}'s HP is {}.".format(player_hit, enemy, Enemy.hp))
    if Enemy.hp <= 0:
      print("You have finally defeated it. It was a hard fight. You survived with {} health.".format(Player.hp))
      time.sleep(1)
      break
    time.sleep(2)
    Player.hp -= enemy_hit
    print("The {} is hitting you for {} damage. Your HP is {}.".format(enemy, enemy_hit, Player.hp))
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
  time.sleep(2)

def Tavern():
  leave = False
  while leave == False:  
    ans = input("You stand in the middle of the tavern. You can go buy some stuff, go gamble with a group of men, go speak with the tavernkeeper or leave the tavern. (shop/gamble/talk/leave)"'\n')
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
      if Player.coins <= 0:
        print("You don't have enough coins to play!")
        time.sleep(2)
        leave = True
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
  time.sleep(1)
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
    else: 
      print("You found an axe. Unfortunately, it is weaker than your current weapon. You leave it where you found it.")
  elif loot == loot_list[3]:
    Player.defe += 1
    print("You found a {}! It looks sturdy. Your defense is increased by 1. You now have {} defense.".format(loot, Player.defe))

def Quest():
  locations = ["Farm", "Cave", "Harbor"]
  location = random.choice(locations)
  items = ["Necklace", "Ring", "Emblem", "Talisman", "Sword", "Book"]
  item = random.choice(items)
  reward = random.randint(3, 10)

  ans = input("Greetings, traveller. If you want to earn some coin, I have something for ya. I lost {} at the {} narby. Bring it to me, and I will give you {} coins. It may be dangerous... Would you like to help me? (yes/no)"'\n'.format(item, location, reward))
  if ans == "yes":
    print("Great! I will show you the way...")
    time.sleep(0.3)

    have_item = False

    if location == locations[0]:
      have_item = Farm()
    elif location == locations[1]:
      have_item = Cave()
    else: 
      have_item = Harbor()

    if have_item == True:
      print("You get back to the tavern. Tavernkeeper is surprised you cambe back in one piece. You give him the {} and he gives you {} coins. Maybe you can buy new gear...".format(item, reward))
      Player.coins += reward
      Player.lvl = 2
  else:
    print("I guess you can't be bothered... Can't blame you really. Well, if you change your mind. come again.")
    
def Talk():
  leave = False
  while leave == False:
    print("You go to the tavernkeeper. Maybe he has something to say...")
    Quest()
    leave = True

def Farm():
  leave = False
  while leave == False:
    ans = input("You stand in front of a farm. It looks abandoned. You can either go in or go away. (in/away)"'\n')
    if ans == "in":
      ans = input("You are opening the front door. When you walk in, you see a big mess. Windows are broken, furniture is all around the floor. Something is behind you. You turn around. It jumps on you. You unsheet your weapon and get ready for combat...")
      Combat("beast",7,2,3,2)
      input("After the fight you see the {} tavernkeeper asked you to bring him back on him. You quickly take it.")
      have_item = True
      ans = input("You can either leave or check the farm. (check/leave)"'\n')
      if ans == "check":
        print("While scavenging the farm, you find a pouch with 3 coins!")
        time.sleep(1)
        ans = input("You can continue searching or leave. Sun sets soon... (continue/leave)"'\n')
        if ans == "continue":
          print("Outside is already dark... but the search was worth it.")
          RandomLoot()
        else:
          print("You are walking away. You have your reward, let's not push your luck...")
          time.sleep(2)
          return have_item
          leave = True
      else:
        print("You are walking away. You have your reward, let's not push your luck...")
        time.sleep(2)
        return have_item
        leave = True
    else: 
      print("You go away from the farm back. You didn't feel good about that place...")
      leave = True

def Cave():
  leave = False
  while leave == False:
    leave_loc = False
    ans = input("You stand in front of a cave. You see blood trails leading into the cave. It is certain that something will be there... Will you take the risk? (yes/no)"'\n')
    if ans == "yes":
      print("You walk in... Blood is all over the floor and walls. Guts are making you sick.")
      went_right = False
      while leave_loc == False:
        ans = input("You see two ways. The left way leads to a bigger room with dim light. The right way leads is dark and seems lifeless. But who knows what is hiding in there... You can still go away. (left/right/away)"'\n')
        if ans == "left":
          ans = input("You go to the left. The sounds are getting louder and louder. You see a creature eating something at a fireplace. You see what tavernkeeper asked you to bring him back... Fortunately, the creature hasn't noticed you. You can fight it or go back. (fight/back)"'\n')
          if ans == "fight":
            print("You are approaching the creature. It stops eating and grunts. Prepare for the battle...")
            Combat("beast",7, 1, 3, 2)
            have_item = True
            print("After you the defeated creature, you see what it was eating. A human. You take what you came for and go back to the tavern...")
            return have_item
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

def Harbor():
  leave = False
  while leave == False:
    ans = input("He takes you to the harbor warehouse. This place stinks like fish. There is only one way in - through the front door. Will you go there or go back to the tavern?(in/away)"'\n')
    if ans == "in":
      print("You unsheath your weapon and go in. The smell is getting worse and worse. You open the door and see a huge room.")
      time.sleep(0.5)
      ans = input("The tavernkeeper said that he left it in the chest somewhere on the second floor. You can either search the first floor or go to the second floor. (first/second)"'\n')
      if ans == "first":
        rand = random.randint(0,2)
        if rand == 1:
          Player.coins += 2
          print("You are lucky. Someone must have dropped a few coins on the ground. You found 2 coins. You now have {} coins! *33% chance*".format(Player.coins))
        else:
          print("You search the whole first floor. The creates are full of rotten fish. What else could you find in there?")
      time.sleep(1)
      print("You go to the second floor. Stairs are making loud sounds. You hope that there is nothing that will surprise you. As you are reaching the top, you see a light. When you come closer, you see a human. Just staring through you. You greet him, but he doesn't answer. Out of nowhere he gets up and starts yelling at you. You don't understand a single word. He is walking towards you. It looks like he has gone mad...")
      time.sleep(3)
      Combat("human", 6, 1, 3, 0)
      ans = input("Why did he attack you? He was insane. You take a look around. To get the wanted item and get out of here... Luckily it didn't take long. You finally find it. The tavernkeeper said something about military chests around here on the way here. You can stay and look around or go back. (search/away)"'\n')
      have_item = True
      time.sleep(0.5)
      if ans == "search":
        print("After a while, you find a chest with something.")
        RandomLoot()
        rand = random.randint(0,1)
        if rand == 1:
          time.sleep(0.5)
          print("But you won't get it for free. You hear weird sounds. As you take a look at the stairs, you see a zombie walking slowly. Maybe the human that attacked you was about to transform into zombie aswell? No time to think, you have to attack! *50% chance*")
          Combat("zombie", 15, 1, 4, 0)
          print("You hurry out. More zombies could be around. ")
          time.sleep(0.5)
          return have_item
          leave = True
        else:
          print("Luckily you find no resistance on the way out. You found what you need and go back to the tavern.")
          time.sleep(1)
          return have_item
          leave = True
    else:
      print("You go back to the tavern. Let's not risk your life...")
      leave = True


def ActOne():
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
                Combat("beast",6,1,3,0)

              else:
                print("You are waiting and preparing for the right moment, increasing your defense by 1.")
                Player.defe += 1
                Combat("beast",6,1,3,1)
              
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
            Combat("beast",6,1,3,0)
            
          else:
            print("You are waiting and preparing for the right moment, increasing your defense by 1.")
            Player.defe += 1
            Combat("beast",6,1,3,1)
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
      print("You follow the footsteps through the forest. Scary sounds are echoing around you. The footsteps are leading you to a scary mansion. You hear human screams. You walked back to the place you woke up...")
      time.sleep(2)
      ActOne()

def ActTwo():
  print("After a few hours you stand in front of a tavern. The tavern sits on a crossroad. It doesn't look like the shack you saw. You hear... voices? You come in. The place is full of people, four, to be exact. Normal people. A tavernkeeper looks at you. The other three men are not paying any attention to you. They are just playing something. You are finally asked by the tavernkeeper.")
  time.sleep(3)
  print("'Who are you?', he asked. 'My name is {}, I woke up in the forest nearby and don't know how I got here... Tell me, what is happening here?'. The taverkeeper stares at you and answers: 'Interesting. This town is haunted. Dunno if you encountered it, but we are plagued by cursed creatures. It was maybe a month ago. The sky turned green and some people... just begun changing. They were screaming, disgusting to hear. Their bodies were changing... Ever since, we are hiding over here. For some reason they can't go away from that forest. Because of that incident, we are forbidden from other towns. They think we are cursed and attack us on sight...'".format(Player.name))
  time.sleep(5)
  print("Now that he is talking about that, you remember a green sky and roars. Unfortunately, nothing else...")
  time.sleep(2)
  Tavern()
  print("Before you leave, you ask around where are other survivors. To the west of here is a small village. Few people are still living there... hopefully. You decide that you go there.")
  ans = input("Are you ready or do you want to buy something? (yes/no)"'\n')
  if ans == "no":
    Tavern()
  print("You are leaving the tavern and go to the village.")
  ans = input("Walking along the path you hear screams. The screams are few minutes on your left. You can go help to the person screaming or continue on your way. (help/continue)"'\n')
  if ans == "help":
    print("You are running towards the screaming humans. You see a man and a woman behind him. Both are wounded and their clothes torn. But they aren't attacked by the humanoid creature. It's a... skeleton? Sword wielding skeleton. You quickly unsheathe your weapon and attack it.")
    Combat("skeleton", 9, 2, 4, 2)
    print("You are still shaking from this experience. A skeleton? What is this? The pair thanks you for saving them. You ask them where did the skeleton come from. They tell you that they were trying to rob graves in the graveyard nearby. They had a friend coming with them, but he was stabbed by the skeleton. The skeleton was chasing them and caught them here. Luckily, you came at the right time. You look at them disgustedly. Robbing graves is sick. But death is not an adequate punishment... You send them back to the tavern. Before they go, the woman helps with your wounds and try to bandage you a little bit.")
    Player.hp += 3
    print("Your health is increased by 3. You now have {} health.".format(Player.hp))
  else:
    print("The screams for help are getting weaker. There could be more enemies. Maybe it was a smart decision not to go there...")


  print("Few hours later you approach the village. Not a soul to be seen. You see only three huts. You come to the first near you and knock on a door. Nothing happens. Maybe it is abandoned. You go the the second, biggest hut. A man armed with a knife opens a door, prepared for an enemy. He was relieved that you are a normal human. He lets you in and you see at least 2 families. They look scared and hopeless.")
  time.sleep(5)
  print("You take a seat and a cup with water. The armed man, Garvin, sits next to you and asks where are you from and how did you get here alive. You tell him his journey and that you came here from the tavern. He tells you that they can't get there, to the safety, because there is a lot of them and they would make an easy target for the monsters and undead. He also says that there is no escape. Borders are closed and there is no way out. Some men went to the always-dark swamps to a tower that had a lich inside. The lich was experimenting with undead and because of him, all these things are happening. Men never came back.")
  time.sleep(5)
  ans = input("You can help these things get to the tavern. The journey will take the whole day. Otherwise they will never get from here alive. Are you willing to help them, even though it will take longer, or go to the swamps. (help/go)"'\n')
  time.sleep(0.5)
  escort = False
  if ans == "help":
    escort = True
    print("You are willing to help them. Everyone is getting ready, grabbing necessary things to leave this place. The journey takes a long time, longer than expected. You are walking ahead and Garvin is behind the families. With a little bit of luck, all of you will survive...")
    time.sleep(5)
    engage = random.randInt(0, 1)
    if engage == 1:
      ans = input("A creature apprears. You can run towards him and quickly duel him, leaving Garvin to guard them, or stay near the families. If you wait for it to attack first, you may give time to another creature to come here. (attack/stay)"'\n')
      time.sleep(0.5)
      if ans == "attack":
        rand = random.randInt(0, 3)
        Combat("creature", 7, 2, 4, 2)
        print("You leave them behind you and attack at once...")
        
        if rand == 1:
          print("Unfortunately, another creature came while you were fighting. Garvin took the fight with it, but the creature was stronger. You came just in time to save him... *25% chance to happen*")
          Combat("creature", 6, 2, 5, 1)

      else:
        print("You hold your ground. Waiting for it to come closer.")
        Combat("creature", 7, 2, 4, 2)
        rand = random.randInt(0,2)
        if rand == 1:
          print("Unfortunately, another creature came while you were fighting. Garvin took the fight with it, but the creature was stronger. You came just in time to save him... *33% chance to happen*")
          Combat("creature", 6, 2, 5, 1)


    Player.coins += 5
    print("You approach the tavern. Luckily, everyone is safe now. They give you everything they can spare. You get 5 coins for your help. You now have {} coins. Since you are here, you go inside.".format(Player.coins))
    Tavern()
    print("It took you some time, but it was worth it. Walking back to the small village, you think about the folks. If you were to leave them, they would probably all end up dead...")
  else:
    print("You decide not to help them. You will help them on the way back... if you ever will come back...")

  print("On the way to the swamps you see a cave. ")
  
  

      

Start()

