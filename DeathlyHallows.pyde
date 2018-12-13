add_library('minim')
import os, random, time 
path=os.getcwd()
boardSize=50 #this changes the board size 
gridwidth=185
gridheight=142
player=Minim(this)
hallowVals = ['wand', 'stone', 'cloak']
profVals = ['snape','mcg','moody']
#harry, ghost, professor, hallows (-> character class)
#background assembly (-> background hidden/not hidden)

#don't get the same values for prof ghost and hallows
#lives and time clock 
#game win and lose conditions 
#lifecount

class Grid:
    def __init__(self,r,c,v,h):
        self.r=r
        self.c=c 
        self.v=v #value. empty by default, can be the name of one of the hallows OR 'ghost' or 'prof'
        self.h=h #hidden or revealed 
        self.caption = "" # for ghosts to store the text they need to show
        self.hintedAt = False # so that we don't accidentally give two hints about the same prof or hallow
        
    def display(self):
        #if hidden, show grid (background)
        #if clicked, show what's inside 
        if self.h == True:
            image(g.bgImg,self.c*100,self.r*100,100,100,self.c*100,self.r*100,self.c*100+100,self.r*100+100)
        else:
            # empty tile? show the same thing
            if self.v == 'empty':
                image(g.bgImg,self.c*100,self.r*100,100,100,self.c*100,self.r*100,self.c*100+100,self.r*100+100)
            elif self.v in ['wand', 'cloak', 'stone']:
                tileImg = loadImage(path + '/images/' + self.v + '.png')
                image(tileImg, self.c*100, self.r*100)
            elif self.v in ['snape','mcg','moody']:
                tileImg = loadImage(path + '/images/' + self.v + '.png')
                image(tileImg, self.c*100, self.r*100)
            elif self.v == 'ghost':
                tileImg = loadImage(path + '/images/' + self.v + '.png')
                image(tileImg, self.c*100, self.r*100)


                # write 
                

    
class Game:
    def __init__(self):
        
        self.numRows=7
        self.numCols=10
        self.grids=[]
        self.game="Continue"
        self.bgImg=loadImage(path+"/images/gamebackground.png")
        self.gsImg=loadImage(path+"/images/gamestart.png")
        self.gwImg=loadImage(path+"/images/youwon.jpg")
        self.glImg=loadImage(path+"/images/youlose.jpg")
        self.state="Start"
        self.lives = 3
        self.hallowsFound = 0
        self.captionToDraw = ""
        # self.music=player.loadFile(path+"/sounds/inside_bg.mp3")
        # self.music.play()
        
    def createboard(self):
        cnt=1
        for r in range(self.numRows):
            for c in range(self.numCols):
                self.grids.append(Grid(r,c,"empty",True))
                cnt+=1
                
        # #hiding three hallows,         
        hallows=0
        while hallows < 3:
            hallowrow=random.randint(1,self.numRows-1)
            hallowcol=random.randint(0,self.numCols-1)
            
            hallowgrid=self.getGrid(hallowrow,hallowcol)
            if hallowgrid.v not in hallowVals and hallowgrid.v == "empty":
                hallowgrid.v = hallowVals.pop()
                hallows += 1
                        
        #assign random grids with professors 
        profs = 0
        while profs < 3: 
            profrow=random.randint(1,self.numRows-1)
            profcol=random.randint(0,self.numCols-1)
            
            #assign random grids with professors 
            profgrid=self.getGrid(profrow,profcol)
            if profgrid.v == 'empty':
                profgrid.v = profVals.pop()
                profs += 1                
        
        #assign random grids with ghosts 
        ghosts=0
        while ghosts < 3:
            ghostrow=random.randint(1,self.numRows-1)
            ghostcol=random.randint(0,self.numCols-1)
            
            #assign random grids with ghosts 
            ghostgrid=self.getGrid(ghostrow,ghostcol)
            if ghostgrid.v == "empty":
                ghostgrid.v = "ghost"
                print("ghost at {}, {}".format(ghostrow, ghostcol))
                ghostgrid.caption = self.makeGhostCaption()
                # print(ghostgrid.caption)
                ghosts += 1 
                
    
    def displayBoard(self):
        if self.state == "Start":
            image(self.gsImg,0,0,1000,700)
            return
        
        else:
            for g in self.grids:
                g.display()
            self.drawHUD()
            if self.state == "Win":
                imageMode(CENTER)
                image(self.gwImg,500,350)
                imageMode(CORNER)
                
            elif self.state == "Lose":
                imageMode(CENTER)
                image(self.glImg,500,350)
                imageMode(CORNER)
        
        
    # creates a caption either about the position of a professor or the position of a hallow
    def makeGhostCaption(self):
        coinFlip = random.randint(1,2) # if 1, tell about prof, if 2 tell about hallow
        if coinFlip == 1:
            for g in self.grids:
                if g.v in ['snape','mcg','moody'] and g.hintedAt == False:
                    g.hintedAt = True
                    if g.r < 4:
                        hintLoc = "spying from among the candles!"
                    elif g.r == 4:
                        hintLoc = "in line with the staff table"
                    else:
                        hintLoc = "hiding among the students!"
                    return "I saw Professor {} {}".format(g.v, hintLoc)
        else:
            for g in self.grids:
                if g.v in ['wand', 'stone', 'cloak'] and g.hintedAt == False:
                    g.hintedAt = True
                    if g.r < 4:
                        hintLoc = "lost in the rafters!"
                    elif g.r == 4:
                        hintLoc = "at the far end of the hall"
                    else:
                        hintLoc = "lost among the students!"
                    return "Ahoy! There's a {} {}".format(g.v, hintLoc)

    def openGrid(self,r,c):
        openingGrid=self.getGrid(r,c)
        
        if openingGrid.h == True:
            if openingGrid.v in ['snape','mcg','moody']:
                self.lives -= 1 
            elif openingGrid.v in ['wand', 'stone', 'cloak']:
                self.hallowsFound += 1
            elif openingGrid.v == 'ghost':
                self.captionToDraw = openingGrid.caption
            openingGrid.h = False
            return
        
    def getGrid(self,r,c):
        for g in self.grids:
            if g.r==r and g.c==c:
                return g
        return None
    
    def checkWin(self):
        if self.lives == 0:
            g.state = "Lose"            
            
        elif self.hallowsFound == 3: 
            g.state = "Win" 
            
        
    
    def drawHUD(self):
        # draw the heads-up display in the top 1000 * 100 pixels
        if self.state == "Play":
            # draw game info
            fill(0)
            rect(720,0, 280, 100)
            fill(255)
            textSize(30)
            livesText = "Lives: " + str(self.lives)
            hallowText = "Hallows Found: " + str(self.hallowsFound)       
            text(livesText, 880,30)
            text(hallowText, 740, 70)
        
            # draw ghost hint if available
            if self.captionToDraw != "":
                fill(0)
                rect(0,0, 600,100)
                fill(255)
                textSize(20)
                fill(255)
                # print(self.captionToDraw)
                text(self.captionToDraw,30,60)
        
        
        
