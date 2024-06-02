import machine
import utime

TRIG_PIN = 3
ECHO_PIN = 2

trigger = machine.Pin(TRIG_PIN, machine.Pin.OUT)
echo = machine.Pin(ECHO_PIN, machine.Pin.IN)

def measure_distance():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(10)
    trigger.low()
    while echo.value() == 0:
        pulse_start = utime.ticks_us()
    while echo.value() == 1:
        pulse_end = utime.ticks_us()

    pulse_duration = utime.ticks_diff(pulse_end, pulse_start)
    distance = (pulse_duration * 0.0343) / 2
    distance = round(distance, 2)
    return distance

try:
    while True:
        distance = measure_distance()
        print(f"Distance: {distance} cm")
        utime.sleep(1)
except KeyboardInterrupt:
    print("Exiting")
