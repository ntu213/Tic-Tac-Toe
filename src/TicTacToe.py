import pygame


pygame.init()

clock=pygame.time.Clock()
screen = pygame.display.set_mode((340, 340))
pygame.display.set_caption("Tic Tac Toe")
pygame.display.set_icon(pygame.image.load("icon.png"))

boxes = []
for i in range(3):
	for j in range(3):
		rectangle = pygame.Rect(110*j + 10, 110*i + 10, 100, 100)
		boxes.append(rectangle)

running=True
player_turn = False
turns_played = 0
winner = 0
grid = [[0, 0, 0] for _ in range(3)]


def draw_cross(surface, x, y):
	'''Draw a cross on a surface at coordinates x, y'''

	size = 40
	pygame.draw.line(screen, (255, 50, 50), (x-size, y-size), (x+size, y+size), 15)
	pygame.draw.line(screen, (255, 50, 50), (x-size, y+size), (x+size, y-size), 15)


def checkIndex(idx):
	'''Check and place a player's symbol, and can declare a winner'''

	global player_turn, turns_played, winner
	if not grid[idx//3][idx%3]:
		grid[idx//3][idx%3] = player_turn+1
		player_turn = not player_turn
		turns_played+=1

	for y in range(3):
		if grid[y][0] == grid[y][1] == grid[y][2] != 0:
			winner = grid[y][0]

	for x in range(3):
		if grid[0][x] == grid[1][x] == grid[2][x] != 0:
			winner = grid[0][x]

	if grid[0][0] == grid[1][1] == grid[2][2] != 0 or grid[0][2] == grid[1][1] == grid[2][0] != 0:
		winner = grid[1][1]

	# for e in grid:
	# 	print(e)


def play():
	'''Game starting function'''

	global boxes, running, player_turn, turns_played, winner, grid

	while running:

		screen.fill((255, 255, 255))
		pygame.draw.rect(screen, (0, 0, 0), (10, 10, 320, 320))
		for i in range(9):
			rectangle = boxes[i]
			pygame.draw.rect(screen, (255, 255, 255), rectangle)
			box = grid[i//3][i%3]
			if box == 1:
				draw_cross(screen, (i%3) * 110 + 60, (i//3) * 110 + 60)
			elif box == 2:
				pygame.draw.circle(screen, (70, 150, 255), ((i%3) * 110 + 60, (i//3) * 110 + 60), 40, 10)



		for event in pygame.event.get():
			if event.type == pygame.QUIT or pygame.key.get_pressed()[27]:
				running = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				mousePos = pygame.mouse.get_pos()
				click = pygame.Rect(mousePos[0]-2, mousePos[1]-2, 4, 4)
				for i in range(9):
					if click.colliderect(boxes[i]) and not winner:
						checkIndex(i)
						if winner:
							print(f"WINNER: {['CROSS', 'CIRCLE'][winner-1]}")

		pygame.display.flip()
		clock.tick(60)

	pygame.quit()


if __name__ == "__main__":
	play()

