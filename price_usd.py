import random
import statistics

# 7 days
lastweek_price_mean=[200,199.25,198,198,197,195,193]
lastweek_price_median=[200,199.25,198,198,197,195,193]
lastweek_price_mode=[200,199.25,198,198,197,195,193]
day=0

# Random reference to increase or decrease values 
states=[-1,0,1]

def Mean():
    r = random.choice(states)
    index = day%7
    range = lastweek_price_mean[0:index+1]
    
    if r == -1:
        lastweek_price_mean[index]= int(statistics.mean(range) - 1)
    elif r == 1:
        lastweek_price_mean[index]= int(statistics.mean(range) + 1)
    else:
        lastweek_price_mean[index]= int(statistics.mean(range))
    
    return lastweek_price_mean[index]

def Median():
    r = random.choice(states)
    index = day%7
    range = lastweek_price_median[0:index+1]
    
    if r == -1:
        lastweek_price_median[index]= int(statistics.median(range)-1)
    elif r == 1:
        lastweek_price_median[index]= int(statistics.median(range)+1)
    else: 
        lastweek_price_median[index]= int(statistics.median(range))
    return lastweek_price_median[index]

def Mode():

    r = random.choice(states)
    index = day%7
    range = lastweek_price_mode[0:index+1]
    
    if r == -1:
        lastweek_price_mode[index]= int(statistics.mode(range)-1)
    elif r == 1:
        lastweek_price_mode[index]= int(statistics.mode(range)+1)
    else:
        lastweek_price_mode[index]= int(statistics.mode(range))
    
    return lastweek_price_mode[index]

# Simulation for the next 30 days
while day < 30:
    #mean = Mean()
    print("----------Day-----------:",day)
    print("Mean:",Mean())
    print("Median: ",Median())
    print("Mode: ",Mode())
    day+=1