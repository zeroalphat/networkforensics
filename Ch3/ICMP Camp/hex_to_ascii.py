import binascii


with open("icmp_data.txt", "r") as file:
	read_data = file.read()

for i in read_data.split("\n"):
	print(binascii.unhexlify(i))
