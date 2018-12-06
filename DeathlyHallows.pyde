import os, randome, time 
path=os.getcwd()
boardSize=50 #this changes the board size 
gridrow=25
gridcol=30

#How do we slice the image into smaller parts? -> al reem will work on slicing the picture 

#1. set up the background to be hogwarts -> set up the game start, directions 
#-> we need to have a character (harry with a broomstick -> wherever the mouse moves, harry moves as well) 

#2. make sure if you click the game start, you move to the inside background = grand dining hall
#-> set up the timer, and the life (three), count the deathly hallows (reach three, you win)

#3. you click certain parts of the dining hall and if you click, the grid should reveal whatever it is hiding inside 
#-> if it is an empty tile -> you lose 5 seconds of your time 
#-> if it is a professor -> you lose 1 life 
#-> if it is a deathly hallow -> you add to deathlyhallow.count 
#-> if it is a ghost -> you are given a hint (as to where the hallows are) -> the hint is going to be like pop-up

#4. winning/losing condition 
#-> checkWin function -> if you collect hallows in time, without losing three lives, you win 
#-> checkLose function (above checkwin condition) 
#-> encounter professor three times -> you lose
#-> when time is up -> you lose 

#what we can do now: 
    #get all the images (image slice, value, position, size)
    #images include (hallows, professors(soundtrack), ghosts (soundtrack), harry)
    #sounds for all of them 
    #winning conditions, losing conditions, and i will try to make basic setup (randomly assign the hallows, professors, and the ghosts)
    
    
    
def setup():
    background(0)
    size(boardSize*gridrow, boardsize*gridcol)
    print(path)
    
def draw():
    background(50)
    if deathlyhallows.game == "Lose":
        img=loadImage(path+"/images/"+"youlost.png")
        image(img,50,50)
        
    elif deathlyhallows.game == "Continue":
        deathlyhallows.displayboard() 
        
    elif deathlyhallows.game == "Win":
        img=loadImage(path+"/images/"+"youwon.png")
        image(img,50,50)
        
def mouseClicked():
    if deathlyhallows.game == "Continue":
        deathlyhallows.openGrid(mouseY//gridcol,mouseX//gridrow)
