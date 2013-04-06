#author:Juned Munshi
#contact: juned@ymail.com


from pygame import *

class gameBoard():
	def  __init__(self,title,width,height,fontSize,fps):
		self.width=width
		self.height=height
		self.section=9
		self.fontSize=fontSize
		self.factor_x=width/self.section
		self.factor_y=height/self.section
		font.init()
		self.clock = time.Clock()
		self.screen=display.set_mode((width,height))
		display.set_caption(title)
		self.fps=fps
		self.rects = [self.screen.fill(-1,(x,y,self.factor_x-1,self.factor_y-1)).inflate(-25,-25) for x in range(1,self.width-self.factor_x,self.factor_x)  for y in range(1,self.height-self.factor_y,self.factor_y)]

	def draw(self):
		display.flip()
		self.clock.tick(self.fps)

	def drawText(self,x,y,text):
		index=x*self.section+y
		offset_x=(self.factor_x-self.fontSize)/2
		offset_y=(self.factor_y-self.fontSize)/2
		self.printText(text,self.rects[index].left+offset_x,self.rects[index].top+offset_y)

	def removeText(self,x,y):
		index=x*self.section+y
		self.screen.fill(-1,(self.rects[index].left-12,self.rects[index].top-12,self.factor_x-1,self.factor_y-1))
		self.draw()

	def printText(self,txtText,Textx, Texty):
		myfont = font.Font(None,self.fontSize)
		label = myfont.render(txtText, 1, (0,0,0))
		self.screen.blit(label, (Textx, Texty))
		display.flip()



	
