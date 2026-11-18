from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.pdfgen import canvas

NAVY = colors.HexColor('#101D35')
ORANGE = colors.HexColor('#F15A24')
LIGHT_GREY = colors.HexColor('#F4F6F9')
DARK = colors.HexColor('#17191D')
BORDER_COLOR = colors.HexColor('#D6D9DD')

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_decorations(self, page_count):
        self.saveState()
        # Top banner line
        self.setStrokeColor(ORANGE)
        self.setLineWidth(2.5)
        self.line(40, self._pagesize[1] - 30, self._pagesize[0] - 40, self._pagesize[1] - 30)
        
        # Header text
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(NAVY)
        self.drawString(40, self._pagesize[1] - 25, "NITRO RACING - BIKE SERVICE MANAGEMENT SYSTEM")
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.gray)
        self.drawRightString(self._pagesize[0] - 40, self._pagesize[1] - 25, "Menu & Submenu Functional Requirements v1.0")

        # Bottom banner line
        self.setStrokeColor(BORDER_COLOR)
        self.setLineWidth(0.8)
        self.line(40, 35, self._pagesize[0] - 40, 35)

        # Footer text
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.gray)
        self.drawString(40, 24, "Confidential | Nitro Racing Two-Wheeler Service Platform")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(self._pagesize[0] - 40, 24, page_str)
        self.restoreState()

