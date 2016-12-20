# marinaescalante&dat-finished

#promt: coding bat problem logic-2 make_bricks
#We want to make a row of bricks that is goal inches long.
#We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
#Return True if it is possible to make the goal by choosing from the given bricks. 
#This is a little harder than it looks and can be done without any loops. 

# made in collab w/ dat after he couldn't solve it, but I am proud of our solution
def make_bricks(small, big, goal):
  # set up current 5
  currentFive = 0
  while (currentFive + 5) <= goal and (currentFive + 5) <= (big * 5):
    if small >= (goal - currentFive):
      return True
    currentFive += 5
  # when exit while, we have max 5s less than goal
  if small >= (goal - currentFive):
      return True
  return False