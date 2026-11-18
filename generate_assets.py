import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

os.makedirs('assets', exist_ok=True)

# 1. Architecture Diagram
fig, ax = plt.subplots(figsize=(16, 10), dpi=300)
ax.set_facecolor('#17191D')
fig.patch.set_facecolor('#17191D')

# Title
plt.text(0.5, 0.95, "NITRO RACING - SYSTEM ARCHITECTURE", color="#FFFFFF", fontsize=20, fontweight='bold', ha='center', va='center', fontfamily='sans-serif')
plt.text(0.5, 0.91, "Multi-Tenant Enterprise Motorcycle Workshop & Service Center Management Platform", color="#F47721", fontsize=11, ha='center', va='center', fontfamily='sans-serif')

def draw_box(x, y, w, h, title, subtitle, color, bg="#242A31", border="#D6D9DD"):
    rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.015,rounding_size=0.02",
                                  facecolor=bg, edgecolor=border, linewidth=1.5)
    ax.add_patch(rect)
    plt.text(x + w/2, y + h*0.65, title, color=color, fontsize=10, fontweight='bold', ha='center', va='center', fontfamily='sans-serif')
    plt.text(x + w/2, y + h*0.35, subtitle, color="#D6D9DD", fontsize=8, ha='center', va='center', fontfamily='sans-serif')

# Client Tier (Left)
draw_box(0.04, 0.68, 0.25, 0.16, "PUBLIC WEB PORTAL", "Angular 18+ (SSR / PWA)\nResponsive Desktop & Mobile", "#FFFFFF", "#242A31", "#F47721")
draw_box(0.04, 0.45, 0.25, 0.16, "MANAGEMENT PORTAL", "Angular 18+ (SPA / Material)\nRole-Based Dashboard & Operations", "#FFFFFF", "#242A31", "#F47721")
draw_box(0.04, 0.22, 0.25, 0.16, "MOBILE WORKSHOP UI", "Optimized Touch UI (PWA)\nFast Job Card & Quick Inspection", "#FFFFFF", "#242A31", "#F47721")

# Users/Actors Callouts
plt.text(0.165, 0.86, "CLIENT & USER ACCESS TIER", color="#F47721", fontsize=12, fontweight='bold', ha='center', va='center')
plt.text(0.165, 0.15, "Actors: Customers | Super Admin | Branch Admin | Employees", color="#D6D9DD", fontsize=9, ha='center', va='center')

# Gateway & Security (Middle-Left)
draw_box(0.35, 0.30, 0.14, 0.48, "API GATEWAY & SEC", "Spring Security\nJWT Auth Filter\nRate Limiting\nCORS / SSL (HTTPS)\nBranch Tenant Context", "#F47721", "#1E232A", "#D6D9DD")

# Backend Services Tier (Middle-Right)
draw_box(0.55, 0.68, 0.20, 0.16, "CORE SERVICE SUITE", "Spring Boot 3 REST APIs\nBranch Isolation Layer\nRole & Permission Engine", "#FFFFFF", "#242A31", "#D6D9DD")
draw_box(0.55, 0.48, 0.20, 0.16, "WORKSHOP OPERATIONS", "Job Card & Inspection Engine\nMechanic Allocation\nStatus Progression State Mach.", "#FFFFFF", "#242A31", "#D6D9DD")
draw_box(0.55, 0.28, 0.20, 0.16, "BILLING & INVENTORY", "JasperReports PDF Engine\nPart Deduction & GST Calculator\nPayment & Ledger Manager", "#FFFFFF", "#242A31", "#D6D9DD")
draw_box(0.55, 0.08, 0.20, 0.16, "COMMUNICATION ENGINE", "JavaMail SMTP Gateway\nSMS / WhatsApp Connector (Opt)\nAsync Event Publisher", "#FFFFFF", "#242A31", "#D6D9DD")

# Data & Storage Tier (Right)
draw_box(0.81, 0.55, 0.16, 0.28, "POSTGRESQL 16", "Multi-Tenant RDBMS\nBranch FK Segregation\nAutomated Daily Backup\nACID Transactional Integrity", "#229B62", "#1E232A", "#229B62")
draw_box(0.81, 0.22, 0.16, 0.28, "STORAGE & ASSETS", "Encrypted Object Store\nInspection Photos\nGenerated PDF Invoices\nWorkshop Documents", "#229B62", "#1E232A", "#229B62")

# Connector lines
def connect_points(p1, p2, color="#F47721", style='-', lw=1.5):
    ax.annotate('', xy=p2, xytext=p1,
                arrowprops=dict(arrowstyle="->", color=color, lw=lw, ls=style))

# Connect Frontend to Gateway
connect_points((0.29, 0.76), (0.35, 0.65))
connect_points((0.29, 0.53), (0.35, 0.54))
connect_points((0.29, 0.30), (0.35, 0.43))

# Connect Gateway to Services
connect_points((0.49, 0.65), (0.55, 0.76))
connect_points((0.49, 0.54), (0.55, 0.56))
connect_points((0.49, 0.43), (0.55, 0.36))
connect_points((0.49, 0.35), (0.55, 0.16))

# Connect Services to DB / Storage
connect_points((0.75, 0.76), (0.81, 0.70))
connect_points((0.75, 0.56), (0.81, 0.65))
connect_points((0.75, 0.36), (0.81, 0.36))
connect_points((0.75, 0.16), (0.81, 0.30))

# Footer
plt.text(0.5, 0.02, "Nitro Racing Automobile Service Center Management System | Architecture Specification v1.0 | Arivom Technologies", color="#7C8691", fontsize=8, ha='center', va='center')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
plt.tight_layout()
plt.savefig('Nitro_Racing_Architecture.png', bbox_inches='tight', facecolor='#17191D')
plt.close()
print("Architecture Diagram generated successfully.")
