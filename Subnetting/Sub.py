import math

def subnet_calc(ipsplit, masksplit, octchoice):   
	if octchoice not in [2, 3, 4]:
		print("Not a valid Octett Number.")
		return False
		
	iploct = int(ipsplit[octchoice-1])
	maskloct = int(masksplit[octchoice-1])
	jump = 256 - maskloct
	nIP = (2 ** (math.log(jump, 2) + (8 * (4 - octchoice)))) - 2
	sbnr = int(iploct/jump)
	nID = jump*sbnr
	
	if octchoice in [2, 3]:
		last_2 = nID + jump-1
		first = 1
		brdcst = 255
		last = 254
		if octchoice == 2:
			subnet_details = {
				"Original IP": ip,
				"Subnet ID": ".".join(ipsplit[:octchoice - 1] + [str(nID)] + [str(0)] + [str(0)]),
				"First usable IP": ".".join(ipsplit[:octchoice-1] + [str(nID)] + [str(0)] + [str(first)]),
				"Last usable IP":".".join(ipsplit[:octchoice-1] + [str(last_2)]+ [str(last)] + [str(last)]),
				"Broadcast IP":".".join(ipsplit[:octchoice-1] + [str(last_2)] + [str(last)] + [str(brdcst)]),
				"Total usable IPs in subnet": int(nIP),
			}     
			return subnet_details
		
		elif octchoice == 3:
			subnet_details = {
				"Original IP": ip,
				"Subnet ID": ".".join(ipsplit[:octchoice - 1] + [str(nID)] + [str(0)]),
				"First usable IP": ".".join(ipsplit[:octchoice-1] + [str(nID)] + [str(first)]),
				"Last usable IP":".".join(ipsplit[:octchoice-1] + [str(last_2)] + [str(last)]),
				"Broadcast IP":".".join(ipsplit[:octchoice-1] + [str(last_2)] + [str(brdcst)]),
				"Total usable IPs in subnet": int(nIP),
			}
			return subnet_details
        
	elif octchoice == 4:
		first = nID + 1
		brdcst = nID + jump -1
		last = brdcst - 1
		subnet_details = {
			"Original IP": ip,
			"Subnet ID": ".".join(ipsplit[:octchoice - 1] + [str(nID)] + ipsplit[octchoice:]),
			"First usable IP": ".".join(ipsplit[:octchoice - 1] + [str(first)] + ipsplit[octchoice:]),
			"Last usable IP":".".join(ipsplit[:octchoice - 1] + [str(last)] + ipsplit[octchoice:]),
			"Broadcast IP":".".join(ipsplit[:octchoice - 1] + [str(brdcst)] + ipsplit[octchoice:]),
			"Total usable IPs in subnet": int(nIP),
        }
		return subnet_details
    
ip = (input("Please input an IP-Adress: "))
mask = (input("Please input a Subnetting-Mask: "))
octchoice = -1

ipsplit = ip.split(".")
masksplit = mask.split(".")
if masksplit[1] != "255":
	octchoice = 2
elif masksplit[2] != "255":
	octchoice = 3
elif masksplit[3] != "255":
	octchoice = 4

if not subnet_calc(ipsplit, masksplit, octchoice):
    print("Closing Program.")
else:
    subnet_details = subnet_calc(ipsplit, masksplit, octchoice)
    for key, value in subnet_details.items():
        print(f'{key}: {value}')
"""
for testing without input
ip = "10.0.212.0"
mask = "255.255.248.0"
octchoice = 3
"""
