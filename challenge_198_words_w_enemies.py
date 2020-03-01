left, right = input().split()

for char in left + right:
  if char in left and char in right:
    left = left.replace(char, '', 1)
    right = right.replace(char, '', 1)
    """ #DEBUG
    print(left)
    print(right)
    """

if len(left) == len(right):
  print("TIE")
elif len(left) > len(right):
  print("LEFT SCORES:", len(left))
else:
  print("RIGHT SCORES:", len(right))