print('''
          ______
   _.-\':::::::`.
   \\::::::::::::`.-._
    \\:::\'\'   `::::`-.`.
     \\         `:::::`.\\
      \\          `-::::`:
       \\______       `:::`.
       .|_.-\'__`._     `:::\\
      ,\'`|:::|  )/`.     \:::
     /. -.`--'  : /.\     ::|
     `-,-'  _,'/| \\|\\\\    |:|
      ,'`::.    |/>`;'\   |:|
      (_\\ \\:.:.:`((_));`. ;:|
      \\.:\\ ::_:_:_`-\',\'  `-:|
       `:\\\\|        :
          )`__...---'
''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
s=input("You have a choice; for some the first, for some the last (Left or Right?)\n")
if s=="Left":
    s1=input("There is a lake. As vast as the oceans of Shadesnas, as small as the puddles of Kabarnath. Would you wait for the boat or try your luck by swimming.\n")
    if s1=="Swim":
        s2=input("There are three door. The three doors of silence with a silence of three parts. Which silence would you choose?(First, Second or Third)\n")
        if s2=="Third":
            print("Congratulations, you have found the treasure")
            print('''
                   ____...------------...____
               _.-\"` /o/__ ____ __ __  __ \\o\\_`\"-._
             .\'     / /                    \\ \\     \'.
             |=====/o/======================\\o\\=====|
             |____/_/\________..____..________\\_\\____|
             /   _/ \\_     <_o#\\__/#o_>     _/ \\_   \\
             \\_________\\####/_________/
              |===\\!/========================\\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \\() ()/        | |   |
              |===|o|======{\'-.) A (.-\'}=====|o|===|
              | __/ \\__     \'-.\\uuu/.-\'    __/ \\__ |
              |==== .\'.\'^\'.\'.====|
              |  _\\o/   __  {.\' __  \'.} _   _\o/  _|
              `\"\"\"\"-\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"-\"\"\"\"`
                  ''')
        else:
            print("You fell into a hole. Game Over.")
    else:
        print("You get attacked by an angry boatsman. Game Over.")
else:
    print("You enter a room of beasts. Game Over.")