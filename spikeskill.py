# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 22:47:18 2020

@author: Krishant
"""
import os.path
import pprint
import sys

INITIAL_ELO = 1000

def elo(elo_a, elo_b, score):
    pa = 1 / (1 + 10**((elo_b - elo_a) / 400)) # EXPECTED PERCENT TEAM A WINS
    pb = 1 - pa # EXPECTED PERCENT TEAM B WINS
    K = 50

    if score[:2] > score[3:]: # IF TEAM A WINS
        elo_a = elo_a + K * (1 - pa)
        elo_b = elo_b + K * (0 - pb)
    else: # IF TEAM B WINS
        elo_b = elo_b + K * (1 - pb)
        elo_a = elo_a + K * (0 - pa)

    return [elo_a, elo_b]


def P_elo(teams,players):
    elos=[]
    for p in players.keys():
        for t in teams.keys():
            if p in t:
                elos.append(teams[t][4])
        players[p][4]= sum(elos) / len(elos)
        elos=[]
    return players

def team_check(team,team_dict):
    if team in team_dict:
        x = True
    elif team[2::-1] in team_dict:
        x=True
    else:
        x=False
    return x


def input_stats(team, p_dict, score, team_dict):
    if score[:2] > score[3:]:
        l=1
        r=0
    else:
        l=0
        r=1
            
    if (not team_check(team[:2],team_dict)) and (not team_check(team[3:],team_dict)):
        team_dict[team[:2]] = [0, 0, 0, 0, INITIAL_ELO]
        team_dict[team[3:]] = [0, 0, 0, 0, INITIAL_ELO]
                
    elif (team_check(team[:2],team_dict) and not team_check(team[3:], team_dict)):
        team_dict[team[3:]] = [0, 0, 0, 0, INITIAL_ELO]
               
    elif team_check(team[3:],team_dict) and not team_check(team[:2],team_dict): 
        team_dict[team[:2]] = [0, 0, 0, 0, INITIAL_ELO]
    
    ''' ELOS FOR TEAMS 1 AND 2 '''     
    
    if (team[:2] in team_dict) and (team[3:] in team_dict):
        team_dict[team[:2]][4] = elo(team_dict[team[:2]][4], team_dict[team[3:]][4], score)[0]
        team_dict[team[3:]][4] = elo(team_dict[team[:2]][4], team_dict[team[3:]][4], score)[1]
        
    ### WINS LOSSES GAMES PLAYED WIN/LOSS RATIO UPDATE FOR BOTH TEAMS ###
        team_dict[team[:2]][0]+=l
        team_dict[team[:2]][1]+=(1-l)
        team_dict[team[:2]][2]+=1
        if team_dict[team[:2]][1]==0:
            team_dict[team[:2]][3]= team_dict[team[:2]][0]
        else:
            team_dict[team[:2]][3] = team_dict[team[:2]][0]/team_dict[team[:2]][1]
            
        team_dict[team[3:]][0]+=r
        team_dict[team[3:]][1]+=(1-r)
        team_dict[team[3:]][2]+=1
        if team_dict[team[3:]][1]==0:
            team_dict[team[3:]][3]= team_dict[team[3:]][0]
        else:
            team_dict[team[3:]][3] = team_dict[team[3:]][0]/team_dict[team[3:]][1]
       
    elif (team[:2][2::-1] in team_dict) and (team[3:] in team_dict):
        team_dict[team[:2][2::-1]][4] = elo(team_dict[team[:2][2::-1]][4], team_dict[team[3:]][4], score)[0]
        team_dict[team[3:]][4] = elo(team_dict[team[:2][2::-1]][4], team_dict[team[3:]][4], score)[1]
        
        ''' WINS LOSSES GAMES PLAYED WIN/LOSS RATIO UPDATE FOR BOTH TEAMS '''
        team_dict[team[:2][2::-1]][0]+=l
        team_dict[team[:2][2::-1]][1]+=(1-l)
        team_dict[team[:2][2::-1]][2]+=1
        if team_dict[team[:2][2::-1]][1]==0:
            team_dict[team[:2][2::-1]][3]= team_dict[team[:2][2::-1]][0]
        else:
            team_dict[team[:2][2::-1]][3] = team_dict[team[:2][2::-1]][0]/team_dict[team[:2][2::-1]][1]
            
        team_dict[team[3:]][0]+=r
        team_dict[team[3:]][1]+=(1-r)
        team_dict[team[3:]][2]+=1
        if team_dict[team[3:]][1]==0:
            team_dict[team[3:]][3]= team_dict[team[3:]][0]
        else:
            team_dict[team[3:]][3] = team_dict[team[3:]][0]/team_dict[team[3:]][1]
            
    elif (team[:2] in team_dict) and (team[3:][2::-1] in team_dict):
        team_dict[team[:2]][4] = elo(team_dict[team[:2]][4], team_dict[team[3:][2::-1]][4], score)[0]
        team_dict[team[3:][2::-1]][4] = elo(team_dict[team[:2]][4], team_dict[team[3:][2::-1]][4], score)[1]
        
                ### WINS LOSSES GAMES PLAYED WIN/LOSS RATIO UPDATE FOR BOTH TEAMS ###
        team_dict[team[:2]][0]+=l
        team_dict[team[:2]][1]+=(1-l)
        team_dict[team[:2]][2]+=1
        if team_dict[team[:2]][1]==0:
            team_dict[team[:2]][3]= team_dict[team[:2]][0]
        else:
            team_dict[team[:2]][3] = team_dict[team[:2]][0]/team_dict[team[:2]][1]
            
        team_dict[team[3:][2::-1]][0]+=r
        team_dict[team[3:][2::-1]][1]+=(1-r)
        team_dict[team[3:][2::-1]][2]+=1
        if team_dict[team[3:][2::-1]][1]==0:
            team_dict[team[3:][2::-1]][3]= team_dict[team[3:][2::-1]][0]
        else:
            team_dict[team[3:][2::-1]][3] = team_dict[team[3:][2::-1]][0]/team_dict[team[3:][2::-1]][1]
            
    elif (team[:2][2::-1] in team_dict) and (team[3:][2::-1] in team_dict):
        team_dict[team[:2][2::-1]][4] = elo(team_dict[team[:2][2::-1]][4], team_dict[team[3:][2::-1]][4], score)[0]
        team_dict[team[3:][2::-1]][4] = elo(team_dict[team[:2][2::-1]][4], team_dict[team[3:][2::-1]][4], score)[1]

                ### WINS LOSSES GAMES PLAYED WIN/LOSS RATIO UPDATE FOR BOTH TEAMS ###
        team_dict[team[:2][2::-1]][0]+=l
        team_dict[team[:2][2::-1]][1]+=(1-l)
        team_dict[team[:2][2::-1]][2]+=1
        if team_dict[team[:2][2::-1]][1]==0:
            team_dict[team[:2][2::-1]][3]= team_dict[team[:2][2::-1]][0]
        else:
            team_dict[team[:2][2::-1]][3] = team_dict[team[:2][2::-1]][0]/team_dict[team[:2][2::-1]][1]
            
        team_dict[team[3:][2::-1]][0]+=r
        team_dict[team[3:][2::-1]][1]+=(1-r)
        team_dict[team[3:][2::-1]][2]+=1
        if team_dict[team[3:][2::-1]][1]==0:
            team_dict[team[3:][2::-1]][3]= team_dict[team[3:][2::-1]][0]
        else:
            team_dict[team[3:][2::-1]][3] = team_dict[team[3:][2::-1]][0]/team_dict[team[3:][2::-1]][1]
    
    for i in [0,1,3,4]:
        p=team[i]
        if team[i] not in p_dict: ### Not in dict ###
            p_dict[p] = [0, 0, 0, 0, INITIAL_ELO]
            
            if i < 2: ###first 2 players###
                p_dict[p][0]+=l # wins
                p_dict[p][1]+=(1-l) #losses
                p_dict[p][2]+=1 # games played
                if p_dict[p][1]==0:
                    p_dict[p][3] = p_dict[p][0]
                else: 
                    p_dict[p][3] = p_dict[p][0]/p_dict[p][1] # win loss ratio
            else: ### last 2 players ###
                p_dict[p][0]+=r
                p_dict[p][1]+=(1-r)
                p_dict[p][2]+=1
                if p_dict[p][1]==0:
                    p_dict[p][3] = p_dict[p][0]
                else: 
                    p_dict[p][3] = p_dict[p][0]/p_dict[p][1] # win loss ratio
        else: ### Already in the dictionary ###
            if i < 2: ###first 2 players###
                p_dict[p][0]+=l
                p_dict[p][1]+=(1-l)
                p_dict[p][2]+=1
                if p_dict[p][1]==0:
                    p_dict[p][3] = p_dict[p][0]
                else: 
                    p_dict[p][3] = p_dict[p][0]/p_dict[p][1] # win loss ratio
            else:   ### last 2 players ###
                p_dict[p][0]+=r
                p_dict[p][1]+=(1-r)
                p_dict[p][2]+=1
                if p_dict[p][1]==0:
                    p_dict[p][3] = p_dict[p][0]
                else: 
                    p_dict[p][3] = p_dict[p][0]/p_dict[p][1] # win loss ratio
                
    return [p_dict, team_dict]


# last argument is file name
fname = sys.argv[-1]
with open(fname, "r") as f:
    content = [line.strip() for line in f] # line.rstrip() returns a copy of the string with trailing characters stripped
f.close()

for j in range(len(content)):
    if content[j]=='':
        del content[j:]
        break
teams={}
players={}
standings=[]
i=0
while i < len(content):
    [players, teams] = input_stats(content[i], players, content[i+1], teams)
    i+=2
    
players = P_elo(teams, players)    

# round team elo to 3 decimal places
for t in teams.keys():
    teams[t][3] = round(teams[t][3], 3)
    teams[t][4] = round(teams[t][4], 3)

# round individual elo to 3 decimal places
for p in players.keys():
    players[p][3] = round(players[p][3], 3)
    players[p][4] = round(players[p][4], 1)

# sort by elo
players = sorted(players.items(), key=lambda i: i[1][4], reverse=True)
teams = sorted(teams.items(), key=lambda i: i[1][4], reverse=True)

# pretty
pprint.pprint(teams)
pprint.pprint(players)