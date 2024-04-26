ip = (input("Please input an IP-Adress: "))
mask = (input("Please input a Subnetting-Mask: "))
octchoice = input("Please input in which Octett your Subnet is: ")

ipsplit = ip.split(".")
masksplit = mask.split(".")
print(ipsplit)
print(masksplit)
iploct = int(ipsplit[octchoice])
maskloct = int(masksplit[octchoice])



jump = 256 - maskloct
nIP = jump - 2
sbnr = int(iploct/jump)
nID = jump*sbnr
brdcst = nID + jump - 1
first = nID + 1
last = brdcst - 1

print(jump)
print(nIP)
print(sbnr)
print(nID)
print(brdcst)
print(first)
print(last)