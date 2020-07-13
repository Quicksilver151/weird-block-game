import pygame as pygame

class character(object):
	def __init__(self, win, x, y, width, height, color):
		self.x, self.y = x, y
		self.win = win
		self.width = width
		self.height = height
		self.color = color
		self.rect = pygame.Rect(x, y, width, height)
		self.facing = "D"
		self.speed = 30
		self.isShooting = False
		self.moveU = False
		self.moveD = False
		self.moveL = False
		self.moveR = False
		
	def redraw(self):
		if self.moveU and self.rect.y >= self.speed:
			self.rect.y -= self.speed		
		if self.moveD and self.rect.y <= self.win.get_height() - self.height - self.speed:
			self.rect.y += self.speed
		if self.moveL and self.rect.x >= self.speed:
			self.rect.x -= self.speed
		if self.moveR and self.rect.x <= self.win.get_width() - self.width - self.speed:
			self.rect.x += self.speed
		self.win.fill(self.color, self.rect)
		
class button(object):
	def __init__(self, x, y, width, height, color, on_click, args=None):
		self.width = width
		self.height = height
		self.color = color
		self.args = args
		self.on_click = on_click
		self.rect = pygame.Rect(x, y, width, height)
		
	def redraw(self, win):
		win.fill(self.color, self.rect)
	def press(self):
		if self.args == None:
			self.on_click()
		else:
			self.on_click(self.args)

class projectile(object):
	def __init__(self, x, y, s, vel, facing, dmg):
		self.s = s
		self.vel = vel
		self.dmg = dmg
		self.rect = pygame.Rect(x, y, s, s)
		self.color = (0,0,0)
		moveX, moveY = 0,0
		if facing == "U":
			self.moveX = 0
			self.moveY = -1
		if facing == "D":
			self.moveX = 0
			self.moveY = 1					
		if facing == "L":
			self.moveX = -1
			self.moveY = 0		
		if facing == "R":
			self.moveX = 1
			self.moveY = 0
		
	def redraw(self, win):
		self.rect.x += self.vel * self.moveX
		self.rect.y += self.vel * self.moveY
		
		win.fill(self.color, self.rect)
		
class box(object):
	def __init__(self, x, y, s, color, health):
		self.s = s
		self.color = color
		self.rect = pygame.Rect(x, y, s, s)
		self.health = health
		self.inithealth = health
		self.font = pygame.font.SysFont("DejaVuSans", 1) #self.s*0.2)
	def redraw(self, win):
		label = self.font.render(f"{self.health}/{self.inithealth}", 1, self.color)
		win.blit(label, (self.rect.x+self.s*0.1, self.rect.y+self.s*1.05))
		win.fill(self.color, self.rect)
		
		
		
	
		
	
		
		
