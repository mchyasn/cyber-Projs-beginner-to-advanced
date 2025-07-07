from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.datastore import ModbusSequentialDataBlock
import logging

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*100),
    co=ModbusSequentialDataBlock(0, [0]*100),
    hr=ModbusSequentialDataBlock(0, [0]*100),
    ir=ModbusSequentialDataBlock(0, [0]*100))

context = ModbusServerContext(slaves=store, single=True)

print("[*] Starting Modbus server on localhost:5020")
StartTcpServer(context, address=("localhost", 5020))
