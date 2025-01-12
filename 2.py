import matplotlib.pyplot as plt
import math
import colorsys
import numpy as np
plt.axes(projection = 'polar')

f1=int(input("Enter f1: "))
f2=int(input("Enter f2: "))
df=int(input("Enter df: "))

rad1=[]
rad2=[]
while f1<=f2:
	f1+=df
	hue = f1 % 360 /360
	
	r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
	print(f'r: {r}, g: {g}, b: {b}')

	r1=f1/(4*3.14)
	print(r1)
	rad1.append(r1)

	r2=(1+math.sin(f1)*math.sin(f1))/2
	print(r2)
	rad2.append(r2)

	if r1<r2:
		while r1<r2:
			r1+=0.005
			color=(r,g,b)
			plt.polar(f1,r1,"g.")
	else:
		while r2<r1:
			r2+=0.005
			plt.polar(f1,r2,"r.")

minr1=min(rad1)
maxr2=max(rad2)

i=0	
while i<360:
	i+=1
	plt.polar(i,minr1,"k.")

i=0	
while i<360:
	i+=1
	plt.polar(i,maxr2,"k.")

plt.show()
