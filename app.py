import streamlit as st
from sniffer import start_sniffing
from analyzer import get_protocol_distribution, get_top_ips
from utils import get_bandwidth_usage

st.title("📡 Network Traffic Analyzer")

# Packet selection
packet_count = st.slider("Select number of packets", 10, 200, 50)

# Capture
if st.button("Start Traffic Capture"):

    # FIX: Spinner instead of freeze UI
    with st.spinner("Capturing packets..."):
        packets = start_sniffing(packet_count)

    st.success(f"Captured {len(packets)} packets")

    if len(packets) == 0:
        st.error("No packets captured! Check admin rights or network activity.")
    else:
        # Protocol chart
        st.subheader("📊 Protocol Distribution")
        protocol_data = get_protocol_distribution(packets)
        st.bar_chart(protocol_data)

        # Top IPs
        st.subheader("🌐 Top Source IPs")
        top_ips = get_top_ips(packets)

        for ip, count in top_ips:
            st.write(f"{ip} → {count} packets")

        # Packet preview
        st.subheader("📦 Packet Preview")
        for pkt in packets[:10]:
            st.text(pkt.summary())


# Bandwidth
st.subheader("📶 Bandwidth Usage")

if st.button("Check Bandwidth"):
    upload, download = get_bandwidth_usage()

    st.write(f"⬆ Upload: {upload / 1024:.2f} KB/s")
    st.write(f"⬇ Download: {download / 1024:.2f} KB/s")