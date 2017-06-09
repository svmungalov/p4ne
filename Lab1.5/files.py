import glob
l = list(glob.glob("C:\\Users\\SV.Mungalov\\Seafile\\p4ne_training\\config_files\\*.txt"))

flist = []

for j in l:
    with open (j) as f:
        for i in f:
            if i.find("ip address") == 1:
                flist.append(i.strip())
list(set(flist))

for j in flist:
    print (j)