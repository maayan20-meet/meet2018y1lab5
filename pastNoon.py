x = 0

time = 0
while x<=100000:
    time += 1
    x += 60
    if time == 12:
        time = 0

print(x)
print(str(time-1) + ":" + str(60 - (x-100000)))
      
