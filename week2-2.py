from diagrams import Diagram, Cluster, Edge
from diagrams.generic.compute import Rack
from diagrams.generic.network import Switch, Subnet
from diagrams.onprem.compute import Server
from diagrams.generic.os import Windows
from diagrams.onprem.network import Internet

# Diagram yang lebih detailed dengan flow komunikasi
with Diagram("Lab Week 1 - Detail Komunikasi & Testing", 
             filename="lab_week1_detailed", 
             show=False,
             direction="LR",
             graph_attr={
                 "fontsize": "16",
                 "bgcolor": "white",
                 "pad": "0.8"
             }):
    
    # Cluster untuk menunjukkan subnet
    with Cluster("LAN Segment\n192.168.1.0/24", 
                 graph_attr={"bgcolor": "lightyellow", "style": "rounded"}):
        
        # PC-PC dengan detail OS
        pc0 = Windows("PC0\nHRD Staff\n192.168.1.10\nFastEthernet0")
        pc1 = Windows("PC1\nFinance Staff\n192.168.1.20\nFastEthernet0")
        
        # Switch dengan detail ports
        switch = Switch("Cisco 2960 Switch\nMAC Address Table:\n- Fa0/1: PC0 MAC\n- Fa0/2: PC1 MAC")
        
        # Koneksi dengan detail protocol flow
        pc0 >> Edge(label="1. ARP Request\n2. ICMP Echo Request", 
                   style="dashed", color="blue") >> switch
        
        switch >> Edge(label="3. Forward to Fa0/2\n4. ICMP Echo Reply", 
                      style="dashed", color="orange") >> pc1
        
    # Cluster untuk testing commands
    with Cluster("Testing Commands", 
                 graph_attr={"bgcolor": "lightgreen", "style": "rounded"}):
        test_cmd = Rack("Command Prompt\n\n> ping 192.168.1.20\nReply from 192.168.1.20:\nbytes=32 time<1ms TTL=128\n\n✅ Connectivity Success!")

print("✅ Diagram detailed berhasil dibuat!")
print("📁 File tersimpan sebagai: lab_week1_detailed.png")
print("🎯 Diagram ini menunjukkan:")
print("   - Detail konfigurasi IP address")
print("   - Flow komunikasi ARP dan ICMP")
print("   - Hasil testing yang diharapkan")
print("   - MAC address learning pada switch")