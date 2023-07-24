import pygame
from ellipse_path import path, inner, outer
from car_handle import Car

# Reorganise the boundary data as walls.
walls = []
for i in range(len(inner)):
	walls.append([inner[i-1], inner[i]])
for i in range(len(outer)):
	walls.append([outer[i-1], outer[i]])


# The main program function.
def main():
	pygame.init()
	width, height = 900, 600
	screen = pygame.display.set_mode((width, height))
	clock = pygame.time.Clock()

	car_image = pygame.image.load('car_2.png')
	car_image = pygame.transform.scale(car_image, (42, 20))

	bg = pygame.Surface((width, height))
	bg.fill((80, 50, 80))

	car1 = Car(path[0], 90, 2, 4)
	car1.update(walls)

	drive = False
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			if event.type == pygame.MOUSEBUTTONUP:
				drive = not drive

		if drive:
			car1.update(walls)

		# background surface.
		screen.blit(bg, (0, 0))

		# path and walls boundary.
		for step in path:
			pygame.draw.circle(screen, (30, 30, 30), step, 25)
		for i in range(0, len(outer)):
			pygame.draw.line(screen, (200, 200, 200), outer[i-1], outer[i], 2)
		for i in range(0, len(inner)):
			pygame.draw.line(screen, (200, 200, 200), inner[i-1], inner[i], 2)
		for i in range(0, len(path)):
			pygame.draw.aaline(screen, (10, 20, 200), path[i-1], path[i])

		for ray in car1.rays:
			pygame.draw.aaline(screen, (0, 255, 0), ray.pos, ray.terminus)

		# Rotating and displaying the car.
		car_temp = pygame.transform.rotate(car_image, -car1.dir)
		car_rect = car_temp.get_rect()
		car_rect.center = car1.pos
		screen.blit(car_temp, car_rect)
		
		pygame.display.update()
		clock.tick(60)


if __name__ == '__main__':
	main()
