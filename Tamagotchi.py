import numpy as np

class Tamagotchi:
   def __init__(self, name):
       self.name = name
       self.fullness = 8
       self.happiness = 8
       self.cleanliness = 8
       self.alive = True
       self.stage = "egg"
       self.progress = 1

   def feed(self):
       self.fullness += 3
       if self.fullness > 10:
           self.fullness = 10
           self.cleanliness -= 2
           if self.cleanliness < 1:
               self.cleanliness = 1

   def play(self):
       self.happiness += 3
       if self.happiness > 10:
           self.happiness = 10
           self.fullness -= 2
           if self.fullness < 1:
               self.fullness = 1

   def bathe(self):
       self.cleanliness += 3
       if self.cleanliness > 10:
           self.cleanliness = 10
           self.happiness -= 2
           if self.happiness < 1:
               self.happiness = 1

   def age_up(self):
       self.stage = self.get_next_stage()
       self.progress = 1

   def get_next_stage(self):
       stages = ["egg", "baby", "child", "adult"]
       current_index = stages.index(self.stage)
       return stages[(current_index + 1) % len(stages)]

   def status(self):
       if self.fullness <= 1 or self.happiness <= 1 or self.cleanliness <= 1:
           self.alive = False
           return "dead"
       elif self.fullness <= 5 or self.happiness <= 5 or self.cleanliness <= 5:
           return "distress"
       else:
           return "fine"

   def time_step(self):
       attributes = ["fullness", "happiness", "cleanliness"]
       attribute = np.random.choice(attributes)
       setattr(self, attribute, getattr(self, attribute) - 1)
       self.progress += 1
       if self.progress >= 20:
           self.age_up()
       status = self.status()
       return status

tamagotchi = Tamagotchi("Pet")
print(tamagotchi.name) # Should print "Pet"
tamagotchi.feed()
print(tamagotchi.fullness) # Should print 11


def main():
   # Test 1: Create a Tamagotchi named Goku, and check that after calling bathe(), play() and feed() the values of fullness, cleanliness and happiness are all 10.
   goku = Tamagotchi("Goku")
   goku.bathe()
   goku.play()
   goku.feed()
   goku.fullness == 10
   goku.cleanliness == 10
   goku.happiness == 10

   # Test 2: Create a Tamagotchi named Gohan check that after bathe(), play(), feed(), feed(), bathe(), play(), the values of fullness is 8, cleanliness and happiness are 10.
   gohan = Tamagotchi("Gohan")
   gohan.bathe()
   gohan.play()
   gohan.feed()
   gohan.feed()
   gohan.bathe()
   gohan.play()
   gohan.fullness == 8
   gohan.cleanliness == 10
   gohan.happiness == 10

   # Test 3: Write code to check that Goku’s initial stage is egg. Then, call age_up() four times, each time checking that the stages are baby, child, adult, adult.
   goku.stage == "egg"
   goku.age_up()
   goku.stage == "baby"
   goku.age_up()
   goku.stage == "child"
   goku.age_up()
   goku.stage == "adult"
   goku.age_up()
   goku.stage == "adult"

   # Test 4: Write code to initialize a Tamagotchi named Vegeta with the following attributes:
   # • fullness=6, happiness=6, cleanliness=6 and check the status is fine
   # • fullness=6, happiness=6, cleanliness=3 and check the status is distress
   # • fullness=1, happiness=6, cleanliness=3 and check the status is dead
   vegeta = Tamagotchi("Vegeta")
   vegeta.fullness = 6
   vegeta.happiness = 6
   vegeta.cleanliness = 6
   vegeta.status() == "fine"
   vegeta.fullness = 6
   vegeta.happiness = 6
   vegeta.cleanliness = 3
   vegeta.status() == "distress"
   vegeta.fullness = 1
   vegeta.happiness = 6
   vegeta.cleanliness = 3
   vegeta.status() == "dead"

if __name__ == "__main__":
   main()
