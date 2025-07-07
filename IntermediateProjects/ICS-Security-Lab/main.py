from pymodbus.server.sync import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.datastore.store import ModbusSequentialDataBlock
import logging

# Enable logging
logging.basicConfig(level=logging.INFO)

# Create Modbus data context (simulates coils, registers, etc.)
store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*100),  # Discrete Inputs
    co=ModbusSequentialDataBlock(0, [0]*100),  # Coils
    hr=ModbusSequentialDataBlock(0, [0]*100),  # Holding Registers
    ir=ModbusSequentialDataBlock(0, [0]*100),  # Input Registers
)
context = ModbusServerContext(slaves=store, single=True)

# Server Identity (for info/debug)
identity = ModbusDeviceIdentification()
identity.VendorName = "ICS Corp"
identity.ProductCode = "ICS"
identity.VendorUrl = "https://mchyasn.github.io"
identity.ProductName = "Modbus Simulated Server"
identity.ModelName = "ICS-Test-Model"
identity.MajorMinorRevision = "1.0"

# Start Modbus TCP Server (on localhost:5020)
if __name__ == "__main__":
    print("[*] Starting simulated Modbus TCP server on port 5020...")
    StartTcpServer(context, identity=identity, address=("0.0.0.0", 5020))
