import math
ip = (input("Please input an IP-Adress: "))
mask = (input("Please input a Subnetting-Mask: "))
octchoice = int(input("Please input in which Octett your Subnet is: "))
ipsplit = ip.split(".")
masksplit = mask.split(".")
x = 2
print(ipsplit)
print(masksplit)
print(octchoice)
if octchoice == 4:    
    iploct = int(ipsplit[-1])
    maskloct = int(masksplit[-1]) 
    jump = 256 - maskloct
    nIP = jump - 2
    sbnr = int(iploct/jump)
    nID = jump*sbnr
    brdcst = nID + jump - 1
    first = nID + 1
    last = brdcst - 1
elif octchoice == 3:
    iploct = int(ipsplit[-2])
    maskloct = int(masksplit[-2]) 
    jump = 256 - maskloct
    nIP = 2**(math.log(jump, 2) + 8)
    sbnr = int(iploct/jump)
    nID = jump*sbnr
    brdcst = nID + jump - 1
    first = nID + 1
    last = brdcst - 1
elif octchoice == 2:
    iploct = int(ipsplit[-3])
    maskloct = int(masksplit[-3]) 
    jump = 256 - maskloct
    nIP = 2**(math.log(jump, 2) + 16)
    sbnr = int(iploct/jump)
    nID = jump*sbnr
    brdcst = nID + jump - 1
    first = nID + 1
    last = brdcst - 1
elif octchoice == 1:
    iploct = int(ipsplit[-4])
    maskloct = int(masksplit[-4]) 
    jump = 256 - maskloct
    nIP = 2**(math.log(jump, 2) + 24)
    sbnr = int(iploct/jump)
    nID = jump*sbnr
    brdcst = nID + jump - 1
    first = nID + 1
    last = brdcst - 1
else:
    print("No")
    

print(f"Jump:{jump}")
print(f"Host IPs:{nIP}")
print(f"Subnumber:{sbnr}")
print(f"Network-ID:{nID}")
print(f"Broadcast-IP:{brdcst}")
print(f"First Host IP:{first}")
print(f"Last Host IP:{last}")