import math as m
ab,bc = int(input()),int(input())
h = (ab**2 + bc**2) ** 0.5
h = h / 2.0
a = bc / 2.0
print(round(m.degrees(m.acos(a/h))),u'\N{DEGREE SIGN}',sep="")
