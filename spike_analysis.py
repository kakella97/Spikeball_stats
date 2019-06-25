# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 20:45:09 2019

@author: Krishant
"""
import sys
import os.path

print("What do you want to do? Add data or analysis?")
decision = input('Add data or analysis >')

if decision=='Add data' or decision=='data':
    fname = input(' Enter filename > ')
teams = [fname[:2],fname[4:6]]
try:
    if os.path.exists(fname):
        with open(fname,"a") as f:
            print("How many games?")
            games = input('games >')
            i=1
            while i<=int(games):
                real_score=[]
                print("Score?")
                score = input()
                real_score.append(score[0:2])
                real_score.append(score[3:5])
                f.writelines(','.join(s for s in real_score) + '\n')
                i+=1
    else:
        with open(fname,"w") as f:
            print("How many games?")
            games = input('games >')
            i=1
            f.writelines(','.join(s for s in teams) + '\n')
            while i<=int(games):
                real_score=[]
                print("Score?")
                score = input()
                real_score.append(score[0:2])
                real_score.append(score[3:5])
                f.writelines(','.join(s for s in real_score) + '\n')
                i+=1
except IOError:
    sys.exit('File is corrupt')
    
if decision=='analysis':
    print("Stats for who?")
    player = input()

cwd = os.getcwd()
for file in os.listdir(cwd):
    if file.endswith(".txt"):
        file_names=[]
        file_names.append(file)
for i in range(0,len(file_names)):
    if player==file_names[i][0] or player==file_names[i][1] or player==file_names[i][4] or player==file_names[i][5]:
        with open(file_names) as c:
            content = c.readlines() 
