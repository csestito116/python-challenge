import os
import csv
csvpath = ('election_data.csv')
countv = 0 
Khanvotes = 0 
Correyvotes = 0
Livotes = 0
Tooleyvotes = 0
pKhan = 0
pCorrey = 0
pLi = 0
pTooley = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header =next(csvreader)
    rows =[[row[0], row[1], row[2]] for row in csvreader]
for row in rows:
    countv = countv+1


candidates = []

for x in rows:
    if x[2] not in candidates:
        candidates.append(x[2])

    if x[2] == 'Khan':
        Khanvotes += 1

    if x[2] == 'Correy':
        Correyvotes += 1

    if x[2] == 'Li':
        Livotes += 1
    
    if x[2] == "O'Tooley":
        Tooleyvotes += 1

pKhan = (Khanvotes / countv)*100
pCorrey = (Correyvotes / countv)*100
pLi = (Livotes / countv)*100
pTooley = (Tooleyvotes / countv)*100


winner = max(Khanvotes,Correyvotes,Livotes,Tooleyvotes)
if winner == Khanvotes:
    winnername = 'Khan'
if winner == Correyvotes: 
    winnername = 'Correy'
if winner == Livotes:
    winnername = 'Li'
if winner == Tooleyvotes: 
    winnername = "O'Tooley"

print(f' Election Results \n ------------------------- \n Total Votes:{countv} \n ------------------------- \n Khan: {round(pKhan)}% ({Khanvotes}) \n Correy: {round(pCorrey)}% ({Correyvotes}) \n Li: {round(pLi)}% ({Livotes}) \n OTooley: {round(pTooley)}% ({Tooleyvotes}) \n ------------------------- \n Winner: {winnername}')

resultsdoc = open('Election_Results.txt', 'w')
resultsdoc.write(f' Election Results \n ------------------------- \n Total Votes:{countv} \n ------------------------- \n Khan: {round(pKhan)}% ({Khanvotes}) \n Correy: {round(pCorrey)}% ({Correyvotes}) \n Li: {round(pLi)}% ({Livotes}) \n OTooley: {round(pTooley)}% ({Tooleyvotes}) \n ------------------------- \n Winner: {winnername}')