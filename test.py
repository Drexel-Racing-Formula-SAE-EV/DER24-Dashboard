import serial 

port = serial.Serial("/dev/tty", baudrate=115200, timeout=3.0)
while True:
    try:
        # ser = serial.Serial('/dev/ttyS0', 115200, timeout=1) 
        # # Ensure the port is correct and not already in use
        # print(f"Connected to: {port.portstr}")
        # line = port.readline().decode('utf-8').rstrip()
        # print(line)
        port.write(("\r\nSay something:").encode('utf-8'))
        rcv = port.read(10)
        port.write(("\r\nYou sent:" + repr(rcv)).encode('utf-8'))

    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        exit()