import socket
from time import sleep

def hexShowNew(argv):  
    try:
        result = ''
        hLen = len(argv)
        for i in range(hLen):
            hvol = argv[i]
            hhex = '%02x' % hvol
            result += hhex + ' '
        # print(result)s
        return result
    except:
        pass


class PSMconnection:
    def __init__(self,PSMNetworkConfig,sock):
        self.PSMNetworkConfig = PSMNetworkConfig
        self.sock = sock
    
    def PSMsocket_start(self):
        self.sock = socket.socket()
        print('Networkconfig: '+str(self.PSMNetworkConfig)+' Connecting...')
        try:
            self.sock.connect((self.PSMNetworkConfig))
            print("Socket connection successful")
        except:
            print("Socket connection failed")

    def getrawData(self):
        LisData = ['42']
        while len(LisData) != 32:
            LisData = ['42']
            incomingDataHex = hexShowNew(self.sock.recv(1024))
            LisData += incomingDataHex.split()
        SUM = 0
        Aut = int(LisData[30] + LisData[31],16)
        for i in range(0,29):
            SUM += int(LisData[i],16)
        if SUM == Aut:
            return LisData
        else:
            return 'SUM Authentication failed'

PSM = PSMconnection(PSMNetworkConfig=('192.168.31.230',8080),sock=0)
PSM.PSMsocket_start()
print(PSM.getrawData())