import time
import sys
import random

print("Welcome to my horror game.")
name = input("What is your name? "'\n')
time.sleep(0.5)
print("Hello,", name)

class Player:
  hp = 10
  dmg = 2
  defe = 1
  coins = 0
class Enemy:
   def __init__(this, hp, dmg, defe):
    this.hp = hp 
    this.dmg = dmg
    this.defe = defe


print("You are starting with", Player.hp, "health,""( 1 -",Player.dmg,") damage,", Player.defe, "defense,", Player.coins, "coins.")

def Combat():
  print("The combat begins!")
  print("Your stats: ", Player.hp, "health,""( 1 -",Player.dmg,") damage,", Player.defe, "defense.")
  print("Enemy's stats: ", Enemy.hp, "health,""( 1 -",Enemy.dmg,") damage,", Enemy.defe, "defense.")
  time.sleep(3)
  while Enemy.hp > 0 and Player.hp > 0:
    player_hit = random.randint(1, Player.dmg)
    enemy_hit = random.randint(1, Enemy.dmg)
    Enemy.hp = Enemy.hp - (player_hit - Enemy.defe)
    print("Your turn. You are hitting it for",player_hit,"damage. The creature's HP is",Enemy.hp)
    if Enemy.hp <= 0:
      print("You have finally defeated it. It was a hard fight. You survived with", Player.hp,"health.")
      time.sleep(1)
      break
    time.sleep(3)
    Player.hp = Player.hp - (enemy_hit - Player.defe)
    print("The beast is hitting you for", enemy_hit,"damage. Your HP is", Player.hp)
    if Player.hp <= 0:
      sys.exit("You died...")
    time.sleep(3)
  print("You continue on your journey...")
  time.sleep(2)


