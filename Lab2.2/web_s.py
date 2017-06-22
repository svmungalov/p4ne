from flask import Flask, jsonify
import sys
import glob
import re

app = Flask(__name__)

@app.route('/')
def index():
    return "/python - return JSON </br> /configs - return names hosts </br> \
    /config/hostname - return all IP-address of host"

@app.route('/python')
def python():
    return jsonify(repr(sys.__dict__))

@app.route('/configs')
def configs():
    return jsonify(list(dict.keys()))

@app.route('/config/<hostname>')
def hosts(hostname):
    return jsonify(dict[hostname])

def reg_ip(x):
    ip = re.match('^ ip address (.+?) (.+?)$', x)
    if ip:
      return (str(ip.group(1)), str(ip.group(2)))
    else:
        return False
def reg_h(x):
    name = re.match('^hostname (.+)', x)
    if name:
        return str(name.group(1))
    else:
        return False

if __name__ == '__main__':
    l = list(glob.glob("C:\\Users\\SV.Mungalov\\Seafile\\p4ne_training\\config_files\\*.txt"))
    host = []
    ip = []
    dict = {}
    for j in l:
        with open(j) as f:
            for i in f:
                r1 = reg_ip(i)
                r2 = reg_h(i)
                if r1:
                    ip.append(r1[0])
                if r2:
                    key = r2
            dict[key] = ip
    app.run(debug = True)