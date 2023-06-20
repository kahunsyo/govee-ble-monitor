import asyncio
from bleak import BleakScanner

ADVERTISING_DATA_UUID = 60552 # same to 0xEC88

class Monitor():
    def __init__(self, addr):
        self.addr = addr.upper()
        
    def decode_temp_in_c(self, temp_humidity_bytes):
        # Upper 3 decimal digits indicate temperature.

        # Get upper 3 decimal digits
        temp = int.from_bytes(temp_humidity_bytes, byteorder='big', signed=False)
        temp = int(temp / 1000)

        # Correct units
        temp /= 10
        return temp

    def decode_humidity(self, temp_humidity_bytes):
        # Last 3 decimal digits indicate humidity.

        # Get last 3 decimal digits
        humidity = int.from_bytes(temp_humidity_bytes, byteorder='big', signed=False)
        humidity = humidity % 1000
        
        # Correct units
        humidity /= 10
        return humidity

    def decode_battery_remaining(self, battery_bytes):
        battery = int.from_bytes(battery_bytes, byteorder='big', signed=False)
        return battery


    async def get_data(self):
        """
        return temperature humidity battery
        """
        stop_event = asyncio.Event()
        data_queue = asyncio.Queue()

        def callback(device, advertising_data):
            if device.address == self.addr:
                temp_humidity_bytes = advertising_data.manufacturer_data[ADVERTISING_DATA_UUID][1:4]
                battery_bytes = advertising_data.manufacturer_data[ADVERTISING_DATA_UUID][4:5]
                
                temp = self.decode_temp_in_c(temp_humidity_bytes)
                humidity = self.decode_humidity(temp_humidity_bytes)
                battery = self.decode_battery_remaining(battery_bytes)
                
                stop_event.set()
                data_queue.put_nowait((temp, humidity, battery))
                
        async with BleakScanner(callback) as scanner:
            await stop_event.wait()

        return await data_queue.get()

