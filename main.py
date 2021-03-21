print("Welcome to my first game")
name = input("What is your name? ")
age = int((input("What is your age? ")))

print("Hello,", name, "you are", age, "old.")

health = 10

print("You are starting with", health, "health.")

if age >= 18:
 print("You may enter...")
 wants_to_play = input("Do you want to play? Y or N ").lower()
 if wants_to_play == "y":
   print("Good...")

   left_or_right = input("First choice... Left or Right (left/right)? ")
   if left_or_right == "left":
     ans = input("Good, you follow the path and reach a lake... Do you swim across or go around (across/around)? ")
     if ans == "across":
       ans = input("You are testing the waters... The water is cold and muddy. You can't see your submerged legs. You have a long journey ahead... Some time later, you feel something under you. It felt small, but dangerous. You can try to swim faster OR hold the tempo and swim calmly (faster/slowly). ")
       if ans == "faster":
         print("Your swimming attracted piranhas. They bite you and you loose 2 HP.")
         health -= 2
         print("Your health is", health)
       else:
          print("You keep calm and swim safely to the shore. You see an old fishing shack.")
     else:
        print("You went to the left around the lake. Even though the route around is longer, you feel relieved. The lake is looking suspicious. The forest on your left is looking scary. Better hurry. To that old fishing shack.")
     ans = input("You are approaching the shack. It looks abandoned, but who knows what can be hiding in there.")


   else:
     print("You follow the path through the forest. Scary sounds are echoing around you. You feel an urge to look back. When you turn around to look behing you, your body freezes as you look into the red and lifeless eyes. Sudden pain strikes through your body, you can no longer move. You see the world spin around. Your detached head is landing on the ground... The horror is over.")
  
     


 else:
   print("Pussy...")

  





else:
  print("You are not old enough to play...")
