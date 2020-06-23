import pygame
import random
import math

from pygame import mixer

#for initialisation of the module
pygame.init()

#creating the game window
#set_mod(Screenwidth,screenheight)
screen= pygame.display.set_mode((800,600))

#creating background
backGround= pygame.image.load("bg.png")

#adding bg music
mixer.music.load("bgmusic.wav")
mixer.music.play(-1)


#title and icon setting
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

#defining player

playerImg=pygame.image.load("player.png")
playerX=363
playerY=440
playerX_change=0;

#defining the bullet
#ready-> you cannot see the bullet on the screen
#fire-> the bullet has left the ship and moving

bulletImg=pygame.image.load("bullet.png")
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=3.5
bullet_state="ready"

#defining enemy
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
number_of_enemies=4

for i in range(number_of_enemies):

	enemyImg.append(pygame.image.load("alien.png"))
	enemyX.append(random.randint(30,760))
	enemyY.append( random.randint(50,150))
	enemyX_change.append(2)
	enemyY_change.append(30)

#displaying score
score_val=0
font=pygame.font.Font("Malvie.otf",32)
textX=10
textY=10
over=pygame.font.Font("Malvie.otf",64)

def game_over():
	gameover=over.render("GAME OVER",True,(255,255,255))
	screen.blit(gameover,(200,250))

def show_score(x,y):
	score=font.render("Score:- "+str(score_val),True,(255,255,255))
	screen.blit(score,(x,y))


def player(x,y):
	#blit simply refers to draw an image on the screen at a particular coordinates
	screen.blit(playerImg,(x,y))


def enemy(x,y,i):
	screen.blit(enemyImg[i],(x,y))

def fire_bullet(x,y):
	global bullet_state
	bullet_state="fire"
	screen.blit(bulletImg,(x+15,y))
def iscollision(enemyX,enemyY,bulletX,bulletY):
	distance= math.sqrt((math.pow((enemyX-bulletX),2)+math.pow((enemyY-bulletY),2)))
	if distance<30:
		return True
	return False



#game loop (basic body of a game)
running=True
while (running):
	screen.fill((0,0,0))
	#background
	screen.blit(backGround,(0,0))
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False

	#pygame.KEYDOWN-> a key is pressed
	#pygame.KEYUP->the keystroke is released

		if event.type==pygame.KEYDOWN:
			
			if event.key==pygame.K_LEFT:
				playerX_change=-2
			if event.key==pygame.K_RIGHT:
				playerX_change=2
			if event.key==pygame.K_SPACE:
				if(bullet_state=="ready"):

					#get the current x coordinate of spaceship
					bulletX=playerX
					fire_bullet(bulletX,bulletY)
				

		if event.type==pygame.KEYUP:
			if event.key==pygame.K_RIGHT or event.key== pygame.K_LEFT:
				playerX_change=0;

	playerX+=playerX_change

	if playerX<=0:
		playerX=0
	elif playerX>736:
		playerX=736  #because of the size of the image itself


	for i in range(number_of_enemies):#a loop to handle all the enemies


		if enemyY[i]>430:
			for j in range(number_of_enemies):
				enemyY[j]=2000;
			game_over()
			break


		enemyX[i]+=enemyX_change[i]


	   #movement of the enemy, when it reaches boundary it rebounds,and also descends some pixels
		if enemyX[i]<=0:
			enemyX_change[i]=2
			enemyY[i]+=enemyY_change[i]

		elif enemyX[i]>736:
			enemyX_change[i]=-2
			enemyY[i]+=enemyY_change[i]
		if iscollision(enemyX[i],enemyY[i],bulletX,bulletY):
			collision_sound=mixer.Sound("boom.wav")
			collision_sound.play()
			bulletY=playerY
			bullet_state="ready"
			score_val+=1
			enemyX[i]= random.randint(30,735)
			enemyY[i]= random.randint(50,150)
		enemy(enemyX[i],enemyY[i],i)

	if bulletY<=0:
		
		bullet_state="ready"
		bulletX=playerX
		bulletY=playerY

		



	if bullet_state == "fire":
		fire_bullet(bulletX,bulletY)
		bulletY-=bulletY_change


	


	

	player(playerX,playerY)
	show_score(textX,textY)
	
	pygame.display.update()
    
    
    
	 
    


	
	
