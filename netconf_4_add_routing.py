from ncclient import manager

m = manager.connect(host='ios-xe-mgmt.cisco.com',username='developer',password='C1sco12345',port='10000',device_params={'name':'csr'})
#to checnge the 	

Configuration='''
<config>
	<native
			xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
			<ip>
				<route>
					<ip-route-interface-forwarding-list>
						<prefix>0.0.0.0</prefix>
						<mask>255.255.255.0</mask>
						<fwd-list>
							<fwd>GigabitEthernet1</fwd>
							<interface-next-hop>
								<ip-address>10.10.20.1</ip-address>
							</interface-next-hop>
						</fwd-list>
					</ip-route-interface-forwarding-list>
				</route>
			</ip>
		</native>
</config>
	'''

data = m.edit_config(Configuration,target='running')
print(data)

'''
output
before 
csr1000v#sh run | in ip route
ip route 0.0.0.0 0.0.0.0 GigabitEthernet1 10.10.20.254
after
csr1000v#sh run | in ip route
ip route 0.0.0.0 0.0.0.0 GigabitEthernet1 10.10.20.254
ip route 0.0.0.0 255.255.255.0 GigabitEthernet1 10.10.20.1
<?xml version="1.0" encoding="UTF-8"?>
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:81b2cada-9365-424e-9345-dcff77b97e12" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><ok/></rpc-reply>
'''

