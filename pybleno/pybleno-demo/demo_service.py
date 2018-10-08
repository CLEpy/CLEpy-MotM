from pybleno import *
from rgb_led_characteristic import *
from switch_characteristic import *

class DemoService(BlenoPrimaryService):
    def __init__(self, led, switch):
        BlenoPrimaryService.__init__(self, {
          'uuid': '13333333333333333333333333333337',
          'characteristics': [
            RgbLedCharacteristic(led),
            SwitchCharacteristic(switch),
          ]})

