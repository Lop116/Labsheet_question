z = 8
p = z
for x in range(1,z):
    l = (2*x - 1)
    zp = int((2*z-1)/2)
    print((' '*zp) + ('#'*l) +(' '*zp))
    z-=1
zp = int((2*p-1)/2)
for x in range(3):
    print((' '*zp) + ('H') +(' '*zp))
