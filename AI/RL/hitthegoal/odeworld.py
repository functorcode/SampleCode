# pyODE example 1: Getting started
    
import ode
# Collision callback
def near_callback(args, geom1, geom2):
    """Callback function for the collide() method.

    This function checks if the given geoms do collide and
    creates contact joints if they do.
    """
    print "Called" 
    # Check if the objects do collide
    contacts = ode.collide(geom1, geom2)

    # Create contact joints
    world,contactgroup = args
    for c in contacts:
        c.setBounce(0.2)
        c.setMu(5000)
        j = ode.ContactJoint(world, contactgroup, c)
        j.attach(geom1.getBody(), geom2.getBody())
# Create a world object
world = ode.World()
world.setGravity( (0,-9.81,0) )
# Create a space object
space = ode.Space()
floor = ode.GeomPlane(space, (0,1,0), 0)
# Create a body inside the world
body = ode.Body(world)
M = ode.Mass()
M.setSphere(2500.0, 0.05)
M.mass = 1.0
body.setMass(M)

body.setPosition( (0,0.05,0) )
gsphere=ode.GeomSphere(space=space, radius=0.05)
gsphere.setBody(body)

body.addForce([-0.1615,0,0])


# Do the simulation...
total_time = 0.0
dt = 0.04
y=1
contactgroup = ode.JointGroup()
while total_time<5  and y>-1:


    print body.getPosition()
    x,y,z = body.getPosition()
    u,v,w = body.getLinearVel()
    space.collide((world,contactgroup), near_callback)
    print "%1.2fsec: pos=(%6.3f, %6.3f, %6.3f)  vel=(%6.3f, %6.3f, %6.3f)" % \
         (total_time, x, y, z, u,v,w)
    world.step(dt)
    contactgroup.empty()
    total_time+=dt