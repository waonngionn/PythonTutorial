#for i in range(100):
#  print(i)

import sys, time

for num, i in enumerate(range(100)):
    sys.stdout.write("\r%d" % num)
    sys.stdout.flush()
    time.sleep(0.01)

for i in range(100):
    sys.stdout.write("=")
    sys.stdout.flush()
    time.sleep(0.01)


# printだと勝手に改行される
# sys.stdout.writeだと改行されない
