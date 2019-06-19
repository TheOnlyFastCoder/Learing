import pygame , sys , time, random, threading
from pygame.locals import *


pygame.init()

FPS = pygame.time.Clock()
scr_size = (width,height) = (800,500)
dark = (27,27,38)
pink = ( 82,32,207)
white = (255,255,255)
red = (255,0,0)


obj_x = 10
obj_y = height-50
obj_isJump = False
obj_jumpCount = 10
obj_isCrouch = False
obj_sizeY = 50
game_loss = 0


display =  pygame.display.set_mode(scr_size)
pygame.display.set_caption('Game')



class DrawWindow(pygame.sprite.Sprite):	
	def __init__(self,x,y,sizeY,random_num):
		self.x = obj_x
		self.y = obj_y
		self.sizeY = sizeY
		self.random_num = random_num


	def displaytext(self,text):
		font = pygame.font.SysFont(None, 50)
		text = font.render(str(text), 1, dark)
		textpos = text.get_rect(centerx=50, centery= 50)
		display.blit(text,textpos)

	def person(self):
		pygame.draw.rect(display,dark,(self.x,self.y,50,self.sizeY))

	def Ball(self,count):
		global game_loss , random_num
		pos_y = 20
		pos_x = width - count; 

		if  self.x <= pos_x <= self.x + 50 and self.y <= obj_y+20 <= self.y + 50:
			game_loss += 1 
			return 0
		elif pos_x < 2: 
			return 0		
		else:
			for x in range(0,5):
				count += 20 		
				
			print(count)
			pygame.draw.circle(display, pink, (pos_x-count,self.random_num), 10)	
		self.displaytext(game_loss)

def main():
	global obj_isJump,obj_jumpCount,obj_isCrouch

	gameOver = True
	random_num = random.randint((obj_y+10),(obj_y+60))
	drawWindow = DrawWindow(obj_x,obj_y,50,random_num)
	count = 0

	while gameOver:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
	

		keys = pygame.key.get_pressed()
		if keys[K_RIGHT] and drawWindow.x < width - 50 - 1:
			drawWindow.x += 5
		if keys[K_LEFT] and drawWindow.x > 1:
			drawWindow.x -= 5
		
		if not(obj_isJump):
			if keys[K_UP]:
				obj_isJump = True
		else:
			if obj_jumpCount >= -10:
				if obj_jumpCount < 0:
					drawWindow.y += (obj_jumpCount ** 2) / 4
				else:
					drawWindow.y -=  (obj_jumpCount ** 2) / 4
				obj_jumpCount -= 1
			else:
				obj_isJump = False
				obj_jumpCount = 10
		
		if not(obj_isCrouch):
			if keys[K_SPACE]:
				obj_isCrouch = True
		else:
			if drawWindow.sizeY >= 50:
				drawWindow.sizeY -= 25
				drawWindow.y += 25
			if not(keys[K_SPACE]):	
				drawWindow.sizeY += 25
				drawWindow.y -= 25
				
		count += 9 
		display.fill(white)

		if drawWindow.Ball(count) == 0:
			count = 0
			count += 9 
			drawWindow.Ball(count)
		else: 
			drawWindow.Ball(count)

		drawWindow.Ball(count)
		drawWindow.person()
		pygame.display.update()
		FPS.tick(60)

	pygame.quit()
	quit()
main()
