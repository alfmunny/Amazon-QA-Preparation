"""
code_list = [[apple, apple], [orange, anything, orange]]
cart = [apple, apple, orange, anything, orange]
Two Pointers

pt1 to mark the group in code list
pt2 to mark the current position of cart

found = False
while valid:
  if groupMatched(pt1, pt2, code_list, cart):
    pt1 += 1
    pt2 += len(code_list[pt1])
    if pt1 >= len(code_list):
      found = True
  else:
    pt2 += 1
"""

def solve(code_list, cart):
  i = 0 # index for group
  k = 0 # index for cart

  while i < len(code_list) and k < len(cart):
    if matchGroup(code_list, i, cart, k):
      k += len(code_list[i])
      i += 1
      if i == len(code_list):
        break
    else:
      k += 1
  return 1 if i == len(code_list) else 0

def matchGroup(code_list, i, cart, k):
  window_size = len(code_list[i])
  if k+window_size > len(cart):
    return False
  for j in range(window_size):
    if not isMatch(code_list[i][j], cart[k+j]):
      return False
  return True

def isMatch(s1, s2):
  return s1 == "anything" or s1 == s2

WILD_CARD = 'anything'

secret_code = [['apple', 'banana', 'orange'], ['banana', WILD_CARD, 'banana']]
user_purchase = ['banana', 'apple', 'banana', 'apple', 'banana', 'orange', 'apple', 'banana', 'orange', 'banana']
expected = 1
print(solve(secret_code, user_purchase),  expected)

secret_code = [['apple', 'banana'], ['banana', WILD_CARD, 'banana']]
user_purchase = ['banana', 'apple', 'apple', 'banana', 'apple', 'banana', 'orange', 'banana']
expected = 1
print(solve(secret_code, user_purchase),  expected)

secret_code = [['apple', 'apple'], ['banana', WILD_CARD, 'banana']]
user_purchase = ['orange', 'apple', 'orange', 'apple', 'apple', 'banana', 'orange', 'banana']
expected = 1
print(solve(secret_code, user_purchase),  expected)

secret_code = [['apple', 'apple'], ['banana', WILD_CARD, 'banana']]
user_purchase = ['banana', 'orange', 'banana', 'apple', 'apple']
expected = 0
print(solve(secret_code, user_purchase),  expected)

secret_code = [['apple', 'apple'], ['banana', WILD_CARD, 'banana']]
user_purchase = ['apple', 'banana', 'apple', 'banana', 'orange', 'banana']
expected = 0
print(solve(secret_code, user_purchase),  expected)

secret_code = [['apple', 'apple'], ['banana', WILD_CARD, 'banana']]
user_purchase = ['apple', 'apple', 'apple', 'banana']
expected = 0
print(solve(secret_code, user_purchase),  expected)

secret_code = [['apple', 'apple']]
user_purchase = ['apple', 'apple', 'apple', 'banana']
expected = 1
print(solve(secret_code, user_purchase),  expected)

secret_code = []
user_purchase = ['apple', 'apple', 'apple', 'banana']
expected = 1
print(solve(secret_code, user_purchase),  expected)