#character class (harry)
class Characters:
    def __init__(self,x,y,w,h,img):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.img=loadImage(path+"/images/"+img)
        self.dir=1
        
    
'''    
MOST URGENT: life, time, hallowcount 
background (game start button, instruction button)
        

How do we slice the image into smaller parts? -> al reem will work on slicing the picture 

1. set up the background to be hogwarts -> set up the game start, directions 
-> we need to have a character (harry with a broomstick -> wherever the mouse moves, harry moves as well) 

2. make sure if you click the game start, you move to the inside background = grand dining hall
-> set up the timer, and the life (three), count the deathly hallows (reach three, you win)

3. you click certain parts of the dining hall and if you click, the grid should reveal whatever it is hiding inside 
-> if it is an empty tile -> you lose 5 seconds of your time 
-> if it is a professor -> you lose 1 life 
-> if it is a deathly hallow -> you add to deathlyhallow.count 
-> if it is a ghost -> you are given a hint (as to where the hallows are) -> the hint is going to be like pop-up

4. winning/losing condition 
-> checkWin function -> if you collect hallows in time, without losing three lives, you win 
-> checkLose function (above checkwin condition) 
-> encounter professor three times -> you lose
-> when time is up -> you lose 

what we can do now: 
    get all the images (image slice, value, position, size)
    images include (hallows, professors(soundtrack), ghosts (soundtrack), harry)
    sounds for all of them 
    winning conditions, losing conditions, and i will try to make basic setup (randomly assign the hallows, professors, and the ghosts)
'''
g = Game()

#how to move harry according to mousemove 

moveX=0
moveY=0

def setup():
    size(1000,700)
    background(0)
    g.createboard()
    
def draw():
    
    background(0)
    textSize(30)
    fill(255)
    ellipse(moveX,moveY,33,33)
    g.displayBoard()
    g.checkWin()
    if g.state == "Start":
        text("Click anywhere to enter the castle",260,350)

def mouseClicked():
    # if deathlyhallows.game == "Continue":
    #     deathlyhallows.openGrid(mouseY//142,mouseX//185)
    
    if g.state == "Start":
        print("ssomething")
        g.state = "Play"
    if g.state == "Play":    
        # noFill()
        stroke(20)
        color(255)
        rect(mouseX//100*100,mouseY//100*100,100,100)
        
        g.openGrid(mouseY//100,mouseX//100)
        
        
        
        
def keyReleased():
    if key == 'w':
        g.state = "Win"
        print("win!")
        
    if key == 'l':
        g.state = "Lose"
        print("lose!")
    
def mouseMoved():
    moveX = mouseX
    moveY = mouseY
    
#winning and losing conditions 
#lives 
#click on the grid, you open it 
    
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
