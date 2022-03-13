import smbus

HUNDRED_PERCENT = 2778 
ZERO_PERCENT = 14702

DEVICE_BUS = 1
DEVICE_ADDR = 0x48
bus = smbus.SMBus(DEVICE_BUS)

data = [0x84,0x83]
bus.write_i2c_block_data(0x48, 0x01, data)


def getHumedad():
	value = bus.read_i2c_block_data(0x48, 0x00, 2)
	raw_adc = value[0] * 256 + value[1]

	if raw_adc > 32767:
		raw_adc -= 65535

	percentage_raw_adc = ((raw_adc - ZERO_PERCENT) * 100) / (HUNDRED_PERCENT - ZERO_PERCENT)

	return int(percentage_raw_adc)