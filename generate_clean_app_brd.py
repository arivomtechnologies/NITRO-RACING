import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

doc = docx.Document()

# Page Margins
for section in doc.sections:
    section.top_margin = Inches(0.8)
    section.bottom_margin = Inches(0.8)
    section.left_margin = Inches(0.8)
    section.right_margin = Inches(0.8)
    
    # Footer
    footer = section.footer
    f_p = footer.paragraphs[0]
    f_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    f_p.text = "Nitro Racing – Bike Service Management System | Menu & Submenu Functional Requirements v1.0"
    f_p.runs[0].font.size = Pt(8.5)
    f_p.runs[0].font.color.rgb = RGBColor(120, 120, 120)

# Colors: Racing Orange #F15A24 | Dark Navy #101D35 | Light Grey #F4F6F9
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
    
    # Headers
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
        
    # Rows
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

# ==========================================
# TITLE BLOCK
# ==========================================
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
r_sub = sub_p.add_run("BIKE SERVICE MANAGEMENT SYSTEM\nMenu & Submenu Functional Requirements Document")
r_sub.font.name = "Calibri"
r_sub.font.size = Pt(14)
r_sub.font.bold = True
r_sub.font.color.rgb = C_NAVY

meta_headers = ["Document Detail", "Description"]
meta_rows = [
    ["Document Type", "Application Menu Structure & Functional Requirements"],
    ["Product", "Nitro Racing – Bike Service Management System"],
    ["Version", "1.0"],
    ["Prepared For", "Product, UI/UX, Development and QA Teams"],
    ["Primary Users", "Super Admin, Branch Admin, Technician"],
    ["Customer Login", "Not included; customer records are managed internally"],
    ["Brand Direction", "Racing Orange #F15A24 | Dark Navy #101D35 | Light Grey #F4F6F9"]
]
create_table(meta_headers, meta_rows, [Inches(2.2), Inches(4.8)])

# ==========================================
# 1. DOCUMENT PURPOSE & 2. APPLICATION OVERVIEW
# ==========================================
add_heading_1("1. Document Purpose")
add_body("This document defines the recommended navigation, menu hierarchy, submenu purpose, key functions, data to be maintained, and expected outcomes for Nitro Racing. It is intended to provide a shared functional baseline for design, development, testing, and future enhancements.")

add_heading_1("2. Application Overview")
add_body("Nitro Racing is an internal, branch-aware two-wheeler service operations application. It manages customers and their bikes, service appointments, vehicle check-in, job cards, technician work, spare parts, estimates, invoices, payments, quality checks, delivery, and operational reporting.")

# ==========================================
# 3. USER ROLES & ACCESS MODEL
# ==========================================
add_heading_1("3. User Roles & Access Model")
role_headers = ["Role", "Access Scope", "Typical Responsibilities"]
role_rows = [
    ["Super Admin", "All branches and organization-wide configuration", "Create branches and users, configure masters, view consolidated reports, monitor all operations."],
    ["Branch Admin", "Assigned branch only", "Manage branch customers, bikes, appointments, job cards, technicians, inventory, billing, payments and branch reports."],
    ["Technician", "Assigned jobs and permitted workshop functions", "View assigned job cards, inspect vehicles, update work progress, record parts used and submit work for quality check."]
]
create_table(role_headers, role_rows, [Inches(1.5), Inches(2.3), Inches(3.2)])
add_body("Important Policy: Customers are records only. No customer portal or customer login is included in this scope.", italic=True)

