from govee_ble_monitor import Monitor
import asyncio

ADDR = "A4:C1:38:XX:XX:XX"

monitor = Monitor(ADDR)
temp, humidity, battery = asyncio.run(monitor.get_data())

print(f"Address:     {ADDR}")
print(f"Temperature: {temp:.1f} C")
print(f"Humidity:    {humidity:.1f} %")
print(f"Battery:     {battery} %")