ans = input("Do you want to play? Y or N "'\n').lower()
if ans == "y":
  print("Good...")
  ans = input("You find yourself in the middle of a forest. You are disoriented and your head hurts. How did you get here? You can see human footsteps and a lake in a distance. What are you going to do? (steps/lake) "'\n')
  time.sleep(0.5)
  if ans == "lake":
    ans = input("Good, you follow the path and reach the lake... Do you swim across or go around (across/around)? "'\n')
    time.sleep(0.5)
    if ans == "across":
      ans = input("You are testing the waters... The water is cold and muddy. You can't see your submerged legs. You have a long journey ahead... Some time later, you feel something under you. It felt small, but dangerous. You can try to swim faster OR hold the tempo and swim calmly (faster/slowly). "'\n')
      time.sleep(0.5)
      if ans == "faster":
        print("Your swimming attracted piranhas. They bite you and you loose 2 HP.")
        Player.hp -= 2
        time.sleep(0.5)
        print("Your health is", Player.hp)
      else: #CALM
        print("You keep calm and swim safely to the shore. You see an old fishing shack.")
    else: #AROUND
      print("You went to the left around the lake. Even though the route around is longer, you feel relieved. The lake is looking suspicious. The forest on your left is looking scary. Better hurry. To that old fishing shack.")
      

    ans = input("You are approaching the shack. It looks abandoned, but who knows what can be hiding in there. You can go inside, look around or go away to the forest. What is your decision? (inside/around/away) "'\n')
    time.sleep(0.5)
    if ans == "inside":
      ans = input("You open the front door. Rusty sound is piercing through quiet, dim interior. Disgusting, metal smell is making your eyes wet. You are looking around, noone to be seen. You can see a blood trail heading outside through a broken window. You can search around, maybe find something of use, or go away. (search/away) "'\n')
      time.sleep(0.5)
      if ans == "search":
        print("After a while, you find a rusty knife. It's not great, but better than bare hands...")
        Player.dmg += 1
        print("Your damage was increased by 1! You now have ", Player.dmg,"damage!")
        ans = input("With a weapon in your hand, you can go check the blood trail or go away. (check/away) "'\n')
        time.sleep(0.5)
        if ans == "check":
          ans = input("You go outside, following the trail. You come to some basement door. Will you open the door or go away? (open/away) "'\n')
          time.sleep(0.5)

          if ans == "open":
            ans == input("As you are opening the door, you freeze in panic. You see a human-like creature eating a poor man. An urge to puke is bigger with every second looking at the massacre. The creature sees you. Turns around quickly. Blood is dripping from it's mouth. You can now see the creature more clearly. It's lifeless eyes are piecing through you as it's coming towards you. You probably won't run away, with your rusty knife in your hand, you either run towards it and attack first, or you wait for it to come closer and try to wait for a good opportunity. (attack/wait) "'\n')
            Enemy = Enemy(6, 3, 1)
            combat = True
            time.sleep(0.5)
            if ans == "attack":
              print("You plunge onto it. Taking the creature by surprise (creature's defense decreased by 1).")
              Enemy.defe -= 1
              Combat()

            else:
              print("You are waiting and preparing for the right moment, increasing your defense by 1.")
              Player.defe += 1
              Combat()
              
          else: #AWAY
            print("You move away from the shack. Who knows what's hiding in there. You are heading towards the forest, leaving the shack far behind you...")
        else: #AWAY
          print("You are quickly going away. Who knows what can surprise you.")
          

    elif ans == "around":
      ans = input("You are scouting the outside of the shack. You see a blood trail heading through a window to the back of the shack. When you are following the trail, you stand in front of some basement door. Will you open the door or go away? (open/away)"'\n')
      if ans == "open":
        ans = input("As you are opening the door, you freeze in panic. You see a human-like creature eating a poor man. An urge to puke is bigger with every second looking at the massacre. The creature sees you. Turns around quickly. Blood is dripping from it's mouth. You can now see the creature more clearly. It's lifeless eyes are piecing through you as it's coming towards you. You probably won't run away, with your rusty knife in your hand, you either run towards it and attack first, or you wait for it to come closer and try to wait for a good opportunity. (attack/wait) "'\n')
        Enemy = Enemy(6, 3, 1)
        combat = True
        if ans == "attack":
          print("You plunge onto it. Taking the creature by surprise (creature's defense decreased by 1).")
          Enemy.defe -= 1
          Combat()
            
        else:
          print("You are waiting and preparing for the right moment, increasing your defense by 1.")
          Player.defe += 1
          Combat()
      else:
        print("You move away from the shack. Who knows what's hiding in there. You are heading towards the forest, leaving the shack far behind you...")
    else: #AWAY
	    print("You move away from the shack. Who knows what's hiding in there. You are heading towards the forest, leaving the shack far behind you...")

    ans = input("In the middle of the forest you see an abandoned camp. Smoke is coming from the fireplace, somebody was here not so long ago. You see a leather bag with a bandage and some coins. As the sun sets and darkness is rising, you can either stay in the camp, or take the bag and continue. (stay/continue) "'\n') 
    time.sleep(0.5)
    Player.coins += 5
    if ans == "stay":
      if combat == True:
        print("You are trying to light up the fireplace. You finally feel the warmth. The fight worned you. You are grabing the bandage and try to bandage yourself. Luckily, wounds aren't so bad. It looked like the creature was young, not so experienced. Bleeding wounds are finally sealed.")
        Player.hp += 3
        print("The bandage heals you for 3 health. Your health is now:",Player.hp)
        print("You see 5 coins in a leather pouch. Maybe it will come handy. You now have", Player.coins, "coins."'\n'"As you are falling asleep, you are trying to remember, why the hell are you here. Let's hope that you will survive until morning...")
      else:
        print("You are trying to light up the fireplace. You finally feel the warmth. You see 5 coins in a leather pouch. Maybe it will come handy. You now have", Player.coins, "coins."'\n'"As you are falling asleep, you are trying to remember, why the hell are you here. Let's hope that you will survive until morning...")
        bandage = True
      print("You are waking up. Luckily nothing found you here sleeping. As soon as possible, you continue walking. Better not push your luck again.")


    else: #CONTINUE
      print("You are grabbing the bag and continue walking. Though it may be dangerous, sleeping in the forest may be worse...")
      if combat == True:
        print("As you are walking, you take a look inside the bag, you see a bandage. Walking and bandaging is hard, but you finally did it. The wounds are sealed.")
        Player.hp += 2
        print("The bandage heals you for 2 health. Your health is now:",Player.hp)
        print("You see 5 coins in a leather pouch. Maybe it will come handy. You now have", Player.coins, "coins."'\n'"As you are walking along the path, you are trying to remember, why the hell are you here...")
      else:
        Player.defe -= 1
        print("As you are walking, you take a look inside the bag, you see a bandage. It may come handy.You see 5 coins in a leather pouch. Maybe it will come handy. You now have", Player.coins, "coins."'\n' "As you are walking along the path, you are trying to remember, why the hell are you here... Sun rises and you are very tired. You loose 1 defense. Better be tired than being dead at the camp you passed." '\n' "You now have", Player.defe,"defense.")
        bandage = True
    






  else:
    print("You follow the footsteps through the forest. Scary sounds are echoing around you. You feel an urge to look back. When you turn around to look behing you, your body freezes as you look into the red and lifeless eyes. Sudden pain strikes through your body, you can no longer move. You see the world spin around. Your detached head is landing on the ground... The horror is over.")
    ans = input("Would you like another try? (yes/no) '\n'")
    if ans == "yes":
      print()
    else:
      print()
else:
  print("Pussy...")

def act_two():
  print("After a few hours you stand in front of a tavern. The tavern sits on a crossroad. It doesn't look like the shack you saw. You hear... voices? You come in. The place is full of people, four, to be exact. Normal people. A tavernkeeper looks at you. Not a word. The other three men are not paying any attention to you. They are just staring at their beer.")

