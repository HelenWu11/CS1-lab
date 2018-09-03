import check1

import datetime
class solution(object):
  def __init__(self,board):
    self.b = board
    self.t = 0
    for i1 in range(len(board)):
      items=board[i1]
      for i2 in range(len(items)):
        if board[i1][i2]=='.':
          board[i1][i2]=0
        else:
          board[i1][i2]=(int(board[i1][i2]))    
 
  def check(self,x,y,value):#���ÿ��ÿ�м�ÿ���Ƿ�����ͬ��
    for row_item in self.b[x]:
      if row_item == value:
        return False
    for row_all in self.b:
      if row_all[y] == value:
        return False
    row,col=x//3*3,y//3*3
    row3col3=self.b[row][col:col+3]+self.b[row+1][col:col+3]+self.b[row+2][col:col+3]
    for row3col3_item in row3col3:
      if row3col3_item == value:
        return False
    return True
 
  def get_next(self,x,y):#�õ���һ��δ����
    for next_soulu in range(y+1,9):
      if self.b[x][next_soulu] == 0:
        return x,next_soulu
    for row_n in range(x+1,9):
      for col_n in range(0,9):
        if self.b[row_n][col_n] == 0:
          return row_n,col_n
    return -1,-1 #������һ��δ�������-1

  def try_it(self,x,y):#��ѭ��
    if self.b[x][y] == 0:
      for i in range(1,10):#��1��9����
        self.t+=1
        if self.check(x,y,i):#���� ���й��������� ��
          self.b[x][y]=i #����������������0��
          next_x,next_y=self.get_next(x,y)#�õ���һ��0��
          if next_x == -1: #�������һ��0��
            return True #����True
          else:    #�������һ��0�񣬵ݹ��ж���һ��0��ֱ����������
            end=self.try_it(next_x,next_y)
            if not end:  #�ڵݹ�����д��ڲ����������ģ��� ʹtry_it��������None����
              self.b[x][y] = 0  #��˷����һ�����
            else:
              return True
            
  def try_it(self,x,y):
    if self.b[x][y]!=0:
      return False
    for i in range(1,10):
      self.t+=1
      if not self.check(x,y,i):
        continue
      self.b[x][y]=i
      x_next,y_next=self.get_next(x,y)
      if x_next==-1:
        return True
      if not self.try_it(x_next,y_next):
        continue
      return True
    self.b[x][y]=0
    return False
 
  def start(self):
    begin = datetime.datetime.now()
    if self.b[0][0] == 0:
      self.try_it(0,0)
    else:
      x,y=self.get_next(0,0)
      self.try_it(x,y)
    for i in self.b:
      print (i)
    end = datetime.datetime.now()
    print ('\ncost time:', end - begin)
    print ('times:',self.t)
    return
 
if __name__=='__main__':
  s=solution(check1.bd)
  s.start()

'''import datetime
class solution(object):
  def __init__(self,board):
    self.b = board
    self.t = 0
    for i1 in range(len(board)):
      items=board[i1]
      for i2 in range(len(items)):
        if board[i1][i2]=='.':
          board[i1][i2]=0
        else:
          board[i1][i2]=(int(board[i1][i2]))    
 
  def check(self,x,y,value):#���ÿ��ÿ�м�ÿ���Ƿ�����ͬ��
    for row_item in self.b[x]:
      if row_item == value:
        return False
    for row_all in self.b:
      if row_all[y] == value:
        return False
    row,col=x//3*3,y//3*3
    row3col3=self.b[row][col:col+3]+self.b[row+1][col:col+3]+self.b[row+2][col:col+3]
    for row3col3_item in row3col3:
      if row3col3_item == value:
        return False
    return True
 
  def get_next(self,x,y):#�õ���һ��δ����
    for next_soulu in range(y+1,9):
      if self.b[x][next_soulu] == 0:
        return x,next_soulu
    for row_n in range(x+1,9):
      for col_n in range(0,9):
        if self.b[row_n][col_n] == 0:
          return row_n,col_n
    return -1,-1 #������һ��δ�������-1

  def try_it(self,x,y):#��ѭ��
    if self.b[x][y] == 0:
      for i in range(1,10):#��1��9����
        self.t+=1
        if self.check(x,y,i):#���� ���й��������� ��
          self.b[x][y]=i #����������������0��
          next_x,next_y=self.get_next(x,y)#�õ���һ��0��
          if next_x == -1: #�������һ��0��
            return True #����True
          else:    #�������һ��0�񣬵ݹ��ж���һ��0��ֱ����������
            end=self.try_it(next_x,next_y)
            if not end:  #�ڵݹ�����д��ڲ����������ģ��� ʹtry_it��������None����
              self.b[x][y] = 0  #��˷����һ�����
            else:
              return True
            
  def try_it(self,x,y):
    if self.b[x][y]!=0:
      return False
    for i in range(1,10):
      self.t+=1
      if not self.check(x,y,i):
        continue
      self.b[x][y]=i
      x_next,y_next=self.get_next(x,y)
      if x_next==-1:
        return True
      if not self.try_it(x_next,y_next):
        continue
      return True
    self.b[x][y]=0
    return False
 
  def start(self):
    begin = datetime.datetime.now()
    if self.b[0][0] == 0:
    '''