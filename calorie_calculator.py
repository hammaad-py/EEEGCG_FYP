#modules
import time

'''
accepted actions - 7
					*(jump)
	*(left-punch)				*(right-punch)
	*(left-kick)				*(right-kick)
					*(duck)
'''
#constants
MAXIMUM_WEIGHT = 160.0
MINIMUM_WEIGHT = 10.0
JUMP_KEY = 'w'
LEFT_ARM_KEY = 'a'
RIGHT_ARM_KEY = 'd'
DUCK_KEY = 'x'

class Player:
	calories=0.0
	jump,left_arm,right_arm,duck = 0,0,0,0
	
	def __init__(self,name,weight=10.0):
		self.name = name
		self.weight = weight
	
	def simulating_actions(self,key):
		if key==JUMP_KEY:
			self.jump+=1
		elif key==LEFT_ARM_KEY:
			self.left_arm+=1
		elif key==RIGHT_ARM_KEY:
			self.right_arm+=1
		elif key==DUCK_KEY:
			self.duck+=1


	def calculate_calories(self):
		pass
		#print(f"Name is {self.name} with weight {self.weight}")

if __name__=="__main__":
	name  = input("Please Enter Your Name: ")

	flag=False
	while not flag:
		weight = input("Please Enter Your Weight (10-160 kg): ")
		try:
			weight = float(weight)
			if (weight<MINIMUM_WEIGHT or weight>MAXIMUM_WEIGHT):
				print("Out of Range!\n\n")
				flag = False
				continue
			flag=True
		except:
			print("Please Enter valid Weight!\n\n")
			flag=False

	p1 = Player(name,weight)


	p1.calculate_calories()