from ncclient import manager

m = manager.connect(host='ios-xe-mgmt.cisco.com',username='developer',password='C1sco12345',port='10000',device_params={'name':'csr'})

Filter = '''
<filter>
<native
	xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
	<ip>
		<route>
			<ip-route-interface-forwarding-list></ip-route-interface-forwarding-list>
		</route>
	</ip>

</native>
</filter>
'''

print(m.get_config('running',Filter))