import csv
import os

file_name = "packet_logs.csv"

# create file if not present
if not os.path.exists(file_name):

    with open(file_name, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Source IP",
            "Destination IP",
            "Protocol",
            "Source Port",
            "Destination Port",
            "Packet Size"
        ])


# save packet data
def save_packet(src_ip, dst_ip, protocol, src_port, dst_port, size):

    with open(file_name, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            src_ip,
            dst_ip,
            protocol,
            src_port,
            dst_port,
            size
        ])
