#! /usr/bin/env python3
# # -*- coding: utf-8 -*-

#################################################################
#  get modbus data from CU and save to log file
#  Norihito Nov.2020
#
# Usage: python client_modbus_tcp_ampt.py 
#################################################################

import time
import datetime


# --------------------------------------------------------------------------- #
# import the various server implementations
# --------------------------------------------------------------------------- #
# from pymodbus.client.sync import ModbusTcpClient as ModbusClient
# from pymodbus.client.sync import ModbusUdpClient as ModbusClient
from pymodbus.client.sync import ModbusSerialClient as ModbusClient

# --------------------------------------------------------------------------- #
# configure the client logging
# --------------------------------------------------------------------------- #
#import logging
#FORMAT = ('%(asctime)-15s %(threadName)-15s '
#          '%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
#logging.basicConfig(format=FORMAT)
#log = logging.getLogger()
#log.setLevel(logging.DEBUG)

UNIT = 0x1


def run_sync_client():
    # ------------------------------------------------------------------------#
    # choose the client you want
    # ------------------------------------------------------------------------#
    # Here is an example of using these options::
    #
    #    client = ModbusClient('localhost', retries=3, retry_on_empty=True)
    # ------------------------------------------------------------------------#
    # from pymodbus.transaction import ModbusRtuFramer
    # client = ModbusClient('localhost', port=5020, framer=ModbusRtuFramer)
    # client = ModbusClient(method='binary', port='/dev/ptyp0', timeout=1)
    # client = ModbusClient(method='ascii', port='/dev/ptyp0', timeout=1)
    # client = ModbusClient(method='rtu', port='/dev/ptyp0', timeout=1,
    #                       baudrate=9600)
    client = ModbusClient(method="rtu", port="/dev/ttyUSB0", stopbits=1, bytesize=8, baudrate=9600)
    client.connect()

    n = 0;
    while(n < 10):
        time.sleep(1)
        temps  = client.read_holding_registers(0xFE00, 10, unit=1) # address, count, slave address
        print(temps.registers)
        n += 1

    # assert(not rq.isError())     # test that we are not an error

    # log.debug("Read input registers")
    # rr = client.read_input_registers(1, 8, unit=UNIT)
    # assert(not rq.isError())     # test that we are not an error

    # ----------------------------------------------------------------------- #
    # close the client
    # ----------------------------------------------------------------------- #
    client.close()


if __name__ == "__main__":
    run_sync_client()
