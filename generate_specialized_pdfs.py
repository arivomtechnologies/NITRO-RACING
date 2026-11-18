import os
from reportlab.lib.pagesizes import letter, landscape, A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

GRAPHITE = colors.HexColor('#17191D')
CHARCOAL = colors.HexColor('#242A31')
RACING_ORANGE = colors.HexColor('#F47721')
METALLIC_SILVER = colors.HexColor('#D6D9DD')
OFF_WHITE = colors.HexColor('#F5F5F2')
GREEN = colors.HexColor('#229B62')
WARN_YELLOW = colors.HexColor('#E9A23B')

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
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        # Top banner line
        self.setStrokeColor(RACING_ORANGE)
        self.setLineWidth(3)
        self.line(40, self._pagesize[1] - 30, self._pagesize[0] - 40, self._pagesize[1] - 30)
        
        # Header text
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(CHARCOAL)
        self.drawString(40, self._pagesize[1] - 25, "NITRO RACING - AUTOMOBILE SERVICE CENTER MANAGEMENT SYSTEM")
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.gray)
        self.drawRightString(self._pagesize[0] - 40, self._pagesize[1] - 25, "Arivom Technologies, Chennai")

        # Bottom banner line
        self.setStrokeColor(METALLIC_SILVER)
        self.setLineWidth(0.8)
        self.line(40, 35, self._pagesize[0] - 40, 35)

        # Footer text
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.gray)
        self.drawString(40, 24, "Confidential | Client: Nitro Racing | Version 1.0 (Nov 2026)")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(self._pagesize[0] - 40, 24, page_str)
        self.restoreState()

