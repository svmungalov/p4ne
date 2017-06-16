import glob
import ipaddress
import re

def r_str(x):
     ip = re.match('^ ip address (.+?) (.+?)$', x)
     if ip:
          return (str(ip.group(1)), str(ip.group(2)))
     else:
         return False


files = list(glob.glob("C:\\Users\\SV.Mungalov\\Seafile\\p4ne_training\\config_files\\*.txt"))
ip_adr = []
mask = []
net = []

for j in files:
    with open (j) as f:
        for i in f:
            r = r_str(i)
            if r:
                ip_adr.append(r[0])
                mask.append(r[1])
i = 0
n = len(ip_adr)
while  i < n:
    str1 = ip_adr[i] + "/" + mask[i]
    net.append(ipaddress.ip_network(str1, strict=False))
    i = i+1
i = 0
n = len(net)
m = len (ip_adr)
while i < n:
    j = 0
    prn_ip = []
    while j < m:
        if ipaddress.IPv4Address(ip_adr[j]) in ipaddress.IPv4Network(net[i]):
            prn_ip.append(ip_adr[j])
        j = j+1
    s = ""
    for k in prn_ip:
        s = s + " " + k
    print("Сеть: %s " % ipaddress.ip_network(net[i]).network_address, "Маска: %s " % mask[i], "Адреса: %s " % s)
    i = i+1
