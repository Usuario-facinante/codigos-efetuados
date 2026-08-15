'''Codeforces separates its users into 
4
4 divisions by their rating:

For Division 1: 
1900
≤
r
a
t
i
n
g
1900≤rating
For Division 2: 
1600
≤
r
a
t
i
n
g
≤
1899
1600≤rating≤1899
For Division 3: 
1400
≤
r
a
t
i
n
g
≤
1599
1400≤rating≤1599
For Division 4: 
r
a
t
i
n
g
≤
1399
rating≤1399
Given a 
r
a
t
i
n
g
rating, print in which division the 
r
a
t
i
n
g
rating belongs.'''
Quantidade_reps = int(input())
for i in range (Quantidade_reps):
	rating = None
	rating = int(input())
	if 1900<=rating:
		print ("Division 1")
	elif 1600<=rating<=1899:
		print ("Division 2")
	elif 1400<=rating<=1599:
		print ("Division 3")
	else:
		print ("Division 4")