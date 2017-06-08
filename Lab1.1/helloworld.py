print ("Hello World!")

class Subnet:
    def __init__(self, n="0.0.0.0", p="/0"):
        self.network = n
        self.prefix = p
    def __str__(self):
        return self.network + self.prefix
    def getnet(self):
     return self.network
    def getprefix(self):
        return self.prefix

n1 = Subnet("192.168.1.0", "/24")
n2 = Subnet("172.16.0.0", "/16")
n3 = Subnet()
x1 = n1.getnet()
x2 = n2.getprefix()
print (n1)
print (n2)
print (n3)
print (x1)
print (x2)

class Addr_plan_entry(Subnet):
    def __init__(self, n="0.0.0.0", p="/0", gw="0.0.0.0"):
        Subnet.__init__(self, n, p)
        self.gateway = gw
    def getgw(self):
        return self.gateway
    def __str__(self):
        return "Network: %s, prefix %s, gateway: %s" \
        %(self.network, self.prefix, self.gateway)

n4 = Addr_plan_entry("10.1.1.0", "/24", "10.1.1.1")
print (n4)
n5 = Addr_plan_entry("10.10.10.0", "/24", "10.10.10.1")
print (n5.getnet())
print (n5.getgw())
