Deck=[]
for j in range(1,14):
  for i in range(1,5):
    Deck.append(j)

Round=0
Bot=[]
Player=[]
p,b = 1,1
import random as r

def PDraw():
  R=r.randint(1,13)
  if Deck.count(R)>0:
    Player.append(R)
    Deck[Deck.index(R)] = 0
    return
  else:
    return PDraw()

def BDraw():
  R=r.randint(1,13)
  if Deck.count(R)>0:
    Bot.append(R)
    Deck[Deck.index(R)] = 0
    return
  else:
    return BDraw()

PDraw()
BDraw()
BDraw()
DCFS = ['?',Bot[1:]]
pt = sum(Player)
bt = sum(Bot)
print(f"Dealer's card : {DCFS}")

while pt <= 21:
  if pt > 21 and bt > 21:
    print('draw')
    pt, bt = 22,22
  if bt > 21 and pt < 21:
    print("You Win")
    pt, bt = 22,22
  if pt > 21 and bt < 21:
    print('You Lose')
    pt, bt = 22, 22
  if p == 1:
    PDraw()
    pt = sum(Player)
    print(f"your card : {Player}")
    if pt > 21:
      print("You lose")
      bt = 22
      break
    ans = str(input('stop?'))
    if ans == 'stop':
      p = 0
      break

while bt <= 21:
  if bt > 17:
    b = 0
    if bt > pt:
      print(Bot)
      print("You Lose")
    elif bt == pt:
      print("Draw")
    else:
      print(Bot)
      print("You Win")
    bt = 22
  if b == 1:
    BDraw()
    bt = sum(Bot)
    print(Bot)
    if bt > 21:
      print("You Win")
      break