def build_pdf():
    doc = SimpleDocTemplate(
        "Nitro_Racing_Application_BRD.pdf",
        pagesize=A4,
        leftMargin=40, rightMargin=40, topMargin=50, bottomMargin=50
    )
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle('DocTitle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=22, textColor=ORANGE, spaceAfter=2)
    sub_style = ParagraphStyle('DocSub', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=13, textColor=NAVY, spaceAfter=12)
    h1_style = ParagraphStyle('H1', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=13, textColor=NAVY, spaceBefore=14, spaceAfter=6)
    h2_style = ParagraphStyle('H2', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=10.5, textColor=ORANGE, spaceBefore=10, spaceAfter=4)
    h3_style = ParagraphStyle('H3', parent=styles['Heading3'], fontName='Helvetica-Bold', fontSize=9.5, textColor=NAVY, spaceBefore=6, spaceAfter=3)
    body_style = ParagraphStyle('Body', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=11.5, textColor=DARK, spaceAfter=4)
    bullet_style = ParagraphStyle('Bullet', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=11.5, textColor=DARK, leftIndent=12, spaceAfter=3)
    th_style = ParagraphStyle('TH', fontName='Helvetica-Bold', fontSize=8, textColor=colors.white, alignment=1)
    td_style = ParagraphStyle('TD', fontName='Helvetica', fontSize=7.5, leading=10, textColor=DARK)
    td_bold = ParagraphStyle('TDB', fontName='Helvetica-Bold', fontSize=7.5, leading=10, textColor=DARK)

    story = []

    # Title & Metadata
    story.append(Paragraph("NITRO RACING", title_style))
    story.append(Paragraph("BIKE SERVICE MANAGEMENT SYSTEM — Functional Requirements Document", sub_style))

    meta_data = [
        [Paragraph("Document Detail", th_style), Paragraph("Description", th_style)],
        [Paragraph("Document Type", td_bold), Paragraph("Application Menu Structure & Functional Requirements", td_style)],
        [Paragraph("Product", td_bold), Paragraph("Nitro Racing – Bike Service Management System v1.0", td_style)],
        [Paragraph("Primary Users", td_bold), Paragraph("Super Admin, Branch Admin, Technician (Customer records managed internally)", td_style)],
        [Paragraph("Brand Direction", td_bold), Paragraph("Racing Orange #F15A24 | Dark Navy #101D35 | Light Grey #F4F6F9", td_style)]
    ]
    t_meta = Table(meta_data, colWidths=[150, 365])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, LIGHT_GREY]),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 8))

    # 1. Document Purpose & 2. Application Overview
    story.append(Paragraph("1. Document Purpose", h1_style))
    story.append(Paragraph("This document defines the recommended navigation, menu hierarchy, submenu purpose, key functions, data to be maintained, and expected outcomes for Nitro Racing. It provides a shared functional baseline for design, development, testing, and future enhancements.", body_style))

    story.append(Paragraph("2. Application Overview", h1_style))
    story.append(Paragraph("Nitro Racing is an internal, branch-aware two-wheeler service operations application. It manages customers and their bikes, service appointments, vehicle check-in, job cards, technician work, spare parts, estimates, invoices, payments, quality checks, delivery, and operational reporting.", body_style))

    # 3. User Roles & Access Model
    story.append(Paragraph("3. User Roles & Access Model", h1_style))
    role_data = [
        [Paragraph("Role", th_style), Paragraph("Access Scope", th_style), Paragraph("Typical Responsibilities", th_style)],
        [Paragraph("Super Admin", td_bold), Paragraph("All branches & global config", td_style), Paragraph("Create branches and users, configure masters, view consolidated reports, monitor all operations.", td_style)],
        [Paragraph("Branch Admin", td_bold), Paragraph("Assigned branch only", td_style), Paragraph("Manage branch customers, bikes, appointments, job cards, technicians, inventory, billing, payments and branch reports.", td_style)],
        [Paragraph("Technician", td_bold), Paragraph("Assigned jobs & permitted functions", td_style), Paragraph("View assigned job cards, inspect vehicles, update work progress, record parts used and submit work for quality check.", td_style)]
    ]
    t_roles = Table(role_data, colWidths=[90, 150, 275])
    t_roles.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, LIGHT_GREY]),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t_roles)
    story.append(Paragraph("<b>Note:</b> Customers are records only. No customer portal or customer login is included in this scope.", body_style))

    # 4. Main Menu Hierarchy
    story.append(Paragraph("4. Recommended Main Menu Hierarchy", h1_style))
    menus = [
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
    for m, s in menus:
        story.append(Paragraph(f"• <b>{m}:</b> {s}", bullet_style))

    story.append(PageBreak())

    # 5. Functional Details Summary Table
    story.append(Paragraph("5. Menu & Submenu Functional Details", h1_style))
    
    fn_data = [
        [Paragraph("Submenu", th_style), Paragraph("Purpose & Description", th_style), Paragraph("Key Data & Operations", th_style), Paragraph("Roles", th_style)],
        
        [Paragraph("Dashboard", td_bold), Paragraph("At-a-glance operational & financial summary. Scoped to permitted branch; Super Admin views consolidated.", td_style),
         Paragraph("KPIs (received, WIP, QC, ready, delivered, unpaid), revenue trends, overdue jobs, low-stock alerts.", td_style), Paragraph("Super Admin, Branch Admin", td_style)],

        [Paragraph("Branches", td_bold), Paragraph("Maintain physical service locations and operational capacity.", td_style),
         Paragraph("Branch code, name, structured address, phone, email, manager, GSTIN, business hours, bay capacity.", td_style), Paragraph("Super Admin", td_style)],

        [Paragraph("Users & Roles", td_bold), Paragraph("Manage login credentials and module action permissions.", td_style),
         Paragraph("User account, role mapping, branch mapping, password reset, account deactivation. (No customer login).", td_style), Paragraph("Super Admin", td_style)],

        [Paragraph("Employees", td_bold), Paragraph("Maintain technician roster and workshop staff.", td_style),
         Paragraph("Employee ID, name, mobile, designation, skills/specializations, address, availability, active jobs.", td_style), Paragraph("Super / Branch Admin", td_style)],

        [Paragraph("Customers", td_bold), Paragraph("Single customer profile with structured address.", td_style),
         Paragraph("Customer code, full name, mobile, alternate phone, email, structured address, duplicate detection.", td_style), Paragraph("All Roles", td_style)],

        [Paragraph("Customer Vehicles", td_bold), Paragraph("Register and maintain motorcycles owned by customers.", td_style),
         Paragraph("Reg number, brand, model, variant, engine/chassis no, mfg year, color, odometer. Multi-bike support.", td_style), Paragraph("All Roles", td_style)],

        [Paragraph("Vehicle History", td_bold), Paragraph("Chronological lifetime maintenance record for a bike.", td_style),
         Paragraph("Job card timeline, past complaints, replaced parts, invoice amounts, next service due.", td_style), Paragraph("All Roles", td_style)],

        [Paragraph("Appointments", td_bold), Paragraph("Schedule customer visits and forecast bay capacity.", td_style),
         Paragraph("Date, slot, requested service, complaint, status (Requested, Confirmed, Arrived, Cancelled).", td_style), Paragraph("Branch Admin", td_style)],

        [Paragraph("Vehicle Check-in", td_bold), Paragraph("Capture bike condition & customer complaints at arrival.", td_style),
         Paragraph("Arrival time, odometer, fuel level, scratch/dent map, accessories held, complaint notes.", td_style), Paragraph("All Roles", td_style)],

        [Paragraph("Job Cards", td_bold), Paragraph("Central work order linking bike, complaints, technician, parts & billing.", td_style),
         Paragraph("Unique Job Card #, branch, customer, bike, advance paid, labor lines, parts, approval history.", td_style), Paragraph("All Roles", td_style)],

        [Paragraph("Mechanic Assignment", td_bold), Paragraph("Allocate jobs based on technician skill & bay load.", td_style),
         Paragraph("Technician ID, priority, target duration, reassignment audit reason.", td_style), Paragraph("Branch Admin", td_style)],

        [Paragraph("Service Tracking", td_bold), Paragraph("Track repair milestones from start to completion.", td_style),
         Paragraph("Status (Assigned, In Progress, On Hold, Completed), timestamps, hold reasons, parts consumed.", td_style), Paragraph("All Roles", td_style)],

        [Paragraph("Quality Inspection", td_bold), Paragraph("Pre-delivery checklist verification (brakes, road test).", td_style),
         Paragraph("Checklist items (brakes, lights, oil leaks, road test), pass/fail, final odometer, inspector sign-off.", td_style), Paragraph("Branch Admin, Tech", td_style)],

        [Paragraph("Vehicle Delivery", td_bold), Paragraph("Control vehicle handover after payment settlement.", td_style),
         Paragraph("Handover timestamp, receiver name, payment verification, gate pass, next service reminder.", td_style), Paragraph("Branch Admin", td_style)],

        [Paragraph("Service Catalogue", td_bold), Paragraph("Maintain services, standard labor charges & packages.", td_style),
         Paragraph("Service code, name, category, standard labor rate, duration, packages (Basic, General, Premium).", td_style), Paragraph("Super Admin", td_style)],

        [Paragraph("Spare Parts & Stock", td_bold), Paragraph("Track parts SKU, pricing and branch inventory ledger.", td_style),
         Paragraph("Part SKU, cost, selling price, GST, branch stock on hand, auto-deduction on job cards, low-stock alert.", td_style), Paragraph("Branch Admin", td_style)],

        [Paragraph("Invoices & Payments", td_bold), Paragraph("Tax-compliant PDF billing and payment collection.", td_style),
         Paragraph("Invoice #, itemized labor + parts, GST (CGST/SGST), advance offset, balance due, payment modes (Cash/UPI/Card).", td_style), Paragraph("All Roles", td_style)]
    ]
    t_fn = Table(fn_data, colWidths=[90, 160, 195, 70])
    t_fn.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, LIGHT_GREY]),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
    ]))
    story.append(t_fn)

    story.append(PageBreak())

    # 6. Core Workflow & 7. Statuses & 8. Address Architecture
    story.append(Paragraph("6. Core End-to-End Workflow", h1_style))
    wf_data = [
        [Paragraph("Stage", th_style), Paragraph("Workflow Step", th_style), Paragraph("Expected System Action", th_style)],
        [Paragraph("1", td_bold), Paragraph("Appointment / Walk-in", td_bold), Paragraph("Create appointment or register walk-in arrival.", td_style)],
        [Paragraph("2", td_bold), Paragraph("Customer & Bike", td_bold), Paragraph("Find/create customer with structured address; register bike.", td_style)],
        [Paragraph("3", td_bold), Paragraph("Vehicle Check-in", td_bold), Paragraph("Capture odometer, fuel, scratches, and customer complaints.", td_style)],
        [Paragraph("4", td_bold), Paragraph("Job Card", td_bold), Paragraph("Generate sequential Job Card (#JC-AMB-001) with branch lock.", td_style)],
        [Paragraph("5", td_bold), Paragraph("Estimate & Approval", td_bold), Paragraph("Prepare estimate; record customer approval before chargeable work.", td_style)],
        [Paragraph("6", td_bold), Paragraph("Technician Assignment", td_bold), Paragraph("Allocate technician based on bay load and skill.", td_style)],
        [Paragraph("7", td_bold), Paragraph("Service Execution", td_bold), Paragraph("Track status (In Progress, On Hold, Done); consume spare parts.", td_style)],
        [Paragraph("8", td_bold), Paragraph("Quality Check", td_bold), Paragraph("Complete safety & road test checklist; failed items return to bay.", td_style)],
        [Paragraph("9", td_bold), Paragraph("Final Invoice", td_bold), Paragraph("Generate PDF bill: labor + parts + GST minus advance.", td_style)],
        [Paragraph("10", td_bold), Paragraph("Payment & Delivery", td_bold), Paragraph("Record payment (Cash/UPI/Card); issue gate pass; vehicle handover.", td_style)],
        [Paragraph("11", td_bold), Paragraph("Service History", td_bold), Paragraph("Commit record to bike's permanent history; set next service reminder.", td_style)]
    ]
    t_wf = Table(wf_data, colWidths=[35, 140, 340])
    t_wf.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, LIGHT_GREY]),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    story.append(t_wf)
    story.append(Spacer(1, 6))

    story.append(Paragraph("7. Address Handling Architecture", h1_style))
    story.append(Paragraph("<b>1. Structured Normalization:</b> All physical addresses (Branch, Customer, Employee, Supplier) are broken into discrete fields: <i>Door/Plot No, Street/Road, Landmark, Area/Locality, City, District, State, and 6-digit Pincode</i>.", body_style))
    story.append(Paragraph("<b>2. Branch Multi-Tenancy:</b> Branches store exact geo-coordinates (Lat/Long) for mapping and customer routing.", body_style))
    story.append(Paragraph("<b>3. Customer Address Mobility:</b> Updating a customer's address on their master profile updates future interactions without altering past historical records.", body_style))
    story.append(Paragraph("<b>4. Immutable Invoice Address Snapshot:</b> When an invoice is finalized, the customer billing address and branch GSTIN address are frozen into the invoice record. Even if a customer moves or a branch relocates 2 years later, printed historical invoices remain 100% legally accurate.", body_style))

    story.append(Paragraph("8. Important Business Rules & Scope Summary", h1_style))
    story.append(Paragraph("• Every operational record belongs to a branch; Super Admin accesses all, Branch Admin is restricted to assigned store.", bullet_style))
    story.append(Paragraph("• Single customer can own multiple bikes; each bike accumulates permanent cross-branch service history.", bullet_style))
    story.append(Paragraph("• Stock is reduced strictly via recorded job card issue transactions, never by arbitrary quantity edits.", bullet_style))
    story.append(Paragraph("• Issued invoices and completed payments must not be silently deleted; use controlled credit notes/cancellations.", bullet_style))
    story.append(Paragraph("• Technicians have zero access to dashboards, financial reports, or user administration.", bullet_style))
    story.append(Paragraph("• Customer login is strictly out of scope. First release prioritizes core garage operations from check-in to delivery.", bullet_style))

    doc.build(story, canvasmaker=NumberedCanvas)
    print("Nitro_Racing_Application_BRD.pdf generated successfully.")

build_pdf()
