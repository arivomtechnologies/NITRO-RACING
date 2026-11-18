import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Load the workbook
wb = openpyxl.load_workbook("Nitro_Racing_Application_Data_Flow.xlsx")

NAVY = "101D35"
ORANGE = "F15A24"
LIGHT_GREY = "F4F6F9"
WHITE = "FFFFFF"
BORDER_GREY = "D6D9DD"

font_col_hdr = Font(name="Calibri", size=10, bold=True, color=WHITE)
font_sec_hdr = Font(name="Calibri", size=12, bold=True, color=WHITE)
font_data = Font(name="Calibri", size=9.5, color="17191D")
font_bold = Font(name="Calibri", size=9.5, bold=True, color="17191D")
font_code = Font(name="Consolas", size=9, bold=True, color="101D35")

fill_navy = PatternFill(start_color=NAVY, end_color=NAVY, fill_type="solid")
fill_orange = PatternFill(start_color=ORANGE, end_color=ORANGE, fill_type="solid")
fill_light = PatternFill(start_color=LIGHT_GREY, end_color=LIGHT_GREY, fill_type="solid")
fill_white = PatternFill(start_color=WHITE, end_color=WHITE, fill_type="solid")
fill_tag_green = PatternFill(start_color="D1E7DD", end_color="D1E7DD", fill_type="solid")
fill_tag_orange = PatternFill(start_color="FFE5D9", end_color="FFE5D9", fill_type="solid")

thin_border = Border(
    left=Side(style='thin', color=BORDER_GREY),
    right=Side(style='thin', color=BORDER_GREY),
    top=Side(style='thin', color=BORDER_GREY),
    bottom=Side(style='thin', color=BORDER_GREY)
)

# ---------------------------------------------------------
# UPDATE SHEET 5: SERVICE CONFIG & SPARE PARTS
# ---------------------------------------------------------
ws5 = wb["Service Config & Parts (Data)"]

# Clear existing rows from row 5 down
for r in range(5, ws5.max_row + 1):
    for c in range(1, 15):
        ws5.cell(row=r, column=c).value = None
        ws5.cell(row=r, column=c).fill = fill_white
        ws5.cell(row=r, column=c).border = Border()

# 1. Re-write Service Catalogue including Superbike & Modifications
ws5.cell(row=4, column=1, value="1. EXPANDED SERVICE CATALOGUE (INCL. SUPERBIKES & MODIFICATIONS)").font = font_sec_hdr
ws5.cell(row=4, column=1).fill = fill_navy

headers5_s = [
    "Service Code", "Service Operation Name", "Category", "Std Duration", 
    "Base Labor Rate", "GST Rate", "Total Labor", "Applicable Models", "Status"
]
for col_idx, h in enumerate(headers5_s, 1):
    cell = ws5.cell(row=5, column=col_idx, value=h)
    cell.font = font_col_hdr
    cell.fill = fill_navy
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border = thin_border

