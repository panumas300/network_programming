from pysnmp.hlapi import *
g = getCmd(
    SnmpEngine(), CommunityData('public'), UdpTransportTarget(
        ('10.4.15.111', 161)), ContextData(), ObjectType(
            ObjectIdentity('1.3.6.1.2.1.1.1.0')))
errorIndication, errorStatus, errorIndex, varBinds = next(g)
for varBind in varBinds:
    print(' = '.join([x.prettyPrint() for x in varBind]))