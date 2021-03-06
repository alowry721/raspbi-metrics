from pysnmp.hlapi import (
    getCmd, SnmpEngine, CommunityData, UdpTransportTarget, ContextData, ObjectType, ObjectIdentity
)


iterator = getCmd(SnmpEngine(),
                  CommunityData('public'),
                  UdpTransportTarget(('localhost', 161)),
                  ContextData(),
                  ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))

errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

if errorIndication:  # SNMP engine errors
    print(errorIndication)
else:
    if errorStatus:  # SNMP agent errors
        print('%s at %s' % (errorStatus.prettyPrint(), varBinds[int(errorIndex)-1] if errorIndex else '?'))
    else:
        for varBind in varBinds:  # SNMP response contents
            print(' = '.join([x.prettyPrint() for x in varBind]))

