# govee-ble-monitor

monitor Bluetooth Govee Smart Sensors in Python

## Prerequests/Test environment

- Linux: Ubuntu 20.04.6 LTS, Kernel 5.15.0
- Python: 3.8.10
- [Bluez](http://www.bluez.org/): 5.66
- [bleak](https://github.com/hbldh/bleak):  0.20.2
- Govee H5075

## Example

Make sure that the Bluetooth interface is powered on before running.
(For now it uses the ``hci0`` interface as the default.)

Modify ``ADDR`` line to your Govee H5075's MAC address in ``src/test.py``.

Run ``test.py`` code in terminal like this:

```bash
python3 src/test.py
```

The result is displayed as follows.

```
Address:     A4:C1:38:XX:XX:XX 
Temperature: 28.3 C
Humidity:    65.6 %
Battery:     63 %
```

## Tips

If you don't know MAC address of your device, you can get it like this:

```bash
sudo bluetoothctl
[bluetooth]# power on
[bluetooth]# scan le
Discovery started
...
[NEW] Device A4:C1:38:XX:XX:XX GVH5075_XXXX # Get it!
...
```



## Reference

- [Thrilleratplay](https://github.com/Thrilleratplay)/**[GoveeWatcher](https://github.com/Thrilleratplay/GoveeWatcher)** explains how to decode advertising data from Govee H5075.
