from collections import Counter

def get_protocol_distribution(packets):
    protocols = []

    for pkt in packets:
        if pkt.haslayer("TCP"):
            protocols.append("TCP")
        elif pkt.haslayer("UDP"):
            protocols.append("UDP")
        elif pkt.haslayer("ICMP"):
            protocols.append("ICMP")
        else:
            protocols.append("Other")

    return Counter(protocols)


def get_top_ips(packets):
    ips = []

    for pkt in packets:
        if pkt.haslayer("IP"):
            ips.append(pkt["IP"].src)

    return Counter(ips).most_common(5)