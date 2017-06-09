from ipaddress import IPv4Network
import random

class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
        IPv4Network.__init__(self, (random.randint(0x0B000000, 0xDF000000),
        random.randint(8,24)), strict=False)
    def value(self):
        return int(self.network_address) + int(self.netmask) * 2**32

def sortfunc(x):
    return x.value()

i=1
l =[]
while (i < 100):
    l.append (IPv4RandomNetwork())
    i = i + 1
print (l)

l1 = sorted(l, key=sortfunc)
print (l1)
for i in l1:
    print(i)