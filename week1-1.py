from diagrams import Diagram, Cluster, Edge
from diagrams.generic.compute import Rack
from diagrams.generic.network import Switch
from diagrams.onprem.compute import Server
from diagrams.generic.blank import Blank

# Membuat diagram jaringan sederhana untuk Lab Week 1
with Diagram("Lab Week 1 - Topologi Jaringan Sederhana", 
             filename="lab_week1_topology", 
             show=False,
             direction="TB",
             graph_attr={
                 "fontsize": "18",
                 "bgcolor": "white",
                 "pad": "0.5",
                 "nodesep": "1.0",
                 "ranksep": "1.5"
             }):
    
    # Cluster untuk Office Network
    with Cluster("Jaringan Kantor Sederhana\n192.168.1.0/24", 
                 graph_attr={"bgcolor": "lightblue", "style": "rounded"}):
        
        # PC untuk Staff HRD
        pc_hrd = Server("PC0 - HRD Staff\n192.168.1.10")
        
        # Switch sebagai central connectivity
        office_switch = Switch("Office Switch 2960\nFastEthernet Ports")
        
        # PC untuk Staff Finance  
        pc_finance = Server("PC1 - Finance Staff\n192.168.1.20")
        
        # Koneksi dengan label kabel
        pc_hrd >> Edge(label="FastEthernet0/1\nStraight-Through Cable", 
                      style="solid", color="green") >> office_switch
        
        pc_finance >> Edge(label="FastEthernet0/2\nStraight-Through Cable", 
                          style="solid", color="green") >> office_switch

print("✅ Diagram berhasil dibuat!")
print("📁 File tersimpan sebagai: lab_week1_topology.png")
print("🔍 Gunakan diagram ini untuk:")
print("   - Menjelaskan topologi kepada mahasiswa")
print("   - Referensi visual dalam modul praktikum")
print("   - Dokumentasi hasil praktikum")