from pybleno import *
import array
import struct
import sys
import traceback
from builtins import str

class SwitchCharacteristic(Characteristic):
    
    def __init__(self, switch):
        Characteristic.__init__(self, {
            'uuid': '13333333333333333333333333330002',
            'properties': ['read', 'notify'],
            'descriptors': [
                    Descriptor(
                        uuid = '2901',
                        value = 'Switch'
                    )],   
            'value': None
          })
          
        self.switch = switch
        self.updateValueCallback = None

        self.switch.when_pressed = self._on_switch_updated
        self.switch.when_released = self._on_switch_updated
          
    def onReadRequest(self, offset, callback):
        if offset:
            callback(Characteristic.RESULT_ATTR_NOT_LONG, null)
        else:
            data = array.array('B', [0] * 1)
            writeUInt8(data, self.switch.is_pressed, 0)
            callback(Characteristic.RESULT_SUCCESS, data);

    def _on_switch_updated(self):
        if self.updateValueCallback:
            data = array.array('B', [0] * 1)
            writeUInt8(data, self.switch.is_pressed, 0)
            self.updateValueCallback(data);
