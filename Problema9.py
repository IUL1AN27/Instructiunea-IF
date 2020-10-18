xa=int(input("Dati numarul bilelor albe mici:"))
xr=int(input("Dati numarul bilelor rosii mici:"))
xv=int(input("Dati numarul bilelor verzi mici:"))
ya=int(input("Dati numarul bilelor albe mari:"))
yr=int(input("Dati numarul bilelor rosii mari:"))
yv=int(input("Dati numarul bilelor verzi mari:"))
tx=xa+xr+xv
ty=ya+yr+yv
if (tx>ty):
    print("Mai multe sunt bile mici")
if (tx<ty):
    print("Mai multe sunt bile mari")
else:
    print("Bilele mari si mici se contin intr-un numar egal")
if (xa+ya>xr+yr) and (xa+ya>xv+yv):
    print("Mai numeroase sunt bilele albe")
if (xr+yr>xa+ya) and (xr+yr>xv+yv):
    print("Mai numeroase sunt bilele rosii")
if (xv+yv>xa+ya) and (xv+yv>xr+yr):
    print("Mai numeroase sunt bilele verzi")
if ((xa+ya)==(xr+yr)) and (xa+ya>xv+yv) and (xr+yr>xv+yv):
    print("Mai numeroase sunt bilele albe si rosii")
if ((xr+yr)==(xv+yv)) and (xr+yr>xa+ya) and (xv+yv>xa+ya):
    print("Mai numeroase sunt bilele rosii si verzi")
if ((xa+ya)==(xv+yv)) and (xa+ya>xr+yr) and (xv+yv>xr+yr):
    print("Mai numeroase sunt bilele albe si verzi")