from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.platypus import Table, TableStyle, Paragraph, SimpleDocTemplate, Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# Set up document
file_path = "/mnt/data/Water_Management_India.pdf"
doc = SimpleDocTemplate(file_path, pagesize=A4)
styles = getSampleStyleSheet()
story = []

# Title
story.append(Paragraph("<b>Status of Water Management in India</b>", styles["Title"]))

# -------- Page 1 --------
story.append(Paragraph("<b>Page 1 — Water Availability & Demand</b>", styles["Heading2"]))
text1 = """
India holds about 18% of the world’s population but only 4% of its freshwater resources. 
Per capita water availability is steadily declining, projected to fall below 1500 m³ by 2050, 
indicating water stress. About 60% of irrigation depends on groundwater. 
Demand projections show irrigation as the largest consumer, followed by domestic and industrial needs.
"""
story.append(Paragraph(text1, styles["BodyText"]))

data1 = [["Year", "Irrigation (BCM)", "Domestic (BCM)", "Industry (BCM)"],
         ["2010", "688", "56", "42"],
         ["2025", "910", "73", "102"],
         ["2050", "1072", "102", "161"]]
table1 = Table(data1)
table1.setStyle(TableStyle([("GRID", (0,0), (-1,-1), 1, colors.black),
                            ("BACKGROUND", (0,0), (-1,0), colors.lightgrey)]))
story.append(table1)

# -------- Page 2 --------
story.append(Paragraph("<b>Page 2 — Key Challenges & Stress Factors</b>", styles["Heading2"]))
text2 = """
India’s rainfall is highly seasonal: nearly 80-90% falls during the monsoon in just four months, 
leading to floods and poor recharge. 60% of districts face critical groundwater stress due to over-extraction. 
Satellite data show groundwater storage declining even in years with normal rainfall. 
Himalayan springs are drying, further straining water supply.
"""
story.append(Paragraph(text2, styles["BodyText"]))

data2 = [["Category", "Districts Affected (%)"],
         ["Over-exploited", "17"],
         ["Critical", "14"],
         ["Semi-critical", "11"],
         ["Safe", "58"]]
table2 = Table(data2)
table2.setStyle(TableStyle([("GRID", (0,0), (-1,-1), 1, colors.black),
                            ("BACKGROUND", (0,0), (-1,0), colors.lightgrey)]))
story.append(table2)

# -------- Page 3 --------
story.append(Paragraph("<b>Page 3 — Institutional Responses & Schemes</b>", styles["Heading2"]))
text3 = """
The government has launched several schemes:
- Namami Gange Programme: River cleaning and rejuvenation, budget of ~₹22,500 crore.
- Atal Bhujal Yojana: Community-led groundwater management in 7 states.
- Mission Kakatiya (Telangana): Restoration of 46,000+ irrigation tanks.
- Kudimaramathu (Tamil Nadu): Revival of traditional water bodies.
- AMRUT: Urban water supply and sewage infrastructure.
"""
story.append(Paragraph(text3, styles["BodyText"]))

data3 = [["Scheme", "Focus", "Budget (₹ crore)"],
         ["Namami Gange", "River cleaning", "22,500"],
         ["Atal Bhujal", "Groundwater", "6,000"],
         ["Mission Kakatiya", "Tanks (Telangana)", "–"],
         ["Kudimaramathu", "Tanks (Tamil Nadu)", "–"],
         ["AMRUT", "Urban water", "78,910"]]
table3 = Table(data3)
table3.setStyle(TableStyle([("GRID", (0,0), (-1,-1), 1, colors.black),
                            ("BACKGROUND", (0,0), (-1,0), colors.lightgrey)]))
story.append(table3)

# -------- Page 4 --------
story.append(Paragraph("<b>Page 4 — Innovations & Data Tools</b>", styles["Heading2"]))
text4 = """
Data-driven approaches are emerging for better water governance. 
India-WRIS provides real-time water reservoir data. Aquifer mapping by the Central Groundwater Board (CGWB) 
supports localized management. New indices like the District Flood Severity Index (DFSI) are being tested 
for flood planning. These digital tools increase transparency and enable data-informed policies.
"""
story.append(Paragraph(text4, styles["BodyText"]))

data4 = [["Tool", "Purpose"],
         ["India-WRIS", "Reservoir and river data"],
         ["CGWB Aquifer Mapping", "Groundwater planning"],
         ["DFSI", "Flood severity assessment"]]
table4 = Table(data4)
table4.setStyle(TableStyle([("GRID", (0,0), (-1,-1), 1, colors.black),
                            ("BACKGROUND", (0,0), (-1,0), colors.lightgrey)]))
story.append(table4)

# -------- Page 5 --------
story.append(Paragraph("<b>Page 5 — Recent Developments & Policy Drivers</b>", styles["Heading2"]))
text5 = """
Recent developments highlight state-level efforts. 
In Madhya Pradesh, Jal Jeevan Mission aims to provide tap water to all rural households, 
with ~16,000 villages already covered. Uttar Pradesh has scaled up Amrit Sarovar and pond rejuvenation 
for water harvesting. Himalayan states face urgent need for spring-shed development programs 
to restore water security for mountain communities.
"""
story.append(Paragraph(text5, styles["BodyText"]))

data5 = [["State", "Key Initiative", "Status"],
         ["Madhya Pradesh", "Jal Jeevan Mission", "16,000/28,000 villages covered"],
         ["Uttar Pradesh", "Amrit Sarovar, ponds", "Thousands created"],
         ["Himalayan States", "Spring-shed revival", "Ongoing need"]]
table5 = Table(data5)
table5.setStyle(TableStyle([("GRID", (0,0), (-1,-1), 1, colors.black),
                            ("BACKGROUND", (0,0), (-1,0), colors.lightgrey)]))
story.append(table5)

# Build PDF
doc.build(story)
file_path
