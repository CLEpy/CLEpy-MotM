from pybleno import *
import array
import struct
import sys
import traceback
from builtins import str

class RgbLedCharacteristic(Characteristic):
    
    def __init__(self, led):
        Characteristic.__init__(self, {
            'uuid': '13333333333333333333333333330001',
            'properties': ['read', 'write'],
            'descriptors': [
                    Descriptor(
                        uuid = '2901',
                        value = 'RGB LED color'
                    )],   
            'value': None
          })
          
        self.led = led
        self.r = 0
        self.g = 0
        self.b = 0
          
    def onReadRequest(self, offset, callback):
        if offset:
            callback(Characteristic.RESULT_ATTR_NOT_LONG, null)
        else:
            data = array.array('B', [0] * 3)
            writeUInt8(data, self.r, 0)
            writeUInt8(data, self.g, 0)
            writeUInt8(data, self.b, 0)
            callback(Characteristic.RESULT_SUCCESS, data);

    def onWriteRequest(self, data, offset, withoutResponse, callback):
        if offset:
            callback(Characteristic.RESULT_ATTR_NOT_LONG)
        elif len(data) != 3:
            callback(Characteristic.RESULT_INVALID_ATTRIBUTE_LENGTH)
        else:
            r = readUInt8(data, 0)
            g = readUInt8(data, 1)
            b = readUInt8(data, 2)
            self.update_rgb(r,g,b)
            callback(Characteristic.RESULT_SUCCESS);

    def update_rgb(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b
        self.led.color = (self.r/255, self.g/255, self.b/255)
