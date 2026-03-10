from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

packet_number = 0

def get_protocol(packet):
    if packet.haslayer(TCP):
        return "TCP"
    elif packet.haslayer(UDP):
        return "UDP"
    elif packet.haslayer(ICMP):
        return "ICMP"
    else:
        return "Other"

def analyze_packet(packet):
    global packet_number
    packet_number += 1

    if packet.haslayer(IP):

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = get_protocol(packet)

        print("\n---------------------------")
        print("Packet:", packet_number)
        print("Source IP:", src_ip)
        print("Destination IP:", dst_ip)
        print("Protocol:", protocol)

        if packet.haslayer(Raw):
            payload = packet[Raw].load
            print("Payload:", payload[:40])   

print("Capturing packets...\n")

sniff(prn=analyze_packet, store=False)
