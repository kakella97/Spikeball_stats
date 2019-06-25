import os.path

print("What do you want to do? Add data or analysis?")
decision = input('Add data or analysis >')

if decision=='Add data' or decision=='data':

    fname = input(' Enter filename > ')

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
if decision=='analysis':
    fname=input('Filename >')
    player=input('Which player for stats? >')
    with open(fname, "r") as f:
        content = [line.rstrip() for line in f]
    f.close()
    if content[-1]=='':
        del content[-1]
    wins=0
    losses=0
    for i in range(0,len(content)):
        if not content[i][0].isdigit():
            if content[i][0]==player or content[i][1]==player:
                j=i+1
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
        if i>=0:
            continue
    games=wins+losses
    ratio=wins/losses
    print('total games played:', games, '\n'
          '# of wins:', wins, '\n'
          '# of losses:', losses, '\n'
          'win/loss ratio:', ratio, '\n')
    

                    
                