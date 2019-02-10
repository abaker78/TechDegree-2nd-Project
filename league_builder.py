import csv

#Create lists to store soccer player info
yes_list = []
no_list = []
Sharks = []
Dragons = []
Raptors = []
teams = [Sharks, Dragons, Raptors]
str_teams = ['Sharks', 'Raptors', 'Dragons']

#Create function to determine whether current player is "skilled". If "YES", then store all "skilled" players in a list
def yes_assign(input):
    for line in input:
        if line[2] == 'YES':
            yes_list.append(line)
        else:continue
    return yes_list

#Create function to determine whether current player is "non-skilled". If "NO", then store all "skilled" players in a list
def no_assign(input):
    for line in input:
        if line[2] == 'NO':
            no_list.append(line)
        else:continue
    return no_list

#Function to loop through team members and teams and send out welcome letters
def player_letter(input, input2):
    player_list = []
    player = input[0]
    guardian = input[3]
    team = input2
    with open('{}.txt'.format(player).lower(),'x') as txtFile:
        txtFile.write('''To {}
                  
    We would like to welcome you and your child, {} to the {}.      
Our first practice is scheduled for Tuesday, February 19th 2019.              
We look forward to hearing your cheers and seeing your childs smile.'''.format(guardian, player, team))
    return player_list
         
#run dunder to determine if script is being imported or ran from the "MAIN" script
if __name__ == "__main__":
    #Create a list to house all player info coming in from csv file.
    player_detail = []
    #Open csv file
    with open('soccer_players.csv','r') as csvfile:
        #Loop through each line in csv file
        for line in csvfile:
            #Store line in new list just created
            player_detail.append(line.split(','))
    #Create and open a new txt file if it doesn't already exist        
    with open('teams.txt', 'a') as file:
        yes_return = yes_assign(player_detail)
        no_return = no_assign(player_detail)
        #Count the number of item in the list of "non-skilled" players, continue to add "skilled" players from the "yes_list" until the number of players in the "yes_list" equals the number of players in the "no_list".
        while len(no_list) != 0:
            for team in teams:
                team.append(yes_list[0])
                yes_list.remove(yes_list[0])
            #Add "non-skilled" players to the "team" list until that list has zero items remaining inside.    
            for team in teams:
                team.append(no_list[0])
                no_list.remove(no_list[0])
        #Create loop to add the same number of players to eah team
        for name in str_teams:
            file.write('''
{}
========
'''.format(name))
            #Add each player in the "teams" list to the .txt file
            for item in teams[0]:
                stripped_item = ','.join(str(i) for i in item)
                file.write(stripped_item)
                test = player_letter(item, name)
            #Remove the current team name from the list
            teams.pop(0)
 
                
                    
                
                       
            
