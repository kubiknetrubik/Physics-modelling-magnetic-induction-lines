from tkinter import *
from math import *
from time import *
from tkinter import messagebox
root=Tk()
root.title("Зачетная работа")
root.geometry("1920x1080")
canv=Canvas(width=1920,height=1080,bg="white")
canv.pack()
canv.create_text(960,300,text="Зачетная работа по информатике",font="Verdana 40")
canv.create_text(960,360,text="тема 12 ",font="Verdana 35")
canv.create_text(960,420,text="Моделирование линий магниной индукции ",font="Verdana 35")
canv.create_text(960,480,text="Ученика 10'Г' ",font="Verdana 30")

canv.create_text(960,520,text="2023 года",font="Verdana 24")

canv.create_text(163,20,text="Для перехода нажмите ENTER",font="Verdana 15")
p=[]
R=15
nomerved=-1
schet=0
ccolour=""
cff=0
def linescolour(schet):
    global ccolour
    if schet==0:
        ccolour="blue"
    if schet==1:
        ccolour="green"
    if schet==2:
        ccolour="purple"
    if schet==3:
        ccolour="brown"
    if schet==4:
        ccolour="orange"
    if schet==5:
        ccolour="red"
    if schet==6:
        ccolour="blue"
        schet=0
    
def proverkanapustotixy(mes,e):
    x=mes.get()
    
    e.delete(0,END)
    e.insert(0,0)
def proverkanapustotiI(mes,e):
    x=mes.get()
    
    e.delete(0,END)
    e.insert(0,100)
def zadanie():
    print("OK")
    canv.delete("all")
    zadaniebutton.place(x=44450,y=190)
    demonbutton.place(x=444450,y=290)
    pomoshbutton.place(x=44450,y=390)
    canv.create_text(201,20,text="Для перехода в меню нажмите Escape",font="Verdana 15")
    canv.create_text(900,430,text="Тема 12",font="Verdana 40")
    canv.create_text(960,530,text="Составить программу, моделирующую построение линий магнитной индукции  поля,",font="Verdana 30")
    canv.create_text(960,580,text="создаваемого  тремя и более проводниками с током, расположенными параллельно.",font="Verdana 30")
    
def ochistkaotznach(p,nomer):
   canv.create_rectangle(1655,160+90*(nomer+1),1760,140+90*(nomer+1),fill="white",outline="white")
   canv.create_rectangle(1650,100+90*(nomer+1),1790,80+90*(nomer+1),fill="white",outline="white")
   canv.create_rectangle(1650,120+90*(nomer+1),1785,100+90*(nomer+1),fill="white",outline="white")
   canv.create_rectangle(1650,140+90*(nomer+1),1785,120+90*(nomer+1),fill="white",outline="white")
def pravstolbik(p,nomer):
   canv.create_rectangle(1655,160+90*nomer,1760,140+90*nomer,fill="white",outline="white")
   canv.create_rectangle(1650,100+90*nomer,1790,80+90*nomer,fill="white",outline="white")
   canv.create_rectangle(1650,120+90*nomer,1785,100+90*nomer,fill="white",outline="white")
   canv.create_rectangle(1650,140+90*nomer,1785,120+90*nomer,fill="white",outline="white")
   
   
   canv.create_text(1690,90+90*nomer,text="nomer=",font="Verdana 15")
   canv.create_text(1730,80+90*nomer,text=nomer+1,font="Verdana 15",anchor="nw")
   canv.create_text(1670,110+90*nomer,text="I=",font="Verdana 15")
   canv.create_text(1685,100+90*nomer,text=p[nomer].I,font="Verdana 15",anchor="nw")
   canv.create_text(1670,130+90*nomer,text="x=",font="Verdana 15")
   canv.create_text(1685,120+90*nomer,text=round((p[nomer].x-300)/30,1),font="Verdana 15",anchor="nw")
   canv.create_text(1670,150+90*nomer,text="y=",font="Verdana 15")
   canv.create_text(1685,140+90*nomer,text=round((p[nomer].y)/30,1),font="Verdana 15",anchor="nw")
