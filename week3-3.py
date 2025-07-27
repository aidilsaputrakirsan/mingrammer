from diagrams import Diagram, Cluster, Edge
from diagrams.generic.compute import Rack
from diagrams.generic.network import Switch
from diagrams.onprem.compute import Server
from diagrams.generic.os import Windows
from diagrams.generic.blank import Blank

# Diagram Before & After untuk menunjukkan proses setup
with Diagram("Lab Week 1 - Before vs After Setup", 
             filename="lab_week1_before_after", 
             show=False,
             direction="TB",
             graph_attr={
                 "fontsize": "16",
                 "bgcolor": "white",
                 "pad": "1.0",
                 "ranksep": "2.0"
             }):
    
    # BEFORE - Sebelum konfigurasi
    with Cluster("❌ BEFORE - Sebelum Konfigurasi", 
                 graph_attr={"bgcolor": "mistyrose", "style": "rounded"}):
        
        before_pc1 = Windows("PC0\nNo IP Address\nNot Connected")
        before_switch = Switch("Switch 2960\nEmpty MAC Table")
        before_pc2 = Windows("PC1\nNo IP Address\nNot Connected")
        
        # Koneksi terputus
        before_pc1 >> Edge(label="❌ No Connection", 
                          style="dotted", color="red") >> before_switch
        before_pc2 >> Edge(label="❌ No Connection", 
                          style="dotted", color="red") >> before_switch
    
    # Blank space untuk separation
    separator = Blank("")
    
    # AFTER - Setelah konfigurasi
    with Cluster("✅ AFTER - Setelah Konfigurasi & Testing", 
                 graph_attr={"bgcolor": "lightgreen", "style": "rounded"}):
        
        after_pc1 = Windows("PC0 - HRD\n192.168.1.10\n✅ Connected")
        after_switch = Switch("Switch 2960\n✅ MAC Table Learned\n✅ Forwarding")
        after_pc2 = Windows("PC1 - Finance\n192.168.1.20\n✅ Connected")
        
        # Koneksi sukses
        after_pc1 >> Edge(label="✅ ping 192.168.1.20\nReply Success!", 
                         style="solid", color="green") >> after_switch
        after_pc2 >> Edge(label="✅ ping 192.168.1.10\nReply Success!", 
                         style="solid", color="green") >> after_switch
    
    # Flow dari before ke after
    before_switch >> Edge(label="Setup Process:\n1. Connect cables\n2. Configure IP\n3. Test connectivity", 
                         style="bold", color="blue") >> separator
    separator >> after_switch

print("✅ Diagram Before & After berhasil dibuat!")
print("📁 File tersimpan sebagai: lab_week1_before_after.png")
print("📚 Penggunaan dalam modul:")
print("   - Menunjukkan progression praktikum")
print("   - Visual untuk troubleshooting")
print("   - Membantu mahasiswa memahami flow setup")