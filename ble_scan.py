import asyncio
import platform

from bleak import BleakScanner
from bleak import BleakClient

address = "00:90:4C:12:D0:01"
UUID_SERVICE_PRIVATE = "0000180a-0000-1000-8000-00805f9b34fb"
UUID_CHARACTERISTIC_PRIVATE1 = "00001122-0000-1000-8000-00805f9b34fb"

WIFI_SETTING = '{"EID":"SteppingStones_5G","PW":"steppinga"}'

async def run():
    devices = await BleakScanner.discover()
    for d in devices:
        if (str(d.name) == 'IoTube'):
          print("name :: " + str(d.name) + ", address :: " + str(d.address) + ", rssi :: " + str(d.rssi))

          client = BleakClient(d.address)
          try:
            await client.connect()
          
            #### READ 
            model_number = await client.read_gatt_char(UUID_CHARACTERISTIC_PRIVATE1)
            print("Model Number: {0}".format("".join(map(chr, model_number))))

            #### write_value = bytearray(WIFI_SETTING.encode(encoding='utf-8'))
            write_value = bytearray(WIFI_SETTING.encode('utf-8'))
            print("Write Value: {0}".format("".join(WIFI_SETTING)))

            await client.write_gatt_char(UUID_CHARACTERISTIC_PRIVATE1, write_value)

          except Exception as e:
            print(e)
          finally:
            await client.disconnect()

          # async with BleakClient(d.address) as client:
          #   model_number = await client.read_gatt_char(UUID_CHARACTERISTIC_PRIVATE1)
          
        ## print(d)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())