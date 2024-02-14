import math
##Distanza Oslo-Vancouver
λ = 0
ϕ = 0
r=6371
d=0
lat_o,long_o = math.radians(59.9), math.radians(10.8)
lat_v,long_v = math.radians(49.3), math.radians(-123.1)

r-6371

el1=math.sin(1/2 * (lat_v - lat_o))**2
el2=math.cos(lat_o) * math.cos(lat_v) * math.sin(1/2*(long_v - long_o))**2
h=(el1+el2)**0.5
angle=2*math.atan2(math.sqrt(el1 + el2), math.sqrt(el1 + el1/2*el2))
d=6371*angle
print("La distanza tra Oslo e Vancouver è di ", d," km.")
