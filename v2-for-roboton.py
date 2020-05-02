import subprocess
import sys
import time

class Program():
  __interpretation_started_timestamp__ = time.time() * 1000

  pi = 3.1415926535897931
  L = ""

  def execMain(self):

    
    while not brick.keys().wasPressed(Up):
      script.wait(100)
    
    self.L = 30
    while True:
      if (brick.sensor("A1").read() < self.L):
        brick.motor("M3").powerOff()
        brick.motor("M4").powerOff()
        
        brick.motor("M3").setPower(-(100))
        brick.motor("M4").setPower(-(100))
        
        script.wait(3000)
        
        brick.motor("M3").powerOff()
        brick.motor("M4").powerOff()
        
        brick.motor("M4").setPower(100)
        
        script.wait(400)
        
      else:
        brick.motor("M3").setPower(100)
        brick.motor("M4").setPower(100)
        
    

def main():
  program = Program()
  program.execMain()

if __name__ == '__main__':
  main()
