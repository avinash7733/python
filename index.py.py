#imported a module called random
import random
#imported sqlite3 for database purpose
import sqlite3
#connection to the database
conn=sqlite3.connect('game.db')
#Creates a DB-API style cursor for find(),search(),execute(),execute_many()etc.
cursor=conn.cursor()
#lists are taken and data passed into it
list1=['BMW','Apple','Dog']
list2=['Diamond ring','Juice','Cat']
list3=['AC','Chair','Cap']
list4=['Boat','Suit','Salt']
list5=['Guitar','Cup','Pad']
#Above lists are initialised to a new list called (list6)
list6=[[list1],[list2],[list3],[list4],[list5]] 
#Random function is applied to the new list:(list6)
r=random.choice(list6)
#The randomly selected list indexes are assigned to variables below
a=r[0][0]
b=r[0][1]
c=r[0][2]
#Variable (count) is taken for attempts purpose
count=0
#Asking for the player to enter the name
name=input("                            ENTER YOUR NAME :"     )
print ("  \n                              WELCOME --->",name)
#Rules and all about the game are printed here
print('ABOUT GAME:\n' '___________\n\n' '1)Here You can see 3 Doors infront of you.\n'
'2)DOOR1               DOOR2              DOOR3\n'
'3)You have to CHOOSE a door from those.\n'
'4)There will be a Top Most prize in one of the doors displayed.\n'
'5)Based on the door selected ,the prize will be distributed.\n'
'6)Hope  you like it.  LET THE REAL FUN BEGIN !!\n\n')

                                                          
#Defining a class 
class game:
#defining a funtion and passed attributes into it
    def __init__(self,user):
        self.user = user
       
  


#defined another function inside the class
    def play(self):
      

#condition gets satisfied, the statement will get printed 
        if(self.user == "Door1"):

       
                print ("Searching.....")
                print ('CONGRAGULATIONS YOU WON  : ',a),self.user
               
         
        elif(self.user == "Door2"):
            
                print("Searching.....")
                print ("BAD LUCK!! YOU GOT  :",b),self.user
              
            
        elif(self.user == "Door3"):
            
                print("Searching.....")
                print ("BAD LUCK!! YOU GOT  :",c),self.user
               

#The program starts from here, while using below statement
if __name__ == '__main__':
#Attempts are initialised
    while count<1:
#Asking the player to select a door among those doors
       option = input("Choose the right door: [Door1, Door2, Door3]:")
       if(option == "Door1" or option == "Door2" or option == "Door3"):
#The door selected by the player is assigned to a variable
            R = game(option)
#Above declared funtion (play) is called here(function calling)
            R.play()
           
#Initialised the player name to a variable (var1) helps to store in db             
            var1=name
#Initialised the data present in the door to a variable (var3)
            if(option=="Door1"):
               var3=a
            elif(option=="Door2"):
               var3=b
            else:
               var3=c
#Initialised the door selected by the player to a variable (var2)

            if(option=="Door1"):
               var2=option
            elif(option=="Door2"):
               var2=option
            else:
               var2=option
               

#Attempts incrementation              
            count += 1
#Passing the name,door,treasure into database provided by the player
            query="insert into my(name,door,treasure) values ('"+var1+"','"+var2+"','"+var3+"')"
#Try method is used for exception handling
            try:
                cursor.execute(query)
                print("COLLECT your PRIZE at MOURITECH")
            except exception as e:
                print(e)
            
#For commiting changes performed by the player          
            conn.commit()
#For closing the connection for db
            conn.close()
            
            
            
#If attempts are over then below statement will get performed           
    else:
        print('Attempts over, Better luck Next Time!!')
    
       
        
        

 