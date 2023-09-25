import os
import sys
import time
from rcon.source import Client

def stop(message, shutdown):
    try:
        with Client('192.168.1.254', 25575, passwd='1234') as client:
            client.run('say ' + message)
            client.run('stop')
    except:
        os.system("kill " + sys.argv[1])
    if shutdown:
        os.system('sudo shutdown -h 0')

empty = 0
while True:
    try:
        with Client('192.168.1.254', 25575, passwd='1234') as client:
            if not client.run('list').find('There are 0 of a max') == -1:
                empty += 1
            else:
                empty = 0
            if empty == 15:
                stop('Server stopped due to inactivity', True)
                quit()
    except:
        pass
    for i in range(3):
        shell = os.popen("ps o pid,%mem | grep " + sys.argv[1] + " | awk '{print $2}'")
        if float(shell.read().strip('\n')) > 50:
            stop('Server stopped due to memory overflow', False)
            quit()
        time.sleep(40)