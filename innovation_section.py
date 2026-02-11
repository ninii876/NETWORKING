def detect_ip_conflicts():
    n=int(input("enter the number of devices:"))
    ips=[]
    for i in range(n):
        ip=input("enter IP:")
        ips.append(ip)
    found= False
    for i in range(n):
        for j in range(i+1,n):
                if ips[i] == ips[j]:
                   print("Duplicate IP found:", ips[i])
                   found = True
    if (found== False):
        print("No duplicate ip")

