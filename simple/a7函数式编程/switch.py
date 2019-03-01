day = 3
switcher = {
    0:'Today it\'s Sunday',
    1:'Today it\'s Monday',
    2:'Today it\'s Tuesday'
}
#day_name =switcher[day]  #并不能显示default
day_name = switcher.get(day,'Unknown')   # 使用 get,默认 unkonwn
print(day_name)


day = 3

def get_monday():
    return 'Monday'

def  get_sunday():
    return 'Sunday'

def get_tuesday():
    return 'Tuesday'

def get_default():
    return 'Unknown'

switcher1 = {
    0:get_sunday,
    1:get_monday,
    2:get_tuesday
} 

day_name = switcher1.get(day,get_default())
print(day_name)