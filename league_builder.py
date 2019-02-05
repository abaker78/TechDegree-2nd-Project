import csv


yes_list = []
no_list = []
Sharks = []
Dragons = []
Raptors = []
teams = [Sharks, Dragons, Raptors]
str_teams = ['Sharks', 'Raptors', 'Dragons']


def yes_assign(input):
    for line in input:
        if line[2] == 'YES':
            yes_list.append(line)
        else:continue
    return yes_list


def no_assign(input):
    for line in input:
        if line[2] == 'NO':
            no_list.append(line)
        else:continue
    return no_list


if __name__ == "__main__":
    player_detail = []
    with open('soccer_players.csv', 'r') as csvfile:
        for line in csvfile:
            player_detail.append(line.split(','))
            
    with open('--teams_practice.txt---', 'a') as file:
        yes_return = yes_assign(player_detail)
        no_return = no_assign(player_detail)
    
        while len(no_list) != 0:
            for team in teams:
                team.append(yes_list[0])
                yes_list.remove(yes_list[0])
                
            for team in teams:
                team.append(no_list[0])
                no_list.remove(no_list[0])
 
        for name in str_teams:
            file.write('''
{}.
========
'''.format(name))
            for item in teams[0]:
                file.write(str(item)[1:-1].replace("'",'')+"\n")
            teams.pop(0)

for member in player_detail:
    with open('{}.txt.txt'.format(member[0]).lower(),'x') as txtFile:
        txtFile.write('''Welcome {},
    
We would like to officially congratulate you on your enrollment
        
with the league.'''.format(member[0]))

         
                    
                
                    
            
