import random

WIDTH = 600
HEIGHT = 600

background = Actor('background')
player = Actor('player')
player.x = 200
player.y = 200
enemy = Actor('enemy', pos = (400, 400))
item = Actor('item',pos = (300, 300))
score = 0
time = 30

player2 = Actor('player2')

score2 = 0

def draw ():
    screen.clear()
    background.draw()
    player.draw()
    enemy.draw()
    item.draw()
    player2.draw()

    score_string = str(score)
    screen.draw.text(score_string, (0, 0), color = 'black')

    score_string2 = str(score2)
    screen.draw.text( score_string2, (10, 0), color = 'black')

    time_string = str(round(time))
    screen.draw.text(time_string, (50, 0), color = 'black')

def update(delta):
    global score, time, score2

    time = time - delta
    if time <= 0:
        exit()

    if keyboard.right:
        player.x = player.x + 4
    if keyboard.left:
        player.x = player.x - 4
    if keyboard.down:
        player.y = player.y + 4
    if keyboard.up:
        player.y = player.y - 4


    if enemy.x < player.x:
        enemy.x = enemy.x + 1
    if enemy.x > player.x:
        enemy.x = enemy.x - 1
    if enemy.y < player.y:
        enemy.y = enemy.y + 1
    if enemy.y > player.y:
        enemy.y = enemy.y - 1
    if player.colliderect(enemy):
        exit()

    if keyboard.d:
        player2.x = player2.x + 4
    if keyboard.a:
        player2.x = player2.x - 4
    if keyboard.s:
        player2.y = player2.y + 4
    if keyboard.w:
        player2.y = player2.y - 4

    if item.colliderect(player):
        item.x = random.randint(0, WIDTH)
        item.y = random.randint(0, HEIGHT)
        score = score + 1


    if item.colliderect(player2):
        item.x = random.randint(0, WIDTH)
        item.y = random.randint(0, HEIGHT)
        score2 = score2 + 1
