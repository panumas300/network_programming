from pysnmp.hlapi import *

communityName = 'public'
ipAddress = '10.4.15.111'
OID = '1.3.6.1.2.1.1.1.0'

errorIndication, errorStatus, errorIndex, varBinds = next(
    nextCmd(SnmpEngine(),
            CommunityData(communityName),
            UdpTransportTarget((ipAddress, 161)),
            ContextData(),
            ObjectType(ObjectIdentity(OID)))
)

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) -1][0] or '?'))
else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))