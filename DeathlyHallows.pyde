add_library('minim')
import os, random, time 
path=os.getcwd()
boardSize=50 #this changes the board size 
gridwidth=185
gridheight=142
player=Minim(this)
#harry, ghost, professor, hallows (-> character class)
#background assembly (-> background hidden/not hidden)
#lives and time clock 

class Grid:
    def __init__(self,r,c,v,h):
        self.r=r
        self.c=c 
        self.v=v #value
        self.h=h #hidden or revealed 
        self.img=loadImage(path+"/images/"+str(v)+".png")
        
    def display(self):
        #if hidden, show grid (background)
        #if clicked, show what's inside 
        if self.h == True:
            for v in range(36):
                img=loadImage(path+"/images/"+str(v)+".png")
                image(img,self.c*142,self.r*185)            
        else:
            img=loadImage(path+"/images/"+str(v)+".png")
            image(img,self.c*142,self.r*185)
            
class Game:
    def __init__(self):
        self.numRows=7
        self.numCols=5
        self.grids=[]
        self.game="Continue"
        # self.music=player.loadFile(path+"/sounds/inside_bg.mp3")
        # self.music.play()
        
    def createboard(self):
        cnt=0
        for r in range(self.numRows):
            for c in range(self.numCols):
                self.grids.append(Grid(r,c,cnt,True))
                cnt+=1
                
        #hiding three hallows,         
        hallows=0
        while hallows < 3:
            hallowrow=random.randint(0,self.r-1)
            hallowcol=random.randint(0,self.c-1)
            
            #assign random grids with hallows 
            hallowgrid=self.getGrid(hallowrow,hallowcol)
            if hallowgrid.v != "40" or "41" or "42":
                hallowgrid.v = random.choice("40","41","42")
                
                hallows += 1
            
        #assign random grids with ghosts 
        ghosts=0
        while ghosts < 3:
            ghostrow=random.randint(0,self.r-1)
            ghostcol=random.randint(0,self.c-1)
            
            #assign random grids with ghosts 
            ghostgrid=self.getGrid(ghostrow,ghostcol)
            for i in range(4):
                if ghostgrid.v != "36":
                    ghostgrid.v = "36"
                    
                    ghosts+=1
            
        #assign random grids with professors 
        professors = 0
        while professors < 3: 
            professorrow=random.randint(0,self.r-1)
            professorcol=random.randint(0,self.c-1)
            
            #assign random grids with professors 
            professorgrid=self.getGrid(professorrow,professorcol)
            if professorgrid.v != "37" or "38" or "39":
                professorgrid.v = random.choice("37","38","39")
                
                professors += 1
        
            
    def getGrid(self,r,c):
        for g in self.grids:
            if g.r==r and g.c==c:
                return g         
        return None 
    
    def checkWin(self):
        False 
    
        

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
    
g = Game()

def setup():
    size(1295,710)
    background(0)
    
def draw():
    background(0)

def mouseClicked():
    if deathlyhallows.game == "Continue":
        deathlyhallows.openGrid(mouseY//142,mouseX//185)
    
    
    # if deathlyhallows.game == "Lose":
    #     img=loadImage(path+"/images/"+"youlost.png")
    #     image(img,50,50)
        
    # elif deathlyhallows.game == "Continue":
    #     deathlyhallows.displayboard() 
        
    # elif deathlyhallows.game == "Win":
    #     img=loadImage(path+"/images/"+"youwon.png")
    #     image(img,50,50)
        
# def mouseClicked():
#     if deathlyhallows.game == "Continue":
#         deathlyhallows.openGrid(mouseY//gridwidth,mouseX//gridheight)
