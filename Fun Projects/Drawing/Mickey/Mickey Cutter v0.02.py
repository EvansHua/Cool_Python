# Mickey Cutter
# By Evans.
# Last modified on Oct 29, 2017.
# Changes:
#20171029 set start point parameters x and y.
def mickey(x,y):
    import turtle, time
    from datetime import datetime
    t=turtle
    dt=datetime
    t.penup()
    t.home()
    t.goto(x,y)
    #t.clear()
    t.shape("arrow")
    t.pendown()
    t.circle(100) #draw face (0,0) r=100
    t.penup()
    t.goto(x-100,y+120)
    t.pendown()
    t.circle(50) #draw left ear (-100,120) r=50
    t.penup()
    t.goto(x+100,y+120)
    t.pendown()
    t.circle(50) #draw right ear (100,120) r=50
    #draw left eye (-20,120) shapesize(4,1.5,1)
    t.penup()
    t.shape("circle")
    t.shapesize(4,1.5,1)
    t.fillcolor("white")
    t.goto(x-20,y+120)
    t.stamp()
    #draw right eye (20,120) shapesize(4,1.5,1)
    t.goto(x+20,y+120)
    t.stamp()
    #draw left eye ball (-16,100) shapesize(1.5,0.5,1)
    t.fillcolor("black")
    t.shapesize(1.5,0.5,1)
    t.goto(x-16,y+100)
    t.stamp()
    #draw right eye ball (16,100) shapesize(1.5,0.5,1)
    t.goto(x+16,y+100)
    t.stamp()
    #draw nose (0,70) shapesize(0.8,1.5,1)
    t.goto(x+0,y+70)
    t.shapesize(0.8,1.5,1)
    t.stamp()
    #draw mouth (-40,50) SE circle(60,90)
    t.shape('arrow')
    t.goto(x-40,y+50)
    t.right(45)
    t.pendown()
    t.circle(60,90)
    #reset turtle
    t.penup()
    t.left(45)
    t.goto(x+0,y-20)
    #write label and timestamp
    t.write('By Evans: '+dt.now().strftime("%d%B%Y %I:%M:%S %p"),True,align='center')
    