def antidur(mes,e):
    global nomerved
    x=mes.get()
    if x.isdigit()and len(x)<5:
        if float(x)<=500:
            pass
        else:
            e.delete(0,END)
            e.insert(0,x[:-1])
    else:
##     if float(y)<44:
        e.delete(0,END)
        y=""
        for i in range(0,len(x)):
            
            if x[i].isdigit() or (x[i]=="." and y.count(".")==0 and  len(x)>1)or (x[i]=="-" and y.count("-")==0 and  len(x)>0):
              if len(y[(y.find(".")):-1])<=1:
                  if len(y)<5:
                
                    y+=x[i]
              else:
                  pass
        e.insert(0,y)
def antidur2(mes,e):
    global nomerved
    x=mes.get()
    if x.isdigit() and len(x)<4:
        if float(x)<=43:
            pass
        else:
            e.delete(0,END)
            e.insert(0,x[:-1])
    else:
##     print(x)


        e.delete(0,END)
        y=""
        for i in range(0,len(x)):
            
            if x[i].isdigit() or (x[i]=="." and y.count(".")==0 and  len(x)>1):
              if len(y[(y.find(".")):-1])<=1:
                if len(y)<4:
                  y+=x[i]
              else:
                  pass
        e.insert(0,y)


def vvodannix(e):
    
    global nomer,p
    print(nomer)
    
    antidur2(messagex,e1)
    antidur2(messagey,e2)
    antidur(messageI,e3)
    p[nomer].I=round(float(messageI.get()),1)
    if p[nomer].I<0:
       canv.itemconfig(p[nomer].figura,text="·")
    elif  p[nomer].I==0:
         canv.itemconfig(p[nomer].figura,text="?")
    else:
       canv.itemconfig(p[nomer].figura,text="x")
    if messagex.get()!="":
     p[nomer].x=round(30*float(messagex.get())+300,1)
    if messagey.get()!="":
     p[nomer].y=round(30*float(messagey.get()),1)
    canv.coords(p[nomer].picture,p[nomer].x-R,p[nomer].y-R,p[nomer].x+R,p[nomer].y+R)
    canv.coords(p[nomer].obvodka,p[nomer].x-R,p[nomer].y-R,p[nomer].x+R,p[nomer].y+R)
    for gh in range(0,len(p)):
        
     pravstolbik(p,gh)
def udalenie():
  print("udalenie")
  global nomer
  canv.delete(p[nomer].picture)
  canv.delete(p[nomer].figura)
  canv.delete(p[nomer].obvodka)
  for ggg in range(0,len(p)):
      
   canv.delete(p[ggg].nomervnutr)
  del p[nomer]
  ochistkaotznach(p,len(p)-1)
  print(len(p))
  for gx in range(0,len(p)):
   canv.create_rectangle(1655,160+90*gx,1760,140+90*gx,fill="white",outline="white")
   canv.create_rectangle(1650,100+90*gx,1790,80+90*gx,fill="white",outline="white")
   canv.create_rectangle(1650,120+90*gx,1785,100+90*gx,fill="white",outline="white")
   canv.create_rectangle(1650,140+90*gx,1785,120+90*gx,fill="white",outline="white")
   pravstolbik(p,gx)
   p[gx].vvestinomer(gx)
 
def postroy():
 print("OK")
 global p,schet
 print(len(p))
 root.unbind("<Button-1>")
 canv.create_rectangle(1480,950,1620,970,fill="white")
 cx=0
 udaleniebutton.config(state="disabled")
 postroybutton.config(state="disabled")
 udalenielinesbutton.config(state="disabled")
 ochisneniebutton.config(state="disabled")
 e1.config(state="disabled")
 e2.config(state="disabled")
 e3.config(state="disabled")
 linescolour(schet)
 for l in range(0,len(p)):
  cd=0
  for j in range(70,210,70):