# ----------------- 1. SITEMAP PDF -----------------
def generate_sitemap_pdf():
    doc = SimpleDocTemplate(
        "Nitro_Racing_Sitemap.pdf",
        pagesize=landscape(A4),
        leftMargin=40, rightMargin=40, topMargin=50, bottomMargin=50
    )
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        textColor=GRAPHITE,
        spaceAfter=6
    )
    subtitle_style = ParagraphStyle(
        'DocSub',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        textColor=RACING_ORANGE,
        spaceAfter=15
    )
    section_h2 = ParagraphStyle(
        'SecH2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=13,
        textColor=CHARCOAL,
        spaceBefore=12,
        spaceAfter=8
    )
    cell_bold = ParagraphStyle('CB', fontName='Helvetica-Bold', fontSize=8, textColor=colors.white)
    cell_text = ParagraphStyle('CT', fontName='Helvetica', fontSize=8, leading=10, textColor=GRAPHITE)
    cell_tag_conf = ParagraphStyle('Conf', fontName='Helvetica-Bold', fontSize=7, textColor=GREEN)
    cell_tag_rec = ParagraphStyle('Rec', fontName='Helvetica-Bold', fontSize=7, textColor=WARN_YELLOW)
    cell_tag_opt = ParagraphStyle('Opt', fontName='Helvetica-Bold', fontSize=7, textColor=colors.gray)

    story = []
    story.append(Paragraph("NITRO RACING - COMPLETE APPLICATION SITEMAP & MENU ARCHITECTURE", title_style))
    story.append(Paragraph("Comprehensive Visual Hierarchy: Public Business Website & Role-Based Management Portal", subtitle_style))
    
    story.append(Paragraph("1. Public Business Website Sitemap (Customer Facing)", section_h2))
    web_data = [
        [Paragraph("Top-Level Menu", cell_bold), Paragraph("Submenu / Anchor Sections", cell_bold), Paragraph("Business Purpose & Scope", cell_bold), Paragraph("Scope Status", cell_bold)],
        [Paragraph("HOME", cell_text), Paragraph("Hero Banner, Why Nitro Racing, Express Services, Branch Quick-Finder, Reviews", cell_text), Paragraph("Brand authority, customer engagement, conversion CTA for service bookings", cell_text), Paragraph("SOURCE CONFIRMED", cell_tag_conf)],
        [Paragraph("ABOUT US", cell_text), Paragraph("Heritage, Certified Technicians, Advanced Garage Infrastructure, Quality Promise", cell_text), Paragraph("Establish high-performance trust in motorcycle repair expertise", cell_text), Paragraph("SOURCE CONFIRMED", cell_tag_conf)],
        [Paragraph("SERVICES", cell_text), Paragraph("Engine Tune-Up, Oil Change, Brake Service, Clutch Overhaul, Chain/Sprocket, Electricals", cell_text), Paragraph("Detailed motorcycle service catalogue with scope, benefits and pricing transparency", cell_text), Paragraph("SOURCE CONFIRMED (Rec Categories)", cell_tag_rec)],
        [Paragraph("OUR BRANCHES", cell_text), Paragraph("Ambattur Branch, Avadi Branch, Future Network Locator (Geo-Maps, Contact, Hours)", cell_text), Paragraph("Multi-branch presence, localized directions, direct call, and branch-specific booking", cell_text), Paragraph("SOURCE CONFIRMED", cell_tag_conf)],
        [Paragraph("GALLERY", cell_text), Paragraph("Workshop Bays, Diagnostic Benches, Superbike Repairs, Before-and-After Overhauls", cell_text), Paragraph("Visual proof of craftsmanship, clean workspace, and professional care", cell_text), Paragraph("RECOMMENDED", cell_tag_rec)],
        [Paragraph("TESTIMONIALS", cell_text), Paragraph("Customer Stories, Google Reviews Feed, Biker Community Feedback", cell_text), Paragraph("Social proof to build trust for new customers", cell_text), Paragraph("SOURCE CONFIRMED", cell_tag_conf)],
        [Paragraph("CONTACT / ENQUIRY", cell_text), Paragraph("Enquiry Submission Form, Branch Direct Lines, WhatsApp Chatbot, Feedback", cell_text), Paragraph("Lead generation; inquiries automatically saved to database and notified via email", cell_text), Paragraph("SOURCE CONFIRMED", cell_tag_conf)],
        [Paragraph("ACTIONS / CTA", cell_text), Paragraph("1. Book a Service (Request Appointment)\n2. Staff Login (Direct to Management Portal)", cell_text), Paragraph("Direct conversion funnel and internal staff gateway (No public customer registration)", cell_text), Paragraph("SOURCE CONFIRMED (Book: Rec)", cell_tag_conf)]
    ]
    t_web = Table(web_data, colWidths=[110, 240, 280, 130])
    t_web.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), GRAPHITE),
        ('GRID', (0, 0), (-1, -1), 0.5, METALLIC_SILVER),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, OFF_WHITE]),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(t_web)
    
    story.append(PageBreak())
    
    story.append(Paragraph("2. Management Portal Menu Hierarchy & Role-Based Access", section_h2))
    portal_data = [
        [Paragraph("Module", cell_bold), Paragraph("Sidebar Menu & Submenus", cell_bold), Paragraph("Super Admin", cell_bold), Paragraph("Branch Admin", cell_bold), Paragraph("Employee", cell_bold), Paragraph("Scope Category", cell_bold)],
        [Paragraph("DASHBOARD", cell_text), Paragraph("Overview | Daily Operations | Branch Performance Comparison", cell_text), Paragraph("All Branches", cell_text), Paragraph("Own Branch Only", cell_text), Paragraph("BLOCKED (FR-26)", cell_tag_opt), Paragraph("SOURCE CONFIRMED", cell_tag_conf)],
        [Paragraph("STORE MGMT", cell_text), Paragraph("Branch Directory | Add New Branch | Edit/Deactivate Branch", cell_text), Paragraph("Full Access", cell_text), Paragraph("View Own Details", cell_text), Paragraph("Hidden", cell_tag_opt), Paragraph("SOURCE CONFIRMED", cell_tag_conf)],
        [Paragraph("USER MGMT", cell_text), Paragraph("Branch Admins | Employee Directory | Roles & Access Matrix", cell_text), Paragraph("All Users", cell_text), Paragraph("Own Employees Only", cell_text), Paragraph("Hidden", cell_tag_opt), Paragraph("SOURCE CONFIRMED", cell_tag_conf)],
        [Paragraph("WORKSHOP OPS", cell_text), Paragraph("Appointments | Vehicle Check-in | Job Cards (Received, WIP, Done, Delivered) | QC Inspection", cell_text), Paragraph("All Branches", cell_text), Paragraph("Own Branch", cell_text), Paragraph("Create / Update Status", cell_text), Paragraph("SOURCE CONFIRMED (Inspection: Rec)", cell_tag_conf)],
        [Paragraph("CUSTOMERS & BIKES", cell_text), Paragraph("Customer Directory | Bike Profiles | Service Due Reminders", cell_text), Paragraph("All Branches", cell_text), Paragraph("Own Branch", cell_text), Paragraph("View / Link on Job Card", cell_text), Paragraph("RECOMMENDED", cell_tag_rec)],
        [Paragraph("SERVICE CATALOG", cell_text), Paragraph("Service Menu | Labor Charges | Standard Service Packages", cell_text), Paragraph("Full Config", cell_text), Paragraph("View / Custom Charge", cell_text), Paragraph("Select Only", cell_text), Paragraph("RECOMMENDED", cell_tag_rec)],
        [Paragraph("MECHANIC MGMT", cell_text), Paragraph("Technician Roster | Workload Allocation | Efficiency Tracking", cell_text), Paragraph("All Branches", cell_text), Paragraph("Own Branch", cell_text), Paragraph("View Assigned Jobs", cell_text), Paragraph("RECOMMENDED", cell_tag_rec)],
        [Paragraph("INVENTORY & PARTS", cell_text), Paragraph("Spare Parts Master | Stock Inward | Job Card Part Issue | Low Stock Alert", cell_text), Paragraph("All Branches", cell_text), Paragraph("Own Branch", cell_text), Paragraph("View / Issue to Job", cell_text), Paragraph("RECOMMENDED", cell_tag_rec)],
        [Paragraph("ESTIMATES", cell_text), Paragraph("Create Quotation | Customer Approval Workflow | Convert to Job Card", cell_text), Paragraph("All Branches", cell_text), Paragraph("Own Branch", cell_text), Paragraph("Create Draft", cell_text), Paragraph("RECOMMENDED", cell_tag_rec)],
        [Paragraph("BILLING & INVOICE", cell_text), Paragraph("Generate Invoice | Invoice Directory | PDF Download | Mobile Share/Print", cell_text), Paragraph("All Branches", cell_text), Paragraph("Own Branch", cell_text), Paragraph("Generate PDF (FR-19)", cell_text), Paragraph("SOURCE CONFIRMED", cell_tag_conf)],
        [Paragraph("PAYMENTS & LEDGER", cell_text), Paragraph("Payment Collection | Advance Adjustment | Outstanding Balances", cell_text), Paragraph("All Branches", cell_text), Paragraph("Own Branch", cell_text), Paragraph("Collect Payment", cell_text), Paragraph("RECOMMENDED", cell_tag_rec)],
        [Paragraph("EXPENSES & P&L", cell_text), Paragraph("Operating Expenses | Parts Purchase Cost | Gross & Net Profit Engine", cell_text), Paragraph("All Branches", cell_text), Paragraph("Own Branch", cell_text), Paragraph("Hidden", cell_tag_opt), Paragraph("RECOMMENDED (Pending P&L Form.)", cell_tag_rec)],
        [Paragraph("REPORTS & BI", cell_text), Paragraph("Daily Sales | Monthly Revenue | Mechanic Productivity | Parts Consumption", cell_text), Paragraph("Consolidated BI", cell_text), Paragraph("Branch Reports", cell_text), Paragraph("Blocked", cell_tag_opt), Paragraph("SOURCE CONFIRMED (Adv: Rec)", cell_tag_conf)],
        [Paragraph("COMMUNICATIONS", cell_text), Paragraph("SMS / WhatsApp Service Milestones | Email Notifications | Reminders", cell_text), Paragraph("Global Templates", cell_text), Paragraph("Branch Alerts", cell_text), Paragraph("Trigger Milestones", cell_text), Paragraph("OPTIONAL (Pending Gateway)", cell_tag_opt)],
        [Paragraph("SYSTEM CONFIG", cell_text), Paragraph("Business Profile | Tax / GST Settings | Audit Trail Logs | Session Security", cell_text), Paragraph("Full Control", cell_text), Paragraph("Read Only Profile", cell_text), Paragraph("Hidden", cell_tag_opt), Paragraph("RECOMMENDED", cell_tag_rec)]
    ]
    t_portal = Table(portal_data, colWidths=[90, 220, 100, 110, 110, 130])
    t_portal.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), GRAPHITE),
        ('GRID', (0, 0), (-1, -1), 0.5, METALLIC_SILVER),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, OFF_WHITE]),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t_portal)
    
    doc.build(story, canvasmaker=NumberedCanvas)
    print("Nitro_Racing_Sitemap.pdf generated successfully.")

