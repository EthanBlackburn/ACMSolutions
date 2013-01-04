f = open('/users/ethan/python/LRU/input.txt','r')
line = f.readline().rstrip()

cache = ''

while(int(line[0:1]) != 0):
	insert_array = line[2:].split('!')
	for i in range(len(insert_array)-1):
		cache = insert_array[i][::-1] + cache
		
		cache = cache[0:int(line[0:1])]
			
		print cache
	line = f.readline().rstrip()
	cache = ''
	
	