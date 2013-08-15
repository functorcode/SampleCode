from scipy import clip, asarray

from pybrain.rl.environments.task import Task
from numpy import *
import math
class HitTheGoalTask(Task):

	def __init__(self,environment,goal):
		self.env = environment
		self.goal=goal
		self.lastreward = 0

	def performAction(self,action):
		self.env.performAction(action)
	def getObservation(self):
		sensors = self.env.getSensors()
		self.ballposition=sensors
		return [sensors[0],sensors[1]]
	def reset(self):
		self.env.resetposition()
	def getReward(self):
		x=0.0;
		for i in range(len(self.goal)):
			x=x+(self.goal[i]-self.ballposition[i])*(self.goal[i]-self.ballposition[i])
		dist=math.sqrt(x)
		#if (dist < 2):
		#	reward = 2-dist
		#	#print reward
		#else:
		reward= -1*dist
		print dist, reward
		return reward