##    if i==0:
##       if (p[i].x-p[i+1].x<150 or (p[i].x-p[i+1].x>-150 and p[i].x-p[i+1].x<0)):
##           
##         xn=p[i].x+130+1.3*j
##         yn=p[i].y+130+1.3*j
##       else:
##         xn=p[i].x+60+1.3*j
##         yn=p[i].y+60+1.3*j  
##    elif i==len(p)-1:
##        if (p[i].x-p[i-1].x<150 or (p[i].x-p[i-1].x>-150 and p[i].x-p[i-1].x<0)):
##           
##         xn=p[i].x+130+1.3*j
##         yn=p[i].y+130+1.3*j
##        else:
##         xn=p[i].x+80+1.3*j
##         yn=p[i].y+80+1.3*j
##    else:
##        if (p[i].x-p[i+1].x<150 or (p[i].x-p[i+1].x>-150 and p[i].x-p[i+1].x<0)):
##           
##         xn=p[i].x+130+1.3*j
##         yn=p[i].y+130+1.3*j
##        else:
##         xn=p[i].x+60+1.3*j
##         yn=p[i].y+60+1.3*j
    xn=p[l].x+140+1.5*j+cd*60+len(p)*20
    yn=p[l].y+140+1.5*j+cd*60+len(p)*20
    cx+=1
    cd+=1
##    print("i",l)
##    print("j",j)
##    print(cx)
##    canv.create_rectangle(1480,950,1480+(140/(len(p)*2))*cx,970,fill="green") 
##    canv.create_rectangle(1480,950,1480+(140/len(p))*(i+1),970,fill="green") 
##    xn=p[i].x+80+1.3*j
##    yn=p[i].y+80+1.3*j
    x=xn
    y=yn

    k=1.2
    c=0
## for i in range(0,len(p)):
##     dxx.append(0)
##     dyy.append(0)
 
    while True:
     xf=x
     yf=y
  
     for i in range(0,len(p)):
##    if cx<=len(p):
##     r=sqrt(((x-p[i].x)**2)+((y-p[i].y)**2))
##     
##     B=k*(p[i].I/r)
##     dx=B*((p[i].y-y)/r)
##     dy=B*((x-p[i].x)/r)
##     dxx.append(dx)
##     dyy.append(dy)
##     cx=cx+1
##    else:
      r=sqrt(((x-p[i].x)**2)+((y-p[i].y)**2))
      
      B=k*(p[i].I/r)
      
      
      xf+=B*((p[i].y-y)/r)
      yf+=B*((x-p[i].x)/r)
##  for i in range(0,len(dxx)):
##      xf=xf+dxx[i]
##      yf=yf+dyy[i]
     
     if (xf<300 or xf>1620) or yf<0 or yf>1080:
      pass
     else:
      
       canv.create_line(x,y,xf,yf,fill=ccolour)
      
     if c%1000==0:
         canv.update()
     x=xf
     y=yf
     c+=1
     if sqrt(((xn-x)**2)+((yn-y)**2))<70 and c >800:
        if x<300 or x>1620:
            pass
        else:
         canv.create_line(x,y,xn,yn,fill=ccolour)
        print(cx)
        break
     
     
     
    print(cx)
    canv.create_rectangle(1480,950,1480+(140/(len(p)*2))*cx,970,fill="green")
 udaleniebutton.config(state="normal")
 postroybutton.config(state="normal")
 udalenielinesbutton.config(state="normal")
 ochisneniebutton.config(state="normal")
 schet+=1
 e1.config(state="normal")
 e2.config(state="normal")
 e3.config(state="normal")    
 root.bind("<Button-1>",LKM)
