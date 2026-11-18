import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(20, 13), dpi=300)
ax.set_facecolor('#17191D')
fig.patch.set_facecolor('#17191D')

plt.text(0.5, 0.97, "NITRO RACING - RELATIONAL DATABASE SCHEMA (ERD)", color="#FFFFFF", fontsize=20, fontweight='bold', ha='center', fontfamily='sans-serif')
plt.text(0.5, 0.94, "Multi-Tenant Architecture with Branch-Level Data Segregation & Foreign Key Integrity", color="#F47721", fontsize=11, ha='center', fontfamily='sans-serif')

def draw_table(x, y, w, h, table_name, pk_list, fk_list, attr_list, header_bg="#242A31", border="#F47721"):
    rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.01,rounding_size=0.015",
                                  facecolor="#1E232A", edgecolor=border, linewidth=1.5)
    ax.add_patch(rect)
    
    # Header box
    header_h = 0.035
    header_rect = patches.FancyBboxPatch((x, y + h - header_h), w, header_h, boxstyle="round,pad=0.01,rounding_size=0.01",
                                         facecolor=header_bg, edgecolor=border, linewidth=1)
    ax.add_patch(header_rect)
    plt.text(x + w/2, y + h - header_h/2, table_name, color="#FFFFFF", fontsize=9, fontweight='bold', ha='center', va='center', fontfamily='sans-serif')
    
    # Content
    curr_y = y + h - header_h - 0.015
    line_spacing = 0.018
    for pk in pk_list:
        plt.text(x + 0.01, curr_y, f"PK  {pk}", color="#F47721", fontsize=7.5, fontweight='bold', va='center', fontfamily='monospace')
        curr_y -= line_spacing
    for fk in fk_list:
        plt.text(x + 0.01, curr_y, f"FK  {fk}", color="#E9A23B", fontsize=7.5, fontweight='bold', va='center', fontfamily='monospace')
        curr_y -= line_spacing
    for attr in attr_list:
        plt.text(x + 0.01, curr_y, f" •  {attr}", color="#D6D9DD", fontsize=7, va='center', fontfamily='monospace')
        curr_y -= line_spacing

# Column 1: Core Tenant & Users
draw_table(0.03, 0.68, 0.16, 0.22, "branches (Stores)", ["branch_id"], [], ["name", "code", "address", "phone", "email", "gstin", "is_active", "created_at"], border="#F47721")
draw_table(0.03, 0.40, 0.16, 0.24, "users (Staff & Admins)", ["user_id"], ["branch_id (nullable)"], ["role_code", "full_name", "email", "password_hash", "phone", "is_active", "last_login", "created_at"], border="#F47721")
draw_table(0.03, 0.16, 0.16, 0.20, "audit_logs", ["log_id"], ["user_id", "branch_id"], ["action_type", "entity_name", "entity_id", "ip_address", "timestamp"], border="#7C8691")

# Column 2: Customers, Bikes, Inquiries & Appointments
draw_table(0.22, 0.70, 0.16, 0.20, "customers", ["customer_id"], ["created_branch_id"], ["full_name", "primary_phone", "alternate_phone", "email", "address", "created_at"], border="#229B62")
draw_table(0.22, 0.44, 0.16, 0.22, "customer_bikes", ["bike_id"], ["customer_id"], ["reg_number", "brand", "model", "bike_name", "manufacture_year", "current_kms", "created_at"], border="#229B62")
draw_table(0.22, 0.20, 0.16, 0.20, "service_appointments", ["appointment_id"], ["branch_id", "customer_id", "bike_id"], ["preferred_date", "preferred_slot", "service_category", "status", "notes"], border="#229B62")
draw_table(0.22, 0.03, 0.16, 0.14, "website_enquiries", ["enquiry_id"], ["target_branch_id"], ["name", "phone", "email", "subject", "message", "status"], border="#7C8691")

# Column 3: Job Cards, Inspection & Status History
draw_table(0.41, 0.58, 0.18, 0.32, "job_cards", ["job_card_id"], ["branch_id", "customer_id", "bike_id", "mechanic_id", "created_by_user_id"], 
           ["job_card_number", "entry_datetime", "purpose_of_entry", "current_kms", "advance_amount", "status", "customer_complaint", "diagnosis", "estimated_completion", "delivered_at"], border="#F47721")
