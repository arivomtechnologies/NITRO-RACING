from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
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
        self.setStrokeColor(ORANGE)
        self.setLineWidth(2.5)
        self.line(40, self._pagesize[1] - 30, self._pagesize[0] - 40, self._pagesize[1] - 30)
        
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(NAVY)
        self.drawString(40, self._pagesize[1] - 25, "NITRO RACING - BIKE SERVICE & MODIFICATION MANAGEMENT SYSTEM")
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.gray)
        self.drawRightString(self._pagesize[0] - 40, self._pagesize[1] - 25, "Functional Requirements v1.1")

        self.setStrokeColor(BORDER_COLOR)
        self.setLineWidth(0.8)
        self.line(40, 35, self._pagesize[0] - 40, 35)

        self.setFont("Helvetica", 8)
        self.setFillColor(colors.gray)
        self.drawString(40, 24, "Confidential | Superbike Care & Nitro Modz Operations")
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

    title_style = ParagraphStyle('DocTitle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=20, textColor=ORANGE, spaceAfter=2)
    sub_style = ParagraphStyle('DocSub', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=12, textColor=NAVY, spaceAfter=10)
    h1_style = ParagraphStyle('H1', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=12, textColor=NAVY, spaceBefore=12, spaceAfter=5)
    h2_style = ParagraphStyle('H2', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=10, textColor=ORANGE, spaceBefore=8, spaceAfter=3)
    body_style = ParagraphStyle('Body', parent=styles['Normal'], fontName='Helvetica', fontSize=8, leading=11, textColor=DARK, spaceAfter=3)
    bullet_style = ParagraphStyle('Bullet', parent=styles['Normal'], fontName='Helvetica', fontSize=8, leading=11, textColor=DARK, leftIndent=10, spaceAfter=2.5)
    th_style = ParagraphStyle('TH', fontName='Helvetica-Bold', fontSize=7.5, textColor=colors.white, alignment=1)
    td_style = ParagraphStyle('TD', fontName='Helvetica', fontSize=7.5, leading=9.5, textColor=DARK)
    td_bold = ParagraphStyle('TDB', fontName='Helvetica-Bold', fontSize=7.5, leading=9.5, textColor=DARK)

    story = []
    story.append(Paragraph("NITRO RACING", title_style))
    story.append(Paragraph("BIKE SERVICE MANAGEMENT SYSTEM — Functional Requirements v1.1", sub_style))

    meta_data = [
        [Paragraph("Document Detail", th_style), Paragraph("Description", th_style)],
        [Paragraph("Product Scope", td_bold), Paragraph("Nitro Racing Bike Service & Nitro Modz Customization Platform", td_style)],
        [Paragraph("Vehicle Coverage", td_bold), Paragraph("Standard Commuters, Sports Bikes, Superbikes (400cc - 1000cc+), Custom Modified Bikes", td_style)],
        [Paragraph("Specialized Divisions", td_bold), Paragraph("1. Superbike Care Division | 2. Nitro Modz Customization & Tuning Division", td_style)],
        [Paragraph("Primary Users", td_bold), Paragraph("Super Admin, Branch Admin, Certified Technicians (Customer records managed internally)", td_style)],
        [Paragraph("Brand Direction", td_bold), Paragraph("Racing Orange #F15A24 | Dark Navy #101D35 | Light Grey #F4F6F9", td_style)]
    ]
    t_meta = Table(meta_data, colWidths=[130, 385])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, LIGHT_GREY]),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 6))

    story.append(Paragraph("1. Superbike Service & Customization Architecture", h1_style))
    story.append(Paragraph("Nitro Racing's operational model incorporates two specialized high-revenue divisions alongside standard maintenance:", body_style))
    story.append(Paragraph("• <b>Superbike Division (400cc – 1000cc+):</b> Desmo valve clearance adjustment, electronic throttle body synchronization, OBD-2 computerized diagnostic scans, radiator high-temp coolant flush (Engine Ice), slipper clutch servicing, and Brembo sintered brake pad fitment. Allocated exclusively to certified Master Technicians in dedicated lift bays with rubberized paddock stands.", bullet_style))
    story.append(Paragraph("• <b>Nitro Modz (Modifications & Performance Tuning):</b> Slip-on and full-system performance exhaust installation (Akrapovič, Arrow), ECU Stage 1/2 fuel map flashing and dyno tuning, BMC high-flow performance air filters, touring auxiliary fog lights with custom dual-relay harnesses, heavy-duty crash guards, tail tidies, and clip-on handlebars.", bullet_style))
    story.append(Paragraph("• <b>Specialized Business Rule:</b> Minimum 50% advance deposit required before placing purchase orders for high-value custom parts. Customer must sign a digital disclaimer acknowledging modification noise/off-road compliance.", bullet_style))

    story.append(Paragraph("2. Expanded Service Catalogue & Labor Pricing", h1_style))
    srv_data = [
        [Paragraph("Code", th_style), Paragraph("Service Name", th_style), Paragraph("Division", th_style), Paragraph("Duration", th_style), Paragraph("Labor Rate", th_style), Paragraph("Target Models", th_style)],
        [Paragraph("SRV-SBK-01", td_bold), Paragraph("Superbike Major Service & Valve Clearance", td_style), Paragraph("Superbike", td_style), Paragraph("240 Mins", td_style), Paragraph("INR 3,500.00", td_bold), Paragraph("Superbikes (600 - 1000cc+)", td_style)],
        [Paragraph("SRV-SBK-02", td_bold), Paragraph("Superbike OBD-2 Diagnostic & Throttle Sync", td_style), Paragraph("Superbike", td_style), Paragraph("60 Mins", td_style), Paragraph("INR 1,200.00", td_bold), Paragraph("Electronic FI / Superbikes", td_style)],
        [Paragraph("SRV-SBK-03", td_bold), Paragraph("Radiator Coolant Flush (Engine Ice)", td_style), Paragraph("Superbike", td_style), Paragraph("45 Mins", td_style), Paragraph("INR 650.00", td_bold), Paragraph("Liquid-Cooled Bikes", td_style)],
        [Paragraph("SRV-MOD-01", td_bold), Paragraph("Performance Exhaust Slip-On Installation", td_style), Paragraph("Nitro Modz", td_style), Paragraph("90 Mins", td_style), Paragraph("INR 1,500.00", td_bold), Paragraph("All Compatible Bikes", td_style)],
        [Paragraph("SRV-MOD-02", td_bold), Paragraph("ECU Stage 1/2 Fuel Map Flashing & Dyno", td_style), Paragraph("Nitro Modz", td_style), Paragraph("120 Mins", td_style), Paragraph("INR 2,800.00", td_bold), Paragraph("Track & Sport Bikes", td_style)],
        [Paragraph("SRV-MOD-03", td_bold), Paragraph("Auxiliary Lights & Custom Relay Wiring", td_style), Paragraph("Nitro Modz", td_style), Paragraph("75 Mins", td_style), Paragraph("INR 850.00", td_bold), Paragraph("Touring & Adventure", td_style)],
        [Paragraph("SRV-MOD-04", td_bold), Paragraph("Crash Guard & Frame Sliders Fitment", td_style), Paragraph("Nitro Modz", td_style), Paragraph("60 Mins", td_style), Paragraph("INR 500.00", td_bold), Paragraph("All Motorcycles", td_style)],
        [Paragraph("SRV-GEN-01", td_bold), Paragraph("General Periodic Service (50-Point)", td_style), Paragraph("Periodic", td_style), Paragraph("90 Mins", td_style), Paragraph("INR 650.00", td_bold), Paragraph("Commuter / Sports", td_style)],
        [Paragraph("SRV-BRK-03", td_bold), Paragraph("Front & Rear Brake Caliper Overhaul", td_style), Paragraph("Brakes", td_style), Paragraph("45 Mins", td_style), Paragraph("INR 350.00", td_bold), Paragraph("Disc Brake Bikes", td_style)]
    ]
    t_srv = Table(srv_data, colWidths=[65, 175, 75, 55, 65, 80])
    t_srv.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, LIGHT_GREY]),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    story.append(t_srv)

    story.append(PageBreak())

    story.append(Paragraph("3. End-to-End Operational Workflow for Superbikes & Modz", h1_style))
    wf_data = [
        [Paragraph("Stage", th_style), Paragraph("Workflow Step", th_style), Paragraph("Superbike & Nitro Modz Specific Operation", th_style)],
        [Paragraph("1", td_bold), Paragraph("Intake & Address", td_bold), Paragraph("Capture customer phone; normalize address (Door No, Street, Landmark, Area, City, Pin).", td_style)],
        [Paragraph("2", td_bold), Paragraph("Detailed Check-in", td_bold), Paragraph("Capture odometer, fuel level, 4 damage photos, pre-existing aftermarket accessories checklist.", td_style)],
        [Paragraph("3", td_bold), Paragraph("Job Card Creation", td_bold), Paragraph("Issue sequential Job Card (#JC-AMB-2026-004); record minimum 50% advance for custom parts.", td_style)],
        [Paragraph("4", td_bold), Paragraph("Estimate & Consent", td_bold), Paragraph("Itemized quotation for performance parts + custom labor + 18% GST; record digital legal waiver.", td_style)],
        [Paragraph("5", td_bold), Paragraph("Master Tech Bay", td_bold), Paragraph("Allocate to Superbike-certified technician (Hari Krishnan) in dedicated paddock-stand bay.", td_style)],
        [Paragraph("6", td_bold), Paragraph("Execution & Stock", td_bold), Paragraph("Fit exhaust, flash ECU, or service engine; parts auto-deducted from Ambattur inventory.", td_style)],
        [Paragraph("7", td_bold), Paragraph("Quality Inspection", td_bold), Paragraph("OBD scan for zero error codes, exhaust DB decibel check, brake test, and road test.", td_style)],
        [Paragraph("8", td_bold), Paragraph("Invoice & Delivery", td_bold), Paragraph("Compile tax invoice with frozen legal address snapshot; collect balance via UPI/Card; release Gate Pass.", td_style)],
        [Paragraph("9", td_bold), Paragraph("Vehicle History", td_bold), Paragraph("Append complete specs (parts, map, technician) to permanent bike log; set 90-day reminder.", td_style)]
    ]
    t_wf = Table(wf_data, colWidths=[35, 130, 350])
    t_wf.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, LIGHT_GREY]),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
    ]))
    story.append(t_wf)
    story.append(Spacer(1, 6))

    story.append(Paragraph("4. Address Handling & Business Governance", h1_style))
    story.append(Paragraph("• <b>Address Normalization:</b> Branches, Customers, Employees, and Suppliers use structured fields (Door No, Street, Landmark, Area, City, State, 6-digit Pincode).", bullet_style))
    story.append(Paragraph("• <b>Immutable Invoice Snapshots:</b> High-value invoices permanently freeze the customer billing address and branch GSTIN address. Customer address updates never alter previously issued tax bills.", bullet_style))
    story.append(Paragraph("• <b>Multi-Tenant Branch Isolation:</b> Ambattur parts inventory and repair jobs remain completely segregated from Avadi operations, while Super Admin maintains consolidated oversight.", bullet_style))

    doc.build(story, canvasmaker=NumberedCanvas)
    print("Updated Nitro_Racing_Application_BRD.pdf generated.")

build_pdf()
