import random
import time
import threading

struct = 0
print("Track Time Sim Monza\n")
cars = 1
mode = int(input("Would you like to simulate a race (1) or a single car (2):"))

if mode == 1:
  cars = int(input("How many cars (1 - 22): "))
  type = int(input("Do you want to define the same car or different cars (1 - 2): "))

print("")

clients = [[""] * 2 for i in range(cars)]

for i in range(cars):
  clients[i][0] = ("car"+str(i+1))
  
if type == (2) and len(clients) > (1):
  struct = cars
else:
  struct = 1

def assignCar(clients):
  print("\nDefine Car:\n")
  carW = int(input("1. Enter Car Weight (1 - 2000kg): "))
  carH = int(input("2. Enter Car Horsepower (1 - 1500hp): "))
  tireT = int(input("3. Enter car tyre type (1>S, 2>M, 3>H): "))
  skill = int(input("5. Enter skill of driver (1 - 100): "))
  skillV = int(input("5. Enter the skill variation of driver (0 - 30): "))
  print("")
  power = pw(carW,carH,tireT) / 10
  dr = oc(skill,skillV)
  result = dr * power
  time = 140 - (515 * result)
  return str(time)

def oc(s,sv):
  new = 0
  d = random.randint(-(sv),sv)
  new = s + d
  new = new / 100
  return new

def pw(W,H,T):
  mul = 0
  eng = 0
  eng = H / W
  if T == 1:
    mul = 1.1
  elif T == 2:
    mul = 1.05
  else:
    mul = 1
  new = eng * mul
  return new

if struct == (1):
  x = assignCar(clients)
  for i in range(len(clients)):
    clients[i][1] = x
else:
  for i in range(struct):
    clients[i][1] = assignCar(clients)

def timer(timer_id, clients, i):
  wait_time = float(clients[i][1])
  time.sleep(0.1)
  print ("car" + str(timer_id) + " Completed Section 1, " + str((wait_time * 0.1897)) + " Seconds")
  time.sleep(0.1)
  print ("car" + str(timer_id) + " Completed Section 2, " + str((wait_time * 0.0517)+(wait_time * 0.1897)) + " Seconds")
  time.sleep(0.1)
  print ("car" + str(timer_id) + " Completed Section 3, " + str((wait_time * 0.7586)+(wait_time * 0.0517)+(wait_time * 0.1897)) + " Seconds")
  time.sleep(0.1)
  print ("car" + str(timer_id) + " Finnished the race with a time of: " + str(wait_time) + " seconds")

def create_timers(num_timers):
  for i in range(num_timers):
      t = threading.Thread(target=timer, args=(i+1,clients,i))
      t.start()

num_timers = cars
create_timers(num_timers)
