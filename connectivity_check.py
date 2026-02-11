
def check_connectivity():
    devices=[]
    n=int(input("enter number of devices:"))
    for i in range(n):
        name = input("Enter device name: ")
        vlan = int(input("Enter VLAN ID: "))
        ip_address=input("enter IP address:")

        devices.append({"name": name, "vlan": vlan,"ip_address":ip_address})

    inter_vlan = input("Is inter-VLAN routing enabled? (yes/no): ")

    print("device connectivity:")
    for i in range(len(devices)):
        for j in range(i+1,len(devices)):
             
             if (devices[i]["vlan"] == devices[j]["vlan"]):
                print(devices[i]["name"], "(", devices[i]["ip_address"], ") and",
                      devices[j]["name"], "(", devices[j]["ip_address"], ") can communicate")
             
             elif inter_vlan == "yes":
                print(devices[i]["name"], "(", devices[i]["ip_address"], ") and",
                      devices[j]["name"], "(", devices[j]["ip_address"], ") can communicate")

             else:
                print(devices[i]["name"], "(", devices[i]["ip_address"], ") and",
                      devices[j]["name"], "(", devices[j]["ip_address"], ") cannot communicate")
        inter_vlan = False
pass


