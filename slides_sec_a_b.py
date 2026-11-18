from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from common_deck import (
    C_GRAPHITE, C_CHARCOAL, C_ORANGE, C_SILVER, C_OFFWHITE, C_WHITE,
    C_GREEN, C_GOLD, C_MUTED, C_CARD_BG, C_DARK_CARD,
    set_bg, add_header, add_footer, add_badge, create_card, create_table_card
)

def build_slides_1_to_9(prs, blank_layout):
    # SLIDE 1: Cover Page (Dark)
    s1 = prs.slides.add_slide(blank_layout)
    set_bg(s1, C_GRAPHITE)
    
    # Accent top bar
    bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.18))
    bar.fill.solid()
    bar.fill.fore_color.rgb = C_ORANGE
    bar.line.fill.background()

    # Brand Title
    t_box = s1.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.3), Inches(2.2))
    tf = t_box.text_frame
    tf.word_wrap = True
    
    p0 = tf.paragraphs[0]
    p0.text = "NITRO RACING"
    p0.font.size = Pt(44)
    p0.font.bold = True
    p0.font.color.rgb = C_ORANGE
    p0.space_after = Pt(10)

    p1 = tf.add_paragraph()
    p1.text = "Automobile Service Center Management System"
    p1.font.size = Pt(26)
    p1.font.bold = True
    p1.font.color.rgb = C_WHITE
    p1.space_after = Pt(12)

    p2 = tf.add_paragraph()
    p2.text = "Business Requirements Document (BRD) & Product Architecture Specification"
    p2.font.size = Pt(14)
    p2.font.color.rgb = C_SILVER

    # Meta card on cover
    create_card(s1, Inches(1.0), Inches(4.5), Inches(11.3), Inches(1.8), 
                "PROJECT INFORMATION & REVIEW CONTROL", [
                    "Target Client: Nitro Racing (Ambattur & Avadi Branches, Chennai)",
                    "Client Representative: Fertrick | Development Lead: Balasubramanian",
                    "Prepared by: Arivom Technologies, Chennai | Document Version: 1.0 (Nov 2026)",
                    "Baseline Contract: INR 60,000 / 2 Months | Status: Client Review & Approval"
                ], is_dark_card=True)
    add_footer(s1, 1, 52, is_dark=True)

    # SLIDE 2: Document Control
    s2 = prs.slides.add_slide(blank_layout)
    set_bg(s2, C_OFFWHITE)
    add_header(s2, "Document Control & Version Management", "SECTION A: PROJECT INTRODUCTION")
    add_badge(s2, Inches(10.3), Inches(0.65), "GOVERNANCE", "CONFIRMED")
    
    doc_meta_headers = ["Attribute", "Specification Details", "Approval Authority"]
    doc_meta_rows = [
        ["Project Name", "Nitro Racing Automobile Service Center Management System", "Nitro Racing / Fertrick"],
        ["Prepared By", "Arivom Technologies, Chennai", "Balasubramanian (Tech Lead)"],
        ["Target Branches", "Ambattur Branch, Avadi Branch (Scalable to N Branches)", "Super Admin / Branch Ops"],
        ["Original Date", "11 Nov 2026", "Arivom Tech & Client"],
        ["Document Status", "Formal Client Review, Scope Demarcation & Sign-off", "Client Representative"],
        ["Baseline Commercials", "Duration: 2 Months | Fixed Baseline Cost: INR 60,000", "Contractual Baseline v1.0"]
    ]
    create_table_card(s2, Inches(0.8), Inches(1.4), Inches(11.7), Inches(2.5), doc_meta_headers, doc_meta_rows, [Inches(2.5), Inches(6.2), Inches(3.0)])

    rev_headers = ["Version", "Release Date", "Author / Role", "Summary of Scope Changes & Governance Notes"]
    rev_rows = [
        ["v1.0 Baseline", "11 Nov 2026", "Arivom Technologies", "Original 5-page BRD with 26 core functional requirements (FR-01 to FR-26)."],
        ["v1.0 Expanded", "11 Nov 2026", "Arivom Product Team", "52-slide comprehensive slide BRD, full module specifications, wireframes, and RTM."]
    ]
    create_table_card(s2, Inches(0.8), Inches(4.3), Inches(11.7), Inches(2.2), rev_headers, rev_rows, [Inches(1.8), Inches(1.8), Inches(2.8), Inches(5.3)])
    add_footer(s2, 2, 52)

    # SLIDE 3: Executive Summary
    s3 = prs.slides.add_slide(blank_layout)
    set_bg(s3, C_OFFWHITE)
    add_header(s3, "Executive Summary & Solution Overview", "SECTION A: PROJECT INTRODUCTION")
    add_badge(s3, Inches(10.3), Inches(0.65), "EXECUTIVE BRIEF", "CONFIRMED")

    create_card(s3, Inches(0.8), Inches(1.4), Inches(3.7), Inches(5.2), "BUSINESS CONTEXT", [
        "Nitro Racing operates high-volume motorcycle service centers in Chennai (Ambattur & Avadi).",
        "Experiencing rapid customer intake growth requiring strict process standardization.",
        "Management requires a modern digital platform to unify multi-branch operations.",
        "Needs high customer retention through transparent service estimates and timely delivery."
    ])

    create_card(s3, Inches(4.8), Inches(1.4), Inches(3.7), Inches(5.2), "DUAL-SURFACE SOLUTION", [
        "1. Public Business Website: Modern brand portal showcasing services, facilities, branch locator, and booking funnel.",
        "2. Management Portal: Role-restricted operations portal (Super Admin, Branch Admin, Employee).",
        "Mobile-first workflow optimization: mechanics create job cards and invoices on mobile phones.",
        "Real-time centralized multi-branch database with automatic daily cloud backups."
    ])

    create_card(s3, Inches(8.8), Inches(1.4), Inches(3.7), Inches(5.2), "BUSINESS VALUE DELIVERED", [
        "100% Paperless Operations: Eliminates lost grease-stained job cards and billing disputes.",
        "Cross-Branch Transparency: Owners see live sales, revenue, profit, and technician workloads.",
        "Instant Invoicing: Automated PDF invoice generation with advance offsets and GST calculations.",
        "Scalable Foundation: Support any number of future branches without code changes."
    ])
    add_footer(s3, 3, 52)

    # SLIDE 4: Business Challenges
    s4 = prs.slides.add_slide(blank_layout)
    set_bg(s4, C_OFFWHITE)
    add_header(s4, "Current Business Challenges vs. Digital Transformation", "SECTION A: PROJECT INTRODUCTION")
    add_badge(s4, Inches(10.3), Inches(0.65), "GAP ANALYSIS", "CONFIRMED")

    ch_headers = ["Operational Area", "Current Manual Reality (As-Is)", "Proposed Nitro Racing System (To-Be)", "Business Impact"]
    ch_rows = [
        ["Job Card Intake", "Paper registers, prone to grease damage and physical loss.", "Digital Job Card created in < 60s on smartphone.", "Zero record loss, instant search."],
        ["Multi-Branch Sync", "Branches isolated; daily revenue phoned manually at night.", "Real-time unified cloud database with instant dashboards.", "Total operational visibility."],
        ["Vehicle History", "Zero historical records when a bike visits for the 2nd time.", "Lifetime service log linked to bike registration number.", "Accurate diagnosis, customer trust."],
        ["Workforce Control", "Mechanic workload is invisible; delays go unnoticed.", "Technician assignment and status tracking on dashboard.", "Balanced workload, faster delivery."],
        ["Billing & Invoicing", "Manual paper bills with delayed math and calculation errors.", "1-Click PDF invoice generation with tax & advance deduction.", "Fast customer pickup, professional look."],
        ["Financial Reports", "No unified calculation of profit, sales, or part consumption.", "Automated daily/monthly sales, revenue, and profit charts.", "Data-driven business decisions."]
    ]
    create_table_card(s4, Inches(0.8), Inches(1.4), Inches(11.7), Inches(5.2), ch_headers, ch_rows, [Inches(2.0), Inches(3.3), Inches(3.8), Inches(2.6)])
    add_footer(s4, 4, 52)

    # SLIDE 5: Project Objectives
    s5 = prs.slides.add_slide(blank_layout)
    set_bg(s5, C_OFFWHITE)
    add_header(s5, "Project Objectives & Strategic Roadmap", "SECTION A: PROJECT INTRODUCTION")
    add_badge(s5, Inches(10.3), Inches(0.65), "STRATEGIC GOALS", "CONFIRMED")

    create_card(s5, Inches(0.8), Inches(1.4), Inches(5.6), Inches(2.5), "1. CENTRALIZED BRANCH CONTROL", [
        "Enable Super Admin to manage all operational stores (Ambattur, Avadi, future stores) from a single screen.",
        "Enforce strict branch data isolation so Branch Admins only see their own store records.",
        "Dynamically provision new branches without rewriting or redeploying code."
    ])
    create_card(s5, Inches(6.9), Inches(1.4), Inches(5.6), Inches(2.5), "2. DIGITAL WORKSHOP OPERATIONS", [
        "Replace physical paperwork with mobile-first digital job cards.",
        "Track vehicle progression through Received, Work In Progress, Completed, and Delivered stages.",
        "Maintain audit trail of every status change with author and timestamp."
    ])
    create_card(s5, Inches(0.8), Inches(4.2), Inches(5.6), Inches(2.5), "3. INSTANT BILLING & COMPLIANCE", [
        "Generate professional PDF invoices directly from job cards within seconds.",
        "Support automated labor and spare parts line items with tax/GST calculation.",
        "Facilitate direct mobile thermal printing and mobile sharing."
    ])
    create_card(s5, Inches(6.9), Inches(4.2), Inches(5.6), Inches(2.5), "4. BUSINESS PERFORMANCE INTELLIGENCE", [
        "Deliver graphical dashboards showing monthly sales, gross revenue, profit, and bike brand breakdown.",
        "Empower owners with cross-branch sales comparisons and technician productivity metrics.",
        "Strictly block employees from sensitive financial metrics."
    ])
    add_footer(s5, 5, 52)

    # SLIDE 6: Scope of the Project
    s6 = prs.slides.add_slide(blank_layout)
    set_bg(s6, C_OFFWHITE)
    add_header(s6, "Commercial Scope Demarcation & Safeguards", "SECTION A: PROJECT INTRODUCTION")
    add_badge(s6, Inches(10.3), Inches(0.65), "COMMERCIAL BOUNDARY", "CONFIRMED")

    create_card(s6, Inches(0.8), Inches(1.4), Inches(5.6), Inches(2.5), "A. ORIGINAL CONFIRMED BASELINE (FR-01 to FR-26)", [
        "Commercial Commitment: INR 60,000 | Timeline: 2 Months.",
        "Covers: Public Website (Home, About, Services, Enquiry, Reviews, Login).",
        "Management Portal: Store Mgmt, User Mgmt, Job Cards (FR-14), PDF Invoice (FR-19), and Role Dashboards (FR-23).",
        "Strict commercial baseline: no feature additions alter this contract unless signed."
    ], title_color=C_GREEN)

    create_card(s6, Inches(6.9), Inches(1.4), Inches(5.6), Inches(2.5), "B. RECOMMENDED ENHANCEMENTS (FR-101 to FR-110)", [
        "Centralized Customer & Bike Master directories (FR-101, FR-102).",
        "Pre-service Estimates & Customer Approval Gateways (FR-105).",
        "Spare Parts Inventory auto-deduction on job card parts issuance (FR-107).",
        "Quality Control (QC) checklist prior to final vehicle delivery (FR-108).",
        "Partial payments ledger and operating expense tracking for net P&L (FR-109, 110)."
    ], title_color=C_GOLD)

    create_card(s6, Inches(0.8), Inches(4.2), Inches(5.6), Inches(2.5), "C. OPTIONAL FUTURE SCOPE (PHASE 2)", [
        "Automated customer SMS & WhatsApp service milestone notifications (FR-111).",
        "Public Website Dynamic Content Management System (CMS) (FR-112).",
        "Technician Biometric / GPS Attendance Integration.",
        "Regional Language localization (Tamil UI interface) (FR-115)."
    ], title_color=C_CHARCOAL)

    create_card(s6, Inches(6.9), Inches(4.2), Inches(5.6), Inches(2.5), "D. PENDING CLIENT DECISIONS (8 QUESTIONS)", [
        "Q1: P&L formula confirmation (Parts purchase cost & expenses).",
        "Q2: GST registration number and tax invoice formatting.",
        "Q3: SMS/WhatsApp gateway credentials and subscription.",
        "Q4: Confirmation of 'Delivered' status addition.",
        "Q5: Employee edit/delete permissions boundary.",
        "Q6: Logo, domain, hosting setup | Q7: Legacy data migration | Q8: Tamil UI."
    ], title_color=C_ORANGE)
    add_footer(s6, 6, 52)

    # SLIDE 7: Application Ecosystem (Dark)
    s7 = prs.slides.add_slide(blank_layout)
    set_bg(s7, C_GRAPHITE)
    add_header(s7, "Application Ecosystem & Enterprise Topology", "SECTION B: APPLICATION OVERVIEW", is_dark=True)
    add_badge(s7, Inches(10.3), Inches(0.65), "ECOSYSTEM MAP", "CONFIRMED")

    create_card(s7, Inches(0.8), Inches(1.4), Inches(3.7), Inches(5.2), "SURFACE 1: PUBLIC BRAND WEB", [
        "Target Audience: Motorcycle Owners & Enthusiasts.",
        "Core Capabilities:",
        "  - Interactive Service Catalogue (11 Categories).",
        "  - Branch Directory & GPS Routing (Ambattur, Avadi).",
        "  - Online Service Appointment Booking Funnel.",
        "  - Lead Enquiry Generation & Email Dispatch.",
        "  - Customer Reviews & Workshop Photo Gallery.",
        "  - Staff Login Entry Gate (No public registration)."
    ], is_dark_card=True)

    create_card(s7, Inches(4.8), Inches(1.4), Inches(3.7), Inches(5.2), "SURFACE 2: MANAGEMENT PORTAL", [
        "Target Audience: Super Admin, Branch Admin, Staff.",
        "Core Capabilities:",
        "  - Mobile-First Job Card Intake Engine (< 60s).",
        "  - Real-time Status Flow: Received -> WIP -> Done.",
        "  - Instant JasperReports PDF Invoice Engine.",
        "  - Branch Isolation: Branch Admins see own data.",
        "  - Super Admin Cross-Branch Analytics Dashboard.",
        "  - Multi-tenant PostgreSQL Cloud Database."
    ], is_dark_card=True)

    create_card(s7, Inches(8.8), Inches(1.4), Inches(3.7), Inches(5.2), "INTEGRATION SERVICES & DB", [
        "Spring Boot 3 RESTful API Gateway with JWT Auth.",
        "PostgreSQL 16 Multi-Tenant RDBMS with schema FKs.",
        "JavaMail SMTP Gateway for Enquiry & Password Resets.",
        "JasperReports PDF Compilation Engine (Immutable).",
        "Automated Daily Cloud Snapshot Backup.",
        "Optional Third-Party SMS / WhatsApp Gateway hooks."
    ], is_dark_card=True)
    add_footer(s7, 7, 52, is_dark=True)

    # SLIDE 8: Application Module Overview
    s8 = prs.slides.add_slide(blank_layout)
    set_bg(s8, C_OFFWHITE)
    add_header(s8, "Complete Application Module Map", "SECTION B: APPLICATION OVERVIEW")
    add_badge(s8, Inches(10.3), Inches(0.65), "MODULE TAXONOMY", "CONFIRMED")

    mod_headers = ["Sub-System", "Module Name", "Primary Purpose", "Core Functions", "Baseline Status"]
    mod_rows = [
        ["Public Web", "Brand & Services", "Showcase repair expertise & packages", "Browse 11 service categories, pricing, inclusions", "SOURCE CONFIRMED"],
        ["Public Web", "Branch Locator", "Guide riders to Ambattur & Avadi", "Address, phone, hours, direct Google Map directions", "SOURCE CONFIRMED"],
        ["Public Web", "Enquiry & Booking", "Capture inbound service leads", "Submit enquiry form, request appointment date/time", "CONFIRMED / REC"],
        ["Portal Ops", "Store Management", "Provision and manage branches", "Add store, edit details, branch-specific dashboard link", "SOURCE CONFIRMED"],
        ["Portal Ops", "User Management", "Enforce role-based access control", "Create Branch Admins, manage branch employees", "SOURCE CONFIRMED"],
        ["Portal Ops", "Job Card Engine", "Core motorcycle service tracking", "Record bike, customer, complaint, advance; update status", "SOURCE CONFIRMED"],
        ["Portal Ops", "Invoicing & PDF", "Generate compliant customer bills", "Calculate parts/labor/tax, offset advance, export PDF", "SOURCE CONFIRMED"],
        ["Portal Ops", "Dashboards & BI", "Executive operations visibility", "Sales, revenue, profit, brand distribution charts", "SOURCE CONFIRMED"]
    ]
    create_table_card(s8, Inches(0.8), Inches(1.4), Inches(11.7), Inches(5.2), mod_headers, mod_rows, [Inches(1.5), Inches(2.0), Inches(2.6), Inches(4.0), Inches(1.6)])
    add_footer(s8, 8, 52)

    # SLIDE 9: Business Process Overview
    s9 = prs.slides.add_slide(blank_layout)
    set_bg(s9, C_OFFWHITE)
    add_header(s9, "End-to-End Workshop Lifecycle State Machine", "SECTION B: APPLICATION OVERVIEW")
    add_badge(s9, Inches(10.3), Inches(0.65), "LIFECYCLE FLOW", "CONFIRMED")

    steps_data = [
        ("Step 1: Check-in", "Customer arrives (walk-in or booking). Staff inputs bike reg & phone; logs odometer, damages, and complaint notes."),
        ("Step 2: Advance & JC", "Advance deposit collected (if any). Unique Job Card generated under status 'RECEIVED'."),
        ("Step 3: Diagnosis", "Mechanic inspects motorcycle; diagnoses root causes, estimates spare parts and required labour."),
        ("Step 4: Approval Gate", "Estimate presented to customer. Upon approval, job transitions to 'WORK IN PROGRESS'."),
        ("Step 5: Workshop Service", "Technician carries out mechanical repairs; parts issued from inventory and deducted from stock."),
        ("Step 6: QC Inspection", "Supervisor verifies completion of all complaints, runs brake/wash checks; marks job 'COMPLETED'."),
        ("Step 7: PDF Invoicing", "System compiles itemized labor + parts + tax, offsets initial advance, and generates immutable PDF."),
        ("Step 8: Delivery & Pmt", "Customer settles balance via UPI/Cash/Card; status updated to 'DELIVERED'; permanent service history committed.")
    ]
    
    col_w = Inches(2.7)
    gap = Inches(0.2)
    left_start = Inches(0.8)
    for idx, (title, text) in enumerate(steps_data):
        row_num = idx // 4
        col_num = idx % 4
        x = left_start + col_num * (col_w + gap)
        y = Inches(1.4) + row_num * Inches(2.7)
        create_card(s9, x, y, col_w, Inches(2.5), title, [text], title_color=C_ORANGE)
        
    add_footer(s9, 9, 52)
    print("Section A & B (Slides 1-9) compiled.")
