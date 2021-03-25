print("Welcome to my first game")
name = input("What is your name? ")

print("Hello,", name)

health = 10
dmg = 1
defe = 1
agi = 3

print("You are starting with", health, "health,", dmg, "damage,", defe, "defense and", agi, "agility.")


ans = input("Do you want to play? Y or N ").lower()
if ans == "y":
  print("Good...")
  ans = input("You find yourself in the middle of a forest. You are disoriented and your head hurts. How did you get here? You can see man footsteps and a lake in a distance. What are you going to do? (steps/lake) ")
  if ans == "lake":
    ans = input("Good, you follow the path and reach the lake... Do you swim across or go around (across/around)? ")
    if ans == "across":
      ans = input("You are testing the waters... The water is cold and muddy. You can't see your submerged legs. You have a long journey ahead... Some time later, you feel something under you. It felt small, but dangerous. You can try to swim faster OR hold the tempo and swim calmly (faster/slowly). ")
      if ans == "faster":
        print("Your swimming attracted piranhas. They bite you and you loose 2 HP.")
        health -= 2
        print("Your health is", health)
      else: #CALM
        print("You keep calm and swim safely to the shore. You see an old fishing shack.")
    else: #AROUND
      print("You went to the left around the lake. Even though the route around is longer, you feel relieved. The lake is looking suspicious. The forest on your left is looking scary. Better hurry. To that old fishing shack.")

    ans = input("You are approaching the shack. It looks abandoned, but who knows what can be hiding in there. You can go inside, look around or go away to the forest. What is your decision? (inside/around/away) ")
    if ans == "inside":
      ans = input("You open the front door. Rusty sound is piercing through quiet, dim interior. Disgusting, metal smell is making your eyes wet. You are looking around, noone to be seen. You can see a blood trail heading outside through a broken window. You can search around, maybe find something of use, or go away. (search/away)")
      if ans == "search":
        print("After a while, you find a rusty knife. It's not great, but better than bare hands...")
        dmg += 1
        print("Your damage was increased by 1! You now have ", dmg, "!")
        ans = input("With a weapon in your hand, you can go check the blood trail or go away. (check/away) ")
        if ans == "check":
          ans = input("You go outside, following the trail. You come to some basement door. Will you open the door or go away? (open/away) ")

          if ans == "open":
            ans == input("As you are opening the door, you freeze in panic. You see a human-like creature eating a poor man. An urge to puke is bigger with every second looking at the massacre. The creature sees you. Turns around quickly. Blood is dripping from it's mouth. You can now see the creature more clearly. It's lifeless eyes are piecing through you as it's coming towards you. You probably won't run away, with your rusty knife in your hand, you either run towards it and attack first, or you wait for it to come closer and try to wait for a good opportunity. (attack/wait) ")

          else: #AWAY
            print("You move away from the shack. Who knows what's hiding in there. You are heading towards the forest, leaving the shack far behind you...")
        else: #AWAY
          print("You are quickly going away. Who knows what can surprise you.")
    elif ans == "around":
      ans = input("You are scouting the outside of the shack. You see a blood trail heading through a window to the back of the shack. When you are following the trail, you stand in front of some basement door. Will you open the door or go away? (open/away)")
      if ans == "open":
        ans = input("You open the front door. Rusty sound is piercing through quiet, dim interior. Disgusting, metal smell is making your eyes wet. You are looking around, noone to be seen. You can see a blood trail heading outside through a broken window. You can search around, maybe find something of use, or go away. (search/away)")
      else:
        print("You move away from the shack. Who knows what's hiding in there. You are heading towards the forest, leaving the shack far behind you...")
    else: #AWAY
	    print("You move away from the shack. Who knows what's hiding in there. You are heading towards the forest, leaving the shack far behind you...")
  else:
    print("You follow the footsteps through the forest. Scary sounds are echoing around you. You feel an urge to look back. When you turn around to look behing you, your body freezes as you look into the red and lifeless eyes. Sudden pain strikes through your body, you can no longer move. You see the world spin around. Your detached head is landing on the ground... The horror is over.")
else:
  print("Pussy...")