def udalenielines():
 global p,schet
 
 canv.delete("all")

 schet=0
 print(len(p))
 canv.create_line(1620,0,1620,1080)
 canv.create_text(80,90,text="x=",font="Verdana 15")
 canv.create_text(80,140,text="y=",font="Verdana 15")
 canv.create_text(80,190,text="I=",font="Verdana 15")
 canv.create_text(150,700,text="Для перехода в меню нажмите \nEscape",font="Verdana 15")
 canv.create_text(100,750,text="Для автозаполнения \nF3",font="Verdana 15")
 for i in range(0,45):#lines gor graph
   canv.create_line(i*30+300,0,i*30+300,1080,width=1,fill="light grey")
   if i!=0:
    canv.create_text(i*30+300,15,text=i,font="Verdana 12")
 for i in range(0,37):
   canv.create_line(300,i*30,1620,i*30,width=1,fill="light grey")
   if i!=0:
    canv.create_text(315,i*30,text=i,font="Verdana 12")
 canv.create_line(300,0,300,1080,width=4,arrow=LAST)
 canv.create_line(300,3,1620,3,width=4,arrow=LAST)
 canv.create_rectangle(1480,950,1620,970)
 for i in range(0,len(p)):
##     canv.coords(p[i].picture,p[i].x-R,p[i].y-R,p[i].x+R,p[i].y+R)
     p[i].posleochishlines()
     pravstolbik(p,i)
 p[nomer].obvesti()
def ochisnenie():
 print("OK")
 canv.delete("all")
 global p,schet
 
 print(len(p))
 schet=0
 canv.create_line(1620,0,1620,1080)
 canv.create_text(80,90,text="x=",font="Verdana 15")
 canv.create_text(80,140,text="y=",font="Verdana 15")
 canv.create_text(80,190,text="I=",font="Verdana 15")
 canv.create_text(150,700,text="Для перехода в меню нажмите \nEscape",font="Verdana 15")
 canv.create_text(100,750,text="Для автозаполнения \nF3",font="Verdana 15")
 for i in range(0,45):#lines gor graph
   canv.create_line(i*30+300,0,i*30+300,1080,width=1,fill="light grey")
   if i!=0:
    canv.create_text(i*30+300,15,text=i,font="Verdana 12")
 for i in range(0,37):
   canv.create_line(300,i*30,1620,i*30,width=1,fill="light grey")
   if i!=0:
    canv.create_text(315,i*30,text=i,font="Verdana 12")
 canv.create_line(300,0,300,1080,width=4,arrow=LAST)
 canv.create_line(300,3,1620,3,width=4,arrow=LAST)
 canv.create_rectangle(1480,950,1620,970)
 print(len(p))
 while p!=[]:
     
  canv.delete(p[0].picture)
  canv.delete(p[0].obvodka)
  canv.delete(p[0].nomervnutr)
  del p[0]
 print(len(p))
 
def autozap(e):
 print("OK")
#переменные
 global p,nomer
 p.append(provodnik((10*30)+300,5.8*30))
 p.append(provodnik((15*30)+300,28*30))
 p.append(provodnik((40.3*30)+300,9.4*30))
 p[0].I=100
 p[1].I=100
 p[2].I=-100
 for gx2 in range(0,len(p)):
   canv.create_rectangle(1655,160+90*gx2,1760,140+90*gx2,fill="white",outline="white")
   canv.create_rectangle(1650,100+90*gx2,1790,80+90*gx2,fill="white",outline="white")
   canv.create_rectangle(1650,120+90*gx2,1785,100+90*gx2,fill="white",outline="white")
   canv.create_rectangle(1650,140+90*gx2,1785,120+90*gx2,fill="white",outline="white")
   pravstolbik(p,gx2)
   canv.delete(p[gx2].obvodka)
 canv.itemconfig(p[2].figura,text="·")
class provodnik:
##    I=100
    
    
        
    def __init__(self,x,y):
        global nomer
        self.x=x
        self.y=y
        self.I=I=100
        self.picture=canv.create_oval(x-R,y-R,x+R,y+R)
        self.obvodka=canv.create_oval(x-R,y-R,x+R,y+R,outline="purple",width=2)
        self.figura=canv.create_text(x,y-2,text="x",font="Verdana 22")
        
