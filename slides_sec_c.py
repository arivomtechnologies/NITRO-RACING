from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from common_deck import (
    C_GRAPHITE, C_CHARCOAL, C_ORANGE, C_SILVER, C_OFFWHITE, C_WHITE,
    C_GREEN, C_GOLD, C_MUTED, C_CARD_BG, C_DARK_CARD,
    set_bg, add_header, add_footer, add_badge, create_card, create_table_card
)

def build_slides_10_to_19(prs, blank_layout):
    # SLIDE 10: Public Website Overview (Dark)
    s10 = prs.slides.add_slide(blank_layout)
    set_bg(s10, C_GRAPHITE)
    add_header(s10, "Public Website: Strategic Brand Portal Overview", "SECTION C: PUBLIC WEBSITE REQUIREMENTS", is_dark=True)
    add_badge(s10, Inches(10.3), Inches(0.65), "BRAND SURFACE", "CONFIRMED")

    create_card(s10, Inches(0.8), Inches(1.4), Inches(3.7), Inches(5.2), "PURPOSE & POSITIONING", [
        "Position Nitro Racing as Chennai's premier racing and high-performance two-wheeler service center.",
        "Showcase workshop capabilities, diagnostic equipment, and skilled mechanic workforce.",
        "Build biker trust through authentic photos, genuine customer testimonials, and clear pricing.",
        "Serve as the primary digital acquisition channel for inbound service leads and bookings."
    ], is_dark_card=True)

    create_card(s10, Inches(4.8), Inches(1.4), Inches(3.7), Inches(5.2), "CORE CUSTOMER JOURNEYS", [
        "1. Service Discovery: Browse service categories, detailed inclusions, and transparent labor charges.",
        "2. Workshop Locator: Find nearest branch (Ambattur, Avadi) with direct phone and GPS directions.",
        "3. Service Appointment: Submit motorcycle details and preferred date/time slot.",
        "4. General Enquiry: Send specialized customization or repair questions directly to the service desk."
    ], is_dark_card=True)

    create_card(s10, Inches(8.8), Inches(1.4), Inches(3.7), Inches(5.2), "ARCHITECTURAL INTEGRATION", [
        "Angular 18+ Server-Side Rendered (SSR) for blazing performance (< 2s) and high SEO ranking.",
        "Submissions automatically persist into PostgreSQL database and dispatch SMTP email alerts.",
        "Staff Login CTA in header routes directly to the Management Portal.",
        "Strict Policy: No public customer self-registration to maintain clean system integrity (FR-01)."
    ], is_dark_card=True)
    add_footer(s10, 10, 52, is_dark=True)

    # SLIDE 11: Public Website Navigation Hierarchy (Sitemap)
    s11 = prs.slides.add_slide(blank_layout)
    set_bg(s11, C_OFFWHITE)
    add_header(s11, "Public Website Sitemap & Navigation Hierarchy", "SECTION C: PUBLIC WEBSITE REQUIREMENTS")
    add_badge(s11, Inches(10.3), Inches(0.65), "SITEMAP TREE", "CONFIRMED")

    create_card(s11, Inches(0.8), Inches(1.4), Inches(2.7), Inches(5.2), "MAIN HEADER NAV", [
        "HOME (Landing Page)",
        "ABOUT US (Workshop Heritage)",
        "SERVICES (Interactive Dropdown)",
        "OUR BRANCHES (Locations)",
        "GALLERY (Workshop Photos)",
        "TESTIMONIALS (Reviews)",
        "CONTACT US (Enquiries)",
        "CTA 1: Book a Service",
        "CTA 2: Staff Login"
    ])

    create_card(s11, Inches(3.8), Inches(1.4), Inches(4.3), Inches(5.2), "SERVICES BREAKDOWN (PROPOSED)", [
        "1. General Periodic Service (50-point check)",
        "2. Engine Diagnostics & Overhaul",
        "3. Engine Oil & Fluid Replacement",
        "4. Brake Overhaul & ABS Calibration",
        "5. Clutch & Transmission Tuning",
        "6. Chain, Sprocket & Drive Assembly",
        "7. Electrical, Battery & Wiring Diagnostics",
        "8. Wheel Balancing & Tyre Replacement",
        "9. Suspension Tuning & Fork Overhaul",
        "10. Performance Accessories & Exhausts",
        "11. Specialized Customization & Detailing"
    ])

    create_card(s11, Inches(8.4), Inches(1.4), Inches(4.1), Inches(5.2), "BRANCH & ACTION NODES", [
        "OUR BRANCHES:",
        "  • Ambattur Branch (Industrial Estate)",
        "  • Avadi Branch (Main Road)",
        "  • All Branches Locator Map",
        "HEADER ACTION WORKFLOWS:",
        "  • 'Book a Service': 3-step appointment modal",
        "  • 'Staff Login': Secure redirect to /admin",
        "FOOTER LINKS:",
        "  • Privacy Policy, Terms & Conditions",
        "  • Quick Links, Working Hours, Social Media"
    ])
    add_footer(s11, 11, 52)

    # SLIDE 12: Home Page Design & Sections
    s12 = prs.slides.add_slide(blank_layout)
    set_bg(s12, C_OFFWHITE)
    add_header(s12, "Homepage Architecture & Conversion Blueprint", "SECTION C: PUBLIC WEBSITE REQUIREMENTS")
    add_badge(s12, Inches(10.3), Inches(0.65), "PAGE WIREFRAME", "CONFIRMED")

    hp_headers = ["Section Order", "UI Component Name", "Content & Functional Elements", "Conversion Objective"]
    hp_rows = [
        ["Section 1", "Hero Banner & CTA", "High-impact motorcycle visual, 'Precision Two-Wheeler Care', Dual CTAs ('Book Service', 'Find Branch')", "Immediate value proposition"],
        ["Section 2", "Trust Credentials", "Metrics strip: '15,000+ Bikes Serviced', '98% On-Time Delivery', 'Certified Technicians'", "Establish workshop authority"],
        ["Section 3", "Service Showcase", "Interactive grid of top 6 services with brief descriptions, pricing indicators, and 'Learn More'", "Encourage service exploration"],
        ["Section 4", "Workshop Process", "4-step graphic: 1. Digital Intake -> 2. Transparent Estimate -> 3. Expert Repair -> 4. Final QC", "Address repair fear & distrust"],
        ["Section 5", "Branch Quick-Cards", "Ambattur & Avadi cards with phone number, current bay status, and direct Google Maps link", "Drive local walk-in traffic"],
        ["Section 6", "Customer Reviews", "Verified customer testimonials carousel with star ratings and bike models serviced", "Social proof and validation"],
        ["Section 7", "Lead Generation CTA", "Banner: 'Is Your Motorcycle Due for Service?' with quick phone number input and callback CTA", "Capture high-intent leads"]
    ]
    create_table_card(s12, Inches(0.8), Inches(1.4), Inches(11.7), Inches(5.2), hp_headers, hp_rows, [Inches(1.5), Inches(2.3), Inches(5.5), Inches(2.4)])
    add_footer(s12, 12, 52)

    # SLIDE 13: About Us Page
    s13 = prs.slides.add_slide(blank_layout)
    set_bg(s13, C_OFFWHITE)
    add_header(s13, "About Us: Heritage, Facilities & Team", "SECTION C: PUBLIC WEBSITE REQUIREMENTS")
    add_badge(s13, Inches(10.3), Inches(0.65), "BRAND STORY", "CONFIRMED")

    create_card(s13, Inches(0.8), Inches(1.4), Inches(3.7), Inches(5.2), "HERITAGE & VISION", [
        "Brand Background: Founded by motorcycle enthusiasts passionate about track and street tuning.",
        "Mission: Deliver racing-grade technical precision to everyday commuters and superbike owners.",
        "Vision: Become Tamil Nadu's most trusted, digitally-advanced multi-branch motorcycle garage.",
        "Values: Absolute honesty, genuine OEM spare parts, zero hidden labor charges."
    ])

    create_card(s13, Inches(4.8), Inches(1.4), Inches(3.7), Inches(5.2), "WORKSHOP INFRASTRUCTURE", [
        "Hydraulic Repair Bays: Dedicated motorcycle lifts preventing frame strain and allowing 360 inspection.",
        "Diagnostic Tools: OBD scanners for modern fuel-injected and electronic ECU motorcycles.",
        "Precision Tooling: Calibrated torque wrenches, ultrasonic parts cleaner, pneumatic tools.",
        "Spacious Customer Lounge: Air-conditioned waiting lounge with viewing window into service bays."
    ])

    create_card(s13, Inches(8.8), Inches(1.4), Inches(3.7), Inches(5.2), "CERTIFIED TECHNICIANS", [
        "Master Mechanics: Over 10+ years specialized experience in Royal Enfield, Yamaha, KTM, Honda.",
        "Continuous Training: Bi-monthly technical refreshers on BS6 electronics and EV powertrains.",
        "Standard Operating Procedures: Strict adherence to torque specs and manufacturer repair manuals.",
        "Quality Accountability: Each mechanic signs off on their specific job card tasks."
    ])
    add_footer(s13, 13, 52)

    # SLIDE 14: Services Pages & Catalogue
    s14 = prs.slides.add_slide(blank_layout)
    set_bg(s14, C_OFFWHITE)
    add_header(s14, "Services Architecture & Dynamic Catalog", "SECTION C: PUBLIC WEBSITE REQUIREMENTS")
    add_badge(s14, Inches(10.3), Inches(0.65), "SERVICE SPEC", "RECOMMENDED")

    srv_headers = ["Catalogue Attribute", "Data Specification & Content Structure", "Management Portal Control"]
    srv_rows = [
        ["Service Name & Slug", "Unique title (e.g., 'Complete Engine De-carbonization') and URL slug", "Editable via Super Admin / Portal CMS"],
        ["Category Mapping", "Mapped to 1 of 11 core categories (Engine, Brakes, Electrical, etc.)", "Selectable from Category Master"],
        ["Thumbnail & Banner", "High-resolution workshop image showcasing technicians performing the service", "Media uploader in Portal"],
        ["What's Included", "Bulleted list of inspection, cleaning, adjustments, and replacement points", "Rich text editor in Portal"],
        ["Key Rider Benefits", "Explains why service matters: 'Improved Fuel Economy', 'Smooth Gearshift'", "Custom benefit cards"],
        ["Standard Turnaround", "Estimated workshop duration (e.g., '2 - 3 Hours')", "Displayed as operational badge"],
        ["Base Labor Pricing", "Indicative starting charge with 'Parts Additional' disclosure", "Can be updated or hidden by admin"],
        ["Direct Action CTA", "'Book This Service' button auto-populating service category in booking form", "Automated link generation"]
    ]
    create_table_card(s14, Inches(0.8), Inches(1.4), Inches(11.7), Inches(5.2), srv_headers, srv_rows, [Inches(2.2), Inches(6.5), Inches(3.0)])
    add_footer(s14, 14, 52)

    # SLIDE 15: Branch Listing and Details
    s15 = prs.slides.add_slide(blank_layout)
    set_bg(s15, C_OFFWHITE)
    add_header(s15, "Multi-Branch Directory & Branch Profile Specification", "SECTION C: PUBLIC WEBSITE REQUIREMENTS")
    add_badge(s15, Inches(10.3), Inches(0.65), "MULTI-BRANCH", "CONFIRMED")

    create_card(s15, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.2), "AMBATTUR BRANCH PROFILE (EXAMPLE)", [
        "Branch Title: Nitro Racing – Ambattur Branch",
        "Physical Address: Industrial Estate Road, Ambattur, Chennai - 600058",
        "Direct Contact: +91 98400 XXXXX | ambattur@nitroracing.in",
        "Operating Hours: Monday – Saturday: 8:30 AM – 8:00 PM | Sunday: 9:00 AM – 2:00 PM",
        "Facilities: 6 Hydraulic Bays, Superbike Diagnostic Station, Customer Lounge",
        "Geo-Coordinates: Lat 13.1143° N, Long 80.1548° E (Google Maps Embedded)",
        "Direct CTA: 'Book Ambattur Service' / 'Call Ambattur Workshop'"
    ])

    create_card(s15, Inches(6.9), Inches(1.4), Inches(5.6), Inches(5.2), "AVADI BRANCH PROFILE (EXAMPLE)", [
        "Branch Title: Nitro Racing – Avadi Branch",
        "Physical Address: New Military Road, Avadi, Chennai - 600054",
        "Direct Contact: +91 98401 XXXXX | avadi@nitroracing.in",
        "Operating Hours: Monday – Saturday: 8:30 AM – 8:00 PM | Sunday: Closed",
        "Facilities: 4 Hydraulic Bays, Quick Oil Service Express Bay, Spare Parts Hub",
        "Geo-Coordinates: Lat 13.1186° N, Long 80.1010° E (Google Maps Embedded)",
        "Direct CTA: 'Book Avadi Service' / 'Call Avadi Workshop'"
    ])
    add_footer(s15, 15, 52)

    # SLIDE 16: Gallery and Testimonials
    s16 = prs.slides.add_slide(blank_layout)
    set_bg(s16, C_OFFWHITE)
    add_header(s16, "Visual Gallery & Customer Social Proof", "SECTION C: PUBLIC WEBSITE REQUIREMENTS")
    add_badge(s16, Inches(10.3), Inches(0.65), "SOCIAL PROOF", "CONFIRMED")

    create_card(s16, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.2), "WORKSHOP PHOTO GALLERY", [
        "Objective: Demonstrate clean, highly-organized, and professional garage environment.",
        "Curated Photo Categories:",
        "  1. Workshop Bays & Lifts in Active Operation",
        "  2. Master Technicians Rebuilding Precision Engines",
        "  3. Modern Computerized Diagnostic Scan Tools",
        "  4. Before-and-After Overhauls (Chain, Carburetor, Paint/Detailing)",
        "  5. Premium Superbikes & Custom Builds on the Work Bench",
        "Interactive UI: Responsive lightbox grid with category filters."
    ])

    create_card(s16, Inches(6.9), Inches(1.4), Inches(5.6), Inches(5.2), "CUSTOMER TESTIMONIALS REPOSITORY", [
        "Objective: Reassure first-time riders regarding pricing transparency and quality.",
        "Testimonial Data Attributes:",
        "  • Customer Name & Neighborhood (e.g. 'Karthik R., Ambattur')",
        "  • Motorcycle Model Serviced (e.g. 'Yamaha R15 V4' or 'Classic 350')",
        "  • Star Rating (1 to 5 Stars)",
        "  • Verified Feedback Review Quote",
        "  • Date of Service & Branch Visited",
        "Moderation Governance: Only admin-approved reviews appear publicly (FR-112)."
    ])
    add_footer(s16, 16, 52)

    # SLIDE 17: Contact and Enquiry Workflow
    s17 = prs.slides.add_slide(blank_layout)
    set_bg(s17, C_OFFWHITE)
    add_header(s17, "Contact & Lead Enquiry Workflow", "SECTION C: PUBLIC WEBSITE REQUIREMENTS")
    add_badge(s17, Inches(10.3), Inches(0.65), "LEAD FUNNEL", "CONFIRMED")

    create_card(s17, Inches(0.8), Inches(1.4), Inches(4.5), Inches(5.2), "ENQUIRY FORM CAPTURE", [
        "Input Fields Required:",
        "  • Full Customer Name (Mandatory)",
        "  • Contact Mobile Number (Mandatory, 10-digit validation)",
        "  • Email Address (Optional / Recommended)",
        "  • Preferred Branch (Ambattur / Avadi / No Preference)",
        "  • Bike Brand & Model (e.g. KTM Duke 390)",
        "  • Subject / Nature of Query (Service, Repair, Parts)",
        "  • Detailed Message / Specific Issue Description",
        "Validation: Bot protection via reCAPTCHA v3."
    ])

    create_card(s17, Inches(5.7), Inches(1.4), Inches(6.8), Inches(5.2), "SYSTEM WORKFLOW & NOTIFICATION ENGINE", [
        "Step 1: Submission -> Form validated and submitted asynchronously via REST API.",
        "Step 2: Database Persistence -> Record saved in 'website_enquiries' table with status 'NEW'.",
        "Step 3: Instant Email Dispatch -> Spring Boot SMTP sends formatted email to branch inbox and CCs Super Admin.",
        "Step 4: Customer Acknowledgement -> Instant on-screen confirmation + optional SMS/Email receipt.",
        "Step 5: Admin Dashboard Alert -> Enquiry appears in Management Portal under 'Pending Inquiries'.",
        "Step 6: Staff Follow-up -> Branch staff calls customer within 30 minutes; updates status to 'CONTACTED'.",
        "Step 7: Conversion -> If customer schedules visit, 1-click conversion to Service Appointment."
    ])
    add_footer(s17, 17, 52)

    # SLIDE 18: Book a Service Workflow
    s18 = prs.slides.add_slide(blank_layout)
    set_bg(s18, C_OFFWHITE)
    add_header(s18, "Online Service Booking Workflow & Appointment Gate", "SECTION C: PUBLIC WEBSITE REQUIREMENTS")
    add_badge(s18, Inches(10.3), Inches(0.65), "BOOKING FUNNEL", "RECOMMENDED")

    bk_headers = ["Workflow Phase", "User / System Action", "Data Exchanged", "Operational Governance Rule"]
    bk_rows = [
        ["Phase 1: Request", "Customer inputs bike reg, model, service category, branch, and preferred slot.", "Reg No, Phone, Date, Time, Issues", "Explicitly marked as 'Appointment Request', not instant guaranteed bay."],
        ["Phase 2: Validation", "System checks branch daily bay capacity (e.g. max 15 bikes/day).", "Branch ID, Slot Capacity Counter", "Prevents workshop overcrowding during peak morning hours."],
        ["Phase 3: Review", "Branch Admin reviews request queue on management portal.", "Appointment ID, Customer Phone", "Staff verifies mechanic availability and parts readiness."],
        ["Phase 4: Confirm", "Staff confirms slot or phones customer to offer alternate hour.", "Status -> CONFIRMED", "Automated SMS / Email reminder sent with Google Map link."],
        ["Phase 5: Arrival", "Customer arrives at workshop; staff enters phone number.", "Status -> ARRIVED", "1-Click conversion into official Job Card with zero duplicate data entry."]
    ]
    create_table_card(s18, Inches(0.8), Inches(1.4), Inches(11.7), Inches(5.2), bk_headers, bk_rows, [Inches(2.0), Inches(3.6), Inches(3.1), Inches(3.0)])
    add_footer(s18, 18, 52)

    # SLIDE 19: Public Website Footer & SEO
    s19 = prs.slides.add_slide(blank_layout)
    set_bg(s19, C_OFFWHITE)
    add_header(s19, "Website Footer, Technical SEO & Responsive Design", "SECTION C: PUBLIC WEBSITE REQUIREMENTS")
    add_badge(s19, Inches(10.3), Inches(0.65), "NON-FUNCTIONAL", "CONFIRMED")

    create_card(s19, Inches(0.8), Inches(1.4), Inches(3.7), Inches(5.2), "FOOTER ARCHITECTURE", [
        "Column 1: Brand identity, workshop slogan, registered business address.",
        "Column 2: Quick Links (Home, About Us, Services, Branches, Book Service).",
        "Column 3: Branch Contacts (Ambattur direct phone, Avadi direct phone, central email).",
        "Column 4: Legal & Compliance (Privacy Policy, Terms of Service, Disclaimer).",
        "Copyright Notice: '© 2026 Nitro Racing. Powered by Arivom Technologies.'"
    ])

    create_card(s19, Inches(4.8), Inches(1.4), Inches(3.7), Inches(5.2), "TECHNICAL SEO SPECIFICATION", [
        "Meta Tags: Dynamic page titles, meta descriptions targeting Chennai motorcycle service keywords.",
        "Local SEO Schema: Schema.org 'AutoRepair' JSON-LD markup for Ambattur and Avadi branches.",
        "Performance Targets: Core Web Vitals optimized (LCP < 2.5s, CLS < 0.1, FID < 100ms).",
        "Sitemap & Robots: Auto-generated sitemap.xml and robots.txt indexable by Google Search Console."
    ])

    create_card(s19, Inches(8.8), Inches(1.4), Inches(3.7), Inches(5.2), "MOBILE RESPONSIVENESS", [
        "100% Mobile Responsive: Over 85% of motorcycle owners book services via smartphone.",
        "Touch Targets: Minimum 48px tap targets for buttons, inputs, and branch calling buttons.",
        "Sticky Bottom Bar: Mobile view features persistent 'Call Branch' and 'Book Service' quick actions.",
        "Cross-Browser Validated: Latest Chrome, Safari iOS, Edge, and Firefox."
    ])
    add_footer(s19, 19, 52)
    print("Section C (Slides 10-19) compiled.")
