import pygame_sdl2 as pygame
from classes import *
pygame.init()
winx, winy = 1080, 1920
win = pygame.display.set_mode((winx, winy), pygame.DOUBLEBUF)
run = True
bgcolor = (173, 216, 230)
clock = pygame.time.Clock()
player = character(win, 0,0, 200, 200, (0,180,0))
bullets = []
bullet_cooldown = 0
def moveU():
	player.moveU = True
	player.facing = "U"
def moveD():
	player.moveD = True
	player.facing = "D"
def moveL():
	player.moveL = True
	player.facing = "L"
def moveR():
	player.moveR = True
	player.facing = "R"
def shoot():
	player.isShooting = True

#buttons to control player's movements and actions
button_size = 150
buttonUP = button(780,winy-450, button_size, button_size, (255, 255, 255), moveU)

buttonDOWN = button(780,winy-150, button_size, button_size, (255, 255, 255), moveD)

buttonLEFT = button(630,winy-300, button_size, button_size, (255, 255, 255), moveL)

buttonRIGHT = button(930,winy-300, button_size, button_size, (255, 255, 255), moveR)

buttonSHOOT = button(button_size, winy-button_size*2, button_size*1.3, button_size*1.3, (255,255,255), shoot)

buttons = [buttonUP, buttonDOWN, buttonLEFT, buttonRIGHT, buttonSHOOT]

#objects in the area
box2 = box(864, 182, 128, (128, 128, 128), 200)
box1 = box(204, 182, 600, (128, 128, 128), 800)


objects = [box1, box2]
objectrect = []
for object in objects:
	objectrect.append(object.rect)


def checkCollisions():
	#This "bounces" the player off to the opposite direction  when it collides with an object
	if not player.rect.collidelist(objectrect) == -1:
		if player.facing == "U":
			player.rect.y += player.speed
		if player.facing == "D":
			player.rect.y -= player.speed
		if player.facing == "L":
			player.rect.x += player.speed
		if player.facing == "R":
			player.rect.x -= player.speed
	#Checks if the bullets have hit any objects (this is probably bad way to do it but idk any other way)
	for bullet in bullets:
		index = bullet.rect.collidelist(objectrect)
		print(index)
		if not index == -1:
			objects[index].health -= bullet.dmg
			if objects[index].health <= 0:				
				objectrect.pop(index)
				objects.pop(index)
			
			bullets.pop(bullets.index(bullet))
			

def Update():
	global bgcolor, buttons, bullets, win, bullet_cooldown, objects
	win.fill(bgcolor)
	for object in objects:
		object.redraw(win)
	
	for bullet in bullets:
		if (bullet.rect.x <= 0 or bullet.rect.x >= win.get_width()) or (bullet.rect.y <= 0 or bullet.rect.y >= win.get_height()):
			bullets.pop(bullets.index(bullet))
		bullet.redraw(win)
		
	if player.isShooting and bullet_cooldown == 0:
		bullets.append(projectile(player.rect.x + player.width/2 - 20, player.rect.y + player.height/2 - 20, 50, 80, player.facing, 50))
	
		bullet_cooldown = 7
	if bullet_cooldown > 0:
		bullet_cooldown -= 1
	player.redraw()
	for button in buttons:
		button.redraw(win)
	checkCollisions()

############ MAIN LOOP ##############
while run:
	for ev in pygame.event.get():
		if ev.type == pygame.QUIT:
			run = False
		if ev.type == pygame.MOUSEBUTTONDOWN:
			for button in buttons:
				if button.rect.collidepoint(ev.pos):
					button.color = (255,0,0)
					button.press()
		elif ev.type == pygame.MOUSEBUTTONUP:
			for button in buttons:
				button.color = (255,255,255)
			player.isShooting = False
			player.moveU = False
			player.moveD = False
			player.moveL = False
			player.moveR = False
	Update()
	pygame.display.update()
	clock.tick(35)
pygame.quit()