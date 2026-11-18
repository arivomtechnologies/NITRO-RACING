from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from common_deck import (
    C_GRAPHITE, C_CHARCOAL, C_ORANGE, C_SILVER, C_OFFWHITE, C_WHITE,
    C_GREEN, C_GOLD, C_MUTED, C_CARD_BG, C_DARK_CARD,
    set_bg, add_header, add_footer, add_badge, create_card, create_table_card
)

def build_slides_20_to_25(prs, blank_layout):
    # SLIDE 20: User Roles (Dark)
    s20 = prs.slides.add_slide(blank_layout)
    set_bg(s20, C_GRAPHITE)
    add_header(s20, "User Roles & Operational Responsibilities", "SECTION D: USER HIERARCHY & ACCESS", is_dark=True)
    add_badge(s20, Inches(10.3), Inches(0.65), "RBAC FRAMEWORK", "CONFIRMED")

    create_card(s20, Inches(0.8), Inches(1.4), Inches(3.7), Inches(5.2), "ROLE 1: SUPER ADMIN", [
        "Account Count: 1 Master Account (System Setup).",
        "Target Persona: Nitro Racing Business Owner / General Manager.",
        "Primary Scope: Complete cross-branch authority.",
        "Core Capabilities:",
        "  • Provision, update, and deactivate branches (stores).",
        "  • Create and assign Branch Admins to branches.",
        "  • View all branches' operations and consolidated BI.",
        "  • Global configuration: tax/GST, company profile.",
        "  • Full audit trail and financial reporting access."
    ], is_dark_card=True)

    create_card(s20, Inches(4.8), Inches(1.4), Inches(3.7), Inches(5.2), "ROLE 2: BRANCH ADMIN", [
        "Account Count: Exactly 1 per operational branch.",
        "Target Persona: Branch Workshop Manager / Service Head.",
        "Primary Scope: Strict single-branch boundary.",
        "Core Capabilities:",
        "  • Create, edit, and deactivate branch Employees.",
        "  • Manage daily job cards, estimates, and bay allocation.",
        "  • Oversee branch spare parts inventory & stock reorders.",
        "  • Access branch-level sales, revenue, and profit dashboard.",
        "  • Restricted: Cannot access other branches' data."
    ], is_dark_card=True)

    create_card(s20, Inches(8.8), Inches(1.4), Inches(3.7), Inches(5.2), "ROLE 3: EMPLOYEE / TECH", [
        "Account Count: Many per branch (Scalable workforce).",
        "Target Persona: Service Advisors & Master Mechanics.",
        "Primary Scope: Workshop floor execution.",
        "Core Capabilities:",
        "  • Create digital job cards on mobile smartphones.",
        "  • Update repair progression (Received, WIP, Done).",
        "  • Generate instant PDF customer invoices.",
        "  • Strictly Blocked: No dashboard or financial metrics.",
        "  • Cannot edit/delete store settings or other users."
    ], is_dark_card=True)
    add_footer(s20, 20, 52, is_dark=True)

    # SLIDE 21: Organization Hierarchy
    s21 = prs.slides.add_slide(blank_layout)
    set_bg(s21, C_OFFWHITE)
    add_header(s21, "Organizational Structure & Data Governance Tree", "SECTION D: USER HIERARCHY & ACCESS")
    add_badge(s21, Inches(10.3), Inches(0.65), "TENANCY MODEL", "CONFIRMED")

    create_card(s21, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.2), "HIERARCHICAL GOVERNANCE ARCHITECTURE", [
        "ENTERPRISE ROOT: NITRO RACING HEADQUARTERS",
        "  └── SUPER ADMIN (Global Visibility & Governance)",
        "       ├── BRANCH 1: AMBATTUR BRANCH",
        "       │    ├── Branch Admin (Ambattur Operations Manager)",
        "       │    └── Employees (Advisors, Mechanics, Technicians)",
        "       ├── BRANCH 2: AVADI BRANCH",
        "       │    ├── Branch Admin (Avadi Operations Manager)",
        "       │    └── Employees (Advisors, Mechanics, Technicians)",
        "       └── FUTURE BRANCH N... (Dynamically Provisioned)",
        "",
        "Key Governance Rule: Multi-tenant foreign key separation ensures complete security while enabling unified analytics."
    ])

    create_card(s21, Inches(6.9), Inches(1.4), Inches(5.6), Inches(5.2), "DATA SEPARATION & SECURITY SAFEGUARDS", [
        "1. Dynamic Branch Context: When Branch Admin or Employee logs in, the security context pins their tenant ID to their branch.",
        "2. Database Level Isolation: All queries (Job Cards, Invoices, Customers, Stock) automatically append 'WHERE branch_id = :tenant_id'.",
        "3. Cross-Branch Prevention: A branch admin in Ambattur cannot view, query, or edit Avadi repair orders or customer invoices.",
        "4. Super Admin Aggregation: Super Admin queries bypass branch filter to compute enterprise-wide totals and comparative metrics.",
        "5. Unlimited Branch Scaling: New branches added without code modification or database schema migration (FR-11)."
    ])
    add_footer(s21, 21, 52)

    # SLIDE 22: Role Permission Matrix
    s22 = prs.slides.add_slide(blank_layout)
    set_bg(s22, C_OFFWHITE)
    add_header(s22, "Comprehensive Role-Based Access Control (RBAC) Matrix", "SECTION D: USER HIERARCHY & ACCESS")
    add_badge(s22, Inches(10.3), Inches(0.65), "SECURITY MATRIX", "CONFIRMED")

    perm_headers = ["System Capability / Feature", "Super Admin", "Branch Admin", "Employee", "Baseline Authority"]
    perm_rows = [
        ["Add / Edit / Delete Stores (Branches)", "YES (All)", "NO (Blocked)", "NO (Blocked)", "SOURCE CONFIRMED (Sec 4)"],
        ["View List of Stores", "YES (All)", "NO (Own branch info)", "NO (Blocked)", "SOURCE CONFIRMED (Sec 4)"],
        ["Create / Edit / Delete Branch Admins", "YES (All)", "NO (Blocked)", "NO (Blocked)", "SOURCE CONFIRMED (Sec 4)"],
        ["Create / Edit / Delete Employees", "YES (All)", "YES (Own branch only)", "NO (Blocked)", "SOURCE CONFIRMED (Sec 4)"],
        ["Branch Operations Dashboard", "YES (Any branch drill-down)", "YES (Own branch only)", "NO (BLOCKED FR-26)", "SOURCE CONFIRMED (Sec 4)"],
        ["Consolidated Overall Dashboard", "YES (Cross-branch BI)", "NO (Blocked)", "NO (BLOCKED FR-26)", "SOURCE CONFIRMED (Sec 4)"],
        ["Create & Update Job Cards", "YES (All branches)", "YES (Own branch)", "YES (Own branch)", "SOURCE CONFIRMED (Sec 4)"],
        ["Update Repair Status (Received -> Done)", "YES (All branches)", "YES (Own branch)", "YES (Own branch)", "SOURCE CONFIRMED (Sec 4)"],
        ["Generate PDF Invoice", "YES (All branches)", "YES (Own branch)", "YES (Own branch)", "SOURCE CONFIRMED (Sec 4)"],
        ["Manage Spare Parts Inventory (Proposed)", "YES (All branches)", "YES (Own branch)", "NO (Issue only)", "RECOMMENDED (FR-107)"]
    ]
    create_table_card(s22, Inches(0.8), Inches(1.4), Inches(11.7), Inches(5.2), perm_headers, perm_rows, [Inches(3.3), Inches(2.1), Inches(2.1), Inches(2.0), Inches(2.2)])
    add_footer(s22, 22, 52)

    # SLIDE 23: Authentication and User Lifecycle
    s23 = prs.slides.add_slide(blank_layout)
    set_bg(s23, C_OFFWHITE)
    add_header(s23, "Authentication Engine & User Lifecycle Governance", "SECTION D: USER HIERARCHY & ACCESS")
    add_badge(s23, Inches(10.3), Inches(0.65), "AUTH LIFECYCLE", "CONFIRMED")

    auth_headers = ["Auth Lifecycle Stage", "Functional Requirement & Security Protocol", "Technical Implementation"]
    auth_rows = [
        ["Login & Credentials (FR-01)", "Login via email/username and secure password. Public registration is strictly disabled.", "Spring Security + BCrypt password hashing (12 rounds)"],
        ["Forgot Password (FR-02)", "Self-service password recovery. Generates time-limited cryptographic reset token sent via email.", "SMTP Gateway dispatch with 15-minute token expiry"],
        ["24-Hour Session (FR-03)", "Session remains valid for at least 24 hours (1 day) so workshop mechanics don't re-login mid-shift.", "JWT Access Token (24hr expiry) stored in HttpOnly cookie"],
        ["Remember Me (FR-04)", "Login screen supports credentials auto-fill and 'Remember Me' for fast smartphone access.", "Browser credential management API & persistent refresh token"],
        ["Personalized Greeting (FR-05)", "Greeting dynamically reflects identity and branch: 'Hi Super Admin', 'Hi Hari - Ambattur (Employee)'.", "JWT payload claims unpacked upon initial portal hydration"],
        ["Account Deactivation (FR-06)", "Admins can immediately suspend or deactivate employee accounts; blocks further token refresh.", "Database 'is_active' boolean checked on every API request"]
    ]
    create_table_card(s23, Inches(0.8), Inches(1.4), Inches(11.7), Inches(5.2), auth_headers, auth_rows, [Inches(2.5), Inches(5.7), Inches(3.5)])
    add_footer(s23, 23, 52)

    # SLIDE 24: Complete Management Portal Navigation (Dark)
    s24 = prs.slides.add_slide(blank_layout)
    set_bg(s24, C_GRAPHITE)
    add_header(s24, "Management Portal: Complete Navigation Architecture", "SECTION E: MANAGEMENT PORTAL MENUS", is_dark=True)
    add_badge(s24, Inches(10.3), Inches(0.65), "PORTAL SITEMAP", "CONFIRMED")

    create_card(s24, Inches(0.8), Inches(1.4), Inches(3.7), Inches(5.2), "DASHBOARD & OPERATIONS", [
        "1. DASHBOARD",
        "  • Executive Overview (FR-24)",
        "  • Daily Workshop Operations",
        "  • Branch Performance Comparison",
        "2. WORKSHOP OPERATIONS",
        "  • Service Appointments (FR-103)",
        "  • Website Lead Enquiries",
        "  • Vehicle Check-in (FR-104)",
        "  • Job Cards: Received, WIP, Done, Delivered",
        "  • Quality Control (QC) Checklist"
    ], is_dark_card=True)

    create_card(s24, Inches(4.8), Inches(1.4), Inches(3.7), Inches(5.2), "MASTERS & INVENTORY", [
        "3. CUSTOMERS & BIKES",
        "  • Customer Directory & Profiles",
        "  • Motorcycle Master & History",
        "4. SERVICE CATALOGUE",
        "  • Service Menu & Packages",
        "  • Standard Labor Charges",
        "5. MECHANIC WORKFORCE",
        "  • Technician Directory & Workload",
        "6. SPARE PARTS & INVENTORY",
        "  • Parts Master & Stock Inward",
        "  • Stock Adjustment & Low Stock Alerts"
    ], is_dark_card=True)

    create_card(s24, Inches(8.8), Inches(1.4), Inches(3.7), Inches(5.2), "FINANCE, BI & ADMIN", [
        "7. ESTIMATES & QUOTATIONS",
        "  • Create Estimate & Approval Gate",
        "8. BILLING & INVOICES",
        "  • Generate Invoice (PDF Only)",
        "9. PAYMENTS & EXPENSES",
        "  • Multi-mode Payment Ledger",
        "  • Operating Expenses & Net P&L",
        "10. REPORTS & ANALYTICS",
        "  • Sales, Revenue & Part Output",
        "11. ADMINISTRATION & SETTINGS",
        "  • Branches, Users, Audit Logs"
    ], is_dark_card=True)
    add_footer(s24, 24, 52, is_dark=True)

    # SLIDE 25: Role-Specific Menu Hierarchy
    s25 = prs.slides.add_slide(blank_layout)
    set_bg(s25, C_OFFWHITE)
    add_header(s25, "Role-Specific Sidebar Visibility & UI Adaptation", "SECTION E: MANAGEMENT PORTAL MENUS")
    add_badge(s25, Inches(10.3), Inches(0.65), "UI ADAPTATION", "CONFIRMED")

    create_card(s25, Inches(0.8), Inches(1.4), Inches(3.7), Inches(5.2), "SUPER ADMIN SIDEBAR", [
        "UNRESTRICTED ENTERPRISE VISIBILITY:",
        "  ✔ Multi-Branch Consolidated Dashboard",
        "  ✔ Store Management (Add/Edit/Delete)",
        "  ✔ Branch Admin & Employee User Master",
        "  ✔ Enterprise Job Card & Invoice Archive",
        "  ✔ Master Spare Parts & Supplier Catalog",
        "  ✔ Cross-Branch P&L and Sales Analytics",
        "  ✔ Global Tax, GST, & Audit Trail Logs",
        "  ✔ Website CMS & Lead Inquiries"
    ], title_color=C_CHARCOAL)

    create_card(s25, Inches(4.8), Inches(1.4), Inches(3.7), Inches(5.2), "BRANCH ADMIN SIDEBAR", [
        "ISOLATED BRANCH OPERATIONS:",
        "  ✔ Own Branch Dashboard (FR-25)",
        "  ✔ Branch Employee Management (FR-13)",
        "  ✔ Branch Job Cards & Inspection Checklists",
        "  ✔ Branch Estimate Creation & Approvals",
        "  ✔ Branch Spare Parts Stock & Inward",
        "  ✔ PDF Invoicing & Payment Collection",
        "  ✔ Branch Operating Expenses Entry",
        "  ✖ BLOCKED: Cross-branch views & stores"
    ], title_color=C_ORANGE)

    create_card(s25, Inches(8.8), Inches(1.4), Inches(3.7), Inches(5.2), "EMPLOYEE / TECH SIDEBAR", [
        "MOBILE STREAMLINED OPERATIONAL UI:",
        "  ✔ Active Job Cards (Received, WIP, Done)",
        "  ✔ New Job Card Quick Intake (< 60s)",
        "  ✔ Status Progression Update Engine",
        "  ✔ Issue Spare Parts to Active Job Card",
        "  ✔ Generate Customer PDF Invoice (FR-19)",
        "  ✖ BLOCKED: All Dashboards (FR-26)",
        "  ✖ BLOCKED: User management & branch config",
        "  ✖ BLOCKED: Expenses & profit analytics"
    ], title_color=C_GREEN)
    add_footer(s25, 25, 52)
    print("Section D & E (Slides 20-25) compiled.")