# ==========================================
# 4. RECOMMENDED MAIN MENU HIERARCHY
# ==========================================
add_heading_1("4. Recommended Main Menu Hierarchy")
menu_summary = [
    ("Dashboard", "Dashboard"),
    ("Organization", "Branches | Users & Roles | Employees"),
    ("Customer Management", "Customers | Customer Vehicles | Vehicle History"),
    ("Workshop Operations", "Appointments | Vehicle Check-in | Job Cards | Mechanic Assignment | Service Tracking | Quality Inspection | Vehicle Delivery"),
    ("Service Configuration", "Service Categories | Service Catalogue | Service Packages | Brands | Bike Models"),
    ("Inventory", "Spare Parts | Stock Management | Suppliers | Purchase Orders"),
    ("Finance", "Estimates | Invoices | Payments | Expenses"),
    ("Reports", "Revenue Reports | Service Reports | Branch Reports | Technician Reports | Inventory Reports"),
    ("System", "Notifications | Settings | Audit Logs")
]
for mod, subs in menu_summary:
    add_bullet(subs, f"{mod}: ")

# ==========================================
# 5. DETAILED MENU & SUBMENU REQUIREMENTS
# ==========================================
add_heading_1("5. Menu & Submenu Functional Details")

# 5.1 Dashboard
add_heading_2("5.1 Dashboard")
add_heading_3("Dashboard")
add_body("Provide an at-a-glance operational and financial summary. Default view should be scoped to the logged-in user's permitted branch; Super Admin can switch between branches or view consolidated data.", "Purpose: ")
add_bullet("Jobs received today, awaiting estimate approval, in progress, quality check, ready for delivery, delivered, and outstanding amount.", "KPI Cards: ")
add_bullet("Revenue trend, job status distribution, branch comparison (Super Admin), technician workload.", "Charts: ")
add_bullet("Today's appointments, overdue jobs, low-stock alerts, recent payments and recent activity.", "Lists: ")
add_bullet("Date range, branch, job status and service type where applicable.", "Filters: ")

# 5.2 Organization
add_heading_2("5.2 Organization")
add_heading_3("Branches")
add_body("Maintain the organization's service locations.", "Purpose: ")
add_bullet("Create, view, edit, activate or deactivate a branch.")
add_bullet("branch code, branch name, address, contact number, email, manager, business hours and status.", "Fields: ")
add_bullet("Assign users and technicians to a branch; configure branch-specific invoice sequence and service availability.")
add_bullet("Prevent branch users from accessing another branch's operational records unless explicitly permitted.")

add_heading_3("Users & Roles")
add_body("Manage application login accounts and permissions.", "Purpose: ")
add_bullet("Create and edit user accounts; map each account to a role and branch.")
add_bullet("Super Admin, Branch Admin and Technician (No customer login).", "Roles in Scope: ")
add_bullet("Configure permissions by module and action: view, create, edit, delete, approve, export.")
add_bullet("Support account activation/deactivation, password reset and last-login visibility.")

add_heading_3("Employees")
add_body("Maintain employee and technician profiles used in workshop operations.", "Purpose: ")
add_bullet("employee ID, name, mobile, email, branch, designation, joining date, skills/specialization and employment status.", "Fields: ")
add_bullet("Link employee records to login users where required.")
add_bullet("Maintain technician availability and active/inactive status; view assigned jobs and completed-job summary.")

# 5.3 Customer Management
add_heading_2("5.3 Customer Management")
add_heading_3("Customers")
add_body("Maintain a single customer profile and contact record.", "Purpose: ")
add_bullet("customer code, full name, mobile number, alternate number, email, address and notes.", "Fields: ")
add_bullet("Search by name, mobile number or customer code.")
add_bullet("View linked bikes, appointments, job cards, invoices, payments and outstanding balance.")
add_bullet("Detect possible duplicate customers using mobile number; allow authorized users to resolve duplicates.")

add_heading_3("Customer Vehicles")
add_body("Register and maintain bikes owned or used by a customer.", "Purpose: ")
add_bullet("Link each bike to a customer.")
add_bullet("registration number, brand, model, variant, engine number, chassis number, manufacturing year, colour and current odometer reading.", "Fields: ")
add_bullet("Capture fuel level and visible condition at check-in as visit-specific data, not as permanent vehicle master data.")
add_bullet("Support multiple bikes per customer and vehicle ownership updates with an audit trail.")