# ----------------- 2. WORKFLOWS PDF -----------------
def generate_workflows_pdf():
    doc = SimpleDocTemplate(
        "Nitro_Racing_Workflows.pdf",
        pagesize=A4,
        leftMargin=40, rightMargin=40, topMargin=50, bottomMargin=50
    )
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        textColor=GRAPHITE,
        spaceAfter=6
    )
    subtitle_style = ParagraphStyle(
        'DocSub',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        textColor=RACING_ORANGE,
        spaceAfter=15
    )
    h2_style = ParagraphStyle(
        'H2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        textColor=CHARCOAL,
        spaceBefore=14,
        spaceAfter=8
    )
    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=GRAPHITE
    )
    badge_style = ParagraphStyle(
        'Badge',
        fontName='Helvetica-Bold',
        fontSize=7.5,
        textColor=colors.white
    )

    story = []
    story.append(Paragraph("NITRO RACING - END-TO-END BUSINESS WORKFLOW SPECIFICATION", title_style))
    story.append(Paragraph("Detailed Swimlane Logic, Decision Gates, Lifecycle State Machines & Data Synchronization", subtitle_style))
    
    workflows = [
        ("Workflow 1: Vehicle Intake, Digital Check-in & Job Card Creation", 
         "Covers customer walk-in or booked arrival, physical bike condition recording, initial odometer check, advance deposit collection, and job card number generation.",
         [
             ("Step 1: Arrival & Lookup", "Customer arrives at Ambattur/Avadi branch. Staff queries customer phone number. If returning, bike & customer profiles auto-populate; if new, quick registration is completed."),
             ("Step 2: Vehicle Inspection", "Staff inspects motorcycle: logs current KMs, scratches/damages, fuel level, and customer complaints (e.g. Engine noise, front brake spongy). Inspection photos uploaded."),
             ("Step 3: Advance Deposit", "Staff records advance amount received (if any, e.g. INR 500) and payment method. System issues digital receipt."),
             ("Step 4: Job Card Emission", "System generates unique Job Card (e.g., #JC-AMB-2026-0842) under status 'RECEIVED'. Audit timestamp and staff ID recorded.")
         ]),
        ("Workflow 2: Estimate Preparation & Customer Approval Gateway",
         "Ensures financial transparency before dismantling major engine/transmission components. Proposed enhancement to eliminate customer billing disputes.",
         [
             ("Step 1: Diagnostic Teardown", "Mechanic inspects components and identifies necessary parts replacement (e.g., clutch plates, chain sprocket) and estimated labour hours."),
             ("Step 2: Quotation Generation", "Branch Admin drafts digital estimate. System verifies spare parts availability and unit selling prices."),
             ("Step 3: Customer Approval Gate", "Estimate shared with customer via WhatsApp/SMS/Call. Customer approves full or partial items. Rejected items are flagged."),
             ("Step 4: Status Transition", "Upon approval, Job Card automatically transitions to 'WORK IN PROGRESS'. Approved parts reserved in inventory.")
         ]),
        ("Workflow 3: Workshop Execution, Parts Issuance & Status Tracking",
         "Core workshop operations tracking technician workload, spare part deduction from stock, and progress visibility across mobile devices.",
         [
             ("Step 1: Mechanic Allocation", "Branch Admin assigns Job Card to designated mechanic based on current bay workload and specialization."),
             ("Step 2: Spare Parts Issuance", "Parts store issues spare parts against Job Card number. System decrements branch inventory in real-time. If stock drops below threshold, low stock alert triggers."),
             ("Step 3: Service Execution", "Mechanic carries out repairs. Status remains 'WORK IN PROGRESS'. If unexpected defects found, supplementary estimate triggered."),
             ("Step 4: Completion", "Mechanic marks all checklist items as done. Job Card transitions to 'COMPLETED'.")
         ]),
        ("Workflow 4: Quality Control (QC), Billing & Tax Invoicing",
         "Pre-delivery road test, final invoice generation with tax/GST calculation, advance adjustment, and PDF compilation.",
         [
             ("Step 1: Quality Control (QC)", "Floor supervisor conducts QC check (brakes, tire pressure, wash, electricals). Signs off inspection checklist."),
             ("Step 2: Invoice Compilation", "System aggregates all billed services, issued spare parts, and applies tax/GST (if confirmed by client)."),
             ("Step 3: Advance Deduction & Balance", "Advance payment (recorded at intake) is automatically subtracted from grand total to determine exact balance due."),
             ("Step 4: PDF Generation", "JasperReports engine compiles immutable, professionally branded PDF invoice. Excel export is explicitly restricted (FR-21).")
         ]),
        ("Workflow 5: Payment Collection, Delivery & Historical Archival",
         "Final settlement, vehicle handover, status closure to 'DELIVERED', and automatic entry into vehicle's lifetime service log.",
         [
             ("Step 1: Balance Collection", "Customer arrives for pickup. Pays outstanding balance via UPI, Cash, or Card. System logs transaction reference."),
             ("Step 2: Status -> DELIVERED", "Job Card status is updated to 'DELIVERED'. Vehicle handover completed. Gate pass / invoice shared on customer mobile."),
             ("Step 3: Service History Archival", "Complete service record (KMs, parts, labour, mechanic notes) is committed to bike's permanent digital service history."),
             ("Step 4: Post-Service Engagement", "Automated service feedback reminder scheduled. Next service due date calculated based on mileage/time interval.")
         ])
    ]

    for title, desc, steps in workflows:
        story.append(Paragraph(title, h2_style))
        story.append(Paragraph(desc, body_style))
        story.append(Spacer(1, 6))
        
        table_rows = [
            [Paragraph("Milestone Stage", ParagraphStyle('TH1', fontName='Helvetica-Bold', fontSize=8, textColor=colors.white)),
             Paragraph("Operational Procedure & System Execution Rules", ParagraphStyle('TH2', fontName='Helvetica-Bold', fontSize=8, textColor=colors.white))]
        ]
        for s_title, s_desc in steps:
            table_rows.append([
                Paragraph(s_title, ParagraphStyle('ST', fontName='Helvetica-Bold', fontSize=8, textColor=RACING_ORANGE)),
                Paragraph(s_desc, ParagraphStyle('SD', fontName='Helvetica', fontSize=8, leading=10, textColor=GRAPHITE))
            ])
            
        t_flow = Table(table_rows, colWidths=[140, 375])
        t_flow.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), CHARCOAL),
            ('GRID', (0, 0), (-1, -1), 0.5, METALLIC_SILVER),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, OFF_WHITE]),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ]))
        story.append(t_flow)
        story.append(Spacer(1, 10))

    doc.build(story, canvasmaker=NumberedCanvas)
    print("Nitro_Racing_Workflows.pdf generated successfully.")

generate_sitemap_pdf()
generate_workflows_pdf()
