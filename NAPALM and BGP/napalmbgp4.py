import json
from napalm import get_network_driver

bgplist = ['17.1.1.1',
           '17.1.1.2',
           '8.8.8.2',
           '15.1.1.2'
           ]

for ip_address in bgplist:
    print ("Connecting to " + str(ip_address))
    driver = get_network_driver('ios')
    iosv_router = driver(ip_address, 'mohamed', 'cisco')
    iosv_router.open()
    bgp_neighbors = iosv_router.get_bgp_neighbors()
    print (json.dumps(bgp_neighbors, indent=4))
    iosv_router.close()