add_heading_3("Vehicle History")
add_body("Show the chronological service history for a selected bike.", "Purpose: ")
add_bullet("Display job card number, visit date, odometer, complaints, work performed, parts used, invoice amount and next service due.")
add_bullet("Open historical job card and invoice details.")
add_bullet("Show previous repairs and recurring complaints to help the service advisor.")

# 5.4 Workshop Operations
add_heading_2("5.4 Workshop Operations")
add_heading_3("Appointments")
add_body("Schedule customer visits and expected workshop capacity.", "Purpose: ")
add_bullet("Create appointment against an existing or new customer and registered bike.")
add_bullet("date, time slot, requested service, complaint, preferred branch and contact details.", "Fields: ")
add_bullet("requested, confirmed, arrived, rescheduled, cancelled and no-show.", "Statuses: ")
add_bullet("Calendar/list views, appointment reminders and conversion to vehicle check-in.")

add_heading_3("Vehicle Check-in")
add_body("Record the bike's condition and customer-reported concerns when it arrives.", "Purpose: ")
add_bullet("Create a check-in/inspection record and link it to the customer and bike.")
add_bullet("Capture arrival date/time, odometer, fuel level, accessories received, visible damage and photos if enabled.")
add_bullet("Record customer complaints and requested work; generate check-in reference and proceed to job card.")

add_heading_3("Job Cards")
add_body("Act as the central work order connecting customer, vehicle, services, technician, parts and billing.", "Purpose: ")
add_bullet("Create a unique job card number and link branch, customer, bike and check-in.")
add_bullet("Record customer complaints, inspection findings, requested services, labour lines, parts and estimated completion time.")
add_bullet("Maintain status, notes, attachments/photos and approval history.")
add_bullet("Track estimate approval or rejection; record customer approval and timestamp.")
add_bullet("Support additional work only after recording the additional estimate and customer approval.")
add_bullet("Show a complete job card timeline and linked estimate, invoice and payment.")

add_heading_3("Mechanic Assignment")
add_body("Allocate work to one or more technicians.", "Purpose: ")
add_bullet("Assign technician, task or service line, priority and target completion time.")
add_bullet("Show technician workload and availability before assignment.")
add_bullet("Allow reassignment with reason and audit history; technician sees only assigned work and permitted information.")

add_heading_3("Service Tracking")
add_body("Track work progress from assignment through completion.", "Purpose: ")
add_bullet("assigned, in progress, on hold, work completed and submitted for quality check.", "Statuses: ")
add_bullet("Record start/pause/resume/completion timestamps and technician remarks.")
add_bullet("awaiting spare part, customer approval, technical review or other.", "On-Hold Reasons: ")
add_bullet("Record parts consumed and labour performed against the job card; show pending duration and overdue work.")

add_heading_3("Quality Inspection")
add_body("Verify that work is completed correctly before billing/delivery.", "Purpose: ")
add_bullet("Use configurable checklist items such as brakes, lights, horn, tyres, chain, oil leakage and road test.")
add_bullet("Record pass/fail/not applicable, remarks and inspector; failed checks return the job to the workshop.")
add_bullet("Record final odometer and test-ride result; approve job for invoicing and delivery.")

add_heading_3("Vehicle Delivery")
add_body("Control final handover of the serviced bike.", "Purpose: ")
add_bullet("Confirm final invoice and payment status or authorized credit/partial-payment exception.")
add_bullet("Record delivery date/time, receiver name, handover remarks and confirmation.")
add_bullet("Provide invoice/receipt and service summary; set job card to delivered and update next service due.")

