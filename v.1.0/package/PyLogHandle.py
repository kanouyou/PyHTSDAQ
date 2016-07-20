## @package PyLogHandle
#  module to handle the logger file
#

import logging as log

## class to handle the logger
#
class PyLogHandle:

    ## constructor
    def __init__(self, filename="meas.log"):
        logformat = "%(asctime)s  %(levelname)s : %(message)s"
        datformat = "%m/%d/%Y %I:%M:%S %p"
        self._logger = log.getLogger()

        # stream logger handler
        self._stream = log.StreamHandler()
        self._stream.setFormatter( log.Formatter(logformat, datformat) )

        # file logger handler
        self._file = log.FileHandler(filename=filename, "a+")
        self._file.setFormatter( log.Formatter(logformat, datformat) )

    ## set log level
    def SetLevel(self, level="debug"):
        if level=="debug" or level=="DEBUG":
            loglevel = log.DEBUG
        elif level=="info" or level=="INFO":
            loglevel = log.INFO
        elif level=="warn" or level=="WARN":
            loglevel = log.WARNING
        elif level=="error" or level=="ERROR":
            loglevel = log.ERROR

        self._stream.setLevel(loglevel)
        self._file.setLevel(loglevel)

        # set logger
        self._logger.addHandler(self._stream)
        self._logger.addHandler(self._file)

    ## set log message for debug
    def Debug(self, message):
        pass
