import serial

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

ser = serial.Serial('COM25', 9600, timeout=200)
while True:
    LisFormat = []
    RawData = ser.read(size = 32)
    Hexformat = hexShowNew(RawData)
    #print(Hexformat)
    LisFormat = Hexformat.split()
    #print(LisFormat)
    print("PM1.0: {0}  PM2.5: {1}  PM10: {2}  PM1.0(air): {3}  PM2.5(air): {4}  PM10(air): {5}  0.3um: {6}  0.5um: {7}  1.0um: {8}  2.5um: {9}  5.0um: {10}  10um: {11}".format(
    int(LisFormat[4] + LisFormat[5],  16),
    int(LisFormat[6] + LisFormat[7],  16),
    int(LisFormat[8] + LisFormat[9],  16),
    int(LisFormat[10] + LisFormat[11],16),
    int(LisFormat[12] + LisFormat[13],16),
    int(LisFormat[14] + LisFormat[15],16),
    int(LisFormat[16] + LisFormat[17],16),
    int(LisFormat[18] + LisFormat[19],16),
    int(LisFormat[20] + LisFormat[12],16),
    int(LisFormat[22] + LisFormat[23],16),
    int(LisFormat[24] + LisFormat[25],16),
    int(LisFormat[26] + LisFormat[27],16),
    ))
