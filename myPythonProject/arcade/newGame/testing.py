from time import sleep
import sys
line_1 = "Hello World"
pr = ""
for x in line_1:
    pr += x
    sys.stdout.flush()
    sleep(0.3)
    print(pr)