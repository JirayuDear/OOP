time = (input()).split()
time = [int(i) for i in time]
count = 0
price = 0
if (7 <= time[0] <= 23 and 7 <= time[2] <= 23) and (0 <= time[1] < 60 and 0 <= time[3] < 60 and time[0] <= time[2])  :
    if time[2] == 23 and time[3] > 0:
      print("Invalid")
      count = 1
    if count != 1:
      time[0] = int(time[0])*60
      time[2] = int(time[2])*60
      time_in = int(time[0]+int(time[1]))
      time_out = int(time[2]+int(time[3]))

      sumtime = abs(time_in - time_out)

      if sumtime <= 15:
        price = 0
      if 15 < sumtime <= 180:
        price = ((sumtime)//60)*10
        if sumtime%60 >= 1 :
          price = price+10
      if 180 < sumtime <= 360 :
        sumtime = sumtime - 180
        price = price+30
        price = price+((sumtime)//60)*20
        if sumtime%60 >= 1 :
          price = price+20
      if 360 < sumtime :
        price = 200

      print(abs(price))
else:
  print("Invalid")