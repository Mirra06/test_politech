import random

snake_x = list()
snake_y = list()
k=0
right_move=0
up_move=-1
snake_size=20

def setup():
    global score
    score=0
    global y_apple
    global x_apple
    global x_start
    global y_start
    size(650,650)
    x_start=320
    y_start=320
    global snake_size
    snake_count=7 
    global snake_x
    global snake_y
    background(131,94,57) 
    fill(86,180,113)
 
    eat=Food() 
    x_apple,y_apple=eat.food()
    fill(255,0,0)
    ellipseMode(CENTER)
    ellipse(x_apple,y_apple,10,10)

    apple=Snake()
    snake_x,snake_y = apple.snake_creation(x_start,y_start,snake_size,snake_count)
    fill(86,180,113)
    i=0
    while i<len(snake_x):
        rectMode(CENTER)
        rect(snake_x[i], snake_y[i], snake_size, snake_size)
        i=i+1
    return snake_x, snake_y, snake_size

def draw():
    global score
    global y_apple
    global x_apple
    global k
    global snake_x, snake_y, snake_size
    global right_move
    global up_move
    reptile=Snake()
    dinner=Food()
    k=k+1
    if (k%30==0):        
        background(131,94,57) 
        snake_x,snake_y = reptile.tail_turning(snake_x, snake_y)          
        snake_x[0]=snake_x[0]+right_move*snake_size
        snake_y[0]=snake_y[0]+up_move*snake_size
        fill(0,0,0)
        text1="score: "+str(score)
        textSize(20)
        text(text1,width-100,25)
        fill(255,0,0)
        ellipseMode(CENTER)
        ellipse(x_apple,y_apple,10,10)
        fill(86,180,113)
        i=0
        while i<len(snake_x):
            rectMode(CENTER)
            rect(snake_x[i], snake_y[i], snake_size, snake_size)
            i=i+1 
        reptile.death(snake_x,snake_y)

        
        eat=dinner.check_eaten(snake_x, x_apple, snake_y, y_apple, snake_size)
        if (eat==True):
            x_apple,y_apple=dinner.food()
            fill(255,0,0)
            ellipseMode(CENTER)
            ellipse(x_apple,y_apple,10,10)
            score=score+1
    right_move,up_move=reptile.key_Pressed()
                
            
class Snake: 
    def snake_creation(self,x_start,y_start,snake_size,snake_count):  
        snake_x=list()
        snake_y=list()
        i=0
        while i<snake_count:
            snake_x.append(x_start)
            snake_y.append(y_start+snake_size*i)
            i=i+1
        return snake_x, snake_y


    def tail_turning(self,snake_x, snake_y):  
        i=len(snake_x)-1
        while i>0:
            snake_x[i]=snake_x[i-1]
            snake_y[i]=snake_y[i-1]
            i=i-1
        return snake_x, snake_y
    
    
    def death(self,snake_x,snake_y):
        if (snake_x[0]<=0 or snake_y[0]<=0 or snake_x[0]>=height-20 or snake_y[0]>=width-20):
            noLoop()
            fill(255,3,11)
            textSize(50)
            text("game over!",height/2-125,width/2)
        i=0
        while i<(len(snake_x)-1):
            j=i+1
            while j<len(snake_x):
                if (snake_x[i]==snake_x[j] and snake_y[i]==snake_y[j]):
                    noLoop()
                    fill(255,3,11)
                    textSize(50)
                    text("game over!",height/2-125,width/2)
                j=j+1
            i=i+1
            
    def key_Pressed(self):    
        global right_move
        global up_move
        if ((keyPressed) and (keyCode==RIGHT)):
            right_move=1
            up_move=0
        elif ((keyPressed) and (keyCode==LEFT)):
            right_move=-1
            up_move=0
        elif ((keyPressed) and (keyCode==DOWN)):
            right_move=0
            up_move=1
        elif ((keyPressed) and (keyCode==UP)):
            right_move=0
            up_move=-1
        
        return right_move,up_move
class Food:
    def food(self):
        x = random.randrange(20,620,20)
        y = random.randrange(20,620,20)
        return x,y

    def check_eaten(self,snake_x, x_food, snake_y, y_food, snake_size):
        if (snake_x[0]==x_food and snake_y[0]==y_food):
            snake_x.append(snake_x[len(snake_x)-1])
            snake_y.append(snake_y[len(snake_y)-1]+snake_size)
            return True
        return False

    
     
    
    
