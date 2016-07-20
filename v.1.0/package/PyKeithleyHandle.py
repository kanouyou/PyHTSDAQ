## @package PyKeithleyHandle
#  module handle the keithley voltage meter

import visa
import time

## base class to handle the keithley voltage meter
#
class PyVoltageMeterBase:

    ## constructor
    def __init__(self):
        self.fRm = visa.ResourceManager()

    ## check gpib port
    def GetGpibPort(self):
        gpib = self.fRm.list_resources()
        return gpib

    ## set gpib port
    def SetGpib(self, address):
        self.fIst = self.fRm.open_resource( address )

    ## check instrument info
    def GetInstrInfo(self):
        w = self.fIst.write("*IDN?")
        r = self.fIst.read()
        return r

    ## read data from instrument
    def Read(self):
        w = self.fIst.write(":sense:data:fresh?")
        r = self.fIst.read()
        return float(r)

    