##        if I>0:
##         self.picture=canv.create_oval(x-R,y-R,x+R,y+R,fill="red")
##        elif I==0:
##            canv.itemconfig(self.picture,fill="green")
##        else:
##            canv.itemconfig(self.picture,fill="blue")
    def posleochishlines(self):
       
       
       if self.I<0:
          self.figura=canv.create_text(self.x,self.y-2,text="·",font="Verdana 22")
          self.picture=canv.create_oval(self.x-R,self.y-R,self.x+R,self.y+R)
       elif  self.I==0:
         self.figura=canv.create_text(self.x,self.y-2,text="?",font="Verdana 22")
         self.picture=canv.create_oval(self.x-R,self.y-R,self.x+R,self.y+R)
       else:
           self.figura=canv.create_text(self.x,self.y-2,text="x",font="Verdana 22")
           self.picture=canv.create_oval(self.x-R,self.y-R,self.x+R,self.y+R)
    def obvesti(self):
        self.obvodka=canv.create_oval(self.x-R,self.y-R,self.x+R,self.y+R,outline="purple",width=4)
    def vvestinomer(self,nomer1):
        self.nomervnutr=canv.create_text(self.x+19,self.y-12,text=nomer1+1,font="Verdana 15",fill="red")
def LKMmotion(e):
    global nomerved
    
    canv.coords(p[nomerved].picture,e.x-R,e.y-R,e.x+R,e.y+R)
    canv.coords(p[nomerved].figura,e.x,e.y-2)
    canv.coords(p[nomerved].nomervnutr,e.x+19,e.y-12)
    
    canv.coords(p[nomerved].obvodka,10000-R,10000-R,10000+R,10000+R)
   
def LKMdrop(e):
    global nomerved,nomer
    print(132)
    root.unbind("<Motion>")
    root.unbind("<ButtonRelease>")
    x,y=e.x,e.y
    f=0
    for i in range(0,len(p)):
        if(2*R)**2>(x-p[i].x)**2+(y-p[i].y)**2:
            f=i+1
    if f==0:
        p[nomerved].x=x
        p[nomerved].y=y
        print(x,y)
        canv.coords(p[nomerved].picture,e.x-R,e.y-R,e.x+R,e.y+R)
        canv.coords(p[nomerved].obvodka,e.x-R,e.y-R,e.x+R,e.y+R)
        canv.coords(p[nomerved].figura,e.x,e.y-2)
        canv.coords(p[nomerved].nomervnutr,e.x+19,e.y-12)
        nomerved=-1
        
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e1.insert(0,round((x-300)/30,1))
        e2.insert(0,round((y)/30,1))
        e3.insert(0,p[nomer].I)
        for ggh in range(0,len(p)):
          pravstolbik(p,ggh)   
        root.bind("<Button-1>",LKM)
    else:
        canv.coords(p[nomerved].picture,p[nomerved].x-R,p[nomerved].y-R,p[nomerved].x+R,p[nomerved].y+R)
        canv.coords(p[nomerved].obvodka,p[nomerved].x-R,p[nomerved].y-R,p[nomerved].x+R,p[nomerved].y+R)
        canv.coords(p[nomerved].figura,p[nomerved].x,p[nomerved].y-2)
        canv.coords(p[nomerved].nomervnutr,p[nomerved].x+19,p[nomerved].y-12)
        nomerved=-1
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e1.insert(0,round((p[nomer].x-300)/30,1))
        
        e2.insert(0,round((p[nomer].y)/30,1))
        e3.insert(0,p[nomer].I)
        for ggx in range(0,len(p)):
            pravstolbik(p,ggx) 
        root.bind("<Button-1>",LKM)

