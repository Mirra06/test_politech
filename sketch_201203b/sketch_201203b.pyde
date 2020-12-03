x=320
y=320
c=1
e=0
def setup():
    size(640,640)
    
def draw():
    global x
    global y
    global c
    global e
    background(255,255,255)
    x=x+c
    y=y+e
    fill(136,222,221)
    ellipseMode(CENTER)
    ellipse(x,y,50,50)
    if(x==25):
        c=2
    elif(x==615):
        c=-2
    elif(y==25):
        e=2    
    elif(y==615):  
        e=-2  
