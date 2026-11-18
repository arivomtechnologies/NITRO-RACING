import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()
# Remove default sheet
wb.remove(wb.active)

# Color Palette: Racing Orange #F15A24, Dark Navy #101D35, Light Grey #F4F6F9
NAVY = "101D35"
ORANGE = "F15A24"
LIGHT_GREY = "F4F6F9"
WHITE = "FFFFFF"
BORDER_GREY = "D6D9DD"
GREEN = "229B62"
YELLOW = "E9A23B"

font_title = Font(name="Calibri", size=15, bold=True, color=WHITE)
font_sec_hdr = Font(name="Calibri", size=12, bold=True, color=WHITE)
font_col_hdr = Font(name="Calibri", size=10, bold=True, color=WHITE)
font_data = Font(name="Calibri", size=9.5, color="17191D")
font_bold = Font(name="Calibri", size=9.5, bold=True, color="17191D")
font_code = Font(name="Consolas", size=9, bold=True, color="101D35")
font_sub = Font(name="Calibri", size=9, italic=True, color="555555")

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

def format_title_banner(ws, title, subtitle):
    ws.merge_cells("A1:I1")
    c1 = ws["A1"]
    c1.value = title
    c1.font = font_title
    c1.fill = fill_navy
    c1.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws.row_dimensions[1].height = 36

    ws.merge_cells("A2:I2")
    c2 = ws["A2"]
    c2.value = subtitle
    c2.font = Font(name="Calibri", size=10, italic=True, color="EEEEEE")
    c2.fill = fill_orange
    c2.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws.row_dimensions[2].height = 22
    ws.row_dimensions[3].height = 10

def style_table_headers(ws, row_idx, headers):
    ws.row_dimensions[row_idx].height = 26
    for col_idx, h in enumerate(headers, 1):
        cell = ws.cell(row=row_idx, column=col_idx, value=h)
        cell.font = font_col_hdr
        cell.fill = fill_navy
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = thin_border

def autofit_cols(ws, min_widths=None):
    ws.views.sheetView[0].showGridLines = True
    for col in ws.columns:
        col_letter = get_column_letter(col[0].column)
        max_len = 0
        for cell in col:
            val = str(cell.value or '')
            if '\n' in val:
                lines = val.split('\n')
                max_len = max(max_len, max(len(l) for l in lines))
            else:
                max_len = max(max_len, len(val))
        calc_w = max(max_len + 3, 10)
        if min_widths and col_letter in min_widths:
            calc_w = max(calc_w, min_widths[col_letter])
        ws.column_dimensions[col_letter].width = min(calc_w, 55)

# ==============================================================================
# SHEET 1: MENU & SUBMENU MATRIX
# ==============================================================================
ws1 = wb.create_sheet(title="Menu & Submenu Matrix")
format_title_banner(ws1, "NITRO RACING - APPLICATION MENU & SUBMENU ARCHITECTURE", 
                    "Functional Mapping: 9 Modules, 32 Submenus, Role Permissions, Data Maintained & Target Screens")

headers1 = [
    "Module #", "Main Menu", "Submenu Name", "Business Purpose & Description", 
    "Key Functions & Capabilities", "Permitted Roles", "Data Fields Maintained", 
    "Expected Outcome / Screen Result", "Key Screen Reference"
]
style_table_headers(ws1, 4, headers1)

