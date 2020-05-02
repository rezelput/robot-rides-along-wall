import sys
import time
import random
import math

class Program():
  __interpretation_started_timestamp__ = time.time() * 1000

  pi = 3.141592653589793
  u = None
  x = None
  y = None

  def execMain(self):

    
    while True:
      self.x = brick.sensor("A1").read()
      self.u = 3 * self.x
      if (self.x < 40 or self.x < 20):
        brick.motor("M3").setPower(50)
        brick.motor("M4").setPower(50)
        
        script.wait(1000)
        
      else:
        brick.motor("M3").powerOff()
        brick.motor("M4").powerOff()
        
        script.wait(500)
        
        brick.motor("M4").setPower(50)
        
        brick.motor("M3").setPower(15)
        
        script.wait(500)
        
        if (self.x < 50 or self.x < 20):
          brick.motor("M3").setPower(15)
          
          brick.motor("M4").setPower(25)
          
          script.wait(300)
          
        else:
          brick.motor("M3").setPower(50)
          brick.motor("M4").setPower(50)
          
          script.wait(150)
          
      self.y = 2 * self.x
      if (self.x < 20):
        brick.motor("M3").setPower(-(100))
        brick.motor("M4").setPower(-(100))
        
        script.wait(500)
        
        brick.motor("M3").setPower(35)
        
        brick.motor("M4").setPower(15)
        
        script.wait(400)
        
      else:
        brick.motor("M3").setPower(50)
        brick.motor("M4").setPower(50)
        
        script.wait(500)
        
        brick.encoder("E3").reset()
        

def main():
  program = Program()
  program.execMain()

if __name__ == '__main__':
  main()
