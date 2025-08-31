from scapy.all import sniff, IP, IPv6, ARP

def packet_handler(packet):
    if IP in packet:  # IPv4 packets
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        print(f"[IPv4] {src_ip} → {dst_ip} | Protocol: {proto}")

    elif IPv6 in packet:  # IPv6 packets
        src_ip = packet[IPv6].src
        dst_ip = packet[IPv6].dst
        proto = packet[IPv6].nh
        print(f"[IPv6] {src_ip} → {dst_ip} | Next Header: {proto}")

    elif ARP in packet:  # ARP requests/replies
        src_mac = packet[ARP].hwsrc
        src_ip = packet[ARP].psrc
        dst_mac = packet[ARP].hwdst
        dst_ip = packet[ARP].pdst
        print(f"[ARP] {src_mac} ({src_ip}) → {dst_mac} ({dst_ip})")

    else:  # Other protocols
        print(f"[Other] {packet.summary()}")

print("--------------- Packet Sniffing Tool ---------------")
print("Capturing packets... Press Ctrl+C to stop.\n")

# Start sniffing (might require admin/root privileges)
sniff(prn=packet_handler, store=False)
