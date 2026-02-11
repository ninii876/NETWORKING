def analyze_ip():
    print("IP ANALYSIS")
    ip=input("enter IP address:")
    parts=ip.split(".")
    if len(parts) !=4:
        print("Invalid IP format")
        return

    for part in parts:
        if not part.isdigit():   
            print("Invalid IP: Only numbers allowed")
            return
        
        number = int(part)
        if number < 0 or number > 255:   
            print("Invalid IP: Each number must be between 0 and 255")
            return
    first_octet = int(parts[0])
    last_octet = int(parts[3])

    if first_octet == 10:
        print("IP Type: Private")
    elif first_octet == 172:
        print("IP Type: Private")
    elif first_octet == 192 and int(parts[1]) == 168:
        print("IP Type: Private")
    else:
        print("IP Type: Public")
    network_id = parts[0] + "." + parts[1] + "." + parts[2] + ".0"
    broadcast = parts[0] + "." + parts[1] + "." + parts[2] + ".255"

    print("Network ID:", network_id)
    print("Broadcast Address:", broadcast)

    if last_octet == 0:
        print("Role: Network Address")
    elif last_octet == 255:
        print("Role: Broadcast Address")
    else:
        print("Role: Usable Host")
        print("Total Usable Hosts: 254")

pass

