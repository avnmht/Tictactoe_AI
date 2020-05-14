import turtle
import random
import tkinter
E=[2,4,6,8]
O=[1,3,5,7,9]
Q=9
F11=True
G11=2
F12=True
G12=2
F13=True
G13=2
F21=True
G21=2
F22=True
G22=2
F23=True
G23=2
F31=True
G31=2
F32=True
G32=2
F33=True
G33=2

def finalwinner():
    
    if(G11==G12==G13==0 or G21==G22==G23==0 or G31==G32==G33==0  ):
        print('X is the winner !!!')
    elif(G11==G12==G13==1 or G21==G22==G23==1 or G31==G32==G33==1  ):
        print('O is the winner !!!')
    if(G11==G22==G33==0 or G31==G22==G13==0  ):
        print('X is the winner !!!')
    elif(G11==G22==G33==1 or G31==G22==G13==1 ):
        print('O is the winner !!!')
    if(G11==G21==G31==0 or G12==G22==G32==0 or G13==G23==G33==0 ):
        print('X is the winner !!!')
    elif(G11==G21==G31==1 or G12==G22==G32==1 or G13==G23==G33==1 ):
        print('O is the winner !!!')
    elif(Q==0):
        print('Tie')
        
        
    
    
def O11():
    global B10
    global F11
    global Q
    global G11
    global G12
    global G13
    global G21
    global G22
    global G23
    global G31
    global G32
    global G33
    if(F11==True):
        
        tut.speed(0)
        tut.up()
        tut.goto(22,40)
        tut.down()
        i=0
        while i<=25:
            
             tut.forward(4)
             tut.right(15)
             i+=1
        tut.up()
        tut.goto(0,50)
        tut.setheading(0)
        tut.down()
        F11=False
        G11=1
        Q-=1
        
        
        
        main()
        
        finalwinner()
    else:
        print('you cant play this...')
def O12():
    
    global F12
    global G11
    global G12
    global G13
    global G21
    global G22
    global G23
    global G31
    global G32
    global G33
    global Q
    if(F12==True):
        tut.up()
        tut.speed(0)
        tut.goto(72,40)
        tut.down()
        i=0
        while i<=25:
            
             tut.forward(4)
             tut.right(15)
             i+=1
        tut.up()
        tut.goto(0,50)
        tut.setheading(0)
        tut.down()
        F12=False
        G12=1
        Q-=1

        finalwinner()
        main()
    else:
        print('you cant play this...')
    
def O13():
    global G11
    global G12
    global G13
    global G21
    global G22
    global G23
    global G31
    global G32
    global G33
    global F13
    global Q
    if(F13==True):
        tut.up()
        tut.speed(0)
        tut.goto(122,40)
        tut.down()
        i=0
        while i<=25:
            
             tut.forward(4)
             tut.right(15)
             i+=1
        tut.up()
        tut.goto(0,50)
        tut.setheading(0)
        tut.down()
        F13=False
        G13=1
        Q-=1
        finalwinner()
        main()
    else:
        print('you cant play this...')
def O21():
    global Q
    global G11
    global G12
    global G13
    global G21
    global G22
    global G23
    global G31
    global G32
    global G33
    global F21
    if(F21==True):
        tut.speed(0)
        tut.up()
        tut.goto(22,-10)
        tut.down()
        i=0
        while i<=25:
            
             tut.forward(4)
             tut.right(15)
             i+=1
        tut.up()
        tut.goto(0,50)
        tut.setheading(0)
        tut.down()
        F21=False
        G21=1
        Q-=1
        finalwinner()
        main()
    else:
        print('you cant play this...')
def O22():
    global Q
    global G11
    global G12
    global G13
    global G21
    global G22
    global G23
    global G31
    global G32
    global G33
    global F22
    if(F22==True):
        tut.up()
        tut.speed(0)
        tut.goto(72,-10)
        tut.down()
        i=0
        while i<=25:
            
             tut.forward(4)
             tut.right(15)
             i+=1
        tut.up()
        tut.goto(0,50)
        tut.setheading(0)
        tut.down()
        F22=False
        G22=1
        Q-=1
        finalwinner()
        main()
    else:
        print('you cant play this...')
