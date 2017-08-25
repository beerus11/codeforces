matrix=[]
i=0
while i<5:
	string=raw_input()
	matrix.append(map(int,string.split(" ")))
	i+=1

point=[[index, row.index(1)] for index, row in enumerate(matrix) if 1 in row][0]
centre=[len(matrix)/2,len(matrix[0])/2]
print abs(centre[0]-point[0])+abs(centre[1]-point[1])
