import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()

# Sheet 1: Traceability Matrix
ws = wb.active
ws.title = "Requirement Traceability"

# Ensure grid lines
ws.views.sheetView[0].showGridLines = True

# Colors
GRAPHITE = "17191D"
CHARCOAL = "242A31"
ORANGE = "F47721"
SILVER = "D6D9DD"
OFFWHITE = "F5F5F2"
GREEN = "229B62"
YELLOW = "E9A23B"
BLUE = "2B6CB0"

font_header = Font(name="Arial", size=11, bold=True, color="FFFFFF")
fill_header = PatternFill(start_color=GRAPHITE, end_color=GRAPHITE, fill_type="solid")

thin_border = Border(
    left=Side(style='thin', color="CCCCCC"),
    right=Side(style='thin', color="CCCCCC"),
    top=Side(style='thin', color="CCCCCC"),
    bottom=Side(style='thin', color="CCCCCC")
)

headers = [
    "Req ID", "Module", "Functional Requirement Description", 
    "Original Source Ref", "Priority (MoSCoW)", "Category", 
    "Approval Status", "Target Role Access", "Dependencies"
]

ws.append([])
# Title block
ws.cell(row=2, column=1, value="NITRO RACING - REQUIREMENTS TRACEABILITY MATRIX (RTM)").font = Font(name="Arial", size=14, bold=True, color=ORANGE)
ws.cell(row=3, column=1, value="Project: Automobile Service Center Management System | Prepared by: Arivom Technologies | Baseline BRD v1.0").font = Font(name="Arial", size=10, italic=True, color="555555")
ws.append([])

header_row = 5
for col_num, h_text in enumerate(headers, 1):
    cell = ws.cell(row=header_row, column=col_num, value=h_text)
    cell.font = font_header
    cell.fill = fill_header
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