def O23():
    global F23
    global Q
    global G11
    global G12
    global G13
    global G21
    global G22
    global G23
    global G31
    global G32
    global G33
    if(F23==True):
        tut.up()
        tut.speed(0)
        tut.goto(122,-10)
        tut.down()
        i=0
        while i<=25:
            
             tut.forward(4)
             tut.right(15)
             i+=1
        tut.up()
        tut.goto(0,50)
        tut.setheading(0)
        tut.down()
        F23=False
        G23=1
        Q-=1
        finalwinner()
        main()
    else:
        print('you cant play this...')
def O31():
    global F31
    global G11
    global G12
    global G13
    global G21
    global G22
    global G23
    global G31
    global G32
    global G33
    global Q
    if(F31==True):
        tut.speed(0)
        tut.up()
        tut.goto(22,-60)
        tut.down()
        i=0
        while i<=25:
            
             tut.forward(4)
             tut.right(15)
             i+=1
        tut.up()
        tut.goto(0,50)
        tut.setheading(0)
        tut.down()
        F31=False
        G31=1
        Q-=1
        finalwinner()
        main()
    else:
        print('you cant play this...')
def O32():
    global G11
    global G12
    global G13
    global G21
    global G22
    global G23
    global G31
    global G32
    global G33
    global F32
    global Q
    if(F32==True):
        tut.up()
        tut.speed(0)
        tut.goto(72,-60)
        tut.down()
        i=0
        while i<=25:
            
             tut.forward(4)
             tut.right(15)
             i+=1
        tut.up()
        tut.goto(0,50)
        tut.setheading(0)
        tut.down()
        F32=False
        G32=1
        Q-=1
        finalwinner()
        main()
    else:
        print('you cant play this...')
    
def O33():
    global G11
    global G12
    global G13
    global G21
    global G22
    global G23
    global G31
    global G32
    global G33
    global F33
    global Q
    if(F33==True):
        tut.up()
        tut.speed(0)
        tut.goto(122,-60)
        tut.down()
        i=0
        while i<=25:
            
             tut.forward(4)
             tut.right(15)
             i+=1
        tut.up()
        tut.goto(0,50)
        tut.setheading(0)
        tut.down()
        F33=False
        G33=1
        Q-=1
        finalwinner()
        main()
    else:
        print('you cant play this...')


def X11 ():
    global Q
    global G11
    global G12
    global G13
    global G21
    global G22
    global G23
    global G31
    global G32
    global G33
    global F11
    if(F11==True):
        
        tut.speed(0)
        tut.up()
        tut.setposition(x=25,y=25)
        tut.down()
        tut.left(45)
        tut.forward(20)
        tut.backward(40)
        tut.forward(20)
        tut.left(90)
        tut.forward(20)
        tut.backward(40)
        tut.right(135)
        tut.up()
        tut.goto(x=0,y=50)
        tut.down()
        F11=False
        G11=0
        Q-=1
        finalwinner()
        main()
    else:
        
        print('you cant play this...')
def X12 ():
    global Q
    global G11
    global G12
    global G13
    global G21
    global G22
    global G23
    global G31
    global G32
    global G33
    global F12
    if(F12==True):
        tut.up()
        tut.speed(0)
        tut.setposition(x=75,y=25)
        tut.down()
        tut.left(45)
        tut.forward(20)
        tut.backward(40)
        tut.forward(20)
        tut.left(90)
        tut.forward(20)
        tut.backward(40)
        tut.right(135)
        tut.up()
        tut.goto(x=0,y=50)
        tut.down()
        F12=False
        G12=0
        Q-=1
        finalwinner()
        main()
    else:
        print('you cant play this...')
