import math
import numpy


f = open('/users/ethan/python/slice/moves.txt','r')
line = f.readline().rstrip()
while(int(line) != 0):
	vectors = []
	collision = False
	prev_x = 0
	prev_y = 0
	angle = 90
	instructions_length = int(line)
	for i in range(instructions_length):
		line = f.readline().rstrip()
		instructions = line.split(' ')
		read_angle = int(instructions[0])
		read_moves = int(instructions[1])
		angle += read_angle
		rad_angle = math.radians(angle)
		vector = (prev_x,prev_y), rad_angle,read_moves
		vectors.append(vector)
		for v in range(len(vectors)-1):
			try:
				c0,a,moves = vectors[v]
				xO,yO = c0
				xO-prev_x,yO-prev_y
				eq1 = numpy.array([[math.cos(rad_angle),-math.cos(a)], [math.sin(rad_angle),-math.sin(a)]])
				eq2 = numpy.array([xO-prev_x,yO-prev_y])
				sol = numpy.linalg.solve(eq1,eq2)
				t = sol[0]
				s = sol[1]
				
				if(t <= read_moves and t >= 0.01 and s <= moves and s >= 0.01):
					print i+1
					collision = True
					break
				else:
					if(i == instructions_length - 1 and v == len(vectors)-2):
						print 'SAFE'
			except numpy.linalg.linalg.LinAlgError:
				continue
				
		prev_x += read_moves*math.cos(rad_angle)
		prev_y += read_moves*math.sin(rad_angle)
		if(collision):
			break
	line = f.readline().rstrip()
	while(len(line.split(' ')) > 1):
		line = f.readline().rstrip()
	