#Basic premise:
#This is my Genuis Hour is game made is python using microsofts visual studio code
#The goal is for the giraffe(control with arrow keys at start of game) to get to the tree when that is done 
#it will eat it and the lion will go on the hunt to try to find and eat the girraffe
#when he does the level will switch and you control the lion(will follow mouse cursor)
#extra info:
#full code and assest are open source on github
#this project was not as good as it could have been becuase my plan was to fully make a 3D game 
#I relized that did not have the time for that and resorted to this instead
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#setup
import pygame
import random
import time
pygame.init()
screen=pygame.display.set_mode([1920, 1080])
GiraffeX=30
GiraffeY=400
imagesize=(200,200)
AIX=1000
AiY=900
LionX=random.randint(650,1100)
LionY=random.randint(300,400)
Stage2=False
Giraffe=pygame.image.load('Giraffe.png')
Lion=pygame.image.load('Lion.png')
text=pygame.image.load('Text.png')


#Main loop
Main=True
while Main:
    
    #define sprites
    def Text():
        text=pygame.image.load('Text.png')
        text = pygame.transform.scale(text, (400,400))
        screen.blit(text,(-1000,-1000))

    def sun():
        Sun=pygame.image.load('Sun.png')
        Sun = pygame.transform.scale(Sun, imagesize)
        screen.blit(Sun,(100,2))
    

    def tree():
        Tree=pygame.image.load('Tree.png')
        Tree = pygame.transform.scale(Tree, (400,400))
        screen.blit(Tree,(400,200))
    
    
    def background():
        Background=pygame.image.load('Background.jpg')

        Background = pygame.transform.scale(Background, (1920,1080))
        screen.blit(Background,(0,0))
    
    
    def giraffe():
        Giraffe=pygame.image.load('Giraffe.png')
        Giraffe = pygame.transform.scale(Giraffe, (400,400))
        screen.blit(Giraffe,(GiraffeX,GiraffeY))
    
    def lion():
        Lion=pygame.image.load('Lion.png')
        Lion = pygame.transform.scale(Lion, (400,400))
        screen.blit(Lion,(LionX,LionY))
    #start of game(Draw starting sprites)
    background()
    sun()
    tree()
    giraffe()
    lion()
    Text()
    if Stage2:
            LionX=-1000
            LionX=-1000
            GiraffeX=-1000
            GiraffeY=-1000
            lion2= Lion=pygame.image.load('Lion.png')
            lion2 = pygame.transform.scale(lion2, (400,400))
            lion2x,lion2y=pygame.mouse.get_pos()
            screen.blit(lion2,(lion2x,lion2y))
            
            
            screen.blit(text,(700,1))
            pygame.display.update()
    pygame.display.update()
    
    

    
    #check for events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            Main=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                GiraffeX-=50
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                GiraffeX+=50
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                GiraffeY-=50
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                GiraffeY+=50                
        

        #secret code
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_1:
                LionX=random.randint(10,1000)
                LionY=random.randint(100,500)    
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_2:
                Stage2=True
                
        
    pygame.display.flip()   
