import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Initialize I2C and ADS1115 ADC
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)

# Select Analog Input Channel (A0)
channel0 = AnalogIn(ads, ADS.P0)
channel1 = AnalogIn(ads, ADS.P1)

min_val = 2.10
max_val = 0.95

print(f"0: Raw Value: {channel0.value}, Voltage: {channel0.voltage:.2f}V")
print(f"1: Raw Value: {channel1.value}, Voltage: {channel1.voltage:.2f}V")

def getHumedad(channel):
    if channel == 0:
        value = channel0.voltage
    elif channel == 1:
        value = channel1.voltage

    if value > min_val:
        percentage = 0
    elif value < max_val:
        percentage = 100
    else:
        percentage = (min_val - value) / (min_val - max_val) * 100
    print(value)
    print(f"{percentage:.0f}%")
    return percentage