jmeno = "Michal"
#        012345

print(jmeno[2])
print(jmeno[5])
 
teploty = [2.2, 3.5, 6, 8, 15, 20, 21.2, 25, 30, 15, 10, 5, 3.3]

print(len(teploty))
print(teploty[12])

pizzerie = [
     #01234567
    ["Pizzerie 1", True],   #0
    ["Pizzerie 2", False],  #1
    ["Pizzerie 3", True]    #2
]       #0          #1

print(pizzerie[2][0][2])
print(pizzerie[1][1])

for p in pizzerie:
    if p[1] == True:
        print(f"Pizzerie {p[0]} rozvazi.")

mesta = [
    ["Prerov", 45000],  
    ["Karvina", 50000], 
    ["Praha", 1200000]    
]     

for m in mesta:
    if m[1] < 50000:
        print(f"male mesto {m[0]}")
    elif m[1] < 100000:
        print(f"stredni mesto {m[0]}")
    else:
        print(f"velke mesto {m[0]}")