def LKM(e):
    x=e.x
    y=e.y
    f=0
    
    global nomerved,nomer
    e1.config(state="normal")
    e2.config(state="normal")
    e3.config(state="normal") 
    
    if 300<x<1620 and 0<y<1080:
     for i in range(0,len(p)):
        if(2*R)**2>(x-p[i].x)**2+(y-p[i].y)**2:
            f=i+1
     if f==0:
      if len(p)<5:
        p.append(provodnik(x,y))
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        
        e1.insert(0,round((x-300)/30,1))
        e2.insert(0,round((y)/30,1))
        e3.insert(0,p[nomerved].I)
        print("nomerve",nomerved)
      else:
          messagebox.showwarning("Внимание!","Уже много зарядов")
     else:
        nomerved=f-1
        
        root.unbind("<Button-1>")
        root.bind("<Motion>",LKMmotion)
        root.bind("<ButtonRelease>",LKMdrop)
    if p!=[]:
        for i in range(0,len(p)):
           if(R)**2>(x-p[i].x)**2+(y-p[i].y)**2:
               nomer=i
           else:
                pass
    else:
               nomer=0
    
    print(nomer)
    print(p[nomer].x,p[nomer].y)
    pravstolbik(p,nomer)
    for ghx in range(0,len(p)):
        canv.delete(p[ghx].obvodka)
    p[nomer].obvesti()
    if nomer==len(p)-1:
      try:
          canv.coords(p[nomer].nomervnutr,p[nomer].x+19,p[nomer].y-12)
          #canv.coords(p[nomer].nomervnutr,p[nomer].x-2,p[nomer].y-2)
      except:
          p[nomer].vvestinomer(nomer)
    
    
def demonstrat():
    global p,R,nomerved
    print("yes")
    canv.delete("all")
    zadaniebutton.place(x=44450,y=190)
    demonbutton.place(x=444450,y=290)
    pomoshbutton.place(x=44450,y=390)
    udaleniebutton.place(x=10,y=600)
    postroybutton.place(x=10,y=300)
    udalenielinesbutton.place(x=10,y=500)
    ochisneniebutton.place(x=10,y=400)

    e1.place(x=108,y=80,anchor="nw")
    proverkanapustotixy(messagex,e1)
    

    e2.place(x=108,y=130,anchor="nw")
    proverkanapustotixy(messagey,e2)
    

    e3.place(x=108,y=180,anchor="nw")
    proverkanapustotiI(messageI,e3)
    canv.create_line(1620,0,1620,1080)
    canv.create_text(80,90,text="x=",font="Verdana 15")
    canv.create_text(80,140,text="y=",font="Verdana 15")
    canv.create_text(80,190,text="I=",font="Verdana 15")
    canv.create_text(150,700,text="Для перехода в меню нажмите \nEscape",font="Verdana 15")
    canv.create_text(100,750,text="Для автозаполнения \nF3",font="Verdana 15")
    for i in range(0,45):#lines gor graph
      canv.create_line(i*30+300,0,i*30+300,1080,width=1,fill="light grey")
      if i!=0:
       canv.create_text(i*30+300,15,text=i,font="Verdana 12")
    for i in range(0,37):
      canv.create_line(300,i*30,1620,i*30,width=1,fill="light grey")
      if i!=0:
       canv.create_text(315,i*30,text=i,font="Verdana 12")
    canv.create_line(300,0,300,1080,width=4,arrow=LAST)
    canv.create_line(300,3,1620,3,width=4,arrow=LAST)
    canv.create_rectangle(1480,950,1620,970)
    if len(p)!=0:
        
     for i in range(0,len(p)):
##     canv.coords(p[i].picture,p[i].x-R,p[i].y-R,p[i].x+R,p[i].y+R)
      p[i].posleochishlines()
      pravstolbik(p,i)
    
    e1.config(state="disabled")
    e2.config(state="disabled")
    e3.config(state="disabled")
    root.bind("<Button-1>",LKM)
    root.bind("<F3>",autozap)#AUTOZAPOLNENIE
    root.bind("<KeyPress>",vvodannix)
