from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src = ip_layer.src
        dst = ip_layer.dst
        proto = ip_layer.proto

        if TCP in packet:
            l4 = packet[TCP]
            print(f"[TCP] {src}:{l4.sport} → {dst}:{l4.dport}")
        elif UDP in packet:
            l4 = packet[UDP]
            print(f"[UDP] {src}:{l4.sport} → {dst}:{l4.dport}")
        elif ICMP in packet:
            print(f"[ICMP] {src} → {dst}")
        else:
            print(f"[IP] {src} → {dst} (Proto {proto})")

if __name__ == "__main__":
    print("[*] Starting packet capture... Press Ctrl+C to stop.")
    sniff(prn=packet_callback, store=0)