# Data Rows
rows = [
    # Baseline Confirmed Requirements (FR-01 to FR-26)
    ("FR-01", "Authentication", "Login with username/email and password. No self-registration.", "Original BRD Sec 5.1", "Must Have", "SOURCE CONFIRMED", "Baseline Approved", "All Roles", "None"),
    ("FR-02", "Authentication", "Forgot password / reset password via secure email link.", "Original BRD Sec 5.1", "Must Have", "SOURCE CONFIRMED", "Baseline Approved", "All Roles", "SMTP Gateway"),
    ("FR-03", "Authentication", "Logout button. Session stays active for at least 24 hours (1 day) for mobile staff convenience.", "Original BRD Sec 5.1", "Must Have", "SOURCE CONFIRMED", "Baseline Approved", "All Roles", "JWT / Session Token"),
    ("FR-04", "Authentication", "Save credentials via Remember Me and browser password autofill support.", "Original BRD Sec 5.1", "Must Have", "SOURCE CONFIRMED", "Baseline Approved", "All Roles", "FR-01"),
    ("FR-05", "Authentication", "Post-login personalized greeting and dynamic role-filtered navigation menu.", "Original BRD Sec 5.1", "Must Have", "SOURCE CONFIRMED", "Baseline Approved", "All Roles", "FR-01, Role Engine"),
    ("FR-06", "Authentication", "Self-service change password; admin ability to deactivate user accounts.", "Original BRD Sec 5.1", "Should Have", "SOURCE CONFIRMED", "Baseline Approved", "Super / Branch Admin", "FR-01"),
    ("FR-07", "Store Management", "Super Admin can add new stores/branches (name, address, phone, contact).", "Original BRD Sec 5.2", "Must Have", "SOURCE CONFIRMED", "Baseline Approved", "Super Admin", "None"),
    ("FR-08", "Store Management", "Stores directory listing all operational branches (e.g., Ambattur, Avadi).", "Original BRD Sec 5.2", "Must Have", "SOURCE CONFIRMED", "Baseline Approved", "Super Admin", "FR-07"),
    ("FR-09", "Store Management", "Super Admin can edit store details and deactivate/delete stores.", "Original BRD Sec 5.2", "Must Have", "SOURCE CONFIRMED", "Baseline Approved", "Super Admin", "FR-07"),
    ("FR-10", "Store Management", "Clicking a store from directory opens that specific branch's management dashboard.", "Original BRD Sec 5.2", "Must Have", "SOURCE CONFIRMED", "Baseline Approved", "Super Admin", "FR-08, FR-24"),
    ("FR-11", "Store Management", "System architecture must support unlimited future branches dynamically without code changes.", "Original BRD Sec 5.2", "Must Have", "SOURCE CONFIRMED", "Baseline Approved", "System Architecture", "Multi-tenant DB schema"),
    ("FR-12", "User Management", "Super Admin creates Branch Admins and maps each to a designated branch.", "Original BRD Sec 5.3", "Must Have", "SOURCE CONFIRMED", "Baseline Approved", "Super Admin", "FR-07"),
    ("FR-13", "User Management", "Super Admin & Branch Admin create/manage Employees. Branch Admin isolated to own branch.", "Original BRD Sec 5.3", "Must Have", "SOURCE CONFIRMED", "Baseline Approved", "Super / Branch Admin", "FR-12"),
    ("FR-14", "Job Card", "Create job card: Bike (No, Brand, Model, Name, KMs), Service (purpose, entry datetime, mechanic), Customer (Name, Phone, Address), Payment (advance).", "Original BRD Sec 5.4", "Must Have", "SOURCE CONFIRMED", "Baseline Approved", "All Roles", "Customer & Bike entities"),
    ("FR-15", "Job Card", "Each job card is strictly segregated by and belongs to a single branch.", "Original BRD Sec 5.4", "Must Have", "SOURCE CONFIRMED", "Baseline Approved", "All Roles", "FR-07, FR-14"),
    ("FR-16", "Job Card", "Status flow: Received -> Work In Progress -> Completed (optional Delivered). All roles update status.", "Original BRD Sec 5.4", "Must Have", "SOURCE CONFIRMED", "Baseline Approved", "All Roles", "FR-14"),
    ("FR-17", "Job Card", "Search and filter job cards by bike number, customer phone, status, and entry date.", "Original BRD Sec 5.4", "Should Have", "SOURCE CONFIRMED", "Baseline Approved", "All Roles", "FR-14"),
    ("FR-18", "Job Card", "Audit history of status changes tracking who changed status and exact timestamp.", "Original BRD Sec 5.4", "Should Have", "SOURCE CONFIRMED", "Baseline Approved", "All Roles", "FR-16"),
    ("FR-19", "Billing & Invoice", "Generate invoice directly from an existing job card by any of the 3 roles.", "Original BRD Sec 5.5", "Must Have", "SOURCE CONFIRMED", "Baseline Approved", "All Roles", "FR-14, FR-16"),
    ("FR-20", "Billing & Invoice", "Invoice details: business/branch details, invoice no/date, customer/bike, itemized services/parts, tax, advance, balance due, total.", "Original BRD Sec 5.5", "Must Have", "SOURCE CONFIRMED", "Baseline Approved", "All Roles", "FR-19"),
    ("FR-21", "Billing & Invoice", "Invoice downloads strictly as formatted PDF document (no Excel export allowed).", "Original BRD Sec 5.5", "Must Have", "SOURCE CONFIRMED", "Baseline Approved", "All Roles", "FR-20, JasperReports"),
    ("FR-22", "Billing & Invoice", "Direct mobile sharing and thermal/A4 printing support from smartphone interface.", "Original BRD Sec 5.5", "Should Have", "SOURCE CONFIRMED", "Baseline Approved", "All Roles", "FR-21"),
    ("FR-23", "Dashboard", "Dashboard metrics: monthly sales, monthly revenue, monthly profit, bike types, and jobs by status.", "Original BRD Sec 5.6", "Must Have", "SOURCE CONFIRMED", "Baseline Approved", "Admins Only", "FR-14, FR-19"),
    ("FR-24", "Dashboard", "Super Admin views consolidated cross-branch dashboard plus individual branch drill-downs.", "Original BRD Sec 5.6", "Must Have", "SOURCE CONFIRMED", "Baseline Approved", "Super Admin", "FR-23"),
    ("FR-25", "Dashboard", "Branch Admin is strictly restricted to viewing only their own branch's dashboard metrics.", "Original BRD Sec 5.6", "Must Have", "SOURCE CONFIRMED", "Baseline Approved", "Branch Admin", "FR-23"),
    ("FR-26", "Dashboard", "Employees are strictly blocked from accessing any business or financial dashboard.", "Original BRD Sec 5.6", "Must Have", "SOURCE CONFIRMED", "Baseline Approved", "System Security", "RBAC Engine"),
    
    # Recommended Additional Requirements (FR-101 onwards)
    ("FR-101", "Customer Hub", "Centralized Customer Master storing multiple bikes per customer and duplicate phone check.", "Domain Standard", "Should Have", "RECOMMENDED", "Pending Client Review", "Super / Branch Admin", "FR-14"),
    ("FR-102", "Bike Master", "Vehicle Master record maintaining complete lifetime service history across branches.", "Domain Standard", "Should Have", "RECOMMENDED", "Pending Client Review", "All Roles", "FR-14"),
    ("FR-103", "Appointments", "Public service booking request converted to confirmed workshop appointment slot.", "Public Web Integration", "Should Have", "RECOMMENDED", "Pending Client Review", "Branch Admin", "Public Website"),
    ("FR-104", "Inspection", "Digital vehicle check-in checklist: scratch diagram, fuel level, photos, tool-kit custody.", "Domain Standard", "Should Have", "RECOMMENDED", "Pending Client Review", "All Roles", "FR-14"),
    ("FR-105", "Estimates", "Pre-service formal quotation generation and customer estimate approval tracking.", "Domain Standard", "Should Have", "RECOMMENDED", "Pending Client Review", "Branch Admin", "FR-14"),
    ("FR-106", "Mechanic Hub", "Mechanic skill assignment, active job workload tracking, and turnaround performance.", "Domain Standard", "Should Have", "RECOMMENDED", "Pending Client Review", "Branch Admin", "FR-14"),
    ("FR-107", "Inventory", "Spare parts catalog with stock inward, auto-deduction on job cards, and low stock alerts.", "Domain Standard", "Should Have", "RECOMMENDED", "Pending Client Review", "Branch Admin", "FR-14, FR-20"),
    ("FR-108", "Quality Control", "Mandatory QC verification checklist prior to vehicle release and final delivery status.", "Domain Standard", "Should Have", "RECOMMENDED", "Pending Client Review", "Branch Admin", "FR-16"),
    ("FR-109", "Payments", "Support for partial payments, multi-mode collections (UPI, Cash, Card), and pending balance ledger.", "Domain Standard", "Should Have", "RECOMMENDED", "Pending Client Review", "All Roles", "FR-20"),
    ("FR-110", "Expenses", "Operational expense tracking (rent, utilities, consumables) to compute true net profit.", "Domain Standard", "Should Have", "RECOMMENDED", "Pending Client Review", "Super / Branch Admin", "FR-23"),
    ("FR-111", "Communications", "Automated SMS and WhatsApp notifications at major service milestones (Start, QC, Ready).", "Domain Standard", "Nice to Have", "OPTIONAL", "Pending Client Decision", "System", "Third-party Gateway"),
    ("FR-112", "Web CMS", "Dynamic management of public website services, branch details, banners, and customer testimonials.", "Public Web Integration", "Should Have", "RECOMMENDED", "Pending Client Review", "Super Admin", "Public Website"),
    ("FR-113", "Service Catalog", "Standardized service menu with predefined labor hours, charges, and package definitions.", "Domain Standard", "Should Have", "RECOMMENDED", "Pending Client Review", "Super / Branch Admin", "FR-14"),
    ("FR-114", "Audit & Security", "Comprehensive audit log of critical data alterations, deletions, and invoice modifications.", "Security Standard", "Should Have", "RECOMMENDED", "Pending Client Review", "Super Admin", "All Modules"),
    ("FR-115", "Localization", "Multi-lingual user interface support (e.g., Tamil language support for workshop technicians).", "Client Clarification #8", "Nice to Have", "OPTIONAL", "Pending Client Decision", "All Roles", "UI Framework")
]