expanded_services = [
    ("SRV-SBK-01", "Superbike Full Desmo / Valve Clearance & Major Service", "Superbike Service", "240 Mins", "INR 3,500.00", "18%", "INR 4,130.00", "Superbikes (600cc - 1000cc+)", "ACTIVE"),
    ("SRV-SBK-02", "Superbike Computerized OBD-2 Diagnostic & Throttle Sync", "Superbike Service", "60 Mins", "INR 1,200.00", "18%", "INR 1,416.00", "Electronic FI / Superbikes", "ACTIVE"),
    ("SRV-SBK-03", "Superbike Radiator High-Performance Coolant Flush (Engine Ice)", "Superbike Service", "45 Mins", "INR 650.00", "18%", "INR 767.00", "Liquid Cooled / Superbikes", "ACTIVE"),
    ("SRV-MOD-01", "Performance Exhaust Slip-On / Full System Installation", "Modifications & Modz", "90 Mins", "INR 1,500.00", "18%", "INR 1,770.00", "All Compatible Bikes", "ACTIVE"),
    ("SRV-MOD-02", "ECU Stage 1 / Stage 2 Fuel Map Flashing & Dyno Calibration", "Modifications & Modz", "120 Mins", "INR 2,800.00", "18%", "INR 3,304.00", "Fuel Injected & Track Bikes", "ACTIVE"),
    ("SRV-MOD-03", "Auxiliary Lights, Fog Lamps & Custom Harness Wiring", "Modifications & Modz", "75 Mins", "INR 850.00", "18%", "INR 1,003.00", "Touring & Adventure Bikes", "ACTIVE"),
    ("SRV-MOD-04", "Crash Guard, Frame Sliders & Engine Protection Installation", "Modifications & Modz", "60 Mins", "INR 500.00", "18%", "INR 590.00", "All Motorcycles", "ACTIVE"),
    ("SRV-MOD-05", "Tail Tidy, Custom Handlebar & Ergonomic Lever Setup", "Modifications & Modz", "60 Mins", "INR 650.00", "18%", "INR 767.00", "Street & Sport Bikes", "ACTIVE"),
    ("SRV-GEN-01", "General Periodic Service (50-Point Standard Inspection)", "Periodic Maintenance", "90 Mins", "INR 650.00", "18%", "INR 767.00", "Commuter & Sports (100-250cc)", "ACTIVE"),
    ("SRV-OIL-02", "Engine Oil & Filter Replacement Service", "Engine Operations", "30 Mins", "INR 150.00", "18%", "INR 177.00", "All Two-Wheelers", "ACTIVE"),
    ("SRV-BRK-03", "Front & Rear Brake Caliper Overhaul & Fluid Bleeding", "Brake System", "45 Mins", "INR 350.00", "18%", "INR 413.00", "Disc Brake Bikes", "ACTIVE"),
    ("SRV-WSH-06", "Premium Foam Wash, Engine Degreasing & Ceramic Polish", "Detailing & Wash", "60 Mins", "INR 550.00", "18%", "INR 649.00", "All Motorcycles", "ACTIVE")
]

for idx, s in enumerate(expanded_services, start=6):
    ws5.row_dimensions[idx].height = 22
    for c_i, val in enumerate(s, 1):
        cell = ws5.cell(row=idx, column=c_i, value=val)
        cell.font = font_data
        cell.border = thin_border
        cell.fill = fill_white if idx % 2 == 1 else fill_light
        if c_i in [1, 4, 6, 7, 9]:
            cell.alignment = Alignment(horizontal="center", vertical="center")
            if c_i == 1:
                cell.font = font_code
        elif c_i == 5:
            cell.alignment = Alignment(horizontal="right", vertical="center")
            cell.font = font_bold
        else:
            cell.alignment = Alignment(horizontal="left", vertical="center")

# 2. Re-write Spare Parts Master including Superbike & Modification Parts
start_p = len(expanded_services) + 8
ws5.cell(row=start_p, column=1, value="2. SPARE PARTS & PERFORMANCE COMPONENTS MASTER").font = font_sec_hdr
ws5.cell(row=start_p, column=1).fill = fill_orange

headers5_p = [
    "Part SKU", "Part Description", "Category", "Brand / OEM", "Unit", 
    "Purchase Cost", "Selling Price", "GST Rate", "Ambattur Stock", "Avadi Stock", "Reorder Level"
]
for col_idx, h in enumerate(headers5_p, 1):
    cell = ws5.cell(row=start_p+1, column=col_idx, value=h)
    cell.font = font_col_hdr
    cell.fill = fill_navy
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border = thin_border

