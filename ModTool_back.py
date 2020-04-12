#!usr/bin/env/python

from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import sys
import py_compile
print ("Welcome to the Register & Coils updater")
choos=input("Please choose Reg or Coil:   ")
if choos== "Reg":
   print ("Regiters updater")
   Srv_ip=input("Insert IP: ")
   reg_num=input("Insert Register Number: ")
   reg_val=input("Insert Reg Value: ")
   client=ModbusClient(str(Srv_ip), port=502)
   client.write_register(int(reg_num), int(reg_val))
   rr=client.read_holding_registers(int(reg_num),1, unit=0x01).registers[0]
   print ("The new value of Register",reg_num,"is",rr)
   client.close()
elif choos=="Coil":
   print ("Coils updater")
   Srv_ip=input("Insert IP: ")
   reg_num=input("Insert Coil Number: ")
   reg_val=input("Insert Coil Value (1/0): ")
   client=ModbusClient(str(Srv_ip), port=502)
   client.write_coil(int(reg_num), int(reg_val))
   rr=client.read_coils(int(reg_num),1, unit=0x01)
   print ("The new value of Register number",reg_num,"is",rr.bits[0])
   client.close()
i=0
b=0
print ("The first 10 registers:")
while i<9:
    tt=client.read_holding_registers(i,1, unit=0x01).registers[0]
    print ("Reg num",i,tt)
    i+=1
print ("The first 10 Coils:")
while b<9:
    pp=client.read_coils(b,1, unit=0x01)
    print ("Coil num",b,pp.bits[0])
    b+=1
print ("Till next time, Bye Bye")