def pomosh():
    print('pomosh')
    canv.delete("all")
    zadaniebutton.place(x=44450,y=190)
    demonbutton.place(x=444450,y=290)
    pomoshbutton.place(x=44450,y=390)
    canv.create_text(201,20,text="Для перехода в меню нажмите Escape",font="Verdana 15")
    canv.create_text(250,300,text="1)Для перехода из вкладок в меню надо нажать ESCAPE",font="Verdana 30",anchor="sw")
    canv.create_text(250,350,text="2)Для перехода с титульного листа в меню надо нажать кнопку //Построить//",font="Verdana 30",anchor="sw")
    canv.create_text(250,400,text="3)Для того,чтобы запустить построение, надо нажать ENTER",font="Verdana 30",anchor="sw")
    canv.create_text(250,450,text="4)Для того,чтобы перейти вo вкладку в меню,надо навести курсор",font="Verdana 30",anchor="sw")
    canv.create_text(250,500,text="на кнопку с нужным названием и нажать левой кнопкой мыши",font="Verdana 30",anchor="sw")
    canv.create_text(250,550,text="5)Для того,чтобы вбить значения в таблицу, используйте цифры с клавиатуры",font="Verdana 30",anchor="sw")
    canv.create_text(250,600,text="6)Для того,чтобы вбивать значения  в поля использовать цифры",font="Verdana 30",anchor="sw")
    canv.create_text(250,650,text="7)Для того,чтобы удалить проводник ,нажмите кнопку //Удалить проводник//",font="Verdana 30",anchor="sw")
    canv.create_text(250,700,text="8)Для того,чтобы удалить линии ,нажмите кнопку //Удалить линии//",font="Verdana 30",anchor="sw")
    canv.create_text(250,750,text="9)Для того,чтобы очистить экран,нажмите кнопку //Очистить// ",font="Verdana 30",anchor="sw")


zadaniebutton=Button(text="Задание",command=zadanie,width=40,height=2,font="Verdana 30")
zadaniebutton.pack()
zadaniebutton.place(x=44450,y=190)

demonbutton=Button(text="Демонстрация",command=demonstrat,width=40,height=2,font="Verdana 30")
demonbutton.pack()
demonbutton.place(x=444450,y=290)

pomoshbutton=Button(text="Помощь",command=pomosh,width=40,height=2,font="Verdana 30")
pomoshbutton.pack()
pomoshbutton.place(x=44450,y=390)

udaleniebutton=Button(text="Удалить проводник",command=udalenie,width=16,height=1,font="Verdana 20")
udaleniebutton.pack()
udaleniebutton.place(x=44450,y=190)

postroybutton=Button(text="Построить",command=postroy,width=16,height=1,font="Verdana 20")
postroybutton.pack()
postroybutton.place(x=44450,y=190)

udalenielinesbutton=Button(text="Удалить линии",command=udalenielines,width=16,height=1,font="Verdana 20")
udalenielinesbutton.pack()
udalenielinesbutton.place(x=44450,y=190)

ochisneniebutton=Button(text="Очистить",command=ochisnenie,width=16,height=1,font="Verdana 20")
ochisneniebutton.pack()
ochisneniebutton.place(x=44450,y=190)

messagex=StringVar()
e1=Entry(width=14,textvariable=messagex,font="Verdana 15")
e1.pack()
e1.place(x=102220,y=500,anchor="nw")

messagey=StringVar()
e2=Entry(width=14,textvariable=messagey,font="Verdana 15")
e2.pack()
e2.place(x=222200,y=200,anchor="nw")

messageI=StringVar()
e3=Entry(width=14,textvariable=messageI,font="Verdana 15")
e3.pack()
e3.place(x=122200,y=500,anchor="nw")

def perexodvmenu(e):
 canv.delete("all")
 root.unbind("<Return>")
 root.unbind("<Button-1>")

 canv.create_text(890,220,text="МЕНЮ",font="Verdana 40")
 
 zadaniebutton.place(x=430,y=310)
 
 
 demonbutton.place(x=430,y=510)

 
 pomoshbutton.place(x=430,y=710)
 
 e2.place(x=222200,y=200,anchor="nw")
 e3.place(x=122200,y=500,anchor="nw")
 e1.place(x=102220,y=500,anchor="nw")
 ochisneniebutton.place(x=44450,y=190)
 udalenielinesbutton.place(x=44450,y=190)
 postroybutton.place(x=44450,y=190)
 udaleniebutton.place(x=44450,y=190)
 canv.create_text(563,20,text="Для перехода вo вкладку меню, наведите курсор на кнопку с нужным названием и нажмите левой кнопкой мыши",font="Verdana 15")
 root.bind("<Escape>",perexodvmenu)




root.bind("<Return>",perexodvmenu)
root.mainloop()