menu_rows = [
    # 1. Dashboard
    ("1.0", "Dashboard", "Dashboard", 
     "At-a-glance operational and financial summary. Default view scoped to user's branch; Super Admin can view consolidated cross-branch data.",
     "Filter by branch, date range, job status; view live KPI cards; monitor overdue jobs and low-stock alerts; quick drill-down.",
     "Super Admin, Branch Admin",
     "Branch ID, Date Range, KPI counts (received, WIP, QC, ready, delivered, unpaid), revenue trends, technician bay load.",
     "Live executive operational dashboard with charts, alerts, and pending action queues.", "Branch / Consolidated Dashboard"),

    # 2. Organization
    ("2.1", "Organization", "Branches", 
     "Maintain physical service locations, geo-coordinates, and operational capacity.",
     "Create, view, edit, activate/deactivate branches; set business hours, GSTIN, invoice sequence prefix, and bay counts.",
     "Super Admin",
     "branch_code, branch_name, door_no, street, landmark, area, city, district, state, pincode, phone, email, manager, gstin, status.",
     "Multi-tenant branch master isolating operational data by branch.", "Branch Management Form / List"),
    ("2.2", "Organization", "Users & Roles", 
     "Manage application login accounts, authentication credentials, and permission profiles.",
     "Create login accounts, map to Role (Super Admin / Branch Admin / Technician) and branch; reset passwords; deactivate users.",
     "Super Admin",
     "user_id, username, email, password_hash, role_code, branch_id, is_active, last_login_at.",
     "Secure role-based access control; no public customer registration.", "User List & Role Permission Matrix"),
    ("2.3", "Organization", "Employees", 
     "Maintain workshop workforce, service advisors, mechanics, and technicians.",
     "Track employee profiles, joining date, skill tags (Engine, Electricals, Superbikes), map to login user account; view workload.",
     "Super Admin, Branch Admin",
     "emp_id, full_name, mobile, email, branch_id, designation, skills_json, address, emergency_contact, status.",
     "Complete technician roster available for job card mechanic allocation.", "Employee Directory / Profile"),

    # 3. Customer Management
    ("3.1", "Customer Management", "Customers", 
     "Maintain centralized customer master profiles, contact records, and structured addresses.",
     "Search customer by mobile/name; detect duplicate mobile numbers; view linked vehicles, job cards, outstanding ledger balance.",
     "Super Admin, Branch Admin, Technician (Search/Create)",
     "customer_code, full_name, primary_mobile, alt_mobile, email, door_no, street_name, landmark, locality, city, pincode, notes.",
     "Single customer profile linked to multiple motorcycles and past repair orders.", "Customer Profile & Ledger View"),
    ("3.2", "Customer Management", "Customer Vehicles", 
     "Register and maintain motorcycles owned or used by customers.",
     "Link bike to customer; capture registration number, brand, model, engine/chassis no, year, color, initial odometer; support ownership transfer.",
     "Super Admin, Branch Admin, Technician",
     "bike_id, customer_id, reg_number, brand, model, variant, engine_no, chassis_no, mfg_year, color, current_odometer.",
     "Persistent vehicle master with permanent technical specifications.", "Bike Profile & Ownership Card"),
    ("3.3", "Customer Management", "Vehicle History", 
     "Chronological timeline of all service visits, replaced parts, and recorded complaints for a bike.",
     "Lookup bike registration; inspect past job cards, replaced parts, previous diagnoses, recurring complaints, invoice history.",
     "Super Admin, Branch Admin, Technician",
     "bike_id, job_card_id, visit_date, odometer, customer_complaint, work_performed, parts_used, invoice_amount, next_service_due.",
     "Complete service timeline assisting service advisor in accurate diagnosis.", "Vehicle Timeline & Past Repairs"),

    # 4. Workshop Operations
    ("4.1", "Workshop Operations", "Appointments", 
     "Schedule customer visits and forecast daily workshop bay capacity.",
     "Create appointment, select customer/bike, service package, time slot; track status (Requested, Confirmed, Arrived, Cancelled).",
     "Super Admin, Branch Admin",
     "appointment_id, branch_id, customer_id, bike_id, scheduled_date, time_slot, service_requested, status, notes.",
     "Controlled workshop intake preventing morning rush and bay overcrowding.", "Appointment Calendar & Booking Queue"),
    ("4.2", "Workshop Operations", "Vehicle Check-in", 
     "Record physical condition and customer concerns when motorcycle arrives at garage.",
     "Capture check-in date/time, exact odometer, fuel level, scratch/dent map, accessories received (helmet, tool kit), customer complaints.",
     "Super Admin, Branch Admin, Technician",
     "checkin_id, branch_id, bike_id, customer_id, arrival_time, odometer, fuel_level, scratch_notes, tool_kit_held, complaint_text.",
     "Formal intake record protecting garage from pre-existing damage disputes.", "Vehicle Check-in / Damage Inspection Form"),
    ("4.3", "Workshop Operations", "Job Cards", 
     "Central operational work order connecting customer, vehicle, services, technician, parts, and billing.",
     "Generate unique Job Card (#JC-AMB-001); attach complaints, inspection findings, labor lines, spare parts, advance deposit paid.",
     "Super Admin, Branch Admin, Technician",
     "job_card_no, branch_id, customer_id, bike_id, checkin_id, status, advance_paid, est_completion, mechanic_id, total_amount.",
     "End-to-end work order tracking vehicle from intake to final handover.", "Job Card Detail & Service Board"),
    ("4.4", "Workshop Operations", "Mechanic Assignment", 
     "Allocate repair orders to specialized technicians based on workload.",
     "View active technician bay load; assign primary technician and assistant; reassign with recorded reason and audit timestamp.",
     "Branch Admin",
     "assignment_id, job_card_id, technician_id, assigned_at, target_completion, priority, reassignment_reason.",
     "Balanced workshop floor throughput with clear technician accountability.", "Technician Assignment Board"),
    ("4.5", "Workshop Operations", "Service Tracking", 
     "Real-time workshop progress tracking through repair milestones.",
     "Technician updates status: Assigned -> In Progress -> On Hold -> Completed; record hold reasons (parts/approval); log parts used.",
     "Super Admin, Branch Admin, Technician",
     "tracking_id, job_card_id, status, start_time, pause_time, resume_time, complete_time, hold_reason, technician_notes.",
     "Live workshop tracking with real-time status visibility.", "Service Tracker & Bay Status"),
    ("4.6", "Workshop Operations", "Quality Inspection", 
     "Pre-delivery verification verifying work is completed correctly before billing.",
     "Complete checklist (brakes, lights, chain tension, fluid leaks, road test); record pass/fail; failed checks return to workshop.",
     "Branch Admin, Lead Technician",
     "qc_id, job_card_id, inspected_by, checklist_results_json, road_test_done, final_odometer, qc_status, remarks.",
     "Zero-defect vehicle release ensuring safety and high customer satisfaction.", "QC Checklist & Inspection Form"),
    ("4.7", "Workshop Operations", "Vehicle Delivery", 
     "Control final handover of serviced motorcycle to customer.",
     "Verify invoice payment or authorized balance; record handover time, receiver name, gate pass release; update next service reminder.",
     "Branch Admin, Service Advisor",
     "delivery_id, job_card_id, invoice_id, delivered_at, received_by_name, payment_verified, gate_pass_no, handover_remarks.",
     "Job card finalized to 'Delivered' and vehicle returned to owner.", "Delivery Gate Pass & Handover Form"),

    # 5. Service Configuration
    ("5.1", "Service Configuration", "Service Categories", 
     "Logical grouping of motorcycle service offerings.",
     "Maintain categories (Periodic Maintenance, Engine Overhaul, Brake Service, Electricals, Tyres, Detailing); set display order.",
     "Super Admin",
     "category_id, category_name, description, display_order, is_active.",
     "Organized service taxonomy for catalog and reporting.", "Service Category Master"),
    ("5.2", "Service Configuration", "Service Catalogue", 
     "Master list of individual service operations, standard labor charges, and turnaround durations.",
     "Create services (e.g. Engine Oil Change, Front Brake Pad Replacement); configure standard labor charge, duration, GST rate.",
     "Super Admin, Branch Admin (Price Override)",
     "service_code, service_name, category_id, description, standard_labor_rate, est_minutes, tax_rate, is_active.",
     "Standardized labor pricing across branches with controlled price override.", "Service Catalogue Master"),
    ("5.3", "Service Configuration", "Service Packages", 
     "Predefined bundles of common services and included parts for popular maintenance tiers.",
     "Define packages (Basic Service, General Periodic Service, Premium Track Service); bundle labor ops and standard parts at fixed price.",
     "Super Admin",
     "package_id, package_name, included_services_json, included_parts_json, package_price, duration_hours, applicable_models.",
     "1-Click package selection on appointment or job card.", "Service Package Configuration"),
    ("5.4", "Service Configuration", "Brands", 
     "Maintain supported two-wheeler motorcycle manufacturers.",
     "Add brands (Yamaha, Royal Enfield, KTM, Honda, Bajaj, TVS, Suzuki); prevent duplicates; link to bike models.",
     "Super Admin",
     "brand_id, brand_name, description, logo_url, is_active.",
     "Master brand directory ensuring clean motorcycle registration.", "Brand Master"),
    ("5.5", "Service Configuration", "Bike Models", 
     "Maintain vehicle models and engine variants under each brand.",
     "Create models (e.g., Yamaha R15 V4, RE Classic 350, KTM Duke 390); record engine capacity (CC), fuel type, oil capacity.",
     "Super Admin",
     "model_id, brand_id, model_name, variant, engine_cc, fuel_type, engine_oil_capacity_litres, is_active.",
     "Structured model selection for bike profiles and service specs.", "Bike Model & Variant Master"),

    # 6. Inventory
    ("6.1", "Inventory", "Spare Parts", 
     "Maintain spare parts product catalog, SKUs, and retail pricing.",
     "Create parts (Spark Plug, Synthetic Engine Oil, Brake Pads, Chain Sprocket Kit); maintain SKU, brand, cost, selling price, GST rate, reorder level.",
     "Super Admin, Branch Admin",
     "part_id, part_sku, part_name, category, brand, unit, purchase_cost, selling_price, gst_rate, min_reorder_level, is_active.",
     "Master parts catalog preventing price leakage and manual entry errors.", "Spare Parts Master Catalog"),
    ("6.2", "Inventory", "Stock Management", 
     "Track real-time quantity and valuation of spare parts at each branch.",
     "Record stock receipts, job card auto-deduction, inter-branch transfers, physical stock adjustments; view low-stock alerts.",
     "Branch Admin",
     "stock_id, branch_id, part_id, qty_on_hand, qty_reserved, qty_available, bin_location, last_counted_at.",
     "Branch inventory ledger preventing pilferage and stockouts.", "Stock Balance & Movement Ledger"),
    ("6.3", "Inventory", "Suppliers", 
     "Maintain vendor profiles for parts procurement and wholesale accounts.",
     "Create suppliers (Motul Distributors, Bosch Spares, Brembo India); record address, contact person, mobile, email, GSTIN, payment terms.",
     "Super Admin, Branch Admin",
     "supplier_id, supplier_name, contact_person, mobile, email, address_line1, city, state, gstin, payment_terms_days.",
     "Vendor directory linked to purchase orders and spare parts inward.", "Supplier Directory"),
    ("6.4", "Inventory", "Purchase Orders", 
     "Manage parts procurement orders from draft through goods receipt.",
     "Create PO to supplier with item lines, ordered qty, negotiated unit rate; track statuses (Draft, Submitted, Approved, Received); auto-update stock on GRN.",
     "Super Admin, Branch Admin",
     "po_no, branch_id, supplier_id, order_date, expected_date, subtotal, tax_amount, grand_total, status, grn_notes.",
     "Controlled procurement with verified stock inward against purchase bill.", "Purchase Order & Goods Receipt (GRN)"),

    # 7. Finance
    ("7.1", "Finance", "Estimates", 
     "Prepare itemized cost quotations before starting chargeable repairs.",
     "Build estimate from labor lines and spare parts; calculate tax and discounts; share with rider; record customer approval/rejection timestamp.",
     "Super Admin, Branch Admin",
     "estimate_no, job_card_id, branch_id, labor_total, parts_total, gst_amount, grand_total, status, approval_method, approved_at.",
     "Transparent quotation eliminating customer bill shock and payment disputes.", "Estimate Builder & Approval Gateway"),
    ("7.2", "Finance", "Invoices", 
     "Generate official, tax-compliant PDF bill from approved work and consumed parts.",
     "Compile invoice from job card; apply labor, parts, GST (CGST/SGST), advance offset; generate immutable PDF with branch-specific invoice number.",
     "Super Admin, Branch Admin, Technician (Generate/Print)",
     "invoice_no, job_card_id, branch_id, customer_id, invoice_date, labor_amount, parts_amount, tax_amount, advance_deducted, balance_due, status.",
     "Immutable PDF invoice ready for mobile sharing, printing, and tax filing.", "Tax Invoice Detail & PDF Generator"),
    ("7.3", "Finance", "Payments", 
     "Record money collections, advance deposits, and balance settlements.",
     "Collect payment via Cash, UPI (GPay/PhonePe), Credit/Debit Card; support partial payments, split modes; print digital receipt.",
     "Super Admin, Branch Admin, Technician",
     "payment_id, invoice_id, job_card_id, branch_id, amount_paid, payment_mode, transaction_ref, payment_date, collected_by.",
     "Complete payment audit ledger with cash drawer reconciliation.", "Payment Collection & Receipt Ledger"),
    ("7.4", "Finance", "Expenses", 
     "Record branch operating overheads to compute true workshop net profit.",
     "Log expenses (rent, electricity, shop consumables, tea/refreshments, equipment service); categorize and attach vouchers.",
     "Branch Admin, Super Admin",
     "expense_id, branch_id, expense_date, category, description, amount, payment_mode, vendor_name, approved_by.",
     "Branch operating expenses separated from customer service revenue.", "Expense Entry & Daily Cash Book"),

    # 8. Reports
    ("8.1", "Reports", "Revenue Reports", 
     "Summarize service income, labor recovery, parts sales, and collections.",
     "Filter by branch, date range, payment method; view invoiced sales, tax collections, advance adjustments, and unpaid balances.",
     "Super Admin, Branch Admin",
     "Report parameters: branch_id, start_date, end_date, summary metrics (invoiced, collected, tax, receivables).",
     "Exportable revenue statements in PDF and spreadsheet format.", "Revenue & Collection Statement"),
    ("8.2", "Reports", "Service Reports", 
     "Measure workshop service throughput, turnaround time, and popular models.",
     "Analyze jobs received, WIP, completed, delivered; break down by service category and bike brand/model; track average turnaround hours.",
     "Super Admin, Branch Admin",
     "Aggregated metrics: job counts by category, brand breakdown, turnaround SLAs, repeat service count.",
     "Operational efficiency trends and capacity planning data.", "Workshop Throughput & SLA Report"),
    ("8.3", "Reports", "Branch Reports", 
     "Compare operational performance across service locations.",
     "Side-by-side comparison of Ambattur vs Avadi on revenue, jobs handled, technician productivity, parts profit, expenses.",
     "Super Admin",
     "Comparative table: branch, total jobs, gross sales, expenses, net profit margin, customer count.",
     "Multi-branch comparative analytics for executive decision-making.", "Multi-Branch Comparison Matrix"),
    ("8.4", "Reports", "Technician Reports", 
     "Evaluate technician productivity, completed jobs, and service quality.",
     "Review assigned jobs, completed jobs, billed labor recovery, average turnaround, and rework/QC failure incidents.",
     "Super Admin, Branch Admin",
     "Technician metrics: emp_id, jobs_completed, labor_billed, hours_logged, rework_count, qc_pass_rate.",
     "Transparent technician performance metrics for appraisal and incentives.", "Technician Productivity & QC Scorecard"),
    ("8.5", "Reports", "Inventory Reports", 
     "Monitor parts movement, stock valuation, and stockout warnings.",
     "View current stock by branch, valuation, low-stock reorder lists, fast-moving vs slow-moving parts, inventory turnover.",
     "Super Admin, Branch Admin",
     "Inventory ledger: part_id, opening_qty, receipts, job_issues, adjustments, closing_qty, total_valuation.",
     "Stock optimization preventing capital lockup and workshop delays.", "Inventory Valuation & Movement Report"),

    # 9. System
    ("9.1", "System", "Notifications", 
     "Manage internal task alerts and automated customer service milestones.",
     "In-app notifications for technician assignment, QC approval, job on hold; template triggers for customer SMS/WhatsApp/email.",
     "Super Admin, Branch Admin",
     "notification_id, trigger_event, recipient_role/customer, channel (in-app, SMS, email), template_body, delivery_status.",
     "Real-time operational alerts keeping staff and riders informed.", "Notification Center & Message Logs"),
    ("9.2", "System", "Settings", 
     "Configure organization-wide parameters, tax rules, and document sequences.",
     "Configure business profile, logo, GST registration, branch invoice prefixes (INV-AMB-, INV-AVD-), default appointment slots.",
     "Super Admin",
     "setting_key, setting_value, branch_id (null for global), description, updated_by, updated_at.",
     "Centralized application configuration without modifying code.", "System & Branch Settings Console"),
    ("9.3", "System", "Audit Logs", 
     "Maintain immutable traceability for security and compliance.",
     "Record user, role, branch, action type (CREATE, UPDATE, DELETE, OVERRIDE), record reference, before/after values, timestamp, IP address.",
     "Super Admin",
     "log_id, user_id, branch_id, action_type, entity_name, entity_id, change_summary, ip_address, created_at.",
     "Immutable audit trail protecting against unauthorized changes or fraud.", "Security & Audit Trail Log")
]

