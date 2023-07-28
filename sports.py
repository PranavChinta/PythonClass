class Team:
		
	TeamName = ""
	NumbPlayers = 0
	PlayTeamCt = 0
	
	
	def __init__(self):
		self.p = self.Player()
	
	def disp(self):
		print("Your team is called " + self.TeamName + " and there are " + str(self.NumbPlayers) + " players in total and there are " + str(self.PlayTeamCt) + " starting team players")
	class Player:
	
		Name = ""
		Ht = 0
		Numb = 0
			
		def display(self):
			print("Player " + str(self.Numb) + " is " + self.Name + " and he is " + str(self.Ht) + " inches tall")
		
class Basketball(Team):
	pass

team = Basketball()
	
team.TeamName = raw_input("Input your basketball team name: ")
team.NumbPlayers = int(input("How many total players are on your basketball team: "))
team.PlayTeamCt = int(input("How many total players are on your starting team: "))
 			
team.disp()			
 
p1 = team.p 			
p1.Name = raw_input("What is your player's name: ")
p1.Ht = int(input("How tall is your player(inches): "))
p1.Numb = int(input("Which number is this player: "))	

p1.display() 	
