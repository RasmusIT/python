# 18.10.2024 Rasmus
# Ülesanne 6
import turtle
import math

# Redel
## Matem
korgus = 4.4
nurk = math.radians(53)
kaugus = abs(korgus / math.tan(nurk))
c = math.sqrt(korgus**2 + kaugus**2)
print(kaugus)
#Joonis
kordaja = 10
turtle.fd(kaugus*kordaja)
turtle.left(90)
turtle.fd(korgus*kordaja)
turtle.left(180-37)
turtle.fd(c*kordaja)






turtle.done()