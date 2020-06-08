import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.72', 'david', 'cisco')
iosvl2.open()

ios_output = iosvl2.get_config()
print(json.dumps(ios_output, indent=4))

saveoutput = open("config-switch", "w")
saveoutput.write(ios_output.decode('ascii'))
saveoutput.write("\n")
saveoutput.close

iosvl2.close()