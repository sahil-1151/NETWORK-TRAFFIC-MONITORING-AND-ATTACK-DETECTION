from scapy.all import *
from scapy.layers.inet import IP

# this function run when packet is come
def packet_info(packet):

    # only check IP packets for now
    if packet.haslayer(IP):

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        print("Source IP :", src_ip)
        print("Destination IP :", dst_ip)
        print("-------------------------")


# start packet capture
def start_capture():

    print("Packet capture is starting...")
    print("Press Ctrl + C to stop")

    # store=False because we not need save packets in memory
    sniff(prn=packet_info, store=False)


if __name__ == "__main__":
    start_capture()


