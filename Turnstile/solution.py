# numCustomers
# arrTime
# direction
# 1. collect the customers who want to enter
# 2. collect the customers who want to exit

def solve(numCustomers, arrTime, direction):

  exit = []
  enter = []

  for i in range(len(arrTime)):
    if direction[i] == 1:
      exit.append([arrTime[i], i])
    else:
      enter.append([arrTime[i], i])

  state = -1 # previous state: -1:not used,  1: enter, 0: exit
  timer = 0 #
  ans = [0] * len(arrTime)

  while exit or enter:
    if exit and exit[0][0] <= timer and (state == -1 or state == 0 or not enter or enter[0][0] > timer):
      ans[exit[0][1]] = timer
      exit.pop(0)
      state = 0
    elif enter and enter[0][0] <= timer:
      ans[enter[0][1]] = timer
      enter.pop(0)
      state = 1
    else:
      state = -1

    timer += 1

  return ans


testcases = [
    [[0,0,1,5], [0,1,1,0], [2,0,1,5] ],\
    [[1,2,4], [0,1,1], [1,2,4]],\
    [[1,1], [1,1], [1,2]], \
    [[1,1,3,3,4,5,6,7,7], [1,1,0,0,0,1,1,1,1], [1,2,3,4,5,6,7,8,9]]
]

for case in testcases:
  print(solve(len(case[0]), case[0], case[1]), case[2])



