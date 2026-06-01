import random
import sys

count=0

def play_rsp():

     player_choice=input("ENTER....\n1 ROCK \n2 SCISSORS \n3 PAPER\n \n")
     player=str(player_choice.upper())

     if player not in "ROCK" "PAPER" "SCISSORS" :
          return play_rsp()

     computer_choice=random.choice(['ROCK', 'SCISSORS', 'PAPER'])
     computer=str(computer_choice)


     print("MY CHOICE:",player)
     print("COMPUTER CHOICE:",computer)

     if player=="ROCK" and computer=="SCISSORS":
          print("YOU HAVE WIN THE GAME🤩")
     elif player =="SCISSORS" and computer=="PAPER":
          print("YOU HAVE WIN THE GAME🤩")
     elif player=="PAPER" and computer=="ROCK":
          print("YOU HAVE WIN THE GAME🤩")
     elif player == computer:
          print("TIE GAME😑")
     else:
          print('YOU ARE DEFEAD😒\n 🖥️ COMPUTER IS WIN THE GAME\n BETTER LUCK NEXT TIME')     
     
     global count
     count+=1
     print(count)
     while True:
          playagain=input("Y FOR YES-PLAYAGAIN\n Q FOR QUIT-STOP THE GAME")
          if playagain.lower() not in ("y","q") :
               continue
          else:
               break

     if playagain.lower()=="y" :
          return play_rsp()
     else :
          print("THANKS FOR PLAYING")
          sys.exit("BYE")

play_rsp()          

