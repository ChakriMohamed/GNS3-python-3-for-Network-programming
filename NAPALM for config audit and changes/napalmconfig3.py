import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.72', 'david', 'cisco')
iosvl2.open()

print ('Accessing 192.168.122.72')

with open('fichier_config') as f:
    lines = f.read().splitlines()
print(lines[1])

for n in range (0,2):
    print("configuration of "+lines[i])

    iosvl2.load_merge_candidate(filename=lines[i])

    diffs = iosvl2.compare_config()
    if len(diffs) > 0:
        print(diffs)
        iosvl2.commit_config()
    else:
        print('No changes required.')
        iosvl2.discard_config()

iosvl2.close()
