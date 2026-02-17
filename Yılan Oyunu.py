import json
import os
import random
import sys

try:
	import pygame
except Exception:
	print("Pygame bulunamadı. Önce requirements.txt içindekileri yükleyin:")
	print("pip install -r requirements.txt")
	sys.exit(1)


BASE_DIR = os.path.dirname(__file__)
CONFIG_PATH = os.path.join(BASE_DIR, "config.json")
SCORES_PATH = os.path.join(BASE_DIR, "scores.json")


def load_config():
	default = {
		"cell_size": 20,
		"cols": 30,
		"rows": 20,
		"speed": 10,
		"bg_color": [0, 0, 0],
		"snake_color": [0, 200, 0],
		"food_color": [200, 0, 0]
	}
	if os.path.exists(CONFIG_PATH):
		try:
			with open(CONFIG_PATH, "r", encoding="utf-8") as f:
				cfg = json.load(f)
				default.update(cfg)
		except Exception:
			pass
	return default


def load_scores():
	if os.path.exists(SCORES_PATH):
		try:
			with open(SCORES_PATH, "r", encoding="utf-8") as f:
				return json.load(f)
		except Exception:
			pass
	return {"highscore": 0}


def save_scores(scores):
	try:
		with open(SCORES_PATH, "w", encoding="utf-8") as f:
			json.dump(scores, f, indent=2)
	except Exception as e:
		print("Skor kaydedilemedi:", e)


def draw_text(surface, text, size, color, x, y):
	font = pygame.font.SysFont(None, size)
	img = font.render(text, True, color)
	surface.blit(img, (x, y))


