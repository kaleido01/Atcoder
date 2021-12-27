#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase


def main():

  h, w, n, m = map(int, input().split())


  # 0 は道 -1 は障害物 1はlightがあることを示す
  maze = []
  for _ in range(h):
    maze.append([0] * w)

  lightCount = 0
  for i in range(n):
    y, x = map(int, input().split())
    x -= 1
    y -= 1
    # print(x,y)
    maze[y][x] = 1
    lightCount += 1
    

  for i in range(m):
    y, x = map(int, input().split())
    x -= 1
    y -= 1
    
    maze[y][x] = -1



  # tate up

  for i in range(w):
    flag = False
    for j in range(h-1, -1, -1):
      if maze[j][i] == 1:
        flag = True
      if maze[j][i] == -1:
        flag = False
      if flag and maze[j][i] == 0:
        lightCount += 1
        maze[j][i] = 10
      

  # tate down

  for i in range(w):
    flag = False
    for j in range(h):
      if maze[j][i] == 1:
        flag = True
      if maze[j][i] == -1:
        flag = False
      if flag and maze[j][i] == 0:
        lightCount += 1
        maze[j][i] = 10

  # yoko left

  for i in range(h):
    flag = False
    for j in range(w):
      if maze[i][j] == 1:
        flag = True
      if maze[i][j] == -1:
        flag = False
      if flag and maze[i][j] == 0:
        lightCount += 1
        maze[i][j] = 10


  # yokoright
  for i in range(h):
    flag = False
    for j in range(w-1, -1, -1):
      if maze[i][j] == 1:
        flag = True
      if maze[i][j] == -1:
        flag = False
      if flag and maze[i][j] == 0:
        lightCount += 1
        maze[i][j] = 10


  print(lightCount)
  
  

# region fastio
 
BUFSIZE = 8192
 
 
class FastIO(IOBase):
    newlines = 0
 
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
 
 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
 
 
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
 
# endregion
 
if __name__ == "__main__":
    main()