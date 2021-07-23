##貪吃蛇
# -*- coding: utf-8 -*-
import tkinter as tk 
# 使用Tkinter前需要先匯入
import tkinter.messagebox
import pickle
import random
import time

# 第1步，範例化object，建立視窗window
window = tk.Tk() 
# 第2步，給視窗的視覺化起名字
window.title('Greedy snake')
# 第3步，設定視窗的大小(長 * 寬)
# window.geometry('1004x504')  # 這裡的乘是小x

# 第5步，建立一個主frame，長在主window視窗上
frame = tk.Frame(window, bg = 'blue', bd = 2, relief = tk.FLAT)
frame.pack(side = 'left')
#當前框架被選中，意思是鍵盤觸發，只對這個框架有效
frame.focus_set()
Labellist = [] #存放所有方塊的label
Blocklist = [] #存放背景方塊的值 1：被佔用 0：空閒
Snakelist = [] #存放snake的座標
height = 15
width = 20
#snack前進方向
left = 0
right = 1
up = 2
down =3
pause = 0
start = 1
class App(tk.Frame):  
  def __init__(self,master):    
    self.window = master    
    tk.Frame.__init__(self)    
    master.bind('<Up>',self.Up)    
    master.bind('<Left>',self.Left)    
    master.bind('<Right>',self.Right)    
    master.bind('<Down>',self.Down)    
    master.bind('<p>',self.Pause)    
    master.bind('<s>',self.Start)    
    master.bind('<r>',self.Restart)    
    self.Init_snake() #初始化介面方法
    self.time = 1000    
    self.Onetime()          
  def Up(self, event):    
    if self.Istart:      
      self.direction = up  
  def Down(self, event):    
    if self.Istart:      
      self.direction = down  
  def Left(self, event):    
    if self.Istart:      
      self.direction = left  
  def Right(self, event):    
    if self.Istart:      
      self.direction = right
  def Init_snake(self):    
    del Labellist[:]    
    del Blocklist[:]    
    del Snakelist[:]        
    #初始化背景方塊    
    LabelRowList = []    
    BlockRowlist = []    
    c = r = 0    
    for k in range(width*height):      
      LN=tk.Label(frame,text = '  ', bg = 'black', fg = 'white', relief = tk.FLAT, bd = 4)      
      LN.grid(row=r,column=c,sticky=tk.N+tk.E+tk.S+tk.W)      
      LabelRowList.append(LN)      
      BlockRowlist.append(0)      
      c=c+1  
      if c>=20:
        r=r+1
        c=0        
        Labellist.append(LabelRowList)        
        Blocklist.append(BlockRowlist)        
        LabelRowList = []        
        BlockRowlist = []    
    #初始化snake    
    self.Istart = 0    
    self.direction = left
    self.direction_last = left
    self.overflag = 0  
    #snake head的初始位置    
    self.x = 7    
    self.y = 8    
    #snake tail的初始位置    
    self.x_tail = 7    
    self.y_tail = 10    
    Snakelist.append((7,8))    
    Snakelist.append((7,9))    
    Snakelist.append((7,10))    
    self.snakelen = len(Snakelist)


    Blocklist[self.x][self.y] = 1    
    Blocklist[self.x][self.y+1] = 1    
    Blocklist[self.x][self.y+2] = 1    
    Labellist[self.x][self.y].config(bg = 'green', relief = tk.RAISED)    
    Labellist[self.x][self.y+1].config(bg = 'white', relief = tk.RAISED)    
    Labellist[self.x][self.y+2].config(bg = 'white', relief = tk.RAISED)    
    #初始化food    
    self.food_x = random.randint(0,14)    
    self.food_y = random.randint(0,19)    
    while Blocklist[self.food_x][self.food_y] == 1:      
      self.food_x = random.randint(0,14)      
      self.food_y = random.randint(0,19)          
    Blocklist[self.food_x][self.food_y] = 1    
    Labellist[self.food_x][self.food_y].config(bg = 'red', relief = tk.RIDGE)
  def Pause(self, event):    
    self.Istart = pause  
  def Start(self, event):    
    self.Istart = start  
  def Restart(self, event):    
    self.Init_snake()
  def Onetime(self): #每1000ms做一次介面重新整理    
    if self.Istart and self.overflag == 0:  
      if (self.direction_last == down and self.direction == up )or(self.direction_last == up and self.direction == down )or(self.direction_last ==left and self.direction == right )or(self.direction_last ==right and self.direction == left ):
        self.direction = self.direction_last
      self.direction_last = self.direction 
      x0 = self.x      
      y0 = self.y      
      if self.direction == left:        
        if x0 == self.food_x and y0-1 == self.food_y:                    
          Labellist[x0][y0-1].config(bg = 'green', relief = tk.RAISED)          
          Labellist[x0][y0].config(bg = 'white', relief = tk.RAISED)
          self.food_x = random.randint(0,14)          
          self.food_y = random.randint(0,19)          
          while Blocklist[self.food_x][self.food_y] == 1:            
            self.food_x = random.randint(0,14)            
            self.food_y = random.randint(0,19)          
          Blocklist[self.food_x][self.food_y] = 1          
          Labellist[self.food_x][self.food_y].config(bg = 'red', relief = tk.RIDGE)
          self.snakelen += 1          
          Snakelist.insert(0,(x0,y0-1))           
          self.x = x0          
          self.y = y0 - 1        
        elif (x0>=0 and x0<height and y0-1>=0 and y0-1<width and Blocklist[x0][y0-1] == 0) or (self.x_tail == x0 and self.y_tail == y0 - 1):                              
          Blocklist[self.x_tail][self.y_tail] = 0          
          Labellist[self.x_tail][self.y_tail].config(bg = 'black', relief = tk.FLAT)          
          Blocklist[x0][y0-1] = 1          
          Labellist[x0][y0-1].config(bg = 'green', relief = tk.RAISED)          
          Labellist[x0][y0].config(bg = 'white', relief = tk.RAISED)                     
          del Snakelist[self.snakelen - 1]          
          Snakelist.insert(0,(x0,y0-1))           
          self.x = x0          
          self.y = y0 - 1          
          self.x_tail = Snakelist[self.snakelen - 1][0]          
          self.y_tail = Snakelist[self.snakelen - 1][1]        
        else:          
          tk.messagebox.showinfo(title = 'snake', message = 'game over!!!')          
          self.overflag = 1          
      elif self.direction == up:        
        if x0-1 == self.food_x and y0 == self.food_y:                     
          Labellist[x0-1][y0].config(bg = 'green', relief = tk.RAISED)          
          Labellist[x0][y0].config(bg = 'white', relief = tk.RAISED)
          self.food_x = random.randint(0,14)          
          self.food_y = random.randint(0,19)          
          while Blocklist[self.food_x][self.food_y] == 1:            
            self.food_x = random.randint(0,14)            
            self.food_y = random.randint(0,19)          
          Blocklist[self.food_x][self.food_y] = 1          
          Labellist[self.food_x][self.food_y].config(bg = 'red', relief = tk.RIDGE) 
          self.snakelen += 1          
          Snakelist.insert(0,(x0-1,y0))           
          self.x = x0 - 1          
          self.y = y0 
        elif (x0-1 >=0 and x0-1<height and y0>=0 and y0<width and Blocklist[x0-1][y0] == 0) or (self.x_tail == x0-1 and self.y_tail == y0):                    
          Blocklist[self.x_tail][self.y_tail] = 0          
          Labellist[self.x_tail][self.y_tail].config(bg = 'black', relief = tk.FLAT)          
          Blocklist[x0-1][y0] = 1          
          Labellist[x0-1][y0].config(bg = 'green', relief = tk.RAISED)          
          Labellist[x0][y0].config(bg = 'white', relief = tk.RAISED)
          del Snakelist[self.snakelen - 1]          
          Snakelist.insert(0,(x0 - 1,y0))           
          self.x = x0 - 1          
          self.y = y0          
          self.x_tail = Snakelist[self.snakelen - 1][0]          
          self.y_tail = Snakelist[self.snakelen - 1][1]        
        else:          
          tk.messagebox.showinfo(title = 'snake', message = 'game over!!!')          
          self.overflag = 1      
      elif self.direction == down:        
        if x0+1 == self.food_x and y0 == self.food_y:                    
          Labellist[x0+1][y0].config(bg = 'green', relief = tk.RAISED)          
          Labellist[x0][y0].config(bg = 'white', relief = tk.RAISED)
          self.food_x = random.randint(0,14)          
          self.food_y = random.randint(0,19)          
          while Blocklist[self.food_x][self.food_y] == 1:            
            self.food_x = random.randint(0,14)            
            self.food_y = random.randint(0,19)          
          Blocklist[self.food_x][self.food_y] = 1          
          Labellist[self.food_x][self.food_y].config(bg = 'red', relief = tk.RIDGE) 
          self.snakelen += 1          
          Snakelist.insert(0,(x0+1,y0))           
          self.x = x0 + 1          
          self.y = y0 
        elif (x0+1 >=0 and x0+1 <height and y0>=0 and y0<width and Blocklist[x0+1][y0] == 0) or (self.x_tail == x0+1 and self.y_tail == y0):                              
          Blocklist[self.x_tail][self.y_tail] = 0          
          Labellist[self.x_tail][self.y_tail].config(bg = 'black', relief = tk.FLAT)          
          Blocklist[x0+1][y0] = 1          
          Labellist[x0+1][y0].config(bg = 'green', relief = tk.RAISED)          
          Labellist[x0][y0].config(bg = 'white', relief = tk.RAISED) 
          del Snakelist[self.snakelen - 1]          
          Snakelist.insert(0,(x0 + 1,y0))           
          self.x = x0 + 1          
          self.y = y0          
          self.x_tail = Snakelist[self.snakelen - 1][0]          
          self.y_tail = Snakelist[self.snakelen - 1][1]        
        else:          
          tk.messagebox.showinfo(title = 'snake', message = 'game over!!!')          
          self.overflag = 1     
      elif self.direction == right:        
        if x0 == self.food_x and y0+1 == self.food_y:                    
          Labellist[x0][y0+1].config(bg = 'green', relief = tk.RAISED)          
          Labellist[x0][y0].config(bg = 'white', relief = tk.RAISED)
          self.food_x = random.randint(0,14)          
          self.food_y = random.randint(0,19)          
          while Blocklist[self.food_x][self.food_y] == 1:            
            self.food_x = random.randint(0,14)            
            self.food_y = random.randint(0,19)          
          Blocklist[self.food_x][self.food_y] = 1          
          Labellist[self.food_x][self.food_y].config(bg = 'red', relief = tk.RIDGE) 
          self.snakelen += 1          
          Snakelist.insert(0,(x0,y0 + 1))           
          self.x = x0          
          self.y = y0 + 1 
        elif (x0>=0 and x0<height and y0+1>=0 and y0+1<width and Blocklist[x0][y0+1] == 0) or (self.x_tail == x0 and self.y_tail == y0+1):                            
          Blocklist[self.x_tail][self.y_tail] = 0          
          Labellist[self.x_tail][self.y_tail].config(bg = 'black', relief = tk.FLAT)          
          Blocklist[x0][y0+1] = 1          
          Labellist[x0][y0+1].config(bg = 'green', relief = tk.RAISED)          
          Labellist[x0][y0].config(bg = 'white', relief = tk.RAISED)  
          del Snakelist[self.snakelen - 1]          
          Snakelist.insert(0,(x0,y0 + 1))           
          self.x = x0          
          self.y = y0 + 1          
          self.x_tail = Snakelist[self.snakelen - 1][0]          
          self.y_tail = Snakelist[self.snakelen - 1][1]        
        else:          
          tk.messagebox.showinfo(title = 'snake', message = 'game over!!!')          
          self.overflag = 1    
    self.after(self.time,self.Onetime)
def Start_Stop():  
  app.Istart = 1 - app.Istart 
def Restart():  
  app.Restart(0)  
#主選單
mainmenu = tk.Menu(window)
window['menu'] = mainmenu
#二級選單：game
gamemenu=tk.Menu(mainmenu)
mainmenu.add_cascade(label='遊戲',menu=gamemenu)
gamemenu.add_command(label = '開始/暫停',command=Start_Stop)
gamemenu.add_command(label = '重置',command=Restart)
gamemenu.add_command(label = '退出',command=window.quit)
app = App(window)    
window.mainloop()