draw_table(0.41, 0.33, 0.18, 0.21, "vehicle_inspections", ["inspection_id"], ["job_card_id", "inspected_by_user_id"], ["fuel_level", "scratch_damage_notes", "tool_kit_present", "documents_held", "checklist_json", "photo_urls_json"], border="#D6D9DD")
draw_table(0.41, 0.11, 0.18, 0.18, "job_status_history", ["history_id"], ["job_card_id", "changed_by_user_id"], ["old_status", "new_status", "notes", "changed_at"], border="#D6D9DD")

# Column 4: Services, Parts & Estimates
draw_table(0.62, 0.72, 0.17, 0.18, "service_catalogue", ["service_id"], [], ["service_name", "category", "base_labour_price", "description", "is_active"], border="#D6D9DD")
draw_table(0.62, 0.49, 0.17, 0.19, "job_card_services", ["job_service_id"], ["job_card_id", "service_id"], ["custom_labour_amount", "notes", "completion_status"], border="#D6D9DD")
draw_table(0.62, 0.26, 0.17, 0.19, "estimates", ["estimate_id"], ["job_card_id", "created_by_user_id"], ["estimate_number", "labour_total", "parts_total", "tax_amount", "grand_total", "approval_status"], border="#D6D9DD")
draw_table(0.62, 0.05, 0.17, 0.18, "job_card_parts", ["job_part_id"], ["job_card_id", "part_id"], ["quantity", "unit_price", "total_price", "issued_at"], border="#D6D9DD")

# Column 5: Inventory, Invoicing & Payments
draw_table(0.81, 0.72, 0.16, 0.20, "spare_parts_inventory", ["part_id"], ["branch_id", "supplier_id"], ["part_code", "part_name", "category", "purchase_price", "selling_price", "stock_qty", "min_stock_alert"], border="#229B62")
draw_table(0.81, 0.47, 0.16, 0.21, "invoices", ["invoice_id"], ["job_card_id", "branch_id", "customer_id", "created_by_user_id"], ["invoice_number", "invoice_date", "labour_amount", "parts_amount", "tax_amount", "advance_adjusted", "total_due", "balance_due", "pdf_path"], border="#F47721")
draw_table(0.81, 0.24, 0.16, 0.19, "payments", ["payment_id"], ["invoice_id", "job_card_id", "received_by_user_id"], ["payment_type", "amount_paid", "payment_mode", "transaction_ref", "payment_datetime"], border="#229B62")
draw_table(0.81, 0.04, 0.16, 0.17, "expenses", ["expense_id"], ["branch_id", "entered_by_user_id"], ["category", "amount", "expense_date", "vendor_payee", "description"], border="#7C8691")

# Connectors (Key Foreign Key Relationships)
def connect(x1, y1, x2, y2, color="#F47721"):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="->", color=color, lw=1.2, ls='--'))

# Branch -> Users
connect(0.11, 0.68, 0.11, 0.64)
# Branch -> Job Cards
connect(0.19, 0.79, 0.41, 0.74)
# Customers -> Bikes
connect(0.30, 0.70, 0.30, 0.66)
# Bikes -> Job Cards
connect(0.38, 0.55, 0.41, 0.65)
# Job Cards -> Inspection
connect(0.50, 0.58, 0.50, 0.54)
# Job Cards -> Status History
connect(0.50, 0.33, 0.50, 0.29)
# Job Cards -> Services
connect(0.59, 0.70, 0.62, 0.59)
# Job Cards -> Invoices
connect(0.59, 0.74, 0.81, 0.57)
# Invoices -> Payments
connect(0.89, 0.47, 0.89, 0.43)

plt.text(0.5, 0.015, "Entity Relational Data Model | Fully Normalized 3NF Schema | Nitro Racing Service Platform | Arivom Technologies", color="#7C8691", fontsize=8, ha='center')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
plt.tight_layout()
plt.savefig('Nitro_Racing_ERD.png', bbox_inches='tight', facecolor='#17191D')
plt.close()
print("ERD Diagram generated successfully.")
