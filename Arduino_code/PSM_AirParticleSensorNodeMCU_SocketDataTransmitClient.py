import serial
from time import sleep
import socket
sleeptime = 0.5

def socket_start():
    global sock
    sock = socket.socket()
    host = "192.168.31.230"
    port = 8080
    sock.connect((host, port))
    print("Connected . . .")

def socket_send(st):
    sock.sendall(bytes("$%s" % st, encoding="utf-8"))
    print("sent:%s"%st)


def SerialConnect():
    try:
        global ser
        ser = serial.Serial('COM8', 9600, timeout=200)
        if ser.is_open == True:
            print("Connected")
    except:
        print("Fonction SerialConnect Error, Check if you have connected to port or not.")

def serial_input(A = str):
    str(A)
    input_intiger = A
    bytes_converter_variable = str(input_intiger)
    cstr = bytes( bytes_converter_variable, encoding="utf8")
    ser.write(cstr)
    #print("\ryou had write:{}".format(bstr),end="")   #Print what you had write


def LCD_str_inputmaker(input_str = ""):
    str_lis = input_str.split('&')
    output_str = ""
    for i in str_lis:
        formed_str =  i.ljust(40)
        output_str = output_str + formed_str
    return output_str

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


def main():
    socket_start()
    while True:
        data = sock.recv(1024)
        #print(hexShowNew(data))
        LisFormat = ['42']
        RawData = data
        Hexformat = hexShowNew(RawData)
        #print(Hexformat)
        LisFormat += Hexformat.split()
        #print(LisFormat)
        if len(LisFormat) > 20:
            if len(LisFormat)<35:
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


if __name__ == '__main__':
    main()