for r_idx, r_data in enumerate(menu_rows, start=5):
    ws1.row_dimensions[r_idx].height = 38
    for c_idx, val in enumerate(r_data, start=1):
        cell = ws1.cell(row=r_idx, column=c_idx, value=val)
        cell.font = font_data
        cell.border = thin_border
        cell.fill = fill_white if r_idx % 2 == 1 else fill_light
        
        # Alignments
        if c_idx in [1, 6]:
            cell.alignment = Alignment(horizontal="center", vertical="center")
            if c_idx == 1:
                cell.font = font_code
        elif c_idx in [2, 3]:
            cell.alignment = Alignment(horizontal="left", vertical="center")
            cell.font = font_bold
        else:
            cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

autofit_cols(ws1, {"A": 10, "B": 22, "C": 22, "D": 38, "E": 38, "F": 24, "G": 38, "H": 34, "I": 26})

# ==============================================================================
# SHEET 2: ADDRESS HANDLING ARCHITECTURE
# ==============================================================================
ws2 = wb.create_sheet(title="Address Handling Architecture")
format_title_banner(ws2, "NITRO RACING - ADDRESS DATA MODEL & HANDLING ARCHITECTURE", 
                    "Comprehensive Guide: Handling Structured Addresses across Branches, Customers, Employees & Invoices")

