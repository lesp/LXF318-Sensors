import machine
import utime

# Define pin for the PIR sensor
PIR_PIN = 16

# Setup GPIO pin
pir = machine.Pin(PIR_PIN, machine.Pin.IN, machine.Pin.PULL_UP)

counter = 1
print("Starting PIR sensor monitoring...")
while True:
    if pir.value() == 0:
        print(f"Motion detected, {counter} times")
        counter += 1
        while pir.value() == 0:
            utime.sleep(0.1)
    utime.sleep(0.1)