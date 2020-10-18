zn=int(input('ziua nasterii ='))
zc=int(input('ziua curenta ='))
ln =int(input('luna nasterii ='))
lc=int(input('luna curenta ='))
an =int(input('anul nasterii ='))
ac=int(input('anul curent ='))
if (lc>ln):
    print(ac-an, "ani")
if ((lc==ln) and (zc>=zn)):
    print(ac-an, "ani")
if ((lc==ln) and (zc<zn)):
    print((ac-an)-1, "ani")
if (lc<ln):
    print((ac-an)-1, "ani")