headers2 = [
    "Entity / Context", "Address Field Structure", "Storage Type (Normalized vs Text)", 
    "Mandatory / Optional", "Validation & Formatting Rules", "Lifecycle & Immutability Rules", 
    "Example Value (Nitro Racing Context)"
]
style_table_headers(ws2, 4, headers2)

addr_rows = [
    ("Branch (Store) Address", 
     "• Door / Plot No\n• Street / Road Name\n• Industrial / Commercial Landmark\n• Area / Locality\n• City / Town\n• District\n• State\n• Pincode (6 Digits)\n• Geo-Coordinates (Lat / Long)",
     "Normalized separate fields in 'branches' table + formatted display string helper.",
     "Mandatory (All fields required for branch setup)",
     "• Pincode: Strict 6-digit regex (^[1-9][0-9]{5}$).\n• State: Standardized to 'Tamil Nadu'.\n• Geo-coordinates: Decimal degrees (e.g. 13.1143, 80.1548) for GPS mapping.",
     "Managed exclusively by Super Admin. Updated only when physical branch relocates. Does not retrospectively change historical invoices.",
     "Door No. 14/2A, SIDCO Industrial Estate Road, Near Ambattur Telephone Exchange, Ambattur, Chennai District, Tamil Nadu - 600058 (Lat: 13.1143 N, Long: 80.1548 E)"),

    ("Customer Address", 
     "• Flat / Door / House No\n• Building / Apartment Name\n• Street / Cross Street\n• Landmark (Crucial for Chennai local navigation)\n• Area / Neighborhood\n• City / Town\n• District\n• Pincode (6 Digits)",
     "Normalized separate fields in 'customers' table for accurate searching and geographic clustering.",
     "• Line 1 & Area: Mandatory\n• Pincode: Mandatory\n• Landmark: Recommended",
     "• Primary identification is Mobile Number.\n• Address fields cleansed: trim whitespace, proper-case capitalization.\n• Pincode lookup can auto-populate City ('Chennai') and State ('Tamil Nadu').",
     "Editable on Customer Profile. When customer updates address, existing profile updates; however, previously issued tax invoices retain historical snapshot.",
     "Flat 3B, Sri Sai Apartments, 2nd Cross Street, Opposite Nilgiris Supermarket, Anna Nagar West, Chennai District, Tamil Nadu - 600040"),

    ("Employee / Technician Address", 
     "• Permanent / Residential Door No\n• Street & Locality\n• City & State\n• Pincode\n• Emergency Contact Person\n• Emergency Phone Number",
     "Structured text / normalized fields in 'employees' table.",
     "Mandatory for employee onboarding & HR compliance",
     "• Valid mobile verification for emergency contacts.\n• Proof of address documented in employee master.",
     "Maintained by Branch Admin or Super Admin. Updated upon change of residence.",
     "Old No. 45, New No. 12, Gandhi Street, Near Railway Station, Avadi, Chennai, Tamil Nadu - 600054 (Contact: Priya - 98401 22334)"),

    ("Supplier / Vendor Address", 
     "• Office / Warehouse Plot No\n• Trade Center / Complex\n• Industrial Road / Area\n• City, State & Pincode\n• GSTIN State Code Match",
     "Normalized columns in 'suppliers' table with GSTIN validation.",
     "Mandatory for Purchase Orders and Input Tax Credit (ITC)",
     "• State code in GSTIN (e.g. '33' for Tamil Nadu) must match address state.\n• Essential for CGST/SGST vs IGST tax computation on parts purchase.",
     "Updated only on official vendor notification.",
     "Plot No. 88, Central Auto Spares Complex, G.S.T. Road, Guindy, Chennai, Tamil Nadu - 600032 (GSTIN: 33AAAAA1234A1Z5)"),

    ("Invoice & Job Card Address Snapshot", 
     "• Complete Frozen Address Block (Branch + Customer)\n• Branch GSTIN & Contact\n• Customer Billing Address at time of service",
     "Stored as an immutable JSON/Text snapshot in 'invoices' and 'job_cards' tables.",
     "Mandatory (Permanent Legal Record)",
     "• Read-only upon invoice generation.\n• Must remain 100% identical even if customer or branch details change 2 years later.",
     "Strict Legal Immutability: Ensures audited tax compliance and eliminates tampering of printed invoices.",
     "CUSTOMER SNAPSHOT: Rajesh Kumar, Flat 3B, Sri Sai Apts, Anna Nagar West, Chennai - 600040 | BRANCH: Nitro Racing Ambattur, SIDCO Industrial Estate, Chennai - 600058 (GSTIN: 33AABCN1234D1Z2)")
]