expanded_parts = [
    ("PRT-SBK-001", "Motul 300V Factory Line 15W50 Superbike Synthetic (1L)", "Superbike Lubes", "Motul Racing", "Bottle", "INR 1,250.00", "INR 1,650.00", "18%", "18 Bottles", "8 Bottles", "6 Bottles"),
    ("PRT-SBK-002", "Brembo Racing Sintered Front Brake Pads (07BB38SR)", "Superbike Brakes", "Brembo Italy", "Set", "INR 3,200.00", "INR 4,500.00", "18%", "6 Sets", "2 Sets", "2 Sets"),
    ("PRT-SBK-003", "Engine Ice Hi-Performance Coolant (1/2 Gallon)", "Cooling", "Engine Ice USA", "Bottle", "INR 1,450.00", "INR 1,950.00", "18%", "10 Bottles", "4 Bottles", "4 Bottles"),
    ("PRT-MOD-001", "BMC High-Flow Performance Conical Air Filter", "Performance Air", "BMC Italy", "Piece", "INR 4,800.00", "INR 6,500.00", "18%", "4 Pieces", "2 Pieces", "2 Pieces"),
    ("PRT-MOD-002", "Akrapovič Carbon Slip-On Exhaust Silencer", "Exhaust System", "Akrapovič", "Unit", "INR 28,000.00", "INR 36,000.00", "18%", "2 Units (On-Order)", "1 Unit", "1 Unit"),
    ("PRT-MOD-003", "Maddog Scout Auxiliary Dual LED Fog Light Kit", "Lighting & Aux", "Maddog India", "Kit", "INR 3,850.00", "INR 5,200.00", "18%", "8 Kits", "4 Kits", "3 Kits"),
    ("PRT-MOD-004", "Heavy-Duty Tubular Crash Guard with Delrin Sliders", "Protection", "Nitro Modz OEM", "Set", "INR 2,400.00", "INR 3,600.00", "18%", "12 Sets", "6 Sets", "4 Sets"),
    ("PRT-OIL-001", "Motul 7100 10W50 Fully Synthetic (1L)", "Standard Lubes", "Motul", "Bottle", "INR 720.00", "INR 950.00", "18%", "24 Bottles", "16 Bottles", "10 Bottles"),
    ("PRT-FLT-002", "OEM Engine Oil Filter Element", "Engine Filters", "Yamaha / OEM", "Piece", "INR 110.00", "INR 180.00", "18%", "45 Pieces", "28 Pieces", "15 Pieces"),
    ("PRT-CHN-005", "Rolon Brass Chain & Sprocket Heavy-Duty Kit", "Drive Chain", "Rolon", "Kit", "INR 1,650.00", "INR 2,200.00", "18%", "8 Kits", "5 Kits", "4 Kits")
]

for idx, p in enumerate(expanded_parts, start=start_p+2):
    ws5.row_dimensions[idx].height = 22
    for c_i, val in enumerate(p, 1):
        cell = ws5.cell(row=idx, column=c_i, value=val)
        cell.font = font_data
        cell.border = thin_border
        cell.fill = fill_white if idx % 2 == 1 else fill_light
        if c_i in [1, 5, 8, 9, 10, 11]:
            cell.alignment = Alignment(horizontal="center", vertical="center")
            if c_i == 1:
                cell.font = font_code
        elif c_i in [6, 7]:
            cell.alignment = Alignment(horizontal="right", vertical="center")
            if c_i == 7:
                cell.font = font_bold
        else:
            cell.alignment = Alignment(horizontal="left", vertical="center")

# ---------------------------------------------------------
# UPDATE SHEET 6: WORKSHOP OPERATIONS (DATA)
# ---------------------------------------------------------
ws6 = wb["Workshop Operations (Data)"]

# Add Superbike & Modification Job Cards
new_jc_rows = [
    ("JC-AMB-2026-004", "Ambattur", "Siddharth Menon\n(+91 98415 67890)", "TN-09-CB-1000\nKawasaki ZX-10R (Superbike)", 
     "8,900 km | 3/4 Tank", "1. Major Superbike service\n2. Radiator Engine Ice flush\n3. Front Brembo pad replace", "Hari Krishnan (Superbike Certified)", 
     "IN PROGRESS", "INR 3,000.00 (UPI)", "Tomorrow 05:00 PM", "CHK-AMB-0845"),
    ("JC-AVD-2026-003", "Avadi", "Karthik Raja\n(+91 98416 78901)", "TN-20-EQ-7700\nRE Continental GT 650", 
     "6,400 km | Full Tank", "1. Nitro Modz: Install Slip-on Exhaust\n2. BMC High-flow filter\n3. ECU remap", "M. Suresh (Modz Specialist)", 
     "ESTIMATE APPROVED", "INR 5,000.00 (UPI)", "Friday 06:00 PM", "CHK-AVD-0418")
]

