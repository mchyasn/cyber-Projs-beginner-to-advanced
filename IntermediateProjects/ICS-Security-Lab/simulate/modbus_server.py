from pymodbus.server.sync import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
import logging

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

# Setup data store
store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*100),
    co=ModbusSequentialDataBlock(0, [0]*100),
    hr=ModbusSequentialDataBlock(0, [0]*100),
    ir=ModbusSequentialDataBlock(0, [0]*100),
)
context = ModbusServerContext(slaves=store, single=True)

# Server identity
identity = ModbusDeviceIdentification()
identity.VendorName = 'mchyasn Labs'
identity.ProductCode = 'ICS1'
identity.VendorUrl = 'https://github.com/mchyasn'
identity.ProductName = 'ICS Simulated PLC'
identity.ModelName = 'ModbusServer'
identity.MajorMinorRevision = '1.0'

if __name__ == "__main__":
    print("[*] Starting simulated ICS Modbus TCP server on port 5020...")
    StartTcpServer(context, identity=identity, address=("0.0.0.0", 5020))