for r_idx, r_data in enumerate(addr_rows, start=5):
    ws2.row_dimensions[r_idx].height = 55
    for c_idx, val in enumerate(r_data, start=1):
        cell = ws2.cell(row=r_idx, column=c_idx, value=val)
        cell.font = font_data
        cell.border = thin_border
        cell.fill = fill_white if r_idx % 2 == 1 else fill_light
        if c_idx == 1:
            cell.font = font_bold
            cell.alignment = Alignment(horizontal="center", vertical="center")
        elif c_idx in [3, 4]:
            cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        else:
            cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

autofit_cols(ws2, {"A": 18, "B": 28, "C": 24, "D": 18, "E": 30, "F": 28, "G": 38})

# ==============================================================================
# SHEET 3: BRANCHES & USERS SAMPLE DATA
# ==============================================================================
ws3 = wb.create_sheet(title="Branches & Users (Data)")
format_title_banner(ws3, "NITRO RACING - SAMPLE MASTER DATA: BRANCHES & USERS", 
                    "Multi-Tenant Service Centers with Complete Address Breakdown & Role-Mapped Login Accounts")

# Section A: Branches
ws3.cell(row=4, column=1, value="1. OPERATIONAL BRANCHES (STORES)").font = font_sec_hdr
ws3.cell(row=4, column=1).fill = fill_orange

headers3_b = [
    "Branch Code", "Branch Name", "Door / Plot No", "Street / Area", "Landmark", 
    "City", "State & Pin", "Phone / Email", "Manager", "GSTIN", "Bay Capacity", "Status"
]
style_table_headers(ws3, 5, headers3_b)

branch_data = [
    ("BR-AMB-01", "Nitro Racing – Ambattur Branch", "Plot 14/2A", "SIDCO Industrial Estate Road", "Near Ambattur Telephone Exchange", 
     "Chennai", "Tamil Nadu - 600058", "+91 98400 11223\nambattur@nitroracing.in", "S. Ramanathan", "33AABCN1234D1Z2", "6 Hydraulic Bays", "ACTIVE"),
    ("BR-AVD-02", "Nitro Racing – Avadi Branch", "Old No. 82, New No. 4", "New Military Road", "Opposite Avadi Bus Terminus", 
     "Chennai", "Tamil Nadu - 600054", "+91 98401 22334\navadi@nitroracing.in", "M. Karthikeyan", "33AABCN1234D1Z2", "4 Hydraulic Bays", "ACTIVE"),
    ("BR-TNG-03", "Nitro Racing – T. Nagar Branch (Future)", "No. 25/1", "North Usman Road", "Near Panagal Park", 
     "Chennai", "Tamil Nadu - 600017", "+91 98402 33445\ntnagar@nitroracing.in", "TBD (Under Setup)", "33AABCN1234D1Z2", "8 Hydraulic Bays", "PLANNED")
]

for idx, b in enumerate(branch_data, start=6):
    ws3.row_dimensions[idx].height = 30
    for c_i, val in enumerate(b, 1):
        cell = ws3.cell(row=idx, column=c_i, value=val)
        cell.font = font_data
        cell.border = thin_border
        cell.fill = fill_white if idx % 2 == 1 else fill_light
        if c_i == 1:
            cell.font = font_code
            cell.alignment = Alignment(horizontal="center", vertical="center")
        elif c_i in [6, 11, 12]:
            cell.alignment = Alignment(horizontal="center", vertical="center")
        else:
            cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

# Section B: Users & Roles
start_u = 11
ws3.cell(row=start_u, column=1, value="2. APPLICATION USERS & ROLE ASSIGNMENTS").font = font_sec_hdr
ws3.cell(row=start_u, column=1).fill = fill_navy

headers3_u = [
    "User ID", "Full Name", "Username / Email", "Assigned Role", "Branch Scope", 
    "Linked Employee ID", "Mobile Number", "Last Login", "Session Expiry", "Status"
]
style_table_headers(ws3, start_u+1, headers3_u)

user_data = [
    ("USR-001", "Fertrick / Balasubramanian", "admin@nitroracing.in", "Super Admin", "All Branches (Global)", "EMP-DIR-01", "+91 98400 99999", "2026-11-14 09:15 AM", "24 Hours (Active)", "ACTIVE"),
    ("USR-002", "S. Ramanathan", "ramanathan.amb@nitroracing.in", "Branch Admin", "Nitro Racing – Ambattur", "EMP-AMB-01", "+91 98400 11223", "2026-11-14 08:30 AM", "24 Hours (Active)", "ACTIVE"),
    ("USR-003", "Hari Krishnan", "hari.tech@nitroracing.in", "Technician", "Nitro Racing – Ambattur", "EMP-AMB-03", "+91 98400 55667", "2026-11-14 08:45 AM", "24 Hours (Active)", "ACTIVE"),
    ("USR-004", "M. Karthikeyan", "karthik.avd@nitroracing.in", "Branch Admin", "Nitro Racing – Avadi", "EMP-AVD-01", "+91 98401 22334", "2026-11-14 08:20 AM", "24 Hours (Active)", "ACTIVE"),
    ("USR-005", "Suresh Kumar", "suresh.tech@nitroracing.in", "Technician", "Nitro Racing – Avadi", "EMP-AVD-03", "+91 98401 77889", "2026-11-14 08:50 AM", "24 Hours (Active)", "ACTIVE")
]