# 5.5 Service Configuration
add_heading_2("5.5 Service Configuration")
add_bullet("Group services for easier setup and reporting (Periodic Maintenance, Engine, Brakes, Electrical, Tyres, Wash).", "Service Categories: ")
add_bullet("Maintain individual service operations, standard labour charge, duration, and tax treatment.", "Service Catalogue: ")
add_bullet("Bundle common services into predefined packages (Basic, General, Premium) with included labour and parts.", "Service Packages: ")
add_bullet("Maintain supported motorcycle manufacturers (Yamaha, Royal Enfield, KTM, Honda, Bajaj, etc.).", "Brands: ")
add_bullet("Maintain models and variants under each brand with engine capacity, fuel type, and specifications.", "Bike Models: ")

# 5.6 Inventory
add_heading_2("5.6 Inventory")
add_bullet("Maintain spare parts SKU, name, category, brand, unit, purchase cost, selling price, tax rate and reorder level.", "Spare Parts: ")
add_bullet("Track quantity and valuation by branch; handle receipts, job card auto-deduction, transfers, adjustments, low-stock alerts.", "Stock Management: ")
add_bullet("Maintain vendor profiles, contact person, mobile, email, address, GSTIN and payment terms.", "Suppliers: ")
add_bullet("Manage replenishment orders, PO creation, approval, goods receipt (GRN) and discrepancy notes.", "Purchase Orders: ")

# 5.7 Finance
add_heading_2("5.7 Finance")
add_bullet("Prepare proposed cost before work; calculate subtotal, discount, GST, total; record customer approval method/time.", "Estimates: ")
add_bullet("Generate official tax bill from approved work and parts consumed; unique branch number; immutable PDF download.", "Invoices: ")
add_bullet("Record cash, UPI, card payments; support advance offsets, partial payments, multiple receipts, and balance due.", "Payments: ")
add_bullet("Record branch operating expenses (rent, utilities, consumables) to compute true net profit without mixing with sales.", "Expenses: ")

# 5.8 Reports & 5.9 System
add_heading_2("5.8 Reports")
add_bullet("Summarize invoiced sales, discounts, tax, collections, refunds and outstanding balance by date and branch.", "Revenue Reports: ")
add_bullet("Measure throughput: jobs received, WIP, completed, delivered, turnaround time and repeat-service trends.", "Service Reports: ")
add_bullet("Side-by-side branch comparison: jobs, revenue, collections, expenses, and inventory indicators.", "Branch Reports: ")
add_bullet("Review technician workload, completed jobs, labor recovery, and rework/failed inspection counts.", "Technician Reports: ")
add_bullet("Current stock valuation, low-stock alerts, fast/slow-moving parts, and movement ledger.", "Inventory Reports: ")

add_heading_2("5.9 System")
add_bullet("Manage in-app alerts and external SMS/WhatsApp/email milestone templates and delivery logs.", "Notifications: ")
add_bullet("Configure company profile, GST registration, branch hours, invoice numbering prefixes, and backup policies.", "Settings: ")
add_bullet("Maintain immutable traceability: user, role, branch, action type, before/after values, and timestamps.", "Audit Logs: ")

# ==========================================
# 6. CORE END-TO-END WORKFLOW
# ==========================================
add_heading_1("6. Core End-to-End Workflow")
wf_headers = ["Stage #", "Workflow Stage", "Expected System Behavior"]
wf_rows = [
    ["1", "Appointment / Walk-in", "Create appointment or register a walk-in arrival."],
    ["2", "Customer & Bike", "Find or create the customer and select/register the bike."],
    ["3", "Vehicle Check-in", "Capture odometer, fuel, condition, photos and complaints."],
    ["4", "Job Card", "Create job card and add requested services and inspection findings."],
    ["5", "Estimate & Approval", "Prepare estimate and record customer approval before chargeable work."],
    ["6", "Technician Assignment", "Assign technician(s), tasks and target completion."],
    ["7", "Service Execution", "Update progress, record work and consume spare parts."],
    ["8", "Quality Check", "Complete checklist; failed items return to workshop."],
    ["9", "Final Invoice", "Generate bill from approved work and actual consumption."],
    ["10", "Payment & Delivery", "Record payment/authorized balance and confirm vehicle handover."],
    ["11", "Service History", "Update vehicle history and next service reminder."]
]
create_table(wf_headers, wf_rows, [Inches(1.0), Inches(2.2), Inches(3.8)])

