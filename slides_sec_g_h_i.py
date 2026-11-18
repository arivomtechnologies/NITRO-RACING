from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from common_deck import (
    C_GRAPHITE, C_CHARCOAL, C_ORANGE, C_SILVER, C_OFFWHITE, C_WHITE,
    C_GREEN, C_GOLD, C_MUTED, C_CARD_BG, C_DARK_CARD,
    set_bg, add_header, add_footer, add_badge, create_card, create_table_card
)

def build_slides_40_to_52(prs, blank_layout):
    # SLIDE 40: Super Admin Dashboard (Dark)
    s40 = prs.slides.add_slide(blank_layout)
    set_bg(s40, C_GRAPHITE)
    add_header(s40, "Super Admin Dashboard: Consolidated Business Intelligence", "SECTION G: DASHBOARDS & REPORTS", is_dark=True)
    add_badge(s40, Inches(10.3), Inches(0.65), "EXECUTIVE BI", "CONFIRMED")

    create_card(s40, Inches(0.8), Inches(1.4), Inches(3.7), Inches(5.2), "CONSOLIDATED KPI STRIP", [
        "1. Active Branch Count: Total live stores (Ambattur, Avadi, ...).",
        "2. Total Month-to-Date Sales: Cumulative revenue across all branches.",
        "3. Total Jobs Serviced: Total motorcycles handled across all locations.",
        "4. Net Enterprise Profit: Consolidated profit after parts costing.",
        "5. Average Ticket Size: Mean revenue per completed Job Card."
    ], is_dark_card=True)

    create_card(s40, Inches(4.8), Inches(1.4), Inches(3.7), Inches(5.2), "CORE VISUAL CHARTS (FR-23)", [
        "Chart 1: Monthly Sales Volume Trend (Bar chart showing monthly units).",
        "Chart 2: Monthly Gross Revenue (Revenue curve over last 12 months).",
        "Chart 3: Monthly Net Profit (Gross margin & profit progression).",
        "Chart 4: Bike Types Entered (Pie/Donut: Yamaha 32%, RE 28%, KTM 22%, Honda 18%).",
        "Chart 5: Jobs by Status (Received: 12, WIP: 18, Done: 45, Delivered: 120)."
    ], is_dark_card=True)

    create_card(s40, Inches(8.8), Inches(1.4), Inches(3.7), Inches(5.2), "BRANCH COMPARISON & DRILL-DOWN", [
        "Direct Store Comparison (FR-24): Compare Ambattur vs Avadi on single comparative chart.",
        "1-Click Branch Drill-down: Clicking any branch row instantly loads that branch's full operational view.",
        "Real-Time Data Refresh: Auto-refreshes every 5 minutes during workshop hours.",
        "Export Capability: Print or save monthly executive summary PDF."
    ], is_dark_card=True)
    add_footer(s40, 40, 52, is_dark=True)

    # SLIDE 41: Branch Admin Dashboard
    s41 = prs.slides.add_slide(blank_layout)
    set_bg(s41, C_OFFWHITE)
    add_header(s41, "Branch Admin Dashboard: Local Workshop Operations", "SECTION G: DASHBOARDS & REPORTS")
    add_badge(s41, Inches(10.3), Inches(0.65), "BRANCH DASHBOARD", "CONFIRMED")

    create_card(s41, Inches(0.8), Inches(1.4), Inches(3.7), Inches(5.2), "BRANCH-LEVEL KPIS (FR-25)", [
        "Today's Vehicle Check-ins: Count of bikes received today.",
        "Bays Currently Occupied: Real-time active repair count.",
        "Completed Awaiting Pickup: Vehicles ready for customer delivery.",
        "Daily Cash & UPI Collection: Total revenue collected during current shift.",
        "Low Stock Alerts: Count of spare parts below reorder threshold."
    ])

    create_card(s41, Inches(4.8), Inches(1.4), Inches(3.7), Inches(5.2), "OPERATIONAL CHARTS", [
        "1. Branch Monthly Sales & Revenue Trend (FR-23).",
        "2. Branch Monthly Profit Trend (Local store margin).",
        "3. Local Bike Brand Breakdown (Top models serviced at branch).",
        "4. Current Jobs by Status Breakdown (Active bay workload).",
        "5. Technician Daily Workload Allocation (Jobs per mechanic)."
    ])

    create_card(s41, Inches(8.8), Inches(1.4), Inches(3.7), Inches(5.2), "DATA ISOLATION SAFEGUARD", [
        "Strict Single-Branch Access: Ambattur Admin only sees Ambattur figures; cannot see Avadi.",
        "No Cross-Branch Queries: System enforces branch foreign key filtering on all queries.",
        "Immediate Action Center: Unapproved estimates and overdue job cards highlighted in red.",
        "Shift-End Reconciliation: Summary of daily invoices and cash drawer totals."
    ])
    add_footer(s41, 41, 52)

    # SLIDE 42: Employee Access & Responsibilities
    s42 = prs.slides.add_slide(blank_layout)
    set_bg(s42, C_OFFWHITE)
    add_header(s42, "Employee Portal Access & Security Boundary", "SECTION G: DASHBOARDS & REPORTS")
    add_badge(s42, Inches(10.3), Inches(0.65), "FLOOR WORKFORCE", "CONFIRMED")

    emp_headers = ["Portal Functional Area", "Employee Permission Level", "Business & Security Rationale"]
    emp_rows = [
        ["Executive & Branch Dashboards (FR-26)", "STRICTLY BLOCKED / HIDDEN", "Employees are front-line technicians; sensitive business profit and total sales must remain confidential."],
        ["Job Card Intake (FR-14)", "FULL CREATE PERMISSION", "Service advisors and technicians must rapidly register incoming motorcycles on smartphones."],
        ["Job Status Progression (FR-16)", "FULL UPDATE PERMISSION", "Mechanics must mark jobs as 'Work In Progress' and 'Completed' as physical repairs progress."],
        ["Spare Parts Requisition (FR-107)", "ISSUE ONLY PERMISSION", "Employees can add parts to active job cards, but cannot edit supplier purchase prices or catalog."],
        ["PDF Invoice Generation (FR-19)", "GENERATE & PRINT PERMISSION", "Technicians can generate and print the customer invoice at the workshop counter upon delivery."],
        ["User & Branch Configuration", "STRICTLY BLOCKED / HIDDEN", "Employees cannot access staff lists, modify user roles, or change branch business settings."]
    ]
    create_table_card(s42, Inches(0.8), Inches(1.4), Inches(11.7), Inches(5.2), emp_headers, emp_rows, [Inches(3.2), Inches(3.0), Inches(5.5)])
    add_footer(s42, 42, 52)

    # SLIDE 43: Reports and Analytics Engine
    s43 = prs.slides.add_slide(blank_layout)
    set_bg(s43, C_OFFWHITE)
    add_header(s43, "Management Reports & Export Analytics Suite", "SECTION G: DASHBOARDS & REPORTS")
    add_badge(s43, Inches(10.3), Inches(0.65), "ANALYTICS ENGINE", "CONFIRMED / REC")

    create_card(s43, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.2), "CORE STANDARD REPORTS (CONFIRMED)", [
        "1. Daily Sales Summary Report:",
        "   • List of all invoices generated in a day across branches.",
        "   • Breakdown by Labor Charges, Parts Revenue, and Tax.",
        "   • Cash vs. UPI vs. Card settlement totals.",
        "2. Monthly Sales & Revenue Analytics (FR-23):",
        "   • Month-by-month financial progression.",
        "   • Comparison against preceding months.",
        "3. Job Card Status Volume Report:",
        "   • Total volume handled by status (Received, WIP, Done, Delivered).",
        "   • Average turnaround time per service category.",
        "4. Motorcycle Brand & Model Distribution:",
        "   • High-frequency bike models to guide spare parts stocking."
    ])

    create_card(s43, Inches(6.9), Inches(1.4), Inches(5.6), Inches(5.2), "ADVANCED RECOMMENDED ANALYTICS (PROPOSED)", [
        "5. Spare Parts Consumption & Inventory Velocity:",
        "   • Fast-moving vs. slow-moving spare parts analysis.",
        "   • Parts margin contribution and dead stock identification.",
        "6. Mechanic Productivity & Labor Recovery:",
        "   • Labor hours billed vs. physical technician hours worked.",
        "   • Quality rework tracking per technician.",
        "7. Customer Retention & Repeat Visit Index:",
        "   • Percentage of customers returning for second service within 120 days.",
        "8. Operational Profit & Loss Statement (P&L):",
        "   • True net margin after deducting wholesale parts and operating expenses."
    ])
    add_footer(s43, 43, 52)

    # SLIDE 44: System Architecture Specification (Dark)
    s44 = prs.slides.add_slide(blank_layout)
    set_bg(s44, C_GRAPHITE)
    add_header(s44, "Proposed Technical Architecture & Tech Stack", "SECTION H: TECHNICAL ARCHITECTURE & DATA", is_dark=True)
    add_badge(s44, Inches(10.3), Inches(0.65), "PROPOSED ARCHITECTURE", "CONFIRMED")

    arch_headers = ["Architecture Tier", "Recommended Technology Stack", "Technical Justification & Operational Value"]
    arch_rows = [
        ["Public Brand Website", "Angular 18+ (SSR / PWA)", "Fast load times (< 2s), high SEO indexability, responsive mobile booking interface."],
        ["Management Portal", "Angular 18+ (SPA / Angular Material)", "Rich data-grid tables, instant reactive status updates, mobile touch-friendly design."],
        ["Backend REST API Gateway", "Java Spring Boot 3.3+ (Java 21 LTS)", "Enterprise-grade concurrency, high reliability, strict compile-time type safety."],
        ["Security & RBAC Layer", "Spring Security 6 + JWT Stateless Tokens", "Robust role enforcement on every API; 24-hour persistent mobile sessions (FR-03)."],
        ["Relational Database", "PostgreSQL 16 (Multi-tenant)", "ACID compliance for billing/inventory; branch-isolated schemas; automated daily backups."],
        ["Document Generation Engine", "JasperReports 7.0+", "Pixel-perfect, immutable server-side PDF invoice compilation (No client tampering)."],
        ["Notification Gateway", "JavaMail SMTP + Spring Async", "Asynchronous non-blocking email dispatch for inquiries and password recovery."]
    ]
    create_table_card(s44, Inches(0.8), Inches(1.4), Inches(11.7), Inches(5.2), arch_headers, arch_rows, [Inches(2.5), Inches(3.6), Inches(5.6)])
    add_footer(s44, 44, 52, is_dark=True)

    # SLIDE 45: Database ER Diagram & Relationships
    s45 = prs.slides.add_slide(blank_layout)
    set_bg(s45, C_OFFWHITE)
    add_header(s45, "Relational Database Schema & Entity Relationships", "SECTION H: TECHNICAL ARCHITECTURE & DATA")
    add_badge(s45, Inches(10.3), Inches(0.65), "RELATIONAL SCHEMA", "CONFIRMED")

    create_card(s45, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.2), "CORE RELATIONAL ENTITIES (22+ TABLES)", [
        "1. Multi-Tenant Core: branches (stores), users, audit_logs.",
        "2. Customer & Vehicle Master: customers, customer_bikes.",
        "3. Inbound Funnel: website_enquiries, service_appointments.",
        "4. Workshop Execution: job_cards, vehicle_inspections, job_status_history, job_card_services, job_card_parts.",
        "5. Service Catalog: service_catalogue, service_packages.",
        "6. Parts & Inventory: spare_parts_inventory, stock_transactions, suppliers.",
        "7. Estimates: estimates, estimate_items.",
        "8. Billing & Ledger: invoices, invoice_items, payments, expenses."
    ])

    create_card(s45, Inches(6.9), Inches(1.4), Inches(5.6), Inches(5.2), "KEY FOREIGN KEY INTEGRITY RULES", [
        "• branches -> users (1:N): Every user (except Super Admin) is anchored to one branch.",
        "• customers -> customer_bikes (1:N): One customer can own multiple motorcycles.",
        "• customer_bikes -> job_cards (1:N): Motorcycle accumulates permanent lifetime service history.",
        "• job_cards -> job_status_history (1:N): Immutable chronological status change log.",
        "• job_cards -> invoices (1:1): Exactly one final invoice emitted per repair order.",
        "• invoices -> payments (1:N): Supports advance offset and subsequent balance collections.",
        "• Branch FK Enforcement: Strict data separation prevents cross-branch leakage."
    ])
    add_footer(s45, 45, 52)

    # SLIDE 46: Security and Non-Functional Requirements
    s46 = prs.slides.add_slide(blank_layout)
    set_bg(s46, C_OFFWHITE)
    add_header(s46, "Security, Performance & Non-Functional Compliance", "SECTION H: TECHNICAL ARCHITECTURE & DATA")
    add_badge(s46, Inches(10.3), Inches(0.65), "NFR COMPLIANCE", "CONFIRMED")

    nfr_headers = ["NFR Dimension", "Original BRD Baseline Specification", "Engineering Implementation Standard"]
    nfr_rows = [
        ["Mobile Responsiveness", "Works on mobile, laptop, and desktop; mobile-first design for job card and invoice.", "Responsive CSS Grid/Flexbox; single-hand touch inputs for workshop floor."],
        ["Performance SLA", "Pages load in approximately 3 seconds on normal mobile connection.", "Compressed bundle size (< 500KB initial chunk); browser caching; optimized SQL indices."],
        ["Data Security & SSL", "Encrypted passwords, HTTPS, role-based access on every page and API.", "TLS 1.3 encryption forced; BCrypt password hashing (cost factor 12); JWT auth tokens."],
        ["Multi-Branch Isolation", "Data separated strictly by branch; Branch Admin cannot view other stores.", "Tenant context filter in Spring Security; PostgreSQL row-level branch checks."],
        ["Availability & Backups", "Daily automated data backup to prevent catastrophic data loss.", "Automated pg_dump snapshot cron job executed daily at 02:00 AM offloaded to secure cloud."],
        ["Browser Compatibility", "Latest Chrome, Safari, Edge, and Firefox.", "Cross-browser automated Selenium / Playwright test suite execution on CI/CD."]
    ]
    create_table_card(s46, Inches(0.8), Inches(1.4), Inches(11.7), Inches(5.2), nfr_headers, nfr_rows, [Inches(2.4), Inches(4.5), Inches(4.8)])
    add_footer(s46, 46, 52)

    # SLIDE 47: Testing and Quality Assurance
    s47 = prs.slides.add_slide(blank_layout)
    set_bg(s47, C_OFFWHITE)
    add_header(s47, "Quality Assurance, Testing Matrix & Validation", "SECTION I: PROJECT MANAGEMENT & APPROVAL")
    add_badge(s47, Inches(10.3), Inches(0.65), "QA STRATEGY", "CONFIRMED")

    create_card(s47, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.2), "FUNCTIONAL QA SUITE", [
        "1. Authentication & Session Validation:",
        "   • Verify 24-hour session persistence on mobile devices.",
        "   • Validate password reset tokens expire after 15 minutes.",
        "2. Role-Based Access Control (RBAC) Testing:",
        "   • Confirm Employees are completely blocked from dashboards (FR-26).",
        "   • Validate Branch Admin cannot view other branches' data (FR-25).",
        "3. Job Card Lifecycle State Machine:",
        "   • Verify status transitions: Received -> WIP -> Done -> Delivered.",
        "   • Verify immutable status history logs author and timestamp.",
        "4. Math & Billing Accuracy Testing:",
        "   • Rigorous testing of labor charges, parts pricing, tax/GST, and advance deduction.",
        "   • Ensure balance due = Total - Advance across 100+ edge-case test vouchers."
    ])

    create_card(s47, Inches(6.9), Inches(1.4), Inches(5.6), Inches(5.2), "NON-FUNCTIONAL & MOBILE TESTING", [
        "5. Mobile Device Field Testing:",
        "   • Verified on Android (Chrome) and iOS (Safari) across various screen sizes.",
        "   • Test touch targets and virtual keyboard behavior during greasy workshop operations.",
        "6. PDF Compilation & Rendering Fidelity:",
        "   • Verify JasperReports PDF renders identically across all PDF readers.",
        "   • Validate direct mobile wireless thermal printing and WhatsApp PDF sharing.",
        "7. Network Degradation Testing:",
        "   • Verify 3-second load speed under throttled 4G mobile conditions.",
        "8. Security & Vulnerability Scans:",
        "   • OWASP Top 10 compliance: SQL injection protection via prepared statements, XSS escaping, CSRF protection."
    ])
    add_footer(s47, 47, 52)

    # SLIDE 48: Implementation Timeline
    s48 = prs.slides.add_slide(blank_layout)
    set_bg(s48, C_OFFWHITE)
    add_header(s48, "Implementation Roadmap: 8-Week Timeline (2 Months)", "SECTION I: PROJECT MANAGEMENT & APPROVAL")
    add_badge(s48, Inches(10.3), Inches(0.65), "TIMELINE: 2 MONTHS", "CONFIRMED")

    time_headers = ["Timeline Phase", "Duration", "Key Development Milestones & Deliverables", "Exit Criteria & Review Gate"]
    time_rows = [
        ["Week 1", "Days 1 - 7", "Requirements sign-off, UI/UX design mockups, PostgreSQL schema initialization.", "Client approves visual mockups & final BRD"],
        ["Week 2", "Days 8 - 14", "Authentication engine, JWT security, multi-branch store provisioning (FR-07 to 11).", "Admins can log in and manage stores"],
        ["Week 3", "Days 15 - 21", "User management (Branch Admins & Employees), Customer & Bike database setup.", "Branch staff accounts mapped to branches"],
        ["Week 4", "Days 22 - 28", "Core Job Card intake engine (FR-14), status progression workflow, and audit logging.", "Full job card intake tested on smartphones"],
        ["Week 5", "Days 29 - 35", "Billing engine, JasperReports PDF generation (FR-19 to 21), advance offset math.", "Pixel-perfect PDF invoices generated on mobile"],
        ["Week 6", "Days 36 - 42", "Executive & Branch Dashboards (FR-23 to 25), BI charts, Employee access blocks.", "Live reporting verified against test records"],
        ["Week 7", "Days 43 - 49", "Public brand website (Home, About, Services, Enquiry, Branches, Reviews).", "Public website live on staging server"],
        ["Week 8", "Days 50 - 60", "End-to-end integration testing, UAT, cloud deployment, staff training & Go-Live.", "Production deployment and client sign-off"]
    ]
    create_table_card(s48, Inches(0.8), Inches(1.4), Inches(11.7), Inches(5.2), time_headers, time_rows, [Inches(1.8), Inches(1.6), Inches(5.5), Inches(2.8)])
    add_footer(s48, 48, 52)

    # SLIDE 49: Client Clarifications
    s49 = prs.slides.add_slide(blank_layout)
    set_bg(s49, C_OFFWHITE)
    add_header(s49, "Client Clarifications: 8 Baseline Decisions", "SECTION I: PROJECT MANAGEMENT & APPROVAL")
    add_badge(s49, Inches(10.3), Inches(0.65), "DECISIONS REQUIRED", "PENDING")

    q_headers = ["#", "Original Open Question (BRD Sec 8)", "Arivom Technologies Recommendation", "Impact on System"]
    q_rows = [
        ["Q1", "How should profit be calculated? Will parts purchase cost and expenses be entered?", "Implement Gross Profit = (Billed Labor + Parts Markup) - Direct Cost. Recommend Operating Expenses module.", "Financial reporting logic & P&L dashboard"],
        ["Q2", "Is GST/tax required on invoices? Please share GST number and invoice format.", "Implement configurable tax toggle in administration; support 18% GST with auto HSN breakdown.", "PDF invoice layout & tax calculation engine"],
        ["Q3", "Should customers receive SMS/WhatsApp updates on status changes?", "Highly recommended for customer trust. Scope requires third-party SMS/WhatsApp gateway credentials.", "Third-party webhook & messaging integration"],
        ["Q4", "Should 'Delivered' status be added after 'Completed'?", "Yes, strongly recommended. Separates bikes finished by mechanics from vehicles physically handed over.", "Lifecycle state machine & delivery gate pass"],
        ["Q5", "Can Employees edit/delete job cards, or only create and update status?", "Employees should only create and update status. Edit/Delete restricted to Branch Admins to prevent tampering.", "Permission boundaries in RBAC matrix"],
        ["Q6", "Does client have domain, hosting, and logo/brand colours?", "Arivom proposed the Racing theme (Graphite #17191D, Orange #F47721, Charcoal #242A31). Client to approve.", "Frontend assets, domain DNS, & cloud hosting"],
        ["Q7", "Is old legacy data (paper records/spreadsheets) to be migrated?", "Recommend fresh system start. Legacy data cleaning and migration can be scoped separately.", "Data import pipelines & cleansing scripts"],
        ["Q8", "Is a language other than English (e.g. Tamil) needed?", "Launch Phase 1 in English. Modular i18n architecture ready for Phase 2 Tamil localization.", "UI localization resource bundles"]
    ]
    create_table_card(s49, Inches(0.8), Inches(1.4), Inches(11.7), Inches(5.2), q_headers, q_rows, [Inches(0.6), Inches(4.3), Inches(4.3), Inches(2.5)])
    add_footer(s49, 49, 52)

    # SLIDE 50: Project Cost and Deliverables
    s50 = prs.slides.add_slide(blank_layout)
    set_bg(s50, C_OFFWHITE)
    add_header(s50, "Project Commercials, Scope Demarcation & Deliverables", "SECTION I: PROJECT MANAGEMENT & APPROVAL")
    add_badge(s50, Inches(10.3), Inches(0.65), "COMMERCIAL SUMMARY", "CONFIRMED")

    create_card(s50, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.2), "CONTRACTUAL COMMERCIAL BASELINE", [
        "ORIGINAL AGREED PARAMETERS (BRD v1.0):",
        "  • Fixed Baseline Cost: INR 60,000",
        "  • Baseline Timeline: 2 Months (8 Weeks)",
        "  • Scope Boundary: 26 Functional Requirements (FR-01 to FR-26)",
        "",
        "COMMERCIAL SAFEGUARD:",
        "  • The 15 recommended modules (FR-101 to FR-115) detailed in this presentation represent best-practice engineering proposals.",
        "  • Recommended modules are not automatically included in the baseline INR 60,000 contract.",
        "  • Any approved scope additions will be mutually agreed in writing before implementation."
    ], title_color=C_GREEN)

    create_card(s50, Inches(6.9), Inches(1.4), Inches(5.6), Inches(5.2), "FORMAL DELIVERABLES CHECKLIST", [
        "TECHNICAL & SOFTWARE DELIVERABLES:",
        "  ✔ Public Responsive Website (Angular 18+)",
        "  ✔ Role-Restricted Management Portal (Angular Material)",
        "  ✔ Spring Boot 3 RESTful Backend Services & JWT Auth",
        "  ✔ PostgreSQL Multi-Tenant Database Schema",
        "  ✔ JasperReports PDF Invoicing Engine",
        "  ✔ Cloud Production Deployment & Domain Setup",
        "",
        "DOCUMENTATION & GOVERNANCE ARTIFACTS:",
        "  ✔ Complete 52-Slide BRD Presentation Deck (.pptx & .pdf)",
        "  ✔ Detailed Word Specification Document (.docx)",
        "  ✔ Requirements Traceability Matrix (.xlsx)",
        "  ✔ Database ERD & System Architecture Diagrams (.png)",
        "  ✔ Sitemaps & Swimlane Business Workflows (.pdf)"
    ], title_color=C_CHARCOAL)
    add_footer(s50, 50, 52)

    # SLIDE 51: Approval and Sign-off (Dark)
    s51 = prs.slides.add_slide(blank_layout)
    set_bg(s51, C_GRAPHITE)
    add_header(s51, "Formal Business Requirements Sign-off & Acceptance", "SECTION I: PROJECT MANAGEMENT & APPROVAL", is_dark=True)
    add_badge(s51, Inches(10.3), Inches(0.65), "FORMAL SIGN-OFF", "CONFIRMED")

    create_card(s51, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.2), "CLIENT ACCEPTANCE (NITRO RACING)", [
        "Organization: Nitro Racing",
        "Authorized Representative: Fertrick",
        "Title: Business Owner / Client Representative",
        "",
        "Acceptance Statement:",
        "'I hereby review and approve this Business Requirements Document (BRD v1.0) as accurately representing the functional and technical scope agreed for the Nitro Racing Automobile Service Center Management System.'",
        "",
        "Signature: _____________________________________",
        "",
        "Date:       _____________________________________"
    ], is_dark_card=True)

    create_card(s51, Inches(6.9), Inches(1.4), Inches(5.6), Inches(5.2), "VENDOR COMMITMENT (ARIVOM TECHNOLOGIES)", [
        "Organization: Arivom Technologies, Chennai",
        "Authorized Representative: Balasubramanian",
        "Title: Technical Lead & Solution Architect",
        "",
        "Delivery Commitment:",
        "'Arivom Technologies commits to developing and delivering the Nitro Racing Automobile Service Center Management System conforming strictly to the baseline specifications and agreed architecture detailed herein.'",
        "",
        "Signature: _____________________________________",
        "",
        "Date:       _____________________________________"
    ], is_dark_card=True)
    add_footer(s51, 51, 52, is_dark=True)

    # SLIDE 52: Thank You / Closing Slide (Dark)
    s52 = prs.slides.add_slide(blank_layout)
    set_bg(s52, C_GRAPHITE)

    # Accent top bar
    bar = s52.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.18))
    bar.fill.solid()
    bar.fill.fore_color.rgb = C_ORANGE
    bar.line.fill.background()

    t_box = s52.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(11.3), Inches(2.8))
    tf = t_box.text_frame
    tf.word_wrap = True

    p0 = tf.paragraphs[0]
    p0.text = "NITRO RACING"
    p0.font.size = Pt(44)
    p0.font.bold = True
    p0.font.color.rgb = C_ORANGE
    p0.space_after = Pt(12)

    p1 = tf.add_paragraph()
    p1.text = "\"Smarter Workshop Operations. Better Customer Experience.\""
    p1.font.size = Pt(22)
    p1.font.bold = True
    p1.font.color.rgb = C_WHITE
    p1.space_after = Pt(18)

    p2 = tf.add_paragraph()
    p2.text = "Nitro Racing × Arivom Technologies, Chennai"
    p2.font.size = Pt(16)
    p2.font.color.rgb = C_SILVER
    p2.space_after = Pt(8)

    p3 = tf.add_paragraph()
    p3.text = "Automobile Service Center Management System | BRD v1.0 | November 2026"
    p3.font.size = Pt(12)
    p3.font.color.rgb = C_MUTED

    add_footer(s52, 52, 52, is_dark=True)
    print("Section G, H & I (Slides 40-52) compiled.")