for idx, u in enumerate(user_data, start=start_u+2):
    ws3.row_dimensions[idx].height = 24
    for c_i, val in enumerate(u, 1):
        cell = ws3.cell(row=idx, column=c_i, value=val)
        cell.font = font_data
        cell.border = thin_border
        cell.fill = fill_white if idx % 2 == 1 else fill_light
        if c_i in [1, 4, 10]:
            cell.alignment = Alignment(horizontal="center", vertical="center")
            if c_i == 1:
                cell.font = font_code
            if c_i == 4 and val == "Super Admin":
                cell.font = font_bold
        else:
            cell.alignment = Alignment(horizontal="left", vertical="center")

autofit_cols(ws3)

# ==============================================================================
# SHEET 4: CUSTOMERS & VEHICLES SAMPLE DATA
# ==============================================================================
ws4 = wb.create_sheet(title="Customers & Vehicles (Data)")
format_title_banner(ws4, "NITRO RACING - SAMPLE MASTER DATA: CUSTOMERS & MOTORCYCLES", 
                    "Centralized Customer Master with Full Structured Address Breakdown & Linked Multi-Bike Profiles")

headers4 = [
    "Customer Code", "Customer Name", "Primary Mobile", "Door / Flat No", "Street & Landmark", 
    "Area / Locality", "City & Pin", "Linked Bike Reg #", "Brand & Model", "Current KMs", "Outstanding Bal"
]
style_table_headers(ws4, 4, headers4)

cust_data = [
    ("CUST-2026-001", "Rajesh Kumar", "+91 98410 12345", "Flat 3B, Sri Sai Apts", "2nd Cross Street, Opp Nilgiris", "Anna Nagar West", "Chennai - 600040", "TN-02-CD-4589", "Yamaha R15 V4 (Metallic Blue)", "14,250 km", "INR 0.00"),
    ("CUST-2026-001", "Rajesh Kumar", "+91 98410 12345", "Flat 3B, Sri Sai Apts", "2nd Cross Street, Opp Nilgiris", "Anna Nagar West", "Chennai - 600040", "TN-02-BF-1102", "Honda Activa 6G (Matte Grey)", "8,400 km", "INR 0.00"),
    ("CUST-2026-002", "Vignesh Sundaram", "+91 98411 23456", "Plot 45, Door 8", "Thiruvalluvar Street, Near Pillayar Kovil", "Ambattur OT", "Chennai - 600053", "TN-20-EA-9872", "Royal Enfield Classic 350", "22,800 km", "INR 0.00"),
    ("CUST-2026-003", "Praveen Chandran", "+91 98412 34567", "No. 12/A, Balaji Nagar", "Main Road, Behind Indian Oil Bunk", "Avadi", "Chennai - 600054", "TN-18-AZ-3341", "KTM 390 Duke (Orange/White)", "18,600 km", "INR 0.00"),
    ("CUST-2026-004", "Deepak Narayanan", "+91 98413 45678", "Door 24, 1st Floor", "7th Avenue, Near Shanthi Colony", "Anna Nagar", "Chennai - 600040", "TN-02-DK-7788", "Yamaha MT-15 V2 (Cyan Storm)", "11,200 km", "INR 0.00"),
    ("CUST-2026-005", "Arun Prasath", "+91 98414 56789", "House 6, 3rd Street", "Vivekananda Nagar, Near Lake View", "Kolathur", "Chennai - 600099", "TN-05-BX-5520", "Bajaj Pulsar NS200", "26,400 km", "INR 0.00")
]

for idx, c in enumerate(cust_data, start=5):
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

autofit_cols(ws4)

# ==============================================================================
# SHEET 5: SERVICE CONFIG & SPARE PARTS
# ==============================================================================
ws5 = wb.create_sheet(title="Service Config & Parts (Data)")
format_title_banner(ws5, "NITRO RACING - SAMPLE MASTER DATA: SERVICES & INVENTORY", 
                    "Standard Service Catalogue, Labor Rates, Packages & Spare Parts Product Master with Tax Rates")

# Section A: Services
ws5.cell(row=4, column=1, value="1. SERVICE CATALOGUE & STANDARD LABOR CHARGES").font = font_sec_hdr
ws5.cell(row=4, column=1).fill = fill_navy

headers5_s = [
    "Service Code", "Service Operation Name", "Category", "Std Duration", 
    "Base Labor Rate", "GST Rate", "Total Labor", "Applicable Models", "Status"
]
style_table_headers(ws5, 5, headers5_s)

srv_data = [
    ("SRV-GEN-01", "General Periodic Service (50-Point Inspection)", "Periodic Maintenance", "90 Mins", "INR 650.00", "18%", "INR 767.00", "All Two-Wheelers", "ACTIVE"),
    ("SRV-OIL-02", "Engine Oil & Filter Replacement Service", "Engine Operations", "30 Mins", "INR 150.00", "18%", "INR 177.00", "All Two-Wheelers", "ACTIVE"),
    ("SRV-BRK-03", "Front & Rear Brake Caliper Overhaul & Bleeding", "Brake System", "45 Mins", "INR 350.00", "18%", "INR 413.00", "Disc Brake Bikes", "ACTIVE"),
    ("SRV-CHN-04", "Chain Cleaning, Tensioning & High-Temp Lube", "Drive System", "25 Mins", "INR 200.00", "18%", "INR 236.00", "Chain Drive Bikes", "ACTIVE"),
    ("SRV-CLT-05", "Clutch Plate Assembly Replacement & Cable Setting", "Clutch & Gear", "60 Mins", "INR 450.00", "18%", "INR 531.00", "Manual Transmission", "ACTIVE"),
    ("SRV-WSH-06", "Foam Wash, Engine Degreasing & Teflon Polish", "Detailing & Wash", "40 Mins", "INR 300.00", "18%", "INR 354.00", "All Two-Wheelers", "ACTIVE")
]

for idx, s in enumerate(srv_data, start=6):
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

# Section B: Spare Parts
start_p = 14
ws5.cell(row=start_p, column=1, value="2. SPARE PARTS & INVENTORY PRODUCT MASTER").font = font_sec_hdr
ws5.cell(row=start_p, column=1).fill = fill_orange

headers5_p = [
    "Part SKU", "Part Description", "Category", "Brand / OEM", "Unit", 
    "Purchase Cost", "Selling Price", "GST Rate", "Ambattur Stock", "Avadi Stock", "Reorder Level"
]
style_table_headers(ws5, start_p+1, headers5_p)