# ==========================================
# 7. COMMON STATUS DEFINITIONS & 8. BUSINESS RULES
# ==========================================
add_heading_1("7. Common Status Definitions")
stat_headers = ["Functional Area", "Recommended Status Progression"]
stat_rows = [
    ["Appointment", "Requested → Confirmed → Arrived / Rescheduled / Cancelled / No-show"],
    ["Estimate", "Draft → Shared → Awaiting Approval → Approved / Rejected / Revised"],
    ["Job Card", "Received → Inspection Pending → Estimate Pending → Approved → Assigned → In Progress → On Hold → Quality Check → Completed → Ready for Delivery → Delivered; Cancelled where permitted."],
    ["Purchase Order", "Draft → Submitted → Approved → Partially Received → Received; Cancelled where permitted."],
    ["Payment", "Unpaid / Partially Paid / Paid / Refunded or Adjusted"]
]
create_table(stat_headers, stat_rows, [Inches(1.8), Inches(5.2)])

add_heading_1("8. Important Business Rules")
rules = [
    "Every operational record must belong to a branch. Super Admin can access all branches; Branch Admin is restricted to assigned branch data.",
    "Each customer may have multiple bikes. Each bike may have multiple service visits and job cards.",
    "Job card is the central reference for check-in, work, technician assignment, parts consumption, estimate, invoice and delivery.",
    "Chargeable additional work must be estimated and approved before execution; retain the approval record.",
    "Stock should be reduced only through a recorded issue/consumption transaction, not by directly editing a quantity.",
    "An issued invoice or completed payment must not be silently deleted; use controlled cancellation, refund or adjustment records.",
    "Technicians should not access finance, user administration or organization-wide reports unless explicitly granted.",
    "Customer login is out of scope. Customer communication can be sent through configured channels without creating a customer account.",
    "Record timestamps and user IDs for approvals, status changes, stock movements and financial transactions.",
    "Use configurable tax rules and invoice formats appropriate to the business's applicable GST registration and billing setup."
]
for idx, r in enumerate(rules, 1):
    add_bullet(r, f"Rule {idx}: ")

# ==========================================
# 9. ADDRESS HANDLING ARCHITECTURE
# ==========================================
add_heading_1("9. Address Handling Architecture")
add_body("A robust automotive workshop management system must handle address data across multiple operational contexts with clear distinction between normalized storage, customer contact, and frozen legal invoice snapshots:")

add_heading_2("A. Address Structure Standard")
add_bullet("Door / Flat / Plot No: Precise physical premise identifier (e.g. 'Plot 14/2A' or 'Flat 3B, Sri Sai Apartments').", "1. Line 1: ")
add_bullet("Street Name, Cross Road, or Industrial Main Road (e.g. 'SIDCO Industrial Estate Road').", "2. Line 2: ")
add_bullet("Prominent physical landmark crucial for local delivery and logistics (e.g. 'Near Ambattur Telephone Exchange').", "3. Landmark: ")
add_bullet("Neighborhood / Locality (e.g. 'Anna Nagar West', 'Ambattur OT', 'Avadi').", "4. Area: ")
add_bullet("City / Town (Standardized default 'Chennai').", "5. City: ")
add_bullet("District & State (Standardized to 'Chennai District', 'Tamil Nadu').", "6. District & State: ")
add_bullet("Strict 6-digit numerical postal index code (e.g. '600058', '600054', '600040').", "7. Pincode: ")

