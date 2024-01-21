import pygame

class Timer:
     def __init__(self) -> None:
          self.time = 300
          self.running = False

     def start(self):
          self.running = True
          self.curr_time = pygame.time.get_ticks() // 1000

     def pause(self):
          self.running = False

     def stop(self):
          self.time = 0
          self.running = False

     def get_time(self, time):
          if not self.running:
               return self.time
          else:
               if self.time - (time - self.curr_time) == 0:
                    self.stop()
               return self.time - (time - self.curr_time)

     def reset(self, time):
          self.time = time
          self.running = True
          self.curr_time =  pygame.time.get_ticks()