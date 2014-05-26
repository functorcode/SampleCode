from pybrain.rl.environments.environment import Environment
from scipy import zeros
import ode
class HitTheGoalEnv(Environment):
	indim=1
	outdim=3
	def __init__(self,maxtime):
		self.maxtime=maxtime
		self.createworld()
	def performAction(self,action):
		self.ball.addForce((action.tolist()[0],0,0))
		total_time = 0.0
		dt = 0.04
		y=100
		#print action
	
		while total_time<self.maxtime and y >-1:
		#	print body.getPosition()
			x,y,z = self.ball.getPosition()
			#print x
		#	u,v,w = body.getLinearVel()
		#print "%1.2fsec: pos=(%6.3f, %6.3f, %6.3f)  vel=(%6.3f, %6.3f, %6.3f)" % \
		#      (total_time, x, y, z, u,v,w)
			self.space.collide((self.world,self.contactgroup),self.near_callback)
			self.world.step(dt)
			self.contactgroup.empty()
			total_time+=dt
		#print action,x
		#print "Action",action.tolist(),"Position:",self.ball.getPosition() 
	def  getSensors(self):
		x,y,z= self.ball.getPosition()
		return [x,y,z]
	def resetposition(self):
		self.ball.setPosition( (0,0.05,0) )
	def createworld(self):
		self.world=ode.World()
		self.world.setGravity( (0,-9.81,0) )

		# Create a body inside the world
		self.ball = ode.Body(self.world)
		M = ode.Mass()
		M.setSphere(2500.0, 0.05)
		M.mass = 1.0
		self.ball.setMass(M)
		self.ball.setPosition( (0,0.05,0) )
		self.space=ode.Space()
		self.floor=ode.GeomPlane(self.space, (0,1,0), 0)
		self.gsphere=ode.GeomSphere(space=self.space, radius=0.05)
		self.gsphere.setBody(self.ball)
		self.contactgroup = ode.JointGroup()

	def near_callback(self,args, geom1, geom2):
		"""Callback function for the collide() method.

		This function checks if the given geoms do collide and
		creates contact joints if they do.
		"""
		#print "Called" 
		# Check if the objects do collide
		contacts = ode.collide(geom1, geom2)

		# Create contact joints
		world,contactgroup = args
		for c in contacts:
			c.setBounce(0.2)
			c.setMu(5000)
			j = ode.ContactJoint(world, contactgroup, c)
			j.attach(geom1.getBody(), geom2.getBody())
