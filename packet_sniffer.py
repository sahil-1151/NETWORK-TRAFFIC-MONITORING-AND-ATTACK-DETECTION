from packet_logger import save_packet
from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

tcp_count = 0
udp_count = 0
icmp_count = 0


def packet_info(packet):

    global tcp_count, udp_count, icmp_count

    if packet.haslayer(IP):

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        size = len(packet)

        protocol = "Unknown"
        src_port = "-"
        dst_port = "-"

        # check packet type
        if packet.haslayer(TCP):
            protocol = "TCP"
            tcp_count += 1

            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport

        elif packet.haslayer(UDP):
            protocol = "UDP"
            udp_count += 1

            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport

        elif packet.haslayer(ICMP):
            protocol = "ICMP"
            icmp_count += 1

		save_packet(
   		 src_ip,
    		dst_ip,
    		protocol,
    		src_port,
    		dst_port,
    		size
		)

        print("\n---------------------")
        print("Source IP :", src_ip)
        print("Destination IP :", dst_ip)
        print("Protocol :", protocol)
        print("Packet size :", size)

        print("Source Port :", src_port)
        print("Destination Port :", dst_port)

        print("TCP :", tcp_count)
        print("UDP :", udp_count)
        print("ICMP :", icmp_count)


def start_capture():

    print("Packet capture is starting...")
    print("Press Ctrl + C to stop")

    sniff(prn=packet_info, store=False)


if __name__ == "__main__":
    start_capture() 
