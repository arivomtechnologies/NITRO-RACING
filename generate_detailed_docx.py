import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

doc = docx.Document()

# Page Margins
for section in doc.sections:
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)
    
    # Header & Footer
    footer = section.footer
    f_p = footer.paragraphs[0]
    f_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    f_p.text = "Nitro Racing Automobile Service Center Management System | BRD v1.0 | Arivom Technologies"
    f_p.runs[0].font.size = Pt(8.5)
    f_p.runs[0].font.color.rgb = RGBColor(120, 120, 120)

# Colors
C_GRAPHITE = RGBColor(0x17, 0x19, 0x1D)
C_CHARCOAL = RGBColor(0x24, 0x2A, 0x31)
C_ORANGE = RGBColor(0xF4, 0x77, 0x21)
C_SILVER = RGBColor(0xD6, 0xD9, 0xDD)
C_GREEN = RGBColor(0x22, 0x9B, 0x62)
C_YELLOW = RGBColor(0xE9, 0xA2, 0x3B)

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>'))

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def add_heading_1(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(18)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(16)
    run.font.bold = True
    run.font.color.rgb = C_ORANGE
    return p

def add_heading_2(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(13)
    run.font.bold = True
    run.font.color.rgb = C_CHARCOAL
    return p

def add_heading_3(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(11)
    run.font.bold = True
    run.font.color.rgb = C_GRAPHITE
    return p

def add_body(text, bold_prefix="", italic=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(5)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Arial"
        r_pre.font.size = Pt(9.5)
        r_pre.font.bold = True
        r_pre.font.color.rgb = C_GRAPHITE
    r = p.add_run(text)
    r.font.name = "Arial"
    r.font.size = Pt(9.5)
    r.font.italic = italic
    r.font.color.rgb = C_GRAPHITE
    return p

# ----------------- COVER / TITLE BLOCK -----------------
title_p = doc.add_paragraph()
title_p.paragraph_format.space_before = Pt(36)
title_p.paragraph_format.space_after = Pt(6)
r_org = title_p.add_run("NITRO RACING")
r_org.font.name = "Arial"
r_org.font.size = Pt(28)
r_org.font.bold = True
r_org.font.color.rgb = C_ORANGE

sub_p = doc.add_paragraph()
sub_p.paragraph_format.space_after = Pt(18)
r_sub = sub_p.add_run("Automobile Service Center Management System\nComprehensive Business Requirements Document (BRD) & Technical Specification")
r_sub.font.name = "Arial"
r_sub.font.size = Pt(15)
r_sub.font.bold = True
r_sub.font.color.rgb = C_CHARCOAL

meta_table = doc.add_table(rows=6, cols=2)
meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
meta_data = [
    ("Document Type", "Client-Facing Business Requirements Document (BRD v1.0)"),
    ("Target Client", "Nitro Racing (Branches: Ambattur, Avadi, & Future Multi-Branch Network)"),
    ("Prepared By", "Arivom Technologies, Chennai"),
    ("Client Representative", "Fertrick (Client Sign-off & Review)"),
    ("Development Representative", "Balasubramanian (Technical Lead & Solution Architect)"),
    ("Baseline Agreement", "Original Timeline: 2 Months | Commercial Value: INR 60,000")
]
for idx, (label, val) in enumerate(meta_data):
    row = meta_table.rows[idx]
    c0, c1 = row.cells[0], row.cells[1]
    set_cell_background(c0, "17191D")
    set_cell_background(c1, "F5F5F2")
    set_cell_margins(c0, 80, 80, 120, 120)
    set_cell_margins(c1, 80, 80, 120, 120)
    
    p0 = c0.paragraphs[0]
    r0 = p0.add_run(label)
    r0.font.name = "Arial"
    r0.font.size = Pt(9.5)
    r0.font.bold = True
    r0.font.color.rgb = RGBColor(255, 255, 255)
    
    p1 = c1.paragraphs[0]
    r1 = p1.add_run(val)
    r1.font.name = "Arial"
    r1.font.size = Pt(9.5)
    r1.font.color.rgb = C_GRAPHITE

doc.add_page_break()

# ----------------- SECTION 1: EXECUTIVE SUMMARY -----------------
add_heading_1("1. Executive Summary & Business Background")
add_body("Nitro Racing is an established multi-branch motorcycle service center and workshop enterprise operating in Chennai, currently servicing high customer volumes across prime branches including Ambattur and Avadi. To support rapid business growth and enhance operational control, Nitro Racing requires an enterprise-grade digital platform replacing fragmented paper registers with real-time workshop management.")
add_body("This document transforms the baseline 5-page BRD into an exhaustive product blueprint. It outlines the dual-surface digital solution:", "Architecture Model: ")
add_body("A high-performance brand portal showcasing workshop specializations, branch locators, customer testimonials, and an appointment booking funnel.", "1. Public Business Website: ")
add_body("A secure, responsive, mobile-first operations hub empowering Super Admins, Branch Admins, and Workshop Technicians to manage job cards, diagnostic inspections, spare parts inventory, PDF invoicing, and financial dashboards.", "2. Management Portal: ")

# ----------------- SECTION 2: BUSINESS CHALLENGES & OBJECTIVES -----------------
add_heading_1("2. Existing Business Challenges vs. Digital Transformation")
comp_table = doc.add_table(rows=6, cols=3)
comp_table.alignment = WD_TABLE_ALIGNMENT.CENTER
t_headers = ["Operational Dimension", "Existing Manual / Paper Reality", "Proposed Nitro Racing Digital System"]
for i, h in enumerate(t_headers):
    c = comp_table.rows[0].cells[i]
    set_cell_background(c, "242A31")
    set_cell_margins(c, 100, 100, 100, 100)
    p = c.paragraphs[0]
    r = p.add_run(h)
    r.font.name = "Arial"
    r.font.size = Pt(9)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)

comp_rows = [
    ("Job Card Processing", "Paper job cards are easily damaged by grease, lost in workshop bays, and illegible.", "Digital Job Card accessible via smartphone; cloud-persisted with photos and status tracking."),
    ("Multi-Branch Control", "Head office must manually phone branches to collect daily job volumes and cash collections.", "Centralized Super Admin dashboard providing real-time revenue, job count, and branch comparison."),
    ("Customer Vehicle History", "Mechanics have zero visibility into past repairs, leading to repeated misdiagnoses.", "Centralized bike history tracking all past job cards, replaced parts, and recorded complaints."),
    ("Billing & Tax Compliance", "Invoices prepared by hand at closing, causing pickup delays, arithmetic errors, and disputes.", "Instant automated PDF invoice generation calculating labor, parts, tax/GST, advance, and net balance."),
    ("Parts & Cost Leakage", "Spare parts consumed without accurate job allocation or stock reordering alerts.", "Real-time spare parts stock deduction against job card parts issue with low-stock warnings.")
]
for idx, (dim, old_w, new_w) in enumerate(comp_rows, start=1):
    row = comp_table.rows[idx]
    for c_i, val in enumerate([dim, old_w, new_w]):
        cell = row.cells[c_i]
        set_cell_background(cell, "FFFFFF" if idx % 2 == 1 else "F5F5F2")
        set_cell_margins(cell, 80, 80, 100, 100)
        p = cell.paragraphs[0]
        r = p.add_run(val)
        r.font.name = "Arial"
        r.font.size = Pt(8.5)
        if c_i == 0:
            r.font.bold = True

# ----------------- SECTION 3: COMMERCIAL SAFEGUARD & SCOPE -----------------
add_heading_1("3. Commercial Safeguard & Scope Demarcation")
add_body("To preserve complete commercial integrity, this document explicitly separates the original commercial baseline from recommended operational enhancements:", bold_prefix="Strict Contractual Boundary: ")

add_heading_2("A. Original Confirmed Scope (Fixed Contract: INR 60,000 / 2 Months)")
add_body("The original agreement signed with Arivom Technologies covers 26 Functional Requirements (FR-01 to FR-26) exactly as stipulated in the original BRD v1.0. This includes: User authentication (FR-01 to FR-06), Store/Branch management (FR-07 to FR-11), User management (FR-12 to FR-13), Job Card lifecycle (FR-14 to FR-18), PDF Invoice generation (FR-19 to FR-22), and Role-restricted Dashboards (FR-23 to FR-26).")

add_heading_2("B. Recommended Additional Enhancements (Pending Client Approval)")
add_body("To match industry best practices observed in modern racing garages, Arivom Technologies recommends additional modules including: Centralized Customer & Bike Masters (FR-101/102), Online Appointment Booking (FR-103), Vehicle Inspection Checklists with Damage Photos (FR-104), Formal Pre-Service Estimates (FR-105), Mechanic Workload Allocation (FR-106), Spare Parts Stock Inventory (FR-107), Quality Control Handover (FR-108), Multi-mode Partial Payments (FR-109), Operating Expenses & Net P&L (FR-110), and Dynamic Web CMS (FR-112). These recommendations are subject to mutual discussion and commercial sign-off.")

# ----------------- SECTION 4: USER ROLES & PERMISSION MATRIX -----------------
add_heading_1("4. User Hierarchy & Role-Based Access Control (RBAC)")
add_body("The application implements a strict hierarchical role structure designed for automotive workshop governance:")
add_body("Has unconstrained multi-tenant visibility across all operational branches. Governs branch provisioning, Branch Admin creation, global business profile, tax parameters, and consolidated financial intelligence.", "1. Super Admin: ")
add_body("Assigned exclusively to one branch (e.g., Ambattur or Avadi). Manages branch technicians, vehicle check-ins, job card lifecycles, spare parts inventory, local customer relationships, and branch-specific profit metrics.", "2. Branch Admin: ")
add_body("Front-line workshop staff (service advisors, mechanics). Operates on mobile devices to create job cards, update repair statuses, attach inspection notes, and generate PDF invoices. Strictly blocked from accessing business financial dashboards (FR-26).", "3. Employee / Technician: ")

# ----------------- SECTION 5: CORE MODULE DETAILED SPECIFICATIONS -----------------
add_heading_1("5. Core Module Functional Specifications")

modules = [
    ("Module 5.1: Customer & Vehicle Management",
     "Centralize customer identity and maintain lifetime motorcycle service profiles.",
     "Customers & Bikes",
     "Customer Directory, Add Customer, Customer Profile, Bike Master, Service History",
     "Customer Name, Primary Mobile, Alternate Mobile, Email, Street Address, Bike Registration Number, Bike Brand, Bike Model, Bike Nickname, Year of Manufacture, Initial Odometer (KMs).",
     "1. Phone number is unique customer identifier; system automatically flags existing profiles during entry.\n2. One customer can own multiple motorcycles; each motorcycle maintains an independent service log.\n3. Complete cross-branch service history accessible during vehicle check-in.",
     "SOURCE CONFIRMED (Baseline Job Card fields FR-14) / RECOMMENDED (Standalone Customer Master FR-101)"),
    
    ("Module 5.2: Workshop Job Card & Lifecycle Management",
     "End-to-end digital lifecycle of repair orders from check-in to final vehicle release.",
     "Workshop Operations",
     "Job Cards, Active Jobs, Work in Progress, Completed Jobs, Ready for Delivery",
     "Job Card ID, Branch ID, Customer Details, Bike Details, Current KMs, Purpose of Entry (e.g. Engine Overhaul, Oil Change), Customer Complaint Notes, Mechanic Diagnosis, Advance Amount Paid, Assigned Mechanic, Promised Delivery Date.",
     "1. Job card creation permitted by Super Admin, Branch Admin, and Employee (FR-14).\n2. Status progresses: Received -> Work In Progress -> Completed -> Delivered (FR-16).\n3. Every status modification logs timestamp and user identity in immutable audit table (FR-18).\n4. Mobile-optimized responsive layout designed for single-hand workshop entry.",
     "SOURCE CONFIRMED (FR-14 to FR-18)"),
    
    ("Module 5.3: Spare Parts Inventory & Stock Deduction",
     "Track workshop spare parts, prevent pilferage, and auto-deduct stock on job card billing.",
     "Inventory & Parts",
     "Parts Master, Stock Inward, Parts Requisition, Low Stock Alerts, Suppliers",
     "Part Code, Part Name, Category (Engine, Brakes, Transmission, Consumables), Cost Price, Selling Price, Available Quantity, Minimum Reorder Threshold, Supplier Name, Storage Bin / Rack.",
     "1. Branch Admin records stock inward against supplier bills.\n2. When parts are added to a job card or invoice, physical stock is decremented immediately.\n3. Automatic warning banner displayed when stock falls below minimum threshold.\n4. Branch data isolation: Ambattur stock is tracked separately from Avadi stock.",
     "RECOMMENDED (FR-107) - Pending Client Approval"),
    
    ("Module 5.4: Billing, PDF Invoicing & Payment Collection",
     "Generate professional, tax-compliant PDF invoices with advance adjustments and balance tracking.",
     "Billing & Invoices",
     "Generate Invoice, Invoice Archive, Payment Collection, Outstanding Balances",
     "Invoice Number (auto-incrementing per branch), Invoice Date, Customer Details, Bike Registration, Itemized Service Charges, Itemized Spare Parts, Subtotal, Applicable Tax (GST), Advance Amount Deducted, Net Balance Due, Payment Mode (UPI, Cash, Card), Transaction ID.",
     "1. Any of the 3 roles can generate invoices directly from completed job cards (FR-19).\n2. Strict PDF-only download; Excel export is blocked to ensure invoice tampering protection (FR-21).\n3. Built-in support for native mobile printing and direct WhatsApp/SMS PDF sharing (FR-22).\n4. Multi-payment ledger supports partial advance payments and balance settlement at pickup.",
     "SOURCE CONFIRMED (FR-19 to FR-22) / RECOMMENDED (Partial Payments FR-109)"),
    
    ("Module 5.5: Management Dashboards & Business Analytics",
     "Executive visibility into revenue, sales trends, technician throughput, and branch profitability.",
     "Dashboard & Reports",
     "Executive Overview, Branch Comparison, Daily Sales, Profit & Loss, Mechanic Output",
     "Monthly Sales Volume, Gross Revenue, Estimated Profit, Vehicle Brand Distribution (Yamaha, Honda, Royal Enfield, KTM), Jobs by Status Distribution, Branch-by-Branch Comparison.",
     "1. Super Admin has unrestricted access to consolidated dashboard and individual branch drill-downs (FR-24).\n2. Branch Admin strictly restricted to viewing own branch performance indicators (FR-25).\n3. Employees are completely blocked from accessing any dashboard or financial reports (FR-26).\n4. Profit calculation pending client confirmation on expense capture and part costing.",
     "SOURCE CONFIRMED (FR-23 to FR-26)")
]

for m_title, m_purp, m_menu, m_sub, m_fields, m_rules, m_status in modules:
    add_heading_2(m_title)
    add_body(m_purp, "Business Purpose: ")
    add_body(f"{m_menu} > {m_sub}", "Navigation Hierarchy: ")
    add_body(m_fields, "Key Data Attributes: ")
    add_body(m_rules, "Operational Business Rules: ")
    add_body(m_status, "Scope Status: ")

# ----------------- SECTION 6: CLIENT CLARIFICATIONS -----------------
add_heading_1("6. Client Clarification Decisions & Open Questions")
add_body("The original BRD v1.0 identifies 8 critical architectural and commercial decisions requiring formal client feedback from Nitro Racing (Fertrick). The table below documents the current status and Arivom Technologies' recommendation:")

q_table = doc.add_table(rows=9, cols=3)
q_table.alignment = WD_TABLE_ALIGNMENT.CENTER
q_headers = ["Item #", "Open Question from Client BRD v1.0", "Arivom Technologies Architectural Recommendation"]
for i, h in enumerate(q_headers):
    c = q_table.rows[0].cells[i]
    set_cell_background(c, "242A31")
    set_cell_margins(c, 100, 100, 100, 100)
    p = c.paragraphs[0]
    r = p.add_run(h)
    r.font.name = "Arial"
    r.font.size = Pt(8.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)

q_data = [
    ("Q1", "How should profit be calculated? Will parts purchase cost and workshop expenses be entered?", "Implement Gross Profit = (Billed Labor + Parts Markup) - Direct Cost. Recommend implementing Operating Expenses module (FR-110) for true Net Profit."),
    ("Q2", "Is GST/tax required on invoices? Please provide GSTIN and billing legal structure.", "System designed with configurable GST toggle (e.g. 18% GST). If client operates as composite or unregistered, tax toggle can remain inactive."),
    ("Q3", "Should customers receive SMS/WhatsApp updates on service status changes?", "Highly recommended for customer trust. Scope requires third-party SMS/WhatsApp gateway credentials; setup cost borne by client."),
    ("Q4", "Should the 'Delivered' status be added after 'Completed'?", "Yes, strongly recommended. Separates bikes finished by mechanics from vehicles physically handed over to customers with full payment."),
    ("Q5", "Can an Employee edit or delete a job card after creation, or only create and update status?", "Employees should only create and update status. Edit/Delete should be restricted to Branch Admins to prevent revenue record tampering."),
    ("Q6", "Does client have domain, hosting, logo, and brand color guidelines?", "Arivom Technologies has proposed the Nitro Racing theme (Graphite #17191D, Racing Orange #F47721, Charcoal #242A31). Client to approve."),
    ("Q7", "Is old legacy data (paper records/spreadsheets) to be migrated into new system?", "Initial release planned with fresh database. Historical data migration can be provided as a separate data-cleansing work package."),
    ("Q8", "Is a regional language (e.g., Tamil) required in the management portal?", "Phase 1 will launch in English. Modular i18n localization architecture is integrated to enable Tamil language pack in Phase 2.")
]
for idx, (num, q_txt, r_txt) in enumerate(q_data, start=1):
    row = q_table.rows[idx]
    for c_i, val in enumerate([num, q_txt, r_txt]):
        cell = row.cells[c_i]
        set_cell_background(cell, "FFFFFF" if idx % 2 == 1 else "F5F5F2")
        set_cell_margins(cell, 80, 80, 100, 100)
        p = cell.paragraphs[0]
        r = p.add_run(val)
        r.font.name = "Arial"
        r.font.size = Pt(8)
        if c_i == 0:
            r.font.bold = True

# ----------------- SECTION 7: TECHNICAL ARCHITECTURE & SECURITY -----------------
add_heading_1("7. Technical Architecture & Non-Functional Requirements")
add_body("Modern single-page and server-side responsive web application built on Angular 18+ utilizing Angular Material with customized automotive theme styling.", "Frontend Architecture: ")
add_body("Enterprise Java Spring Boot 3 RESTful micro-services featuring Spring Security, JWT stateless bearer token authentication, and multi-tenant branch context interception.", "Backend Architecture: ")
add_body("Relational PostgreSQL 16 database utilizing connection pooling, schema-level foreign key constraints, automated daily backups, and branch tenant isolation.", "Database Engine: ")
add_body("Dedicated JasperReports rendering engine compiling pixel-perfect, tamper-resistant PDF documents directly on server side.", "Document Generation: ")
add_body("All communication forced over HTTPS/TLS 1.3. Passwords salted and hashed with BCrypt. 24-hour persistent mobile sessions supported via secure refresh tokens.", "Security Standards: ")

# ----------------- SECTION 8: SIGN-OFF & APPROVAL -----------------
add_heading_1("8. Document Review & Acceptance Sign-Off")
add_body("By signing below, the authorized representatives acknowledge that this document reflects the complete functional and architectural requirements for the Nitro Racing Automobile Service Center Management System:")

sign_table = doc.add_table(rows=5, cols=2)
sign_table.alignment = WD_TABLE_ALIGNMENT.CENTER
s_headers = ["Client Acceptance (Nitro Racing)", "Solution Provider (Arivom Technologies)"]
for i, h in enumerate(s_headers):
    c = sign_table.rows[0].cells[i]
    set_cell_background(c, "17191D")
    set_cell_margins(c, 100, 100, 100, 100)
    p = c.paragraphs[0]
    r = p.add_run(h)
    r.font.name = "Arial"
    r.font.size = Pt(9.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)

s_rows = [
    ("Authorized Name: Fertrick", "Authorized Name: Balasubramanian"),
    ("Title: Client Representative / Business Owner", "Title: Technical Lead & Solution Architect"),
    ("Signature: ___________________________", "Signature: ___________________________"),
    ("Date: ___________________________", "Date: ___________________________")
]
for idx, (c1_val, c2_val) in enumerate(s_rows, start=1):
    row = sign_table.rows[idx]
    for c_i, val in enumerate([c1_val, c2_val]):
        cell = row.cells[c_i]
        set_cell_background(cell, "FFFFFF" if idx % 2 == 1 else "F5F5F2")
        set_cell_margins(cell, 100, 100, 100, 100)
        p = cell.paragraphs[0]
        r = p.add_run(val)
        r.font.name = "Arial"
        r.font.size = Pt(9)

doc.save("Nitro_Racing_Detailed_BRD.docx")
print("Nitro_Racing_Detailed_BRD.docx generated successfully.")