parts_data = [
    ("PRT-OIL-001", "Motul 7100 10W50 Fully Synthetic (1L)", "Lubricants", "Motul", "Bottle", "INR 720.00", "INR 950.00", "18%", "24 Bottles", "16 Bottles", "10 Bottles"),
    ("PRT-FLT-002", "OEM Engine Oil Filter Element", "Engine Filters", "Yamaha / OEM", "Piece", "INR 110.00", "INR 180.00", "18%", "45 Pieces", "28 Pieces", "15 Pieces"),
    ("PRT-BRK-003", "Ceramic Front Disc Brake Pad Set", "Braking", "Brembo / Bosch", "Set", "INR 320.00", "INR 480.00", "18%", "18 Sets", "12 Sets", "8 Sets"),
    ("PRT-SPK-004", "NGK Iridium Spark Plug (CR9EIX)", "Ignition", "NGK", "Piece", "INR 450.00", "INR 650.00", "18%", "20 Pieces", "15 Pieces", "5 Pieces"),
    ("PRT-CHN-005", "Rolon Brass Chain & Sprocket Heavy-Duty Kit", "Drive Chain", "Rolon", "Kit", "INR 1,650.00", "INR 2,200.00", "18%", "8 Kits", "5 Kits", "4 Kits"),
    ("PRT-CLT-006", "FCC Genuine Friction Clutch Plate Set", "Transmission", "FCC / OEM", "Set", "INR 680.00", "INR 950.00", "18%", "12 Sets", "7 Sets", "5 Sets")
]

for idx, p in enumerate(parts_data, start=start_p+2):
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

autofit_cols(ws5)

# ==============================================================================
# SHEET 6: WORKSHOP DATA FLOW (CHECK-IN TO JOB CARDS)
# ==============================================================================
ws6 = wb.create_sheet(title="Workshop Operations (Data)")
format_title_banner(ws6, "NITRO RACING - SAMPLE OPERATIONAL DATA FLOW: CHECK-IN TO JOB CARD", 
                    "Active Repair Orders Tracing Customer Arrival, Vehicle Inspection, Job Card Generation & Technician Allocation")

headers6 = [
    "Job Card #", "Branch", "Customer & Phone", "Bike Reg # & Model", 
    "Odometer & Fuel", "Customer Reported Complaints", "Assigned Technician", 
    "Lifecycle Status", "Advance Collected", "Est Completion", "Linked Check-in ID"
]
style_table_headers(ws6, 4, headers6)

jc_data = [
    ("JC-AMB-2026-001", "Ambattur", "Rajesh Kumar\n(+91 98410 12345)", "TN-02-CD-4589\nYamaha R15 V4", 
     "14,250 km | 1/2 Tank", "1. Periodic 15k service\n2. Front brake spongey\n3. Chain loose & dry", "Hari Krishnan (Master Tech)", 
     "IN PROGRESS", "INR 500.00 (UPI)", "Today 04:30 PM", "CHK-AMB-0841"),
    ("JC-AMB-2026-002", "Ambattur", "Vignesh Sundaram\n(+91 98411 23456)", "TN-20-EA-9872\nRE Classic 350", 
     "22,800 km | 3/4 Tank", "1. Engine tappet noise at idle\n2. Oil leak near clutch cover\n3. General checkup", "S. Arumugam (Engine Specialist)", 
     "ESTIMATE PENDING", "INR 1,000.00 (Cash)", "Tomorrow 11:30 AM", "CHK-AMB-0842"),
    ("JC-AVD-2026-001", "Avadi", "Praveen Chandran\n(+91 98412 34567)", "TN-18-AZ-3341\nKTM 390 Duke", 
     "18,600 km | 1/4 Tank", "1. Front fork oil seal leaking\n2. Replace front brake pads\n3. High RPM misfire", "Suresh Kumar (Tech Lead)", 
     "QUALITY CHECK", "INR 1,000.00 (UPI)", "Today 02:00 PM", "CHK-AVD-0412"),
    ("JC-AVD-2026-002", "Avadi", "Deepak Narayanan\n(+91 98413 45678)", "TN-02-DK-7788\nYamaha MT-15 V2", 
     "11,200 km | Full Tank", "1. 10k Regular service\n2. Wash & Teflon Polish\n3. Handlebar vibration", "R. Vijay (Technician)", 
     "READY FOR DELIVERY", "INR 500.00 (UPI)", "Today 12:00 PM", "CHK-AVD-0415"),
    ("JC-AMB-2026-003", "Ambattur", "Arun Prasath\n(+91 98414 56789)", "TN-05-BX-5520\nBajaj Pulsar NS200", 
     "26,400 km | 1/4 Tank", "1. Clutch slipping in 4th/5th gear\n2. Rear tyre puncture check\n3. Oil change", "Hari Krishnan (Master Tech)", 
     "DELIVERED", "INR 500.00 (Cash)", "Yesterday 05:00 PM", "CHK-AMB-0839")
]

for idx, j in enumerate(jc_data, start=5):
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
                if val == "DELIVERED":
                    cell.fill = fill_tag_green
                elif val == "IN PROGRESS":
                    cell.fill = fill_tag_orange
        else:
            cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

autofit_cols(ws6)

# ==============================================================================
# SHEET 7: BILLING, INVOICES & PAYMENTS SAMPLE DATA
# ==============================================================================
ws7 = wb.create_sheet(title="Finance & Invoices (Data)")
format_title_banner(ws7, "NITRO RACING - SAMPLE FINANCIAL FLOW: INVOICES & PAYMENTS", 
                    "Itemized Billing: Labor + Parts + GST Calculation, Advance Deposit Adjustment, Payment Mode & Receipt Ledger")

headers7 = [
    "Invoice #", "Job Card #", "Branch", "Customer Name", 
    "Labor Charges", "Spare Parts Total", "GST (18%)", "Gross Bill", 
    "Less: Advance", "Net Balance Due", "Payment Status", "Payment Mode & Ref"
]
style_table_headers(ws7, 4, headers7)

inv_data = [
    ("INV-AMB-2026-0842", "JC-AMB-2026-001", "Ambattur", "Rajesh Kumar", 
     "INR 1,200.00", "INR 1,610.00", "INR 505.80", "INR 3,315.80", 
     "INR 500.00", "INR 2,815.80", "PENDING (Ready)", "Awaiting Pickup Settlement"),

    ("INV-AVD-2026-0412", "JC-AVD-2026-001", "Avadi", "Praveen Chandran", 
     "INR 950.00", "INR 1,130.00", "INR 374.40", "INR 2,454.40", 
     "INR 1,000.00", "INR 1,454.40", "PENDING (QC)", "Awaiting Delivery Settlement"),

    ("INV-AVD-2026-0415", "JC-AVD-2026-002", "Avadi", "Deepak Narayanan", 
     "INR 950.00", "INR 1,130.00", "INR 374.40", "INR 2,454.40", 
     "INR 500.00", "INR 1,954.40", "PAID IN FULL", "UPI: GPay/PhonePe Ref #981240982"),

    ("INV-AMB-2026-0839", "JC-AMB-2026-003", "Ambattur", "Arun Prasath", 
     "INR 800.00", "INR 1,900.00", "INR 486.00", "INR 3,186.00", 
     "INR 500.00", "INR 0.00", "PAID & CLOSED", "Cash Settlement at Counter")
]

