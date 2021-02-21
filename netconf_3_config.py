from ncclient import manager

m = manager.connect(host='ios-xe-mgmt.cisco.com',username='developer',password='C1sco12345',port='10000',device_params={'name':'csr'})
#to checnge the 

Config = '''
<config>		
<interfaces
	xmlns="http://openconfig.net/yang/interfaces">
	<interface>
		<name>GigabitEthernet2</name>
		<config>
			<name>GigabitEthernet2</name>
			<type
				xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd
					
			</type>
			<description>abc</description>
			<enabled>true</enabled>
		</config>
		<subinterfaces>
			<subinterface>
				<index>0</index>
				<config>
					<index>0</index>
					<description>cde</description>
					<enabled>true</enabled>
				</config>
				<ipv4
					xmlns="http://openconfig.net/yang/interfaces/ip">
					<addresses>
						<address>
							<ip>10.10.20.22</ip>
							<config>
								<ip>10.10.20.22</ip>
								<prefix-length>24</prefix-length>
							</config>
						</address>
					</addresses>
				</ipv4>
</interfaces>
</config>
'''
data = m.edit_config(Config,target='running')
print(data)