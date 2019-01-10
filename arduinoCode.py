import serial #used for Serial Communication



aSerial = serail.Serial('com18',9600)


num = int(input("To turn on LED enter 1, to turn off LED enter 0 and to quit enter -1"))


while(num != -1):

    if(num == 1):
        aSerial.write('1')
        print("LED turned on")

    if(num == 0):
        aSerial.write('0')
        print("LED turned off")


    num = int(input("To turn on LED enter 1, to turn off LED enter 0 and to quit enter -1"))
