import serial 
while True:
    try:
        ser = serial.Serial('/dev/ttyS0', 115200, timeout=1000) 
        # Ensure the port is correct and not already in use
        print(f"Connected to: {ser.portstr}")
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        exit()