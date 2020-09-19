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



def main():
    socket_start()
    while True:
        data = sock.recv(64)
        print(data)


if __name__ == '__main__':
    main()


