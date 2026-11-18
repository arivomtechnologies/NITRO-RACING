from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from common_deck import (
    C_GRAPHITE, C_CHARCOAL, C_ORANGE, C_SILVER, C_OFFWHITE, C_WHITE,
    C_GREEN, C_GOLD, C_MUTED, C_CARD_BG, C_DARK_CARD,
    set_bg, add_header, add_footer, add_badge, create_card, create_table_card
)

def build_slides_26_to_39(prs, blank_layout):
    # SLIDE 26: Customer Management
    s26 = prs.slides.add_slide(blank_layout)
    set_bg(s26, C_OFFWHITE)
    add_header(s26, "Module Specification: Customer Management", "SECTION F: CORE WORKSHOP MODULES")
    add_badge(s26, Inches(10.3), Inches(0.65), "CUSTOMER HUB", "RECOMMENDED")

    create_card(s26, Inches(0.8), Inches(1.4), Inches(3.7), Inches(5.2), "BUSINESS PURPOSE & ROLES", [
        "Purpose: Maintain centralized, 360-degree customer records to eliminate redundant data entry and link owners with their motorcycles.",
        "Target Users: Super Admin, Branch Admin, Employee (Search & Link during Job Card creation).",
        "Navigation: Management Portal > Customers > Customer Directory / Add Customer.",
        "Key Pain Point Solved: Prevents customer dissatisfaction caused by repeatedly asking for contact details on repeat visits."
    ])

    create_card(s26, Inches(4.8), Inches(1.4), Inches(3.7), Inches(5.2), "DATA ATTRIBUTES & FIELDS", [
        "• Customer ID (UUID / Auto-increment PK)",
        "• Full Name (Mandatory, String)",
        "• Primary Mobile Number (Unique Identifier, 10-digit)",
        "• Alternate Mobile Number (Optional)",
        "• Email Address (Optional, for digital invoices)",
        "• Street Address & Area (Mandatory for Job Card)",
        "• Branch Origin ID (Branch where first registered)",
        "• Customer Notes / VIP Status Flag",
        "• Created Timestamp & Last Service Date"
    ])

    create_card(s26, Inches(8.8), Inches(1.4), Inches(3.7), Inches(5.2), "RULES & WORKFLOWS", [
        "1. Instant Phone Lookup: Typing 10-digit phone in Job Card auto-fills name, address, and registered motorcycles.",
        "2. One-to-Many Relationship: Single customer can own multiple motorcycles (e.g. Daily Commuter + Weekend Track Bike).",
        "3. Cross-Branch Portability: Customer registered in Ambattur is immediately recognized when visiting Avadi.",
        "4. Duplicate Prevention: System prevents duplicate records with identical primary phone numbers."
    ])
    add_footer(s26, 26, 52)

    # SLIDE 27: Bike Management
    s27 = prs.slides.add_slide(blank_layout)
    set_bg(s27, C_OFFWHITE)
    add_header(s27, "Module Specification: Bike / Vehicle Management", "SECTION F: CORE WORKSHOP MODULES")
    add_badge(s27, Inches(10.3), Inches(0.65), "VEHICLE MASTER", "RECOMMENDED")

    create_card(s27, Inches(0.8), Inches(1.4), Inches(3.7), Inches(5.2), "BUSINESS PURPOSE & ROLES", [
        "Purpose: Establish persistent digital vehicle profiles tracking technical specifications, ownership history, and lifetime maintenance.",
        "Target Users: All 3 Roles (Super Admin, Branch Admin, Employee).",
        "Navigation: Portal > Bikes > Bike Directory / Register Bike.",
        "Key Value: Empowers mechanics to diagnose recurring issues by reviewing past repairs and replaced components."
    ])

    create_card(s27, Inches(4.8), Inches(1.4), Inches(3.7), Inches(5.2), "DATA ATTRIBUTES & FIELDS", [
        "• Bike ID (Primary Key)",
        "• Registration Number (e.g. TN-02-AX-1234, Unique)",
        "• Brand / Make (Yamaha, Honda, Royal Enfield, KTM)",
        "• Model (R15, Classic 350, Duke 390, Activa)",
        "• Bike Nickname / Name (Optional)",
        "• Engine Displacement (CC) & Variant",
        "• Year of Manufacture / Model Year",
        "• Current Odometer Reading (KMs, updated on intake)",
        "• Associated Customer ID (Foreign Key)"
    ])

    create_card(s27, Inches(8.8), Inches(1.4), Inches(3.7), Inches(5.2), "RULES & WORKFLOWS", [
        "1. Unique Registration: Vehicle identified strictly by government registration plate number.",
        "2. Lifetime Service Timeline: Chronological timeline of all past job cards, replaced parts, and recorded complaints.",
        "3. Service Interval Tracker: System computes next service due date based on elapsed days or kilometer threshold.",
        "4. Vehicle Re-assignment: Supports ownership transfer if a bike is sold to another customer."
    ])
    add_footer(s27, 27, 52)

    # SLIDE 28: Appointment Management
    s28 = prs.slides.add_slide(blank_layout)
    set_bg(s28, C_OFFWHITE)
    add_header(s28, "Module Specification: Appointment Management", "SECTION F: CORE WORKSHOP MODULES")
    add_badge(s28, Inches(10.3), Inches(0.65), "APPOINTMENTS", "RECOMMENDED")

    apt_headers = ["Appointment Status", "Workflow Definition", "Trigger Condition & System Action", "Actor Responsible"]
    apt_rows = [
        ["REQUESTED", "Customer submits online booking form via public website.", "Record created; email alert dispatched to branch.", "Customer (Web)"],
        ["CONFIRMED", "Branch Admin reviews bay capacity and accepts slot.", "Status updated; confirmation SMS/email sent.", "Branch Admin"],
        ["RESCHEDULED", "Customer calls to request alternate date/time.", "Slot revised; calendar availability updated.", "Branch Admin"],
        ["ARRIVED", "Rider arrives at workshop; motorcycle presented at bay.", "Triggers 1-click conversion to official Job Card.", "Employee / Advisor"],
        ["CANCELLED", "Customer cancels booking prior to scheduled time.", "Slot released back to public availability pool.", "Customer / Admin"],
        ["NO SHOW", "Customer fails to arrive within 60 minutes of slot.", "Marked as inactive; follow-up reminder scheduled.", "System / Admin"]
    ]
    create_table_card(s28, Inches(0.8), Inches(1.4), Inches(11.7), Inches(5.2), apt_headers, apt_rows, [Inches(2.0), Inches(4.0), Inches(3.7), Inches(2.0)])
    add_footer(s28, 28, 52)

    # SLIDE 29: Vehicle Check-in and Inspection
    s29 = prs.slides.add_slide(blank_layout)
    set_bg(s29, C_OFFWHITE)
    add_header(s29, "Module Specification: Vehicle Intake & Inspection", "SECTION F: CORE WORKSHOP MODULES")
    add_badge(s29, Inches(10.3), Inches(0.65), "CHECK-IN & QC", "RECOMMENDED")

    create_card(s29, Inches(0.8), Inches(1.4), Inches(3.7), Inches(5.2), "INSPECTION PROTOCOL", [
        "Objective: Protect Nitro Racing from false customer damage claims and record baseline vehicle state.",
        "Performed By: Service Advisor / Workshop Technician.",
        "Device: Mobile smartphone / workshop tablet.",
        "Duration: 90 seconds standard intake inspection.",
        "Customer Engagement: Customer witnesses and signs off on recorded scratches and fuel level."
    ])

    create_card(s29, Inches(4.8), Inches(1.4), Inches(3.7), Inches(5.2), "RECORDED ATTRIBUTES", [
        "• Accurate Odometer Reading (KMs Driven)",
        "• Fuel Gauge Level (E, 1/4, 1/2, 3/4, Full)",
        "• Existing Scratch & Dent Visual Map (Digital diagram)",
        "• Custody Items: Tool kit present? First aid kit? Helmet left?",
        "• Documents Held: RC copy, Insurance copy (if left)",
        "• Damage Photos: Direct smartphone camera capture (up to 4 photos stored in encrypted cloud bucket)"
    ])

    create_card(s29, Inches(8.8), Inches(1.4), Inches(3.7), Inches(5.2), "JOB CARD TRANSITION", [
        "1. Inspection data is immutably linked to the newly generated Job Card ID.",
        "2. Customer Complaints: Advisor logs rider's verbatim complaints (e.g. 'Engine sputtering at 60 km/h').",
        "3. Initial Estimate: Rough cost expectation communicated before dismantling.",
        "4. Digital Receipt: Customer receives instant SMS/WhatsApp check-in summary with Job Card ID."
    ])
    add_footer(s29, 29, 52)

    # SLIDE 30: Job Card Management
    s30 = prs.slides.add_slide(blank_layout)
    set_bg(s30, C_OFFWHITE)
    add_header(s30, "Module Specification: Job Card Management (Core Engine)", "SECTION F: CORE WORKSHOP MODULES")
    add_badge(s30, Inches(10.3), Inches(0.65), "CORE JOB CARD", "CONFIRMED")

    create_card(s30, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.2), "CONFIRMED BASELINE FIELDS (FR-14)", [
        "ORIGINAL BRD v1.0 MANDATORY FIELDS:",
        "1. Bike Details:",
        "   • Bike Registration Number (Mandatory)",
        "   • Bike Brand (e.g. Yamaha, Royal Enfield)",
        "   • Bike Model (e.g. R15 V4, Classic 350)",
        "   • Bike Name (Nickname / Designation)",
        "   • KMs Driven at Entry (Odometer reading)",
        "2. Service Details:",
        "   • Purpose of Entry (e.g. 'Engine Oil Change', 'Periodic Service')",
        "   • Date and Time of Entry (Auto-stamped)",
        "   • Assigned Mechanic (Technician name)",
        "3. Customer Details:",
        "   • Customer Name | Phone Number | Address",
        "4. Payment:",
        "   • Advance Amount Paid (if any, e.g. INR 500)"
    ], title_color=C_GREEN)

    create_card(s30, Inches(6.9), Inches(1.4), Inches(5.6), Inches(5.2), "RECOMMENDED OPERATIONAL EXTENSIONS", [
        "PROPOSED HIGH-EFFICIENCY ENHANCEMENTS:",
        "1. Diagnostic Breakdown:",
        "   • Customer Complaint vs. Mechanic Technical Diagnosis",
        "   • Primary labor tasks selected from Service Catalogue",
        "2. Spare Parts Allocation:",
        "   • Itemized parts requisition linked to branch inventory",
        "3. Turnaround SLA Management:",
        "   • Promised Vehicle Delivery Date & Time",
        "   • Priority Flag: Normal vs. Express Track Bay",
        "4. Strict Branch Ownership (FR-15):",
        "   • Job card strictly belongs to branch where vehicle entered",
        "   • Isolation ensures Avadi cannot alter Ambattur jobs"
    ], title_color=C_ORANGE)
    add_footer(s30, 30, 52)

    # SLIDE 31: Job Card Status Workflow
    s31 = prs.slides.add_slide(blank_layout)
    set_bg(s31, C_OFFWHITE)
    add_header(s31, "Job Card Status Progression & Audit Trail", "SECTION F: CORE WORKSHOP MODULES")
    add_badge(s31, Inches(10.3), Inches(0.65), "STATE MACHINE", "CONFIRMED")

    flow_headers = ["Lifecycle Status", "Who Can Update (FR-16)", "Prerequisite Condition & System Actions", "Next Allowed Transition"]
    flow_rows = [
        ["1. RECEIVED", "Super Admin, Branch Admin, Employee", "Vehicle check-in complete; initial advance logged; Job Card generated.", "-> WORK IN PROGRESS"],
        ["2. WORK IN PROGRESS", "Super Admin, Branch Admin, Employee", "Mechanic assigned; estimate approved; active repairs underway.", "-> COMPLETED"],
        ["3. COMPLETED", "Super Admin, Branch Admin, Employee", "All checklist tasks marked finished; final supervisor QC inspection passed.", "-> DELIVERED (or Invoice)"],
        ["4. DELIVERED (Proposed)", "Super Admin, Branch Admin, Employee", "Full invoice generated; balance payment collected; bike handed to owner.", "Final Archive State"]
    ]
    create_table_card(s31, Inches(0.8), Inches(1.4), Inches(11.7), Inches(2.8), flow_headers, flow_rows, [Inches(2.2), Inches(3.0), Inches(4.3), Inches(2.2)])

    create_card(s31, Inches(0.8), Inches(4.5), Inches(11.7), Inches(2.1), "AUDIT HISTORY SPECIFICATION (FR-18)", [
        "Immutable Audit Logging: System tracks every status alteration in dedicated 'job_status_history' table.",
        "Logged Metadata: Previous Status, New Status, User ID (Who changed it), User Role, Branch ID, Timestamp, Optional Remarks.",
        "Tamper Protection: Status history cannot be updated or deleted by any user (including Super Admin).",
        "Search & Filtering (FR-17): Job cards searchable by Bike Number, Customer Mobile, Status, and Date Range across all screens."
    ])
    add_footer(s31, 31, 52)

    # SLIDE 32: Estimate and Customer Approval
    s32 = prs.slides.add_slide(blank_layout)
    set_bg(s32, C_OFFWHITE)
    add_header(s32, "Module Specification: Estimate & Customer Approval", "SECTION F: CORE WORKSHOP MODULES")
    add_badge(s32, Inches(10.3), Inches(0.65), "ESTIMATES", "RECOMMENDED")

    create_card(s32, Inches(0.8), Inches(1.4), Inches(3.7), Inches(5.2), "BUSINESS OBJECTIVE", [
        "Prevent Billing Disputes: Provide riders with itemized cost transparency before initiating expensive engine/part replacements.",
        "Target Roles: Branch Admin, Service Advisor.",
        "Integration: Linked directly between Job Card 'Received' and 'Work In Progress' stages.",
        "Speed: Fast digital quotation prepared in < 3 minutes."
    ])

    create_card(s32, Inches(4.8), Inches(1.4), Inches(3.7), Inches(5.2), "QUOTATION STRUCTURE", [
        "• Estimate Reference Number (EST-BRANCH-YYYY-XXXX)",
        "• Itemized Labor Operations (Hours & Standard Charge)",
        "• Itemized Spare Parts (Part Code, Unit Price, Qty)",
        "• Consumables & Environmental Disposal Fee",
        "• Applicable Tax / GST Calculation",
        "• Advance Amount Paid Offset",
        "• Net Estimated Payable Amount"
    ])

    create_card(s32, Inches(8.8), Inches(1.4), Inches(3.7), Inches(5.2), "APPROVAL GATEWAY", [
        "1. Multi-Channel Sharing: Estimate sent via WhatsApp link or presented on workshop tablet.",
        "2. Customer Decision: Rider approves full scope, approves partial items, or rejects.",
        "3. Selective Parts Hold: Only approved parts are reserved in branch inventory.",
        "4. Additional Work Gate: If mechanic finds supplementary defects mid-repair, a supplementary estimate is triggered."
    ])
    add_footer(s32, 32, 52)

    # SLIDE 33: Mechanic Management
    s33 = prs.slides.add_slide(blank_layout)
    set_bg(s33, C_OFFWHITE)
    add_header(s33, "Module Specification: Mechanic Workforce & Allocation", "SECTION F: CORE WORKSHOP MODULES")
    add_badge(s33, Inches(10.3), Inches(0.65), "WORKFORCE", "RECOMMENDED")

    create_card(s33, Inches(0.8), Inches(1.4), Inches(3.7), Inches(5.2), "WORKFORCE ARCHITECTURE", [
        "Employee & Mechanic Dual Role: Per original BRD, mechanics are managed as branch Employees with operational permissions.",
        "Specialization Tagging: Tag technicians by skill (e.g. Engine Specialist, Electricals, Superbikes, General).",
        "Branch Scope: Mechanics belong strictly to one branch; can be reassigned by Super Admin.",
        "Mobile App User: Mechanic accesses personal queue on smartphone."
    ])

    create_card(s33, Inches(4.8), Inches(1.4), Inches(3.7), Inches(5.2), "WORKLOAD BALANCING", [
        "Active Bay Visibility: Branch Admin sees active job count per technician (e.g. Hari: 2 active, Rajesh: 0 active).",
        "Smart Allocation: Advisor assigns incoming Job Card based on mechanic availability and skill match.",
        "Turnaround Tracking: Time elapsed from 'Work In Progress' to 'Completed' measured against standard SLA.",
        "Bottleneck Alerts: Warning flag if job remains in WIP > 4 hours without status update."
    ])

    create_card(s33, Inches(8.8), Inches(1.4), Inches(3.7), Inches(5.2), "PERFORMANCE ANALYTICS", [
        "Monthly Output: Total job cards completed per mechanic.",
        "Billed Labor Contribution: Total labor revenue generated by technician.",
        "Quality Metrics: Number of customer rework / repeat complaints within 15 days.",
        "Incentive Calculation: Supports transparent technician performance bonus calculations."
    ])
    add_footer(s33, 33, 52)

    # SLIDE 34: Spare Parts and Inventory
    s34 = prs.slides.add_slide(blank_layout)
    set_bg(s34, C_OFFWHITE)
    add_header(s34, "Module Specification: Spare Parts & Inventory Management", "SECTION F: CORE WORKSHOP MODULES")
    add_badge(s34, Inches(10.3), Inches(0.65), "PARTS INVENTORY", "RECOMMENDED")

    inv_headers = ["Inventory Component", "Operational Workflow & Data Rules", "Control Role & Security"]
    inv_rows = [
        ["Parts Master Catalog", "Master database of parts: Part Code, Description, Category, Cost Price, MRP/Selling Price, Tax Rate.", "Super Admin (Global)"],
        ["Branch Stock Segregation", "Physical stock tracked separately by branch (Ambattur Stock vs. Avadi Stock).", "Branch Admin (Local)"],
        ["Stock Inward (GRN)", "Record supplier shipments, PO reference, inward quantity, purchase invoice number, batch.", "Branch Admin"],
        ["Job Card Auto-Deduction", "When spare parts are issued to a Job Card, branch stock is automatically decremented.", "All Roles / Technicians"],
        ["Low-Stock Reorder Alerts", "System triggers visual warning when item count falls below predefined reorder threshold.", "Branch Admin Dashboard"],
        ["Stock Adjustment Audit", "Record physical count variance with reason (Breakage, Discrepancy, Return to Vendor).", "Super Admin / Branch Admin"]
    ]
    create_table_card(s34, Inches(0.8), Inches(1.4), Inches(11.7), Inches(5.2), inv_headers, inv_rows, [Inches(2.5), Inches(6.4), Inches(2.8)])
    add_footer(s34, 34, 52)

    # SLIDE 35: Quality Control and Delivery
    s35 = prs.slides.add_slide(blank_layout)
    set_bg(s35, C_OFFWHITE)
    add_header(s35, "Module Specification: Quality Control & Vehicle Handover", "SECTION F: CORE WORKSHOP MODULES")
    add_badge(s35, Inches(10.3), Inches(0.65), "QC & HANDOVER", "RECOMMENDED")

    create_card(s35, Inches(0.8), Inches(1.4), Inches(3.7), Inches(5.2), "QUALITY CONTROL (QC)", [
        "Pre-Delivery Protocol: Mandatory digital checklist prior to vehicle release.",
        "Inspector: Workshop Supervisor / Branch Admin.",
        "Key Inspection Checkpoints:",
        "  ✔ Initial Customer Complaints Verified",
        "  ✔ Engine Oil Level & Viscosity Checked",
        "  ✔ Front & Rear Brake Bite & Fluid Level",
        "  ✔ Chain Tension & Lubrication Inspected",
        "  ✔ Tyre Pressure & Tread Depth Verified",
        "  ✔ Road Test Completed (Signed off)"
    ])

    create_card(s35, Inches(4.8), Inches(1.4), Inches(3.7), Inches(5.2), "VEHICLE HANDOVER", [
        "Custody Items Returned: Tool kit, documents, and customer belongings verified.",
        "Replaced Old Parts Policy: Defective parts bagged and presented to customer.",
        "Final Kilometer Capture: Closing odometer recorded post-road test.",
        "Customer Inspection: Rider inspects vehicle and confirms complaint resolution.",
        "Gate Pass Generation: Digital gate pass authorized once invoice payment is settled."
    ])

    create_card(s35, Inches(8.8), Inches(1.4), Inches(3.7), Inches(5.2), "DELIVERY STATUS CLOSURE", [
        "1. Job Card status updated to 'DELIVERED' (FR-16 optional confirmation).",
        "2. Exact delivery timestamp recorded in audit log.",
        "3. Complete maintenance record committed to vehicle lifetime service log.",
        "4. Customer Relationship Trigger: Automated satisfaction SMS/WhatsApp sent after 48 hours."
    ])
    add_footer(s35, 35, 52)

    # SLIDE 36: Invoice Management
    s36 = prs.slides.add_slide(blank_layout)
    set_bg(s36, C_OFFWHITE)
    add_header(s36, "Module Specification: Billing & PDF Invoice Generation", "SECTION F: CORE WORKSHOP MODULES")
    add_badge(s36, Inches(10.3), Inches(0.65), "BILLING & PDF", "CONFIRMED")

    create_card(s36, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.2), "CONFIRMED INVOICE SPECIFICATION (FR-19 to FR-22)", [
        "1. Generation Authority (FR-19): Any of the 3 roles (Super Admin, Branch Admin, Employee) can generate invoices.",
        "2. Core Invoice Elements (FR-20):",
        "   • Business Name & Branch Details (Address, Phone, GSTIN)",
        "   • Invoice Number (e.g. INV-AMB-2026-0842) & Invoice Date",
        "   • Customer Details (Name, Phone, Address)",
        "   • Bike Details (Reg No, Brand, Model, Current KMs)",
        "   • Itemized Services with Labor Charges",
        "   • Itemized Spare Parts with Unit Prices & Quantities",
        "   • Applicable Tax / GST Calculation",
        "   • Advance Amount Deducted Offset",
        "   • Net Balance Due & Grand Total Amount",
        "3. PDF Download Only (FR-21): Download strictly as PDF (No Excel export allowed to prevent billing tampering).",
        "4. Mobile Support (FR-22): Direct sharing and printing from smartphone."
    ], title_color=C_GREEN)

    create_card(s36, Inches(6.9), Inches(1.4), Inches(5.6), Inches(5.2), "SAMPLE INVOICE CALCULATION & LAYOUT", [
        "SAMPLE WORKSHOP INVOICE STRUCTURE:",
        "--------------------------------------------------",
        "LABOR CHARGES:",
        "  • General Periodic Service (50-point)  : INR   650.00",
        "  • Front Brake Caliper Overhaul         : INR   250.00",
        "SPARE PARTS ISSUED:",
        "  • Motul 7100 10W50 Engine Oil (1.5L)   : INR 1,450.00",
        "  • OEM Oil Filter Element               : INR   180.00",
        "  • Front Brake Pad Set                  : INR   480.00",
        "--------------------------------------------------",
        "SUBTOTAL                                 : INR 3,010.00",
        "TAX / GST (Configurable 18%)             : INR   541.80",
        "GROSS TOTAL AMOUNT                       : INR 3,551.80",
        "LESS: ADVANCE DEPOSIT PAID (Intake)      : INR   500.00",
        "NET BALANCE PAYABLE AT DELIVERY          : INR 3,051.80",
        "--------------------------------------------------"
    ], title_color=C_CHARCOAL)
    add_footer(s36, 36, 52)

    # SLIDE 37: Payment Management
    s37 = prs.slides.add_slide(blank_layout)
    set_bg(s37, C_OFFWHITE)
    add_header(s37, "Module Specification: Payments & Ledger Accounting", "SECTION F: CORE WORKSHOP MODULES")
    add_badge(s37, Inches(10.3), Inches(0.65), "PAYMENTS", "RECOMMENDED")

    pmt_headers = ["Payment Stage", "Collection Workflow & Business Rules", "Supported Modes", "Audit & Ledger Action"]
    pmt_rows = [
        ["Advance Deposit", "Collected at vehicle check-in to secure repair authorization.", "Cash, UPI (GPay/PhonePe)", "Recorded on Job Card; printed on intake receipt."],
        ["Delivery Settlement", "Balance settled at pickup prior to vehicle release.", "UPI, Credit/Debit Card, Cash", "Invoice status changes to 'PAID'; receipt issued."],
        ["Partial Payment", "Customer pays portion of balance; leaves outstanding balance.", "Multi-Mode Split", "Remaining balance posted to customer ledger."],
        ["Refund / Adjustment", "Job cancelled or work reduced after advance collection.", "Cash / Original UPI Ref", "Requires Branch Admin authorization & reason log."]
    ]
    create_table_card(s37, Inches(0.8), Inches(1.4), Inches(11.7), Inches(3.2), pmt_headers, pmt_rows, [Inches(2.2), Inches(4.3), Inches(2.4), Inches(2.8)])

    create_card(s37, Inches(0.8), Inches(4.8), Inches(11.7), Inches(1.8), "FINANCIAL RECONCILIATION & CASH DRAWER RULES", [
        "1. Daily Branch Cash Drawer: Shift-end cash tally comparing physical cash against system recorded cash collections.",
        "2. Digital UPI Reconciliation: Transaction reference numbers logged for bank statement matching.",
        "3. Outstanding Balance Tracking: Automated report of customers with pending balances across all branches.",
        "4. Tamper Protection: Payment records cannot be deleted once finalized by employee."
    ])
    add_footer(s37, 37, 52)

    # SLIDE 38: Expense and Profit Management
    s38 = prs.slides.add_slide(blank_layout)
    set_bg(s38, C_OFFWHITE)
    add_header(s38, "Module Specification: Expense Capture & P&L Calculation", "SECTION F: CORE WORKSHOP MODULES")
    add_badge(s38, Inches(10.3), Inches(0.65), "FINANCE ENGINE", "RECOMMENDED")

    create_card(s38, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.2), "PROFIT CALCULATION FORMULAS (OPEN QUESTION Q1)", [
        "CLIENT CLARIFICATION REQUIRED ON FORMULA:",
        "",
        "OPTION A: GROSS SERVICE PROFIT (Simpler)",
        "  • Gross Profit = Total Billed Revenue - Parts Purchase Cost",
        "  • Best if client does not want to enter daily workshop overheads.",
        "",
        "OPTION B: COMPREHENSIVE NET PROFIT (Recommended)",
        "  • Revenue = Labor Charges + Spare Parts Billed (Excl. Tax)",
        "  • Direct Cost = Spare Parts Wholesale Cost Price",
        "  • Operating Expenses = Rent, Utilities, Mechanic Wages, Consumables",
        "  • Net Workshop Profit = Revenue - Direct Cost - Operating Expenses",
        "",
        "Arivom Technologies recommends Option B for complete financial control."
    ])

    create_card(s38, Inches(6.9), Inches(1.4), Inches(5.6), Inches(5.2), "OPERATING EXPENSE TRACKING MODULE", [
        "Captures Daily Workshop Overhead Expenses:",
        "  • Rent & Property Lease Payments",
        "  • Electricity & Workshop Utility Bills",
        "  • Workshop Consumables (Degreaser, Cotton Waste, WD-40)",
        "  • Equipment Maintenance & Tool Calibration",
        "  • Staff Refreshments & Tea Expenses",
        "  • Local Vendor Payables",
        "",
        "Expense Attributes: Date, Category, Amount, Payee, Receipt Upload.",
        "Security Rule: Branch Admins enter branch expenses; Employees have zero access."
    ])
    add_footer(s38, 38, 52)

    # SLIDE 39: Customer Communication
    s39 = prs.slides.add_slide(blank_layout)
    set_bg(s39, C_OFFWHITE)
    add_header(s39, "Module Specification: Customer Communication Engine", "SECTION F: CORE WORKSHOP MODULES")
    add_badge(s39, Inches(10.3), Inches(0.65), "NOTIFICATIONS", "RECOMMENDED / OPTIONAL")

    comm_headers = ["Service Milestone Event", "Notification Channel", "Message Content Template", "Commercial Status"]
    comm_rows = [
        ["Vehicle Check-in", "SMS / WhatsApp", "Hi {Name}, your {Bike} is received at Nitro Racing {Branch}. Job Card: #{JC_No}. Est Delivery: {Time}.", "RECOMMENDED (Pending Gateway)"],
        ["Estimate Ready", "WhatsApp Link", "Hi {Name}, inspection estimate of Rs.{Amount} is ready for #{JC_No}. Please click link to approve: {URL}", "RECOMMENDED (Pending Gateway)"],
        ["Work In Progress", "SMS / WhatsApp", "Work started on your {Bike} by technician {Mechanic}. We will keep you updated.", "OPTIONAL"],
        ["Service Completed", "SMS / WhatsApp", "Good news! Your {Bike} is serviced and passed final QC. Invoice: Rs.{Total}. Ready for pickup!", "RECOMMENDED (Pending Gateway)"],
        ["Invoice PDF Link", "Email & WhatsApp", "Official PDF Invoice attached for your visit at Nitro Racing {Branch}. Thank you for riding with us!", "CONFIRMED (Email) / REC (WA)"],
        ["Next Service Due", "SMS / WhatsApp", "Hi {Name}, your {Bike} is due for regular maintenance. Book your slot today at Nitro Racing: {URL}", "OPTIONAL (Phase 2)"]
    ]
    create_table_card(s39, Inches(0.8), Inches(1.4), Inches(11.7), Inches(5.2), comm_headers, comm_rows, [Inches(2.0), Inches(2.0), Inches(5.2), Inches(2.5)])
    add_footer(s39, 39, 52)
    print("Section F (Slides 26-39) compiled.")
