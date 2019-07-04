import os.path
import numpy as np

def s_standings(x):
    i=0
    while i < (len(x)/2) - 1:
        pivot=x[2*i+1]
        name=x[2*i]
        if pivot < x[2*i+3]:
            x[2*i+1]=x[2*i+3]
            x[2*i]=x[2*i+2]
            x[2*i+2]=name
            x[2*i+3]=pivot
            i=0
        else:
            i+=1
    x=np.reshape(x,(int(len(x)/2),2))
    return(x)

print("What do you want to do? Add data or analysis?")
decision = input('Add data or analysis >')

if decision=='Add data' or decision=='data':

    fname = input(' Enter filename > ')
    answer='Y'
    while answer=='Y':
        print('What are the teams? >')
        teams = input('AB-CD >')
        real_score=[]
        print("How many games?")
        games = input('X >')
        i=1
        while i<=int(games):
            print("Score?")
            score = input('XX-XX >')
            real_score.append(score)
            i+=1
    
        if os.path.exists(fname):
            with open(fname) as f:
                content = [line.rstrip() for line in f]
            j=0
            for i in range(0,len(content)):
                if content[i].startswith(teams):
                    j=i
                    f.close()
                    break
            if j!=0:
                for i in range(0,len(real_score)):
                    content.insert(j+1,real_score[i])
                    j+=1
                    with open(fname, "w") as f:
                        for i in range(0,len(content)):
                            f.writelines(content[i] + '\n')
                    f.close()
            else:
                with open(fname, "a") as f:
                    f.write(teams +'\n')
                    for i in range(0,len(real_score)):
                        f.write(real_score[i] + '\n')
                f.close()
        else:
            with open(fname,"w") as f:
                f.writelines(teams +'\n')
                for i in range(0,len(real_score)):
                    f.writelines(real_score[i] + '\n')
            f.close()
        print("Would you like to continue?")
        answer=input("Y or N >")
    
        
        
if decision=='analysis':
    fname=input('Filename >')
    with open(fname, "r") as f:
        content = [line.rstrip() for line in f]
    f.close()
    if content[-1]=='':
        del content[-1]
    wins=0
    losses=0
    teams=[]
    team_wins=0
    team_losses=0
    spikers=[]
    standings=[]
    i=0
    while i <= len(content):
        if i==0:
            player=input('Which player for stats? >')
        if not content[i][0].isdigit():
            if content[i][0]==player or content[i][1]==player:
                j=i+1
                teams.append(content[i][:2])
                if j>=len(content):
                    if content[j-1][:2]>content[j-1][3:]:
                        wins+=1
                    else:
                        losses+=1
                else:
                    while j<len(content) and content[j][:2].isdigit():
                        if content[j][:2]>content[j][3:]:
                            wins+=1
                            j+=1
                        else:
                            losses+=1
                            j+=1
            if content[i][3]==player or content[i][4]==player:
                j=i+1
                teams.append(content[i][3:])
                if j>=len(content):
                    if content[j-1][:2]<content[j-1][3:]:
                        wins+=1
                    else:
                        losses+=1
                        
                else:
                    while j<len(content) and content[j][:2].isdigit():
                        if j!=len(content) and content[j][:2]<content[j][3:]:
                            wins+=1
                            j+=1
                        else:
                            losses+=1
                            j+=1
        i+=1
        if i>=len(content):
            print("Would you like to continue?")
            answer=input("Y or N >")
            if answer=="Y":
                games=wins+losses
                ratio=wins/losses
                print('total games played:', games, '\n'
                      '# of wins:', wins, '\n'
                      '# of losses:', losses, '\n'
                      'win/loss ratio:', ratio, '\n'  )
                wins=0
                losses=0
                teams=[]
                standings.append(player)
                standings.append(ratio)
                
                i=0
            else:
                games=wins+losses
                ratio=wins/losses
                print('total games played:', games, '\n'
                      '# of wins:', wins, '\n'
                      '# of losses:', losses, '\n'
                      'win/loss ratio:', ratio, '\n')
                standings.append(player)
                standings.append(ratio)
                break
        if i>=0:
            continue
        
                

    

    

                    
                