def X13 ():
    global Q
    global F13
    global G11
    global G12
    global G13
    global G21
    global G22
    global G23
    global G31
    global G32
    global G33
    if(F13==True):
        tut.speed(0)
        tut.up()
        tut.setposition(x=125,y=25)
        tut.down()
        tut.left(45)
        tut.forward(20)
        tut.backward(40)
        tut.forward(20)
        tut.left(90)
        tut.forward(20)
        tut.backward(40)
        tut.right(135)
        tut.up()
        tut.goto(x=0,y=50)
        tut.down()
        F13=False
        G13=0
        Q-=1
        finalwinner()
        main()
    else:
        
        print('you cant play this...')
def X21 ():
    global Q
    global F21
    global G11
    global G12
    global G13
    global G21
    global G22
    global G23
    global G31
    global G32
    global G33
    if(F21==True):
        tut.up()
        tut.speed(0)
        tut.setposition(x=25,y=-25)
        tut.down()
        tut.left(45)
        tut.forward(20)
        tut.backward(40)
        tut.forward(20)
        tut.left(90)
        tut.forward(20)
        tut.backward(40)
        tut.right(135)
        tut.up()
        tut.goto(x=0,y=50)
        tut.down()
        F21=False
        G21=0
        Q-=1
        finalwinner()
        main()
    else:
        print('you cant play this...')
def X22 ():
    global Q
    global G11
    global G12
    global G13
    global G21
    global G22
    global G23
    global G31
    global G32
    global G33
    global F22
    if(F22==True):
        tut.speed(0)
        tut.up()
        tut.setposition(x=75,y=-25)
        tut.down()
        tut.left(45)
        tut.forward(20)
        tut.backward(40)
        tut.forward(20)
        tut.left(90)
        tut.forward(20)
        tut.backward(40)
        tut.right(135)
        tut.up()
        tut.goto(x=0,y=50)
        tut.down()
        F22=False
        G22=0
        Q-=1
        finalwinner()
        main()
    else:
        print('you cant play this...')
def X23 ():
    global Q
    global G11
    global G12
    global G13
    global G21
    global G22
    global G23
    global G31
    global G32
    global G33
    global F23
    if(F23==True):
        tut.up()
        tut.speed(0)
        tut.setposition(x=125,y=-25)
        tut.down()
        tut.left(45)
        tut.forward(20)
        tut.backward(40)
        tut.forward(20)
        tut.left(90)
        tut.forward(20)
        tut.backward(40)
        tut.right(135)
        tut.up()
        tut.goto(x=0,y=50)
        tut.down()
        F23=False
        G23=0
        Q-=1
        finalwinner()
        main()
    else:
        print('you cant play this...')
    
def X31 ():
    global Q
    global G11
    global G12
    global G13
    global G21
    global G22
    global G23
    global G31
    global G32
    global G33
    global F31
    if(F31==True):
        tut.up()
        tut.speed(0)
        tut.setposition(x=25,y=-75)
        tut.down()
        tut.left(45)
        tut.forward(20)
        tut.backward(40)
        tut.forward(20)
        tut.left(90)
        tut.forward(20)
        tut.backward(40)
        tut.right(135)
        tut.up()
        tut.goto(x=0,y=50)
        tut.down()
        F31=False
        G31=0
        Q-=1
        finalwinner()
        main()
    else:
        print('you cant play this...')

def X32 ():
    global F32
    global G11
    global G12
    global G13
    global G21
    global G22
    global G23
    global G31
    global G32
    global G33
    global Q
    if(F32==True):
        tut.speed(0)
        tut.up()
        tut.setposition(x=75,y=-75)
        tut.down()
        tut.left(45)
        tut.forward(20)
        tut.backward(40)
        tut.forward(20)
        tut.left(90)
        tut.forward(20)
        tut.backward(40)
        tut.right(135)
        tut.up()
        tut.goto(x=0,y=50)
        tut.down()
        F32=False
        G32=0
        finalwinner()
        
        Q-=1
        main()
    else:
        print('you cant play this...')