start_jc = ws6.max_row + 1
for idx, j in enumerate(new_jc_rows, start=start_jc):
    ws6.row_dimensions[idx].height = 42
    for c_i, val in enumerate(j, 1):
        cell = ws6.cell(row=idx, column=c_i, value=val)
        cell.font = font_data
        cell.border = thin_border
        cell.fill = fill_white if idx % 2 == 1 else fill_light
        if c_i in [1, 2, 8, 9, 10, 11]:
            cell.alignment = Alignment(horizontal="center", vertical="center")
            if c_i == 1:
                cell.font = font_code
            if c_i == 8:
                cell.font = font_bold
                cell.fill = fill_tag_orange
        else:
            cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

# ---------------------------------------------------------
# UPDATE SHEET 7: FINANCE & INVOICES (DATA)
# ---------------------------------------------------------
ws7 = wb["Finance & Invoices (Data)"]

new_inv_rows = [
    ("INV-AMB-2026-0843", "JC-AMB-2026-004", "Ambattur", "Siddharth Menon (ZX-10R)", 
     "INR 4,700.00", "INR 9,750.00", "INR 2,601.00", "INR 17,051.00", 
     "INR 3,000.00", "INR 14,051.00", "WORK IN PROGRESS", "Advance ₹3k Adjusted (UPI)"),

    ("INV-AVD-2026-0419", "JC-AVD-2026-003", "Avadi", "Karthik Raja (GT 650)", 
     "INR 4,300.00", "INR 18,500.00", "INR 4,104.00", "INR 26,904.00", 
     "INR 5,000.00", "INR 21,904.00", "ESTIMATE APPROVED", "Advance ₹5k Adjusted (UPI)")
]

start_inv = ws7.max_row + 1
for idx, inv in enumerate(new_inv_rows, start=start_inv):
    ws7.row_dimensions[idx].height = 26
    for c_i, val in enumerate(inv, 1):
        cell = ws7.cell(row=idx, column=c_i, value=val)
        cell.font = font_data
        cell.border = thin_border
        cell.fill = fill_white if idx % 2 == 1 else fill_light
        if c_i in [1, 2, 3, 11]:
            cell.alignment = Alignment(horizontal="center", vertical="center")
            if c_i in [1, 2]:
                cell.font = font_code
        elif c_i in [5, 6, 7, 8, 9, 10]:
            cell.alignment = Alignment(horizontal="right", vertical="center")
            if c_i == 10:
                cell.font = font_bold
        else:
            cell.alignment = Alignment(horizontal="left", vertical="center")

# ---------------------------------------------------------
# UPDATE SHEET 4: CUSTOMERS & VEHICLES (DATA) - Add Superbike & Mod Customers
# ---------------------------------------------------------
ws4 = wb["Customers & Vehicles (Data)"]

new_cust_rows = [
    ("CUST-2026-006", "Siddharth Menon", "+91 98415 67890", "Villa 12, Palm Meadows", "1st Seaward Road, Near Beach", "Valmiki Nagar, Thiruvanmiyur", "Chennai - 600041", "TN-09-CB-1000", "Kawasaki Ninja ZX-10R (998cc)", "8,900 km", "INR 0.00"),
    ("CUST-2026-007", "Karthik Raja", "+91 98416 78901", "Door 88, 4th Avenue", "Shanthi Colony Main Road", "Anna Nagar", "Chennai - 600040", "TN-20-EQ-7700", "RE Continental GT 650 (Twin)", "6,400 km", "INR 0.00")
]

start_cust = ws4.max_row + 1
for idx, c in enumerate(new_cust_rows, start=start_cust):
    ws4.row_dimensions[idx].height = 24
    for c_i, val in enumerate(c, 1):
        cell = ws4.cell(row=idx, column=c_i, value=val)
        cell.font = font_data
        cell.border = thin_border
        cell.fill = fill_white if idx % 2 == 1 else fill_light
        if c_i in [1, 3, 7, 8, 10, 11]:
            cell.alignment = Alignment(horizontal="center", vertical="center")
            if c_i == 1:
                cell.font = font_code
            if c_i == 8:
                cell.font = font_bold
        else:
            cell.alignment = Alignment(horizontal="left", vertical="center")

# Save updated workbook
wb.save("Nitro_Racing_Application_Data_Flow.xlsx")
print("Nitro_Racing_Application_Data_Flow.xlsx updated with Superbikes and Modifications!")
