
def vlan_segmentation():
    devices={}
    n=int(input("enter the number of devices:"))
    for i in range(n):
        name=input("enter the device nameL:")
        vlan=input("enter the VLAN ID:")
        if vlan not in devices:
            devices[vlan]=[]
        devices[vlan].append(name)
    print("vlan groups:")
    for vlan in devices:
        print("VLAN", vlan, ":", devices[vlan])

pass