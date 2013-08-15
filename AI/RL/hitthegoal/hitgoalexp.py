from hitgoaltask import *
from hitgoalenv import *
from pybrain.rl.agents import LearningAgent
#from pybrain.rl.learners import Reinforce
from reinforce import *
from pybrain.tools.shortcuts import buildNetwork
from pybrain.rl.experiments import Experiment
from pybrain.rl.explorers import EpsilonGreedyExplorer
from pybrain.rl.agents import OptimizationAgent
from pybrain.rl.learners import ENAC
from pybrain.optimization import CMAES

import numpy
env=HitTheGoalEnv(5)
task=HitTheGoalTask(env,[5,0,0])


net = buildNetwork(2, 1, bias=False)
    # create agent with controller and learner (and its options)
agent=OptimizationAgent(net, CMAES())
#agent = LearningAgent(net,ENAC())
#agent.learner.explorer=EpsilonGreedyExplorer(0.0)
#agent.learner._setExplorer(EpsilonGreedyExplorer(0.0))
#agent.learner.explorer.sigma=[0.1]
#print agent.learner.explorer.sigma
#exit()
experiment = Experiment(task, agent)

itr=0
#task.performAction(numpy.array([36]))
while  True:
	 #print itr
	 experiment.doInteractions(50)
	 agent.learn()
	 agent.reset()
	 task.reset()
#	 env.reset()
	# itr=itr+1