for row_idx, r_data in enumerate(rows, start=header_row+1):
    for col_idx, val in enumerate(r_data, start=1):
        cell = ws.cell(row=row_idx, column=col_idx, value=val)
        cell.font = Font(name="Arial", size=9)
        cell.border = thin_border
        
        # Alignments
        if col_idx in [1, 4, 5, 6, 7, 8]:
            cell.alignment = Alignment(horizontal="center", vertical="center")
        else:
            cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
            
        # Category formatting
        if col_idx == 6:
            if val == "SOURCE CONFIRMED":
                cell.fill = PatternFill(start_color="D1E7DD", end_color="D1E7DD", fill_type="solid")
                cell.font = Font(name="Arial", size=9, bold=True, color="0F5132")
            elif val == "RECOMMENDED":
                cell.fill = PatternFill(start_color="FFF3CD", end_color="FFF3CD", fill_type="solid")
                cell.font = Font(name="Arial", size=9, bold=True, color="664D03")
            elif val == "OPTIONAL":
                cell.fill = PatternFill(start_color="E2E3E5", end_color="E2E3E5", fill_type="solid")
                cell.font = Font(name="Arial", size=9, bold=True, color="41464B")

# Adjust column widths
col_widths = [12, 18, 48, 22, 16, 20, 22, 20, 22]
for idx, width in enumerate(col_widths, 1):
    col_letter = get_column_letter(idx)
    ws.column_dimensions[col_letter].width = width

