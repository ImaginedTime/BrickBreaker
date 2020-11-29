import pygame, random

pygame.init()

# SCREEN VARIABLES
s = 32
width, height = 1080, 680
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Brick Breaker")
clock = pygame.time.Clock()
black, white = (200,200,200), (12,12,12)

# RECTANGLES 
player = pygame.Rect(width / 2 - 70, height - 30, 140 , 20)
ball = pygame.Rect(width / 2 - s/2, height - s - 30, s,s)
bricks = [[], [], [], [], [], [], [], []]

# GAME VARIBALES 
started = False
level = 0
bsx, bsy = 7 * random.choice([-1, 1]), -7
ps = 0
score = 0
chances = 3
lost = False
won = False

# FONT VARIBALES 
font1 = pygame.font.Font("freesansbold.ttf", s)
font2 = pygame.font.Font("freesansbold.ttf", s//2)

# MAKE ALL THE LEVELS OF THE GAME IN BRICKS LIST 
def LevelMaker():
	global bricks

	for i in range(30):
		for j in range(10):
			if i % 3 == j % 3:
				bricks[0].append(pygame.Rect(s/2 + i*s + 3*i, 2 + j*s/2 + 3*j, s, s/2))
			else:
				bricks[0].append(None)
	for i in range(30):
		for j in range(10):
			if i % 3 == j % 2:
				bricks[1].append(pygame.Rect(s/2 + i*s + 3*i, 2 + j*s/2 + 3*j, s, s/2))
			else:
				bricks[1].append(None)
	for i in range(30):
		for j in range(10):
			if i == 0 or j == 0 or i == 29 or j == 9 or j == 8 or (i % 2 == 0 and j % 2 == 0):
				bricks[2].append(pygame.Rect(s/2 + i*s + 3*i, 2 + j*s/2+ 3*j, s, s/2))
			else:
				bricks[2].append(None)
	for i in range(30):
		for j in range(10):
			if not(i % 2 == 0 and j % 2 == 0):
				bricks[3].append(pygame.Rect(s/2 + i*s + 3*i, 2 + j*s/2+ 3*j, s, s/2))
			else:
				bricks[3].append(None)
	for i in range(30):
		for j in range(10):
			if i % 2 == j % 2:
				bricks[4].append(pygame.Rect(s/2 + i*s + 3*i, 2 + j*s/2 + 3*j, s, s/2))
			else:
				bricks[4].append(None)
	for i in range(30):
		for j in range(10):
			if i % 3 != j % 3:
				bricks[5].append(pygame.Rect(s/2 + i*s + 3*i, 2 + j*s/2 + 3*j, s, s/2))
			else:
				bricks[5].append(None) 
	for i in range(30):
		for j in range(10):
			if i % 4 != j % 4:
				bricks[6].append(pygame.Rect(s/2 + i*s + 3*i, 2 + j*s/2 + 3*j, s, s/2))
			else:
				bricks[6].append(None)	
	for i in range(30):
		for j in range(10):
			bricks[7].append(pygame.Rect(s/2 + i*s + 3*i, 2 + j*s/2 + 3*j, s, s/2))

# RESTARTING THE GAME AFTER THE PLAYER LOSES OR WINS
def restart():
	global player, ball, bricks, started, level, bsx, bsy, ps, score, chances
	player = pygame.Rect(width / 2 - 70, height - 30, 140 , 20)
	ball = pygame.Rect(width / 2 - s/2, height - s - 30, s,s)
	bricks = [[], [], [], [], [], [], [], []]
	started = False
	level = 0
	bsx, bsy = 7 * random.choice([-1, 1]), -7
	ps = 0
	score = 0
	chances = 3
	lost = True
	LevelMaker()

# RESETING THE POSITONS OF THE BALL AND THE PLAYER AFTER THE PLAYER MISSES THE BALL 
def reset():
	global player, ball, chances, width, height, lost
	player = pygame.Rect(width / 2 - 70, height - 30, 140 , 20)
	ball = pygame.Rect(width / 2 - s/2, height - s - 30, s,s)
	chances -= 1
	if chances == 0:
		lost = True
		restart()

# ANIMATIONS AND COLLISION CHECK OF THE BALL 
def ballAnimation():
    global ball, player, bricks, bsx, bsy, width ,height, score
    if ball.top <= 0:
        bsy *= -1
        ball.top = 1
    if ball.left <= 0 or ball.right >= width:
    	bsx *= -1
    if ball.colliderect(player):
        bsy *= -1
    if ball.bottom >= height:
    	pygame.time.delay(200)
    	reset()
    for i in range(300):
	    if bricks[level][i] != None and ball.colliderect(bricks[level][i]):
	    	bsy *= -1
	    	bricks[level][i] = None
	    	score += 1
	    	break
    ball.x += bsx
    ball.y += bsy

# ANIMATIONS OF THE PLAYER MOVES
def playerAnimation():
    global player, ps, width ,height
    player.x += ps
    if player.right > width:
        player.right = width
    if player.left < 0:
        player.left = 0

LevelMaker()

while True:
	clock.tick(60)
	# EVENT CHECK 
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			pygame.quit()
			break
		if e.type == pygame.KEYDOWN:
			if started and e.key == pygame.K_RIGHT:
				ps += 7
			if started and e.key == pygame.K_LEFT:
				ps -= 7
			if started and e.key == pygame.K_d:
				ps += 7
			if started and e.key == pygame.K_a:
				ps -= 7
			if (not started) and (not lost) and (not won) and e.key == pygame.K_RETURN:
				started = True
			if lost and e.key == pygame.K_RETURN:
				lost = False
			if won and e.key == pygame.K_RETURN:
				won = False
				restart()
		if e.type == pygame.KEYUP:
			if started and e.key == pygame.K_RIGHT:
				ps -= 7
			if started and e.key == pygame.K_LEFT:
				ps += 7
			if started and e.key == pygame.K_d:
				ps -= 7
			if started and e.key == pygame.K_a:
				ps += 7

	surface.fill(white)

	# THE SCENE WITH THE GAME BEING PLAYED 
	if started:	
		if bricks[level].count(None) == len(bricks[level]):
			started = False
			level += 1
			if level > 7:
				won = True
				started = False
				continue
			chances = 3
			continue
		scoreText = font1.render(f"Score  {score}", True, black)
		chancesText = font1.render(f"Chances {chances}", True, black)
		surface.blit(scoreText, (s, 2*height/3))
		surface.blit(chancesText, (width - chancesText.get_rect().width - s, 2*height/3))
		pygame.draw.rect(surface, black, player)
		pygame.draw.ellipse(surface, black, ball)

		for i in range(300):
			if bricks[level][i] != None:
				pygame.draw.rect(surface, black, bricks[level][i])
		ballAnimation()
		playerAnimation()

	# THE SCENE TO START THE GAME
	elif not lost:
		levelText = font2.render(f"Level  {level + 1}", True, black)
		startText = font1.render("START", True, black)
		pressEnterText = font2.render("Press Enter To Begin", True, black)
		surface.blit(levelText, (width / 2 - levelText.get_rect().width/2, height/2 - levelText.get_rect().height - startText.get_rect().height))
		surface.blit(startText, (width / 2 - startText.get_rect().width/2, height /2 - startText.get_rect().height/2))
		surface.blit(pressEnterText, (width/2 - pressEnterText.get_rect().width/2, height/2 + pressEnterText.get_rect().height/2 + startText.get_rect().height))

	# THE SCENE TO DISPLAY "YOU LOSE"
	else:
		lostText = font1.render("YOU LOST", True, black)
		pressEnterText = font2.render("Press Enter To Continue", True, black)
		surface.blit(lostText, (width / 2 - lostText.get_rect().width/2, height /2 - lostText.get_rect().height/2))
		surface.blit(pressEnterText, (width/2 - pressEnterText.get_rect().width/2, height/2 + pressEnterText.get_rect().height/2 + lostText.get_rect().height))
	
	# THE SCENE TO DISPLAY "YOU WON"
	if won:
		surface.fill(white)
		wonText = font1.render("YOU WON", True, black)
		pressEnterText = font2.render("Press Enter To Continue", True, black)
		surface.blit(wonText, (width / 2 - wonText.get_rect().width/2, height /2 - wonText.get_rect().height/2))
		surface.blit(pressEnterText, (width/2 - pressEnterText.get_rect().width/2, height/2 + pressEnterText.get_rect().height/2 + wonText.get_rect().height))
	
	pygame.display.flip()