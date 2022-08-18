from glob import glob
import random

now = int(1)

P_1 = int(0)
P_2 = int(0)
P_3 = int(0)

def start_1():
  global now
  now_round = "1번 유저 차례 / 1 2중에서 하나를 입력하세요 /" , str(now) + "라운드"
  number = input(now_round)
  dice = random.randint(1, 2)
  global P_1

  if int(number) == int(dice) :
    print("축하드립니다. 내 숫자:", number , "홀짝 숫자:", dice)
    P_1 = (P_1 + 1)
    start_2()

  elif int(number) == 3:
    end()
  else:

    print("틀렸습니다.. 내 숫자:", number , "홀짝 숫자:", dice)
    start_2()

def start_2():
  global now
  now_round = "2번 유저 차례 / 1 2중에서 하나를 입력하세요 /" , str(now) + "라운드"
  number = input(now_round)
  dice = random.randint(1, 2)
  global P_2
  if int(number) == int(dice) :
    print("축하드립니다. 내 숫자:", number , "홀짝 숫자:", dice)
    P_2 = (P_2 + 1)
    start_3()

  elif int(number) == 3:
    end()

  else:
    print("틀렸습니다.. 내 숫자:", number , "홀짝 숫자:", dice)
    start_3()

def start_3():
  global now
  now_round = "3번 유저 차례 / 1 2중에서 하나를 입력하세요 /" , str(now) + "라운드"
  number = input(now_round)
  now = (now + 1)
  dice = random.randint(1, 2)
  global P_3
  if int(number) == int(dice) :
    print("축하드립니다. 내 숫자:", number , "홀짝 숫자:", dice)
    P_3 = (P_3 + 1)
    start_1()

  elif int(number) == 3:
    end()

  else:
    print("틀렸습니다.. 내 숫자:", number , "홀짝 숫자:", dice)
    start_1()


def end():
  global P_1
  global P_2
  global p_3
  print("1번 유저 점수 :", P_1)
  print("2번 유저 점수 :", P_2)
  print("3번 유저 점수 :", P_3)
    

# 시작코드

print("끝내시려면 \"3\" 을 입력해주세요")
start_1()