def main():
	cfg = load_config()
	scores = load_scores()

	CELL = int(cfg["cell_size"])
	COLS = int(cfg["cols"])
	ROWS = int(cfg["rows"])
	SPEED = int(cfg["speed"])

	WIDTH = CELL * COLS
	HEIGHT = CELL * ROWS

	pygame.init()
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Yılan Oyunu (JSON ile)")
	clock = pygame.time.Clock()

	snake = [(COLS // 2, ROWS // 2)]
	direction = (1, 0)
	food = None
	score = 0

	def place_food():
		while True:
			x = random.randrange(0, COLS)
			y = random.randrange(0, ROWS)
			if (x, y) not in snake:
				return (x, y)

	food = place_food()

	running = True
	game_over = False

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN:
				if event.key in (pygame.K_UP, pygame.K_w) and direction != (0, 1):
					direction = (0, -1)
				elif event.key in (pygame.K_DOWN, pygame.K_s) and direction != (0, -1):
					direction = (0, 1)
				elif event.key in (pygame.K_LEFT, pygame.K_a) and direction != (1, 0):
					direction = (-1, 0)
				elif event.key in (pygame.K_RIGHT, pygame.K_d) and direction != (-1, 0):
					direction = (1, 0)
				elif event.key == pygame.K_r and game_over:
					# restart
					snake[:] = [(COLS // 2, ROWS // 2)]
					direction = (1, 0)
					food = place_food()
					score = 0
					game_over = False

		if not game_over:
			head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
			# wall collision
			if head[0] < 0 or head[0] >= COLS or head[1] < 0 or head[1] >= ROWS:
				game_over = True
			else:
				# self collision
				if head in snake:
					game_over = True
				else:
					snake.insert(0, head)
					if head == food:
						score += 1
						food = place_food()
					else:
						snake.pop()

		# draw
		screen.fill(tuple(cfg.get("bg_color", [0, 0, 0])))
		for x, y in snake:
			rect = pygame.Rect(x * CELL, y * CELL, CELL, CELL)
			pygame.draw.rect(screen, tuple(cfg.get("snake_color", [0, 200, 0])), rect)
		fx, fy = food
		frect = pygame.Rect(fx * CELL, fy * CELL, CELL, CELL)
		pygame.draw.rect(screen, tuple(cfg.get("food_color", [200, 0, 0])), frect)

		draw_text(screen, f"Puan: {score}", 24, (255, 255, 255), 5, 5)
		draw_text(screen, f"En Yüksek: {scores.get('highscore',0)}", 24, (255, 255, 255), 120, 5)

		if game_over:
			draw_text(screen, "Oyun Bitti! R: Yeniden oyna  ESC: Çık", 36, (255, 200, 200), WIDTH // 6, HEIGHT // 2)
			# save highscore
			if score > scores.get("highscore", 0):
				scores["highscore"] = score
				save_scores(scores)

		pygame.display.flip()
		clock.tick(SPEED)

		keys = pygame.key.get_pressed()
		if keys[pygame.K_ESCAPE]:
			running = False

	pygame.quit()


if __name__ == "__main__":
	main()


	
	if os.path.exists(CONFIG_PATH):
		try:
			with open(CONFIG_PATH, "r", encoding="utf-8") as f:
				cfg = json.load(f)
				default.update(cfg)
		except Exception:
			pass
	


def load_scores():
	if os.path.exists(SCORES_PATH):
		try:
			with open(SCORES_PATH, "r", encoding="utf-8") as f:
				return json.load(f)
		except Exception:
			pass
	return {"highscore": 0}


def save_scores(scores):
	try:
		with open(SCORES_PATH, "w", encoding="utf-8") as f:
			json.dump(scores, f, indent=2)
	except Exception as e:
		print("Skor kaydedilemedi:", e)


def draw_text(surface, text, size, color, x, y):
	font = pygame.font.SysFont(None, size)
	img = font.render(text, True, color)
	surface.blit(img, (x, y))


def main():
	cfg = load_config()
	scores = load_scores()

	CELL = int(cfg["cell_size"])
	COLS = int(cfg["cols"])
	ROWS = int(cfg["rows"])
	SPEED = int(cfg["speed"])

	WIDTH = CELL * COLS
	HEIGHT = CELL * ROWS

	pygame.init()
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Yılan Oyunu (JSON ile)")
	clock = pygame.time.Clock()

	snake = [(COLS // 2, ROWS // 2)]
	dir = (1, 0)
	food = None
	score = 0

	def place_food():
		while True:
			x = random.randrange(0, COLS)
			y = random.randrange(0, ROWS)
			if (x, y) not in snake:
				return (x, y)

	food = place_food()

	running = True
	game_over = False

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN:
				if event.key in (pygame.K_UP, pygame.K_w) and dir != (0, 1):
					dir = (0, -1)
				elif event.key in (pygame.K_DOWN, pygame.K_s) and dir != (0, -1):
					dir = (0, 1)
				elif event.key in (pygame.K_LEFT, pygame.K_a) and dir != (1, 0):
					dir = (-1, 0)
				elif event.key in (pygame.K_RIGHT, pygame.K_d) and dir != (-1, 0):
					dir = (1, 0)
				elif event.key == pygame.K_r and game_over:
					# restart
					snake = [(COLS // 2, ROWS // 2)]
					dir = (1, 0)
					food = place_food()
					score = 0
					game_over = False

		if not game_over:
			head = (snake[0][0] + dir[0], snake[0][1] + dir[1])
			# wall collision
			if head[0] < 0 or head[0] >= COLS or head[1] < 0 or head[1] >= ROWS:
				game_over = True
			else:
				# self collision
				if head in snake:
					game_over = True
				else:
					snake.insert(0, head)
					if head == food:
						score += 1
						food = place_food()
					else:
						snake.pop()

		# draw
		screen.fill(tuple(cfg.get("bg_color", [0, 0, 0])))
		for x, y in snake:
			rect = pygame.Rect(x * CELL, y * CELL, CELL, CELL)
			pygame.draw.rect(screen, tuple(cfg.get("snake_color", [0, 200, 0])), rect)
		fx, fy = food
		frect = pygame.Rect(fx * CELL, fy * CELL, CELL, CELL)
		pygame.draw.rect(screen, tuple(cfg.get("food_color", [200, 0, 0])), frect)

		draw_text(screen, f"Puan: {score}", 24, (255, 255, 255), 5, 5)
		draw_text(screen, f"En Yüksek: {scores.get('highscore',0)}", 24, (255, 255, 255), 120, 5)

		if game_over:
			draw_text(screen, "Oyun Bitti! R: Yeniden oyna  ESC: Çık", 36, (255, 200, 200), WIDTH // 6, HEIGHT // 2)
			# save highscore
			if score > scores.get("highscore", 0):
				scores["highscore"] = score
				save_scores(scores)

		pygame.display.flip()
		clock.tick(SPEED)

		keys = pygame.key.get_pressed()
		if keys[pygame.K_ESCAPE]:
			running = False

	pygame.quit()


if __name__ == "__main__":
	main()