def X33 ():
    global Q
    global G11
    global G12
    global G13
    global G21
    global G22
    global G23
    global G31
    global G32
    global G33
    global F33
    if(F33==True):
        tut.up()
        tut.speed(0)
        tut.setposition(x=125,y=-75)
        tut.down()
        tut.left(45)
        tut.forward(20)
        tut.backward(40)
        tut.forward(20)
        tut.left(90)
        tut.forward(20)
        tut.backward(40)
        tut.right(135)
        tut.up()
        tut.goto(x=0,y=50)
        tut.down()
        F33=False
        G33=0
        Q-=1
        finalwinner()
        main()
    else:
        print('you cant play this...')




top=tkinter.Tk()
tut=turtle.Turtle()
tut.speed(0)
tut.width(6)
tut.forward(150)
tut.left(90)
tut.forward(50)
tut.left(90)
tut.forward(150)
tut.left(90)
tut.forward(150)
tut.left(90)
tut.forward(150)
tut.left(90)
tut.forward(50)
tut.left(90)
tut.forward(150)
tut.backward(150)
tut.right(90)
tut.forward(100)
tut.left(90)
tut.forward(50)
tut.left(90)
tut.forward(150)
tut.right(90)
tut.forward(50)
tut.right(90)
tut.forward(150)
tut.backward(25)
tut.up()
tut.left(90)
tut.forward(50)
tut.right(90)
tut.forward(25)
tut.right(90)
tut.down()
tut.position()

def main():
    
    
    if(Q in E):
        L1=tkinter.Label(top,text='X turn')
        L1.place(x=20,y=200)
        
        B1=tkinter.Button(top,text='(1,1)',command=X11)
        B1.grid(row=1,column=1)
        B2=tkinter.Button(top,text='(1,2)',command=X12)
        B2.grid(row=1,column=2)
        B3=tkinter.Button(top,text='(1,3)',command=X13)
        B3.grid(row=1,column=3)
        B4=tkinter.Button(top,text='(2,1)',command=X21)
        B4.grid(row=2,column=1)
        B5=tkinter.Button(top,text='(2,2)',command=X22)
        B5.grid(row=2,column=2)
        B6=tkinter.Button(top,text='(2,3)',command=X23)
        B6.grid(row=2,column=3)
        B7=tkinter.Button(top,text='(3,1)',command=X31)
        B7.grid(row=3,column=1)
        B8=tkinter.Button(top,text='(3,2)',command=X32)
        B8.grid(row=3,column=2)
        B9=tkinter.Button(top,text='(3,3)',command=X33)
        B9.grid(row=3,column=3)
    elif(Q in O):
        global B45
        B45.destroy()
        if(Q==9):
            O11()
        if(Q==7):
            if((G12==0) or(G21==0) or(G23==0)or(G31==0)or(G32==0)or(G33==0)):
                O13()
            elif(G13==0):
                O31()
            elif(G22==0):
                O33()
            
        if(Q==5):
            if((G21==0)or(G31==0)or(G32==0)):
                O33()
            elif((G23==0)or (G33==0)or (G22==0)):
                O31()
            elif((G22==0)and(G21==0)):
                O23()
            elif((G22==0)and(G23==0)):
                O21()
            elif((G22==0)and(G31==0)):
                O13()
            elif((G22==0)and(G13==0)):
                O31()
            elif((G22==0)and(G12==0)):
                O32()
            elif((G22==0)and(G32==0)):
                O12()
            
                
        if(Q==3):
            if((G22==0)and(G23==0)):
                O21()
            elif((G23==0)and(G21==0)):
                O22()
            if(((G23==0) and(G32==0)) or((G22==0) and(G33==0))):
                O21()
            elif((G32==0) and((G21==0)or(G22==0))):
                O23()
            elif((G32==0)and(G23==0)):
                O22()
            elif((G23==0) and(G33==0)):
                O21()
            
        
                
            
            
            
                
            


B45=tkinter.Button(top,text='Start',command=main)
B45.place(x=100,y=50)
