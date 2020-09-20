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
    sock=0
    pm1point0 = 0
    pm2point5 = 0
    pm10 = 0
    pm1point0_air = 0
    pm2point5_air = 0
    pm10_air = 0
    over0point3um = 0
    over0point5um = 0
    over1point0um = 0
    over2point5um = 0
    over5point0um = 0
    over10um = 0
    def __init__(self,PSMNetworkConfig):
        self.PSMNetworkConfig = PSMNetworkConfig
    
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

    def RefreshData(self,):
        LisDataDict = self.getrawData()
        self.m1point0      =  int(LisDataDict[4]  + LisDataDict[5] ,16)
        self.pm2point5     =  int(LisDataDict[6]  + LisDataDict[7] ,16)
        self.pm10          =  int(LisDataDict[8]  + LisDataDict[9] ,16)
        self.pm1point0_air =  int(LisDataDict[10] + LisDataDict[11],16)
        self.pm2point5_air =  int(LisDataDict[12] + LisDataDict[13],16)
        self.pm10_air      =  int(LisDataDict[14] + LisDataDict[15],16)
        self.um0point3     =  int(LisDataDict[16] + LisDataDict[17],16)
        self.um0point5     =  int(LisDataDict[18] + LisDataDict[19],16)
        self.um1point0     =  int(LisDataDict[20] + LisDataDict[21],16)
        self.um2point5     =  int(LisDataDict[22] + LisDataDict[23],16)
        self.um5point0     =  int(LisDataDict[24] + LisDataDict[25],16)
        self.um10          =  int(LisDataDict[26] + LisDataDict[27],16)
        
        

PSM = PSMconnection(PSMNetworkConfig=('192.168.31.230',8080))
PSM.PSMsocket_start()
while True:
    PSM.RefreshData()
    print(PSM.pm2point5_air)