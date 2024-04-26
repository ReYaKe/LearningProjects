import math

def subnet_calc(ip,mask,octchoice):   
    ipsplit = ip.split(".")
    masksplit = mask.split(".")
    iploct = int(ipsplit[octchoice-1])
    maskloct = int(masksplit[octchoice-1])
    jump = 256 - maskloct
    nIP = 2 ** (math.log(jump, 2) + (8 * (4 - octchoice)))
    sbnr = int(iploct/jump)
    nID = jump*sbnr
    if octchoice != 4:
        last_2 = nID + jump-1
        first = 0
        brdcst = 255
        last = 254
        subnet_details = {
        "Original IP": ip,
        "Subnet ID": ".".join(ipsplit[:octchoice - 1] + [str(nID)] + ipsplit[octchoice:]),
        "First usable IP": ".".join(ipsplit[:octchoice-1] + [str(nID)] + [str(first)]),
        "Last usable IP":".".join(ipsplit[:octchoice-1] + [str(last_2)] + [str(last)]),
        "Broadcast IP":".".join(ipsplit[:octchoice-1] + [str(last_2)] + [str(brdcst)]),
        "Total usable IPs in subnet": int(nIP),
        }
         
    else:
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
octchoice = int(input("Please input in which Octett your Subnet is: "))

"""
for testing without input
ip = "10.0.212.0"
mask = "255.255.248.0"
octchoice = 3
subnet_details = subnet_calc(ip,mask,octchoice)"""


for key, value in subnet_details.items():
    print(f'{key}: {value}')