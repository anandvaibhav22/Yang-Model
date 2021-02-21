from ncclient import manager

m = manager.connect(host='ios-xe-mgmt.cisco.com',username='developer',password='C1sco12345',port='10000',device_params={'name':'csr'})
#to checnge the 

Config = '''

<config>
	<native
		xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
		<username>
			<name>cisco1</name>
			<privilege>15</privilege>
			<secret>
				<encryption>0</encryption>
				<secret>password1234</secret>
			</secret>
		</username>
	</native>
</config>

'''
data = m.edit_config(Config,target='running')
print(data)

'''
<?xml version="1.0" encoding="UTF-8"?>
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:197ecb64-9471-46be-a6fa-175a3208a5b5" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><ok/></rpc-reply>

output from switch
csr1000v#sh run | in user
username developer privilege 15 secret 5 $1$HtLC$7Kj3hGBoDnSHzdEeR/2ix.
username cisco privilege 15 secret 5 $1$o1Bw$8kTqTgRZebC/IDFurHnco/
username root privilege 15 secret 5 $1$vpY7$mh9d69ui3koSaITBi8k9D/
username cisco1 privilege 15 secret 5 $1$gtnq$E3BBLzrx0xn7sToQSZmpN/             >>> the one we have created 


'''