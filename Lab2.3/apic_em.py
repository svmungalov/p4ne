import requests, json, pprint
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("topology.html")

@app.route('/api/topology')
def api_topology():
    url = "https://" + controller + "/api/v1/topology/physical-topology"
    header = {"content-type": "application/json","X-Auth-Token":ticket}
    responce = requests.get(url, headers=header, verify=False)
    return jsonify(responce.json()['response'])

def new_ticket():
    url = 'https://sandboxapic.cisco.com/api/v1/ticket'
    payload = {"username": "devnetuser","password": "Cisco123!"}
    header = {"content-type": "application/json"}
    response = requests.post(url, data=json.dumps(payload),headers=header, verify=False)
    return response.json()['response']['serviceTicket']

if __name__=='__main__':
    ticket = new_ticket()
    controller = "devnetapi.cisco.com/sandbox/apic_em"
    url = "https://" + controller + "/api/v1/host"
    header = {"content-type": "application/json","X-Auth-Token":ticket}
    responce = requests.get(url, headers=header, verify=False)
    print("Hosts = ")
    pprint.pprint(json.dumps(responce.json()))

    url = "https://" + controller + "/api/v1/network-device"
    header = {"content-type": "application/json","X-Auth-Token":ticket}
    responce = requests.get(url, headers=header, verify=False)
    print("Network device = ")
    pprint.pprint(json.dumps(responce.json()))

    url = "https://" + controller + "/api/v1/topology/physical-topology"
    header = {"content-type": "application/json","X-Auth-Token":ticket}
    responce = requests.get(url, headers=header, verify=False)
    print("Physical topology = ")
    pprint.pprint(json.dumps(responce.json()))

    app.run(debug=True)