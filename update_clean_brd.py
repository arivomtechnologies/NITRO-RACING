import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

doc = docx.Document()

# Margins
for section in doc.sections:
    section.top_margin = Inches(0.8)
    section.bottom_margin = Inches(0.8)
    section.left_margin = Inches(0.8)
    section.right_margin = Inches(0.8)
    
    footer = section.footer
    f_p = footer.paragraphs[0]
    f_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    f_p.text = "Nitro Racing – Bike Service Management System | Menu & Submenu Functional Requirements v1.1"
    f_p.runs[0].font.size = Pt(8.5)
    f_p.runs[0].font.color.rgb = RGBColor(120, 120, 120)

C_NAVY = RGBColor(0x10, 0x1D, 0x35)
C_ORANGE = RGBColor(0xF1, 0x5A, 0x24)
C_DARK = RGBColor(0x17, 0x19, 0x1D)

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>'))

def set_cell_margins(cell, top=100, bottom=100, left=140, right=140):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def add_heading_1(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(15)
    run.font.bold = True
    run.font.color.rgb = C_NAVY
    return p

def add_heading_2(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(12)
    run.font.bold = True
    run.font.color.rgb = C_ORANGE
    return p

def add_heading_3(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(10.5)
    run.font.bold = True
    run.font.color.rgb = C_NAVY
    return p

def add_body(text, bold_prefix="", italic=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Calibri"
        r_pre.font.size = Pt(9.5)
        r_pre.font.bold = True
        r_pre.font.color.rgb = C_DARK
    r = p.add_run(text)
    r.font.name = "Calibri"
    r.font.size = Pt(9.5)
    r.font.italic = italic
    r.font.color.rgb = C_DARK
    return p

def add_bullet(text, bold_prefix=""):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after = Pt(2.5)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Calibri"
        r_pre.font.size = Pt(9.5)
        r_pre.font.bold = True
        r_pre.font.color.rgb = C_DARK
    r = p.add_run(text)
    r.font.name = "Calibri"
    r.font.size = Pt(9.5)
    r.font.color.rgb = C_DARK
    return p

def create_table(headers, rows_data, col_widths=None):
    num_rows = len(rows_data) + 1
    num_cols = len(headers)
    tbl = doc.add_table(rows=num_rows, cols=num_cols)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    for c_i, h in enumerate(headers):
        c = tbl.rows[0].cells[c_i]
        set_cell_background(c, "101D35")
        set_cell_margins(c, 80, 80, 100, 100)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.name = "Calibri"
        r.font.size = Pt(9)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        
    for r_i, r_data in enumerate(rows_data, start=1):
        for c_i, val in enumerate(r_data):
            c = tbl.rows[r_i].cells[c_i]
            bg_col = "FFFFFF" if r_i % 2 == 1 else "F4F6F9"
            set_cell_background(c, bg_col)
            set_cell_margins(c, 60, 60, 100, 100)
            p = c.paragraphs[0]
            r = p.add_run(str(val))
            r.font.name = "Calibri"
            r.font.size = Pt(8.5)
            r.font.color.rgb = C_DARK
            if c_i == 0:
                r.font.bold = True

    if col_widths:
        for r in tbl.rows:
            for idx, w in enumerate(col_widths):
                r.cells[idx].width = w
    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    return tbl

# Title Block
title_p = doc.add_paragraph()
title_p.paragraph_format.space_before = Pt(12)
title_p.paragraph_format.space_after = Pt(2)
r_org = title_p.add_run("NITRO RACING")
r_org.font.name = "Calibri"
r_org.font.size = Pt(24)
r_org.font.bold = True
r_org.font.color.rgb = C_ORANGE

sub_p = doc.add_paragraph()
sub_p.paragraph_format.space_after = Pt(12)
r_sub = sub_p.add_run("BIKE SERVICE MANAGEMENT SYSTEM\nMenu & Submenu Functional Requirements Document (v1.1)\nIncluding Specialized Superbike & Motorcycle Modification Modules")
r_sub.font.name = "Calibri"
r_sub.font.size = Pt(13)
r_sub.font.bold = True
r_sub.font.color.rgb = C_NAVY

meta_headers = ["Document Detail", "Description"]
meta_rows = [
    ["Document Type", "Application Menu Structure & Functional Requirements (Updated)"],
    ["Product", "Nitro Racing – Bike Service Management System v1.1"],
    ["Specialized Operations", "Standard Two-Wheelers, Superbikes (400cc - 1000cc+), and Nitro Modz Customizations"],
    ["Prepared For", "Product, UI/UX, Development and QA Teams"],
    ["Primary Users", "Super Admin, Branch Admin, Technician"],
    ["Customer Login", "Not included; customer records are managed internally"],
    ["Brand Direction", "Racing Orange #F15A24 | Dark Navy #101D35 | Light Grey #F4F6F9"]
]
create_table(meta_headers, meta_rows, [Inches(2.2), Inches(4.8)])

add_heading_1("1. Document Purpose & Operational Scope")
add_body("This document defines the functional requirements for Nitro Racing, expanding upon standard workshop routines to specifically accommodate Superbike servicing (high-displacement 400cc to 1000cc+ performance motorcycles) and Motorcycle Modifications ('Nitro Modz'). It serves as the baseline for system implementation, data models, and screen workflows.")

add_heading_1("2. Specialized Service Modules: Superbikes & Modifications")
add_body("Nitro Racing distinguishes itself from standard commuter repair garages through two specialized business divisions:")

add_heading_2("A. Superbike Service Division (High-CC & Performance Bikes)")
add_bullet("Target Vehicles: High-displacement single, twin, inline-4, and V4 motorcycles (e.g., Kawasaki Ninja ZX-10R/Ninja 400, Yamaha R1/R3, Triumph Street Triple, Ducati Panigale/Scrambler, BMW S1000RR, Honda CBR650R, Suzuki Hayabusa, Royal Enfield 650 Twins).", "Vehicle Scope: ")
add_bullet("Desmo/valve clearance service, computerized OBD-2 fault code diagnosis & sensor calibration, throttle body electronic synchronization, radiator high-performance coolant flush (Engine Ice), slipper clutch inspection, and Brembo brake bleeding.", "Key Operations: ")
add_bullet("Only assigned to certified Master Technicians (e.g. Hari Krishnan); requires specialized bays with rubberized paddock stands and torque calibration.", "Workshop Governance: ")
add_bullet("Premium synthetic racing lubricants (Motul 300V Factory Line), OEM imported oil filters, sintered brake pads.", "Spare Parts & Fluids: ")

add_heading_2("B. Modifications & Customization Division ('Nitro Modz')")
add_bullet("Performance exhaust installation (slip-on & full system), ECU Stage 1/2 fuel map flashing & dyno tuning, high-flow performance air filter fitment (BMC/K&N), auxiliary touring lights & dual-relay wiring harness, heavy-duty tubular crash guards with Delrin sliders, tail tidies, and custom clip-on handlebars.", "Key Customizations: ")
add_bullet("50% mandatory advance payment required before ordering high-value non-stock custom parts (e.g. Akrapovič, Arrow, Brembo calipers).", "Advance Deposit Rule: ")
add_bullet("Customer signs digital waiver acknowledging modification noise levels and off-road / track usage compliance.", "Legal Consent Gate: ")
add_bullet("Vehicle check-in must photograph all pre-existing aftermarket parts to prevent dispute during vehicle handover.", "Inspection Protocol: ")

add_heading_1("3. Updated Service Catalogue Master Data")
srv_headers = ["Service Code", "Operation Title", "Division / Category", "Std Duration", "Base Labor Rate", "Target Models"]
srv_rows = [
    ["SRV-SBK-01", "Superbike Major Service & Valve Clearance", "Superbike Division", "240 Mins", "INR 3,500.00", "Superbikes (600 - 1000cc+)"],
    ["SRV-SBK-02", "Superbike Computerized OBD-2 Diagnostic", "Superbike Division", "60 Mins", "INR 1,200.00", "Electronic FI / Superbikes"],
    ["SRV-SBK-03", "Radiator Coolant Flush (Engine Ice)", "Superbike Division", "45 Mins", "INR 650.00", "Liquid-Cooled / Superbikes"],
    ["SRV-MOD-01", "Performance Exhaust Installation", "Nitro Modz", "90 Mins", "INR 1,500.00", "All Compatible Motorcycles"],
    ["SRV-MOD-02", "ECU Stage 1/2 Fuel Map Flashing", "Nitro Modz", "120 Mins", "INR 2,800.00", "Fuel Injected & Track Bikes"],
    ["SRV-MOD-03", "Auxiliary Lights & Custom Wiring Harness", "Nitro Modz", "75 Mins", "INR 850.00", "Touring & Adventure Bikes"],
    ["SRV-MOD-04", "Crash Guard & Frame Slider Installation", "Nitro Modz", "60 Mins", "INR 500.00", "All Motorcycles"],
    ["SRV-GEN-01", "General Periodic Service (50-Point)", "Periodic Maintenance", "90 Mins", "INR 650.00", "Commuter & Sports (100-250cc)"],
    ["SRV-BRK-03", "Front & Rear Brake Caliper Overhaul", "Brake System", "45 Mins", "INR 350.00", "Disc Brake Motorcycles"]
]
create_table(srv_headers, srv_rows, [Inches(1.2), Inches(2.3), Inches(1.5), Inches(1.0), Inches(1.2), Inches(1.8)])

add_heading_1("4. Core Workshop Operations & Address Architecture")
add_body("The fundamental workshop lifecycle remains consistent while seamlessly adapting to Superbike and Modification workflows:")
add_bullet("Customer arrival, phone lookup, and structured residential address normalization (Door No, Street, Landmark, Area, City, Pincode).", "Stage 1: Intake & Address: ")
add_bullet("Detailed condition recording, 4 damage photos, accessories inventory, customer complaints, and modification wishlist.", "Stage 2: Check-in: ")
add_bullet("Sequential work order generated; status set to RECEIVED. Minimum 50% advance collected for custom performance parts.", "Stage 3: Job Card: ")
add_bullet("Quotation prepared with itemized performance parts + custom labor + 18% GST. Digital sign-off recorded.", "Stage 4: Estimate & Consent: ")
add_bullet("Allocated to Superbike-certified mechanic (Hari Krishnan) or Modz specialist.", "Stage 5: Bay Allocation: ")
add_bullet("Execution of repairs; performance parts issued and auto-decremented from branch inventory.", "Stage 6: Execution: ")
add_bullet("Brake force check, dyno/sound check for exhausts, electronic sensor scan, and comprehensive road test.", "Stage 7: Quality Control (QC): ")
add_bullet("Tax invoice generated with frozen legal address snapshot; balance settled via UPI/Card; Gate Pass issued for vehicle release.", "Stage 8: Invoicing & Handover: ")

doc.save("Nitro_Racing_Application_BRD.docx")
print("Updated Nitro_Racing_Application_BRD.docx generated.")
