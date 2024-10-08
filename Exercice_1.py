#Importing libraries so the code can work
import time
import machine
from machine import Pin, UART

uart = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9))
uart.init(bits=8, parity=None, stop=1)

#Loops infinitly write(send) a message to the other pico, it also reads the message and print the message from the other pico
while True:
    uart.write(b"Oi bruv")
    time.sleep(1)

    if uart.any():
        message = uart.read().decode('utf-8')  # Read and decode the message
        print(message)
    time.sleep(1)