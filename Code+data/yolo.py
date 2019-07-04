# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 21:05:54 2019

@author: Krishant
"""
def stats_all(x):
    players={}
    teams={}
    i=0
    while i<=len(x)-1:

        if not x[i][0].isdigit():

            team=list(x[i]) 
            team[2]=''
            team=''.join(team)

            i+=1
            for k in team:
                if k in players:
                    j=i

                    while j<=len(x)-1 and x[j][0].isdigit():

                        if k==team[0] or k==team[1]:     

                            if x[j][:2]>x[j][3:]:         #FIRST TEAM WINS
                                players[k][0]+=1
                                players[k][2]=players[k][0] + players[k][1]
                                j+=1
                                if players[k][1]==0:
                                    players[k][3]=players[k][0]

                                else:
                                    players[k][3]=players[k][0]/players[k][1]
                                
                                if team[-3:-5:-1] in teams or team[:2] in teams:
                                    if k==team[0] or k==team[2]:
                                        try:
                                            teams[team[:2]][0]+=1
                                            teams[team[:2]][2]=teams[team[:2]][0] + teams[team[:2]][1]

                                            if teams[team[:2]][1]==0:
                                                teams[team[:2]][3]=teams[team[:2]][0]
                                            else:
                                                teams[team[:2]][3]=teams[team[:2]][0]/teams[team[:2]][1]
                                        except:
                                            teams[team[-3:-5:-1]][0]+=1
                                            teams[team[-3:-5:-1]][2]=teams[team[-3:-5:-1]][0] + teams[team[-3:-5:-1]][1]
                                            
                                            if teams[team[-3:-5:-1]][0]==0:
                                                teams[team[-3:-5:-1]][3]=teams[team[-3:-5:-1]][0]
                                            else:
                                                teams[team[-3:-5:-1]][3]=teams[team[-3:-5:-1]][0]/teams[team[-3:-5:-1]][1]
                                    elif k==team[1] or k==team[3]:
                                        continue
                                    
                                else:
                                    teams[team[:2]]=[1,0,1,1]

                            else:         #FIRST TEAM LOSSES
                                players[k][1]+=1
                                players[k][2]=players[k][0] + players[k][1]
                                j+=1
                                if players[k][1]==0:
                                    players[k][3]=players[k][0]
                                else:
                                    players[k][3]=players[k][0]/players[k][1]
                                    
                                if team[-3:-5:-1] in teams or team[:2] in teams:
                                    if k==team[0] or k==team[2]:
                                        try:
                                            teams[team[:2]][1]+=1
                                            teams[team[:2]][2]=teams[team[:2]][0] + teams[team[:2]][1]
                                            if teams[team[:2]][1]==0:
                                                teams[team[:2]][3]=teams[team[:2]][0]
                                            else:
                                                teams[team[:2]][3]=teams[team[:2]][0]/teams[team[:2]][1]
                                        except:
                                            teams[team[-3:-5:-1]][1]+=1
                                            teams[team[-3:-5:-1]][2]=teams[team[-3:-5:-1]][1] + teams[team[-3:-5:-1]][0]
                                            if teams[team[-3:-5:-1]][0]==0:
                                                teams[team[-3:-5:-1]][3]=teams[team[-3:-5:-1]][0]
                                            else:
                                                teams[team[-3:-5:-1]][3]=teams[team[-3:-5:-1]][0]/teams[team[-3:-5:-1]][1]
                                            
                                    elif k==team[1] or k==team[3]:
                                        continue
                                else:
                                    teams[team[:2]]=[0,1,1,0]
                                    
                        else:    #2ND TEAM
                            
                            if x[j][:2]<x[j][3:]:   #2ND TEAM WIN
                                players[k][0]+=1
                                players[k][2]=players[k][0] + players[k][1]
                                j+=1
                                if players[k][1]==0:
                                    players[k][3]=players[k][0]
                                else:
                                    players[k][3]=players[k][0]/players[k][1]
                                
                                if team[-1:-3:-1] in teams or team[2:] in teams:
                                    if k==team[0] or k==team[2]:
                                        try:
                                            teams[team[2:]][0]+=1
                                            teams[team[2:]][2]=teams[team[2:]][0] + teams[team[2:]][1]
                                            if teams[team[2:]][1]==0:
                                                teams[team[2:]][3]=teams[team[2:]][0]
                                            else:
                                                teams[team[2:]][3]=teams[team[2:]][0]/teams[team[2:]][1]
                                        except:
                                            teams[team[-1:-3:-1]][0]+=1
                                            teams[team[-1:-3:-1]][2]=teams[team[-1:-3:-1]][0] + teams[team[-1:-3:-1]][1]
                                            if teams[team[-1:-3:-1]][0]==0:
                                                teams[team[-1:-3:-1]][3]=teams[team[-1:-3:-1]][0]
                                            else:
                                                teams[team[-1:-3:-1]][3]=teams[team[-1:-3:-1]][0]/teams[team[-1:-3:-1]][1]
                                    elif k==team[1] or k==team[3]:
                                        continue
                                    
                                else:
                                    teams[team[2:]]=[1,0,1,1]
                    
                            else:  # 2ND TEAM LOSSES
                                players[k][1]+=1
                                players[k][2]=players[k][0] + players[k][1]
                                j+=1
                                if players[k][1]==0:
                                    players[k][3]=players[k][0]
                                else:
                                    players[k][3]=players[k][0]/players[k][1]
                                    
                                if team[-1:-3:-1] in teams or team[2:] in teams:
                                    if k==team[0] or k==team[2]:
                                        try:
                                            teams[team[2:]][1]+=1
                                            teams[team[2:]][2]=teams[team[2:]][0] + teams[team[2:]][1]
                                            if teams[team[2:]][1]==0:
                                                teams[team[2:]][3]=teams[team[2:]][0]
                                            else:
                                                teams[team[2:]][3]=teams[team[2:]][0]/teams[team[2:]][1]
                                        except:
    
                                            teams[team[-1:-3:-1]][1]+=1
                                            teams[team[-1:-3:-1]][3]=teams[team[-1:-3:-1]][1] + teams[team[-1:-3:-1]][0]
                                            if teams[team[-1:-3:-1]][1]==0:
                                                teams[team[-1:-3:-1]][3]=teams[team[-1:-3:-1]][0]
                                            else:
                                                teams[team[-1:-3:-1]][3]=teams[team[-1:-3:-1]][0]/teams[team[-1:-3:-1]][1]
                                    elif k==team[1] or k==team[3]:
                                        continue
                                else:
                                    teams[team[2:]]=[0,1,1,0]
                else:    ###NEW TEAMS###
                    players[k]=[0,0,0,0]
                    if k==team[0]:
                        teams[team[:2]]=[0,0,0,0]
                    elif k==team[2]:
                        teams[team[2:]]=[0,0,0,0]
                        
                    j=i

                    while j<=len(x)-1 and x[j][0].isdigit():

                        if k==team[0] or k==team[1]:

                            if x[j][:2]>x[j][3:]: #FIRST TEAM WINS
                                players[k][0]+=1
                                players[k][2]=players[k][0] + players[k][1]
                                j+=1

                                if players[k][1]==0:
                                    players[k][3]=players[k][0]
                                else:
                                    players[k][3]=players[k][0]/players[k][1]
                                
                                if team[-3:-5:-1] in teams or team[:2] in teams:
                                    if k==team[0] or k==team[2]:
                                        try:
                                            teams[team[:2]][0]+=1
                                            teams[team[:2]][2]=teams[team[:2]][0] + teams[team[:2]][1]

                                            if teams[team[:2]][1]==0:
                                                teams[team[:2]][3]=teams[team[:2]][0]
                                            else:
                                                teams[team[:2]][3]=teams[team[:2]][0]/teams[team[:2]][1]
                                        except:
                                            teams[team[-3:-5:-1]][0]+=1
                                            teams[team[-3:-5:-1]][2]=teams[team[-3:-5:-1]][0] + teams[team[-3:-5:-1]][1]
                                            
                                            if teams[team[-3:-5:-1]][0]==0:
                                                teams[team[-3:-5:-1]][3]=teams[team[-3:-5:-1]][0]
                                            else:
                                                teams[team[-3:-5:-1]][3]=teams[team[-3:-5:-1]][0]/teams[team[-3:-5:-1]][1]
                                    elif k==team[1] or k==team[3]:
                                        continue
                                    
                                else:
                                    teams[team[:2]]=[1,0,1,1]
                                    
                            else:           #FIRST TEAM LOSSES
                                players[k][1]+=1
                                players[k][2]=players[k][0] + players[k][1]
                                j+=1
                                if players[k][1]==0:
                                    players[k][3]=players[k][0]
                                else:
                                    players[k][3]=players[k][0]/players[k][1]
                                    
                                if team[-3:-5:-1] in teams or team[:2] in teams:
                                    if k==team[0] or k==team[2]:
                                        try:
                                            teams[team[:2]][1]+=1
                                            teams[team[:2]][2]=teams[team[:2]][0] + teams[team[:2]][1]
                                            if teams[team[:2]][1]==0:
                                                teams[team[:2]][3]=teams[team[:2]][0]
                                            else:
                                                teams[team[:2]][3]=teams[team[:2]][0]/teams[team[:2]][1]
                                        except:
                                            teams[team[-3:-5:-1]][1]+=1
                                            teams[team[-3:-5:-1]][2]=teams[team[-3:-5:-1]][1] + teams[team[-3:-5:-1]][0]
                                            if teams[team[-3:-5:-1]][0]==0:
                                                teams[team[-3:-5:-1]][3]=teams[team[-3:-5:-1]][0]
                                            else:
                                                teams[team[-3:-5:-1]][3]=teams[team[-3:-5:-1]][0]/teams[team[-3:-5:-1]][1]
                                            
                                    elif k==team[1] or k==team[3]:
                                        continue
                                else:
                                    teams[team[:2]]=[0,1,1,0]

                        else:      #2ND TEAM
                            
                            if x[j][:2]<x[j][3:]: #2ND TEAM WINS
                                players[k][0]+=1
                                players[k][2]=players[k][0] + players[k][1]
                                j+=1
                                
                                if players[k][1]==0:
                                    players[k][3]=players[k][0]
                                else:
                                    players[k][3]=players[k][0]/players[k][1]
                                
                                if team[-1:-3:-1] in teams or team[2:] in teams:
                                    if k==team[0] or k==team[2]:
                                        try:
                                            teams[team[2:]][0]+=1
                                            teams[team[2:]][2]=teams[team[2:]][0] + teams[team[2:]][1]
                                            if teams[team[2:]][1]==0:
                                                teams[team[2:]][3]=teams[team[2:]][0]
                                            else:
                                                teams[team[2:]][3]=teams[team[2:]][0]/teams[team[2:]][1]
                                        except:
                                            teams[team[-1:-3:-1]][0]+=1
                                            teams[team[-1:-3:-1]][2]=teams[team[-1:-3:-1]][0] + teams[team[-1:-3:-1]][1]
                                            if teams[team[-1:-3:-1]][0]==0:
                                                teams[team[-1:-3:-1]][3]=teams[team[-1:-3:-1]][0]
                                            else:
                                                teams[team[-1:-3:-1]][3]=teams[team[-1:-3:-1]][0]/teams[team[-1:-3:-1]][1]
                                    elif k==team[1] or k==team[3]:
                                        continue
                                    
                                else:
                                    teams[team[2:]]=[1,0,1,1]
                    
                            else:    ### 2ND TEAM LOSSES
                                players[k][1]+=1
                                players[k][2]=players[k][0] + players[k][1]
                                j+=1
                                if players[k][1]==0:
                                    players[k][3]=players[k][0]
                                else:
                                    players[k][3]=players[k][0]/players[k][1]
                                    
                                if team[-1:-3:-1] in teams or team[2:] in teams:
                                    if k==team[0] or k==team[2]:
                                        try:
                                            teams[team[2:]][1]+=1
                                            teams[team[2:]][2]=teams[team[2:]][0] + teams[team[2:]][1]
                                            if teams[team[2:]][1]==0:
                                                teams[team[2:]][3]=teams[team[2:]][0]
                                            else:
                                                teams[team[2:]][3]=teams[team[2:]][0]/teams[team[2:]][1]
                                        except:
    
                                            teams[team[-1:-3:-1]][1]+=1
                                            teams[team[-1:-3:-1]][3]=teams[team[-1:-3:-1]][1] + teams[team[-1:-3:-1]][0]
                                            if teams[team[-1:-3:-1]][1]==0:
                                                teams[team[-1:-3:-1]][3]=teams[team[-1:-3:-1]][0]
                                            else:
                                                teams[team[-1:-3:-1]][3]=teams[team[-1:-3:-1]][0]/teams[team[-1:-3:-1]][1]
                                    elif k==team[1] or k==team[3]:
                                        continue
                                else:
                                    teams[team[2:]]=[0,1,1,0]
        else:
            i+=1
    X=teams
    Y=players
    return (X,Y)

'''
def team_stats(x):
    teams={}
    i=0
    while i<=len(x)-1:

        if not x[i][1].isdigit():
            name=[]
            team=list(x[i]) 
            name.append(team[0]+team[1])
            name.append(team[3]+team[4])
            i+=1
            for k in name:
                j=i
                while x[j][0].isdigit():
                    if k==name[0] or k==name[1]:
'''                       
    
