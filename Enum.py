from enum import IntEnum

class Season(IntEnum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4
print(Season.SPRING)
print(Season.SPRING.name)
print(Season.SPRING.value)
print(type(Season.SPRING))
print(repr(Season.SPRING))
print(list(Season))

list = []
for season in (Season):
    print(season.name)
    list.append(season.name)
print(list)
