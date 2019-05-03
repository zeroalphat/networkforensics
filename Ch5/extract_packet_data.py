from scapy.all import *
import base64

# read pcap file 
network_packets = rdpcap('gnome.pcap')
decoded_commands = []
decoded_data = ""

for packet in network_packets:
	if DNSQR in packet:
		if packet[DNS].id == 0x1337:
			decoded_data = base64.b64decode(packet[DNS].an.rdata[0])
		if 'FILE:' in str(decoded_data):
			continue
		else:
			decoded_commands.append(decoded_data)

for command in decoded_commands:
	if len(command)>1:
		print(str(command.rstrip()))