add_heading_2("B. Entity-Specific Address Lifecycle")
add_bullet("Maintained by Super Admin. Includes geo-coordinates (Lat/Long) for Google Maps navigation. Displayed on invoice headers and job cards.", "Branch Address: ")
add_bullet("Maintained on Customer Profile. Captures customer residential/billing address. When a customer moves, updating the profile updates future visits.", "Customer Address: ")
add_bullet("Recorded for statutory compliance and emergency contact verification.", "Employee Address: ")
add_bullet("Contains vendor warehouse address and GSTIN state code for accurate CGST/SGST vs IGST calculation.", "Supplier Address: ")
add_bullet("CRITICAL RULE: The address printed on an invoice or job card is stored as an immutable frozen snapshot. If a customer or branch relocates two years later, historical tax invoices must NEVER alter their printed address block.", "Invoice Address Snapshot: ")

# ==========================================
# 10. SCREENS, PHASES & CONFIRMATIONS
# ==========================================
add_heading_1("10. Suggested Key Screens & Development Phases")
scr_headers = ["Module Area", "Primary Screens"]
scr_rows = [
    ["Dashboard", "Branch dashboard, consolidated dashboard, date/branch filters"],
    ["Customers & Bikes", "Customer list, customer profile, bike list, bike profile, service history"],
    ["Workshop Operations", "Appointment calendar, check-in form, job card list/detail, assignment board, service tracker, QC checklist, delivery form"],
    ["Service Masters", "Service category, service catalogue, package, brand, model, spare part"],
    ["Inventory", "Stock overview, stock ledger, goods receipt, stock transfer, purchase order"],
    ["Finance", "Estimate builder, invoice detail/PDF, payment collection, receipt, expense entry"],
    ["Administration", "Branch form, user list/form, role-permission matrix, settings, audit log"]
]
create_table(scr_headers, scr_rows, [Inches(2.2), Inches(4.8)])

add_heading_2("Recommended Development Phases")
phase_headers = ["Phase", "Scope", "Outcome"]
phase_rows = [
    ["Phase 1 – Foundation", "Authentication, roles, branches, employees, customers, vehicles, brands and models", "Secure branch-aware master data"],
    ["Phase 2 – Workshop Core", "Appointments, check-in, job cards, estimates, technician assignment, tracking, QC and delivery", "End-to-end service operations"],
    ["Phase 3 – Billing", "Invoices, GST configuration, payments, receipts and expenses", "Operational billing and collection"],
    ["Phase 4 – Inventory", "Parts, stock ledger, suppliers, purchase orders and consumption", "Branch-wise stock control"],
    ["Phase 5 – Insights & Automation", "Reports, notifications, audit logs and reminders", "Management visibility and workflow automation"]
]
create_table(phase_headers, phase_rows, [Inches(1.8), Inches(3.2), Inches(2.0)])

add_heading_1("11. Items to Confirm Before Development")
items = [
    "Is Nitro Racing operating from one branch initially or multiple branches from day one?",
    "Should appointments be entered only by staff, or should a public online booking page be added later?",
    "Will each branch maintain its own spare-parts stock and purchase orders?",
    "Should the system support customer approval by recorded phone/WhatsApp confirmation, signature, or both?",
    "Are technician time tracking, payroll and incentives required, or is technician productivity reporting sufficient?",
    "Which GST invoice rules, numbering format and receipt design should be configured for the business?",
    "Should SMS/WhatsApp integrations be part of the first release or a later phase?"
]
for idx, item in enumerate(items, 1):
    add_bullet(item, f"Question {idx}: ")

add_heading_1("12. Scope Summary")
add_body("The recommended first release should prioritize branch setup, user access, customers and bikes, service configuration, check-in, job cards, technician assignment, service tracking, quality inspection, invoices, payments and delivery. Inventory depth, supplier procurement, advanced analytics and messaging can be delivered in subsequent phases without changing the core job-card-centered workflow.")

doc.save("Nitro_Racing_Application_BRD.docx")
print("Nitro_Racing_Application_BRD.docx generated successfully.")