for idx, inv in enumerate(inv_data, start=5):
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
            if c_i == 11 and "PAID" in val:
                cell.fill = fill_tag_green
                cell.font = font_bold
        elif c_i in [5, 6, 7, 8, 9, 10]:
            cell.alignment = Alignment(horizontal="right", vertical="center")
            if c_i == 10:
                cell.font = font_bold
        else:
            cell.alignment = Alignment(horizontal="left", vertical="center")

autofit_cols(ws7)

# ==============================================================================
# SHEET 8: END-TO-END DATA FLOW PIPELINE
# ==============================================================================
ws8 = wb.create_sheet(title="E2E Application Data Flow")
format_title_banner(ws8, "NITRO RACING - END-TO-END DATA FLOW & ENTITY LIFECYCLE", 
                    "Comprehensive Traceability: How Primary Keys, Foreign Keys, Statuses, and Address Data Flow from Stage 1 to 11")

headers8 = [
    "Stage #", "Workflow Stage", "Primary Menu / Submenu", "Input Entities / Source", 
    "System Actions & Calculations", "Output Entity Created", "Address Context Handled", "Next Transition"
]
style_table_headers(ws8, 4, headers8)

e2e_rows = [
    ("Stage 1", "Appointment / Walk-in", "Workshop Ops > Appointments", "Customer Mobile or Public Website Form", 
     "System checks customer phone number. If exists, loads customer & bike; if new, triggers customer creation.", 
     "appointment_id (Status: REQUESTED -> CONFIRMED)", "Captures preferred branch; verifies service location.", "Proceed to Check-in"),

    ("Stage 2", "Customer & Bike Intake", "Customer Mgmt > Customers / Vehicles", "Customer Name, Mobile, Structured Address, Bike Plate", 
     "Persists customer and vehicle profile. Normalizes address into Door No, Street, Area, City, Pin.", 
     "customer_code, bike_id", "Normalizes residential address for communications and geo-filtering.", "Proceed to Vehicle Check-in"),

    ("Stage 3", "Vehicle Check-in & Condition", "Workshop Ops > Vehicle Check-in", "Arrival time, current odometer, fuel level, scratches", 
     "Records intake condition to prevent garage liability. Attaches complaints.", 
     "checkin_id, vehicle_inspections record", "Tied strictly to physical branch location.", "Proceed to Job Card"),

    ("Stage 4", "Job Card Work Order", "Workshop Ops > Job Cards", "checkin_id, customer_id, bike_id, advance amount", 
     "Generates sequential Job Card (#JC-AMB-001). Locks branch tenancy. Records initial advance deposit.", 
     "job_card_no (Status: RECEIVED)", "Branch address embedded into job card header.", "Proceed to Estimate / Assign"),

    ("Stage 5", "Estimate & Approval", "Finance > Estimates", "Labor operations + required spare parts", 
     "Calculates subtotal, discounts, GST (18%), and net total. Dispatches digital estimate to customer.", 
     "estimate_no (Status: APPROVED / REVISED)", "Transmits via customer mobile / WhatsApp.", "Proceed to Mechanic Assignment"),

    ("Stage 6", "Technician Assignment", "Workshop Ops > Mechanic Assignment", "job_card_no, technician_id, target duration", 
     "Checks technician bay workload. Assigns lead mechanic and assistant with target completion time.", 
     "assignment_id, mechanic_id mapped", "Technician must belong to same branch.", "Proceed to Service Tracking"),

    ("Stage 7", "Service Execution & Parts", "Workshop Ops > Service Tracking", "job_card_no, parts requisitioned", 
     "Technician transitions status to IN PROGRESS. Issues spare parts; system auto-decrements branch stock.", 
     "stock_transactions (decrement qty_on_hand)", "Branch-specific parts store and warehouse bin.", "Proceed to Quality Inspection"),

    ("Stage 8", "Quality Control (QC)", "Workshop Ops > Quality Inspection", "Completed bike, inspection checklist", 
     "Supervisor inspects brakes, lights, fluid leaks, and conducts road test. If pass -> QC Approved; if fail -> rework.", 
     "qc_id (Status: PASSED)", "Final odometer and road test notes recorded.", "Proceed to Final Invoicing"),

    ("Stage 9", "Final Invoicing", "Finance > Invoices", "Approved job card work + actual parts consumed", 
     "Compiles tax invoice: Labor + Parts + GST (CGST/SGST), offsets initial advance, calculates balance due.", 
     "invoice_no (Immutable PDF generated)", "Freezes snapshot of customer address + branch GSTIN address.", "Proceed to Payment & Delivery"),

    ("Stage 10", "Payment Collection & Handover", "Finance > Payments / Vehicle Delivery", "Cash, UPI reference, Card swipe", 
     "Records balance payment transaction. Issues receipt and authorized delivery gate pass. Handover confirmed.", 
     "payment_id, delivery_id (Status: DELIVERED)", "Printed on receipt and mobile invoice download.", "Proceed to Vehicle History"),

    ("Stage 11", "Service History & Reminders", "Customer Mgmt > Vehicle History", "Closed Job Card and Invoice record", 
     "Commits service record to motorcycle's permanent chronological history. Schedules next service reminder in 90 days.", 
     "Permanent vehicle history log entry", "Cross-branch accessible: bike visiting other branch retains full history.", "Cycle Complete")
]

for idx, e in enumerate(e2e_rows, start=5):
    ws8.row_dimensions[idx].height = 40
    for c_i, val in enumerate(e, 1):
        cell = ws8.cell(row=idx, column=c_i, value=val)
        cell.font = font_data
        cell.border = thin_border
        cell.fill = fill_white if idx % 2 == 1 else fill_light
        if c_i in [1, 2, 8]:
            cell.alignment = Alignment(horizontal="center", vertical="center")
            if c_i == 1:
                cell.font = font_code
            if c_i == 2:
                cell.font = font_bold
        else:
            cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

autofit_cols(ws8)

# Save Workbook
wb.save("Nitro_Racing_Application_Data_Flow.xlsx")
print("Nitro_Racing_Application_Data_Flow.xlsx generated successfully with all 8 sheets!")
