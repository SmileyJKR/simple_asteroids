import pygame
import sys
from constants import *
from logger import log_state, log_event
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
	print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	pygame.init()
	FPS = 60
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	running = True
	
	
	#this is to hold everything that has to be updated in the game
	updatable = pygame.sprite.Group()
	
	#this is to hold everything that has to be drawn in the game
	drawable = pygame.sprite.Group()
	
	asteroids = pygame.sprite.Group()
	
	shots = pygame.sprite.Group()
	
	Shot.containers = (shots, drawable, updatable)
	AsteroidField.containers = (updatable)
	Asteroid.containers = (asteroids, updatable, drawable)
	Player.containers = (updatable, drawable)
	player = Player( SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()
	while running:
		log_state()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		screen.fill("black")
		
		updatable.update(dt)
		for objects in drawable:
			objects.draw(screen)
		
		for asteroid in asteroids:
			if asteroid.collides_with(player):
				log_event("player_hit")
				print("Game over!")
				sys.exit()
			for shot in shots:
				if asteroid.collides_with(shot):
					log_event("asteroid_shot")
					shot.kill()
					asteroid.split()
		
		pygame.display.flip()
	   
		dt = clock.tick(FPS) / 1000



if __name__ == "__main__":
	main()
