class Grid(x,y):
	self.length = x
	self.breadth = y
class Rover():
	class north():
		left = 'W'
		right = 'E'
		name = 'north'
	class south():
		left = 'E'
		right = 'N'
		name = 'south'
	class east():
		left = 'N'
		right = 'S'
		name = 'east'
	class west():
		left = 'S'
		right = 'N'
		name = 'west'
	def __init__(self,x,y,compass):
		self.x_position = x
		self.y_position = y 
		self.facing = self.get_direction(compass)
	def get_direction(self,compass):
		if compass == 'N':
			return self.north()
		elif compass == 'S':
			return self.south()
		elif compass == 'E':
			return self.east()
		else:
			return self.west()
	def rotate(self,input):
		if input == 'L':
			 self.facing = self.get_direction(self.facing.left)
			 print 'new facing is %s' % self.facing.name
		elif input == 'R':
			 self.facing = self.get_direction(self.facing.right)
			 print 'new facing is %s' % self.facing.name
	def move(self):
		if self.facing.name == 'north':
			self.y_position += 1
			print 'new y position is %s and new x position is %s' % (self.y_position,self.x_position)
		elif self.facing.name == 'south':
			self.y_position -= 1
			print 'new y position is %s and new x position is %s' % (self.y_position,self.x_position)
		elif self.facing.name == 'east':
			self.x_position += 1
			print 'new y position is %s and new x position is %s' % (self.y_position,self.x_position)
		else:
			self.x_position -= 1
			print 'new y position is %s and new x position is %s' % (self.y_position,self.x_position)
	def locomote(self,command):
		if command == 'M':
			self.move()
		else:
			self.rotate(command)
	def locomotion(self,input_string=[]):
		list_of_commands = list(input_string)
		for command in list_of_commands:
			print command
			self.locomote(command)
			print 'Rover x coordinate is %s, y_coordinate is %s,facing is %s' %(self.x_position,self.y_position,self.facing.name)