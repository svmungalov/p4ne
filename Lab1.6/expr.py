import glob
import re

def reg_exp(x):
    ip = re.match('^ ip address (.+?) (.+?)$', x)
    interface = re.match('^interface (Giga.+|Fast.+)', x)
    name = re.match('^hostname ([A-Za-z0-9]+)', x)
    if ip:
      return ("IP", ip.group(1), ip.group(2))
    elif interface:
        return ("INT", interface.group(1))
    elif name:
        return ("HOST", name.group(1))
    else:
        return ("UNCLASSIFIED", )

l = list(glob.glob("C:\\Users\\SV.Mungalov\\Seafile\\p4ne_training\\config_files\\*.txt"))

for j in l:
    with open (j) as f:
        for i in f:
            r = reg_exp(i)
            if r[0] != "UNCLASSIFIED":
                print(r)
