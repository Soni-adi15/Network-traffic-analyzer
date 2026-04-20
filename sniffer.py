from scapy.all import sniff

def start_sniffing(packet_count):
    packets = sniff(
        iface="Wi-Fi",   # 🔥 IMPORTANT
        count=packet_count,
        timeout=10
    )
    return packets
