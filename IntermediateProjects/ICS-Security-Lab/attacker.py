from pymodbus.client.sync import ModbusTcpClient

TARGET_IP = "127.0.0.1"
TARGET_PORT = 5020

client = ModbusTcpClient(TARGET_IP, port=TARGET_PORT)
client.connect()

print("[*] Connected to Modbus server")

# Read 5 holding registers starting from address 0
result = client.read_holding_registers(0, 5, unit=1)
if result.isError():
    print("[!] Failed to read registers")
else:
    print("[+] Holding Registers (0-4):", result.registers)

# Write value 1337 to holding register 0
write_result = client.write_register(0, 1337, unit=1)
if write_result.isError():
    print("[!] Failed to write to register")
else:
    print("[+] Successfully wrote 1337 to register 0")

# Confirm write
confirm = client.read_holding_registers(0, 1, unit=1)
if confirm.isError():
    print("[!] Failed to confirm write")
else:
    print("[+] Confirmed value in register 0:", confirm.registers[0])

client.close()
