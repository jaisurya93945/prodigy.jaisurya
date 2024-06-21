from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
from colorama import Fore, Style, init

init(autoreset=True)

def packet_callback(packet):
    """Callback function to handle captured packets."""
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        protocol = ip_layer.proto

        if protocol == 6:  # TCP
            protocol_name = "TCP"
        elif protocol == 17:  # UDP
            protocol_name = "UDP"
        elif protocol == 1:  # ICMP
            protocol_name = "ICMP"
        else:
            protocol_name = "Other"

        print(f"{Fore.YELLOW}Source IP: {src_ip}")
        print(f"{Fore.CYAN}Destination IP: {dst_ip}")
        print(f"{Fore.GREEN}Protocol: {protocol_name}")

        if TCP in packet:
            tcp_layer = packet[TCP]
            print(f"{Fore.MAGENTA}Source Port: {tcp_layer.sport}")
            print(f"{Fore.RED}Destination Port: {tcp_layer.dport}")

        if UDP in packet:
            udp_layer = packet[UDP]
            print(f"{Fore.MAGENTA}Source Port: {udp_layer.sport}")
            print(f"{Fore.RED}Destination Port: {udp_layer.dport}")

        print(f"{Fore.WHITE}Payload: {bytes(packet[IP].payload)}\n")
    
def main():
    print("Starting network packet sniffer...")
    # Start sniffing
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