# Sheet 2: Commercial Scope Summary
ws2 = wb.create_sheet(title="Commercial Scope Summary")
ws2.views.sheetView[0].showGridLines = True

ws2.cell(row=2, column=1, value="COMMERCIAL SCOPE DEMARCATION & SAFEGUARD").font = Font(name="Arial", size=14, bold=True, color=ORANGE)
ws2.cell(row=3, column=1, value="Client: Nitro Racing | Vendor: Arivom Technologies | Commercial Baseline: INR 60,000 / 2 Months").font = Font(name="Arial", size=10, italic=True, color="555555")

ws2.append([])
c_headers = ["Scope Dimension", "Original Confirmed Baseline (BRD v1.0)", "Recommended Additions (Pending Approval)", "Impact on Cost / Timeline"]
ws2.append(c_headers)
for c in range(1, 5):
    cell = ws2.cell(row=5, column=c)
    cell.font = font_header
    cell.fill = fill_header
    cell.alignment = Alignment(horizontal="center", vertical="center")

scope_summary_rows = [
    ("Functional Modules", "26 Functional Requirements (FR-01 to FR-26) covering Auth, Store, Users, Job Card, Invoicing, Dashboards", "15 Additional Recommendations (FR-101 to FR-115) covering Inventory, Estimates, QC, Expenses, SMS/WhatsApp", "Original INR 60,000 covers baseline FR-01 to FR-26. Recommended additions require mutual commercial sign-off."),
    ("Project Timeline", "8 Weeks (2 Calendar Months) for development, testing, and cloud deployment", "Optional phased delivery or milestone-based rollout if scope expansion is approved", "Fixed 2-month baseline timeline preserved for confirmed scope."),
    ("Public Website", "Static pages (Home, About, Services, Enquiry, Testimonials, Login)", "Dynamic CMS-driven service catalog and automated customer appointment scheduler", "Basic website included in baseline; advanced CMS & customer booking portal proposed."),
    ("Third-Party Integrations", "SMTP Email notifications for reset password and enquiry submissions", "Paid SMS Gateway (DLT registered) and WhatsApp Business API webhooks", "Email included. SMS/WhatsApp gateway subscription costs borne directly by client."),
    ("Data Migration", "Fresh system initialization with clean branch & admin setup", "Legacy customer history and vehicle records migration from spreadsheets/paper", "Legacy data cleaning and batch migration subject to separate scoping.")
]

for r_idx, r_vals in enumerate(scope_summary_rows, start=6):
    for c_idx, val in enumerate(r_vals, start=1):
        cell = ws2.cell(row=r_idx, column=c_idx, value=val)
        cell.font = Font(name="Arial", size=9)
        cell.border = thin_border
        cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

ws2.column_dimensions['A'].width = 24
ws2.column_dimensions['B'].width = 38
ws2.column_dimensions['C'].width = 38
ws2.column_dimensions['D'].width = 38

wb.save("Nitro_Racing_Requirement_Traceability.xlsx")
print("Requirement Traceability Excel generated successfully.")
