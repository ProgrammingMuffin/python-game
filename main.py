import pygame
import sys

pygame.init()

window = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()

pressed = {
	"right": 0,
	"left": 0,
	"up": 0,
	"down": 0
}

released = []

class world:
	x = 25
	y = 25
	w = 100
	h = 100
	acc = 0.1
	vel = 5
	@staticmethod
	def move_rect(x, y, acc, vel):
		global pressed, released
		if pressed["right"]:
			if(vel >= 5 and vel < 10):
				vel += acc
			x += vel
		if ("right" in released and pressed["right"] != 1):
			if((vel-acc) >= 5 and (vel-acc) <= (5 + acc)):
				vel = 5
			elif((vel-acc) >= (5+acc)):
				vel -= acc
			if(vel != 5):
				x += vel
		if pressed["left"]:
			if(vel >= 5 and vel < 10):
				vel += acc
			x -= vel
		if ("left" in released and pressed["left"] != 1):
			if((vel-acc) >= 5 and (vel-acc) <= (5 + acc)):
				vel = 5
			elif((vel-acc) >= (5+acc)):
				vel -= acc
			if(vel != 5):
				x -= vel
		world.x = x
		world.y = y
		world.acc = acc
		world.vel = vel
	@staticmethod
	def draw_screen():
		#print("x: ", world.x, "\tvelocity: ", world.vel)
		print("acceleration: ", world.acc,  "\tvelocity: ", world.vel)
		window.fill((255, 2, 0))
		pygame.draw.rect(window, (0, 128, 0), (world.x, world.y, world.w, world.h))

while(1):
	clock.tick(50)
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			print("Quit from deepak's game")
			sys.exit()
		elif(event.type == pygame.KEYDOWN):
			if(event.key == pygame.K_RIGHT):
				pressed["right"] = 1
			if(event.key == pygame.K_LEFT):
				pressed["left"] = 1
		elif(event.type == pygame.KEYUP):
			released.clear()
			if(event.key == pygame.K_RIGHT):
				pressed["right"] = 0
				released.append("right")
			if(event.key == pygame.K_LEFT):
				pressed["left"] = 0
				released.append("left")
	world.move_rect(world.x, world.y, world.acc, world.vel)
	world.draw_screen()
	pygame.display.flip()