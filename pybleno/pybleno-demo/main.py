#!/usr/bin/env python3
import sys
import signal
from pybleno import *
from demo_service import *
from gpiozero import Button, RGBLED
from time import sleep

led = RGBLED(17,27,22, active_high=False)
button = Button(4)

bleno = Bleno()

name = 'Demo'
demoService = DemoService(led, button)

def onStateChange(state):
    if (state == 'poweredOn'):
        bleno.startAdvertising(name, [demoService.uuid], on_start_advertising)
    else:
        bleno.stopAdvertising();

bleno.on('stateChange', onStateChange)
    
def on_start_advertising(err):
    if err:
        print(err)

def on_advertising_start(error):
    if not error:
        print('advertising...')
        bleno.setServices([demoService ])

bleno.on('advertisingStart', on_advertising_start)

print ('Hit <ENTER> to disconnect')

if (sys.version_info > (3, 0)):
    input()
else:
    raw_input()

bleno.stopAdvertising()
bleno.disconnect()

print ('terminated.')
sys.exit(1)
