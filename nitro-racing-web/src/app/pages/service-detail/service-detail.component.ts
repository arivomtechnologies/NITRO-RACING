import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { DataService } from '../../services/data.service';
import { WorkshopService } from '../../models/service.model';
import { EnquiryModalComponent } from '../../components/enquiry-modal/enquiry-modal.component';

@Component({
  selector: 'app-service-detail',
  standalone: true,
  imports: [CommonModule, RouterLink, EnquiryModalComponent],
  template: `
    <div class="bg-[#0A0C10] text-white pt-28 pb-24 min-h-screen">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">

        <!-- Breadcrumbs -->
        <nav class="flex items-center gap-2 text-xs text-gray-400 mb-10 font-['JetBrains_Mono']" aria-label="Breadcrumb">
          <a routerLink="/" class="hover:text-white transition-colors">Home</a>
          <span class="text-gray-600">/</span>
          <a routerLink="/services" class="hover:text-white transition-colors">Services</a>
          <span class="text-gray-600">/</span>
          <span class="text-[#00E676] font-semibold">{{ service?.name || 'Service Details' }}</span>
        </nav>

        <!-- Service Found -->
        <div *ngIf="service" class="grid grid-cols-1 lg:grid-cols-3 gap-12">

          <!-- Left Main Column -->
          <div class="lg:col-span-2 space-y-8">
            <div>
              <div class="flex items-center gap-3 mb-4">
                <span class="px-3 py-1 rounded-full bg-[#00E676]/10 text-[#00E676] border border-[#00E676]/20 text-xs font-['JetBrains_Mono'] font-bold uppercase tracking-wider">
                  {{ service.category }}
                </span>
                <span class="text-xs text-gray-400 font-['JetBrains_Mono']">
                  Workshop Bay Time: <strong class="text-white">{{ service.estimatedDuration }}</strong>
                </span>
              </div>
              <h1 class="text-3xl sm:text-5xl font-black uppercase tracking-tight text-white mb-6 font-['Outfit']">
                {{ service.name }}
              </h1>

              <!-- Service Image Hero Card with Telemetry -->
              <div class="relative h-64 sm:h-96 rounded-2xl overflow-hidden border border-white/[0.08] mb-6 bg-[#11151F]">
                <img [src]="service.imageUrl || 'images/hero_superbike.jpg'" [alt]="service.name" class="w-full h-full object-cover" />
                <div class="absolute inset-0 bg-gradient-to-t from-[#0A0C10] via-transparent to-black/30"></div>
                <div class="absolute bottom-4 left-4 right-4 flex items-center justify-between text-xs font-['JetBrains_Mono']">
                  <span class="px-3 py-1.5 rounded-lg bg-black/80 backdrop-blur-md border border-white/10 text-white font-bold flex items-center gap-2">
                    <span class="w-2 h-2 rounded-full bg-[#00E676] animate-pulse"></span>
                    <span>{{ service.telemetryTag || 'NITRO RACING CALIBRATED' }}</span>
                  </span>
                  <span class="px-3 py-1.5 rounded-lg bg-black/80 backdrop-blur-md border border-white/10 text-[#38BDF8] font-bold">
                    {{ service.code }}
                  </span>
                </div>
              </div>

              <p class="text-gray-300 text-base sm:text-lg leading-relaxed font-['Plus_Jakarta_Sans']">
                {{ service.description }}
              </p>
            </div>

            <!-- Inclusions Checklist -->
            <div class="premium-card p-8 scroll-reveal">
              <h2 class="text-xl font-black uppercase text-white mb-6 flex items-center gap-2 font-['Outfit']">
                <span class="w-2.5 h-2.5 rounded-full bg-[#00E676]"></span>
                <span>Included In This Package</span>
              </h2>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div *ngFor="let inc of service.includedItems" class="flex items-start gap-3 text-sm text-gray-300 font-['Plus_Jakarta_Sans']">
                  <div class="w-5 h-5 rounded-full bg-[#00E676]/10 text-[#00E676] flex items-center justify-center shrink-0 mt-0.5 text-xs font-bold font-['JetBrains_Mono']">
                    ✓
                  </div>
                  <span>{{ inc }}</span>
                </div>
              </div>
            </div>

            <!-- Standard Procedure -->
            <div class="premium-card p-8 space-y-4 scroll-reveal">
              <h2 class="text-xl font-black uppercase text-white mb-4 flex items-center gap-2 font-['Outfit']">
                <span class="w-2.5 h-2.5 rounded-full bg-[#38BDF8]"></span>
                <span>Nitro Racing Standard Operating Procedure</span>
              </h2>
              <ol class="space-y-4 text-sm text-gray-400 list-decimal list-inside font-['Plus_Jakarta_Sans'] leading-relaxed">
                <li><strong class="text-white font-['Outfit'] uppercase">Pre-Check Digital Inspection:</strong> Initial symptom capture, battery voltage check, and test ride notes logged in our management software.</li>
                <li><strong class="text-white font-['Outfit'] uppercase">Bay Setup & Torque Spec Calibration:</strong> Vehicle is strapped on hydraulic lift with rubber frame pads. All bolts loosened and torqued using calibrated digital torque wrenches.</li>
                <li><strong class="text-white font-['Outfit'] uppercase">Customer Notification:</strong> Any additional worn parts discovered during disassembly are photographed and sent to the rider via WhatsApp for explicit approval.</li>
                <li><strong class="text-white font-['Outfit'] uppercase">Final Road Test & Quality Signoff:</strong> Chief mechanic performs road test and signs off digital job card before invoicing.</li>
              </ol>
            </div>
          </div>

          <!-- Right Booking Sidebar -->
          <div class="space-y-6">
            <div class="premium-card p-8 sticky top-28 scroll-reveal">
              <div class="border-b border-white/[0.08] pb-6 mb-6">
                <span class="text-xs uppercase tracking-wider text-gray-400 block mb-1 font-['JetBrains_Mono']">Starting Labor Base</span>
                <div class="text-4xl font-black text-white font-['JetBrains_Mono']">{{ service.basePrice }}</div>
                <span class="text-xs text-gray-500 block mt-1 font-['JetBrains_Mono']">*Excludes replacement oils & spare parts</span>
              </div>

              <div class="space-y-3 mb-8 text-xs text-gray-300 font-['JetBrains_Mono']">
                <div class="flex items-center justify-between py-1 border-b border-white/[0.04]">
                  <span class="text-gray-400">Available At:</span>
                  <span class="font-bold text-white">Ambattur & Avadi Bays</span>
                </div>
                <div class="flex items-center justify-between py-1 border-b border-white/[0.04]">
                  <span class="text-gray-400">Service Guarantee:</span>
                  <span class="font-bold text-[#00E676]">30 Days / 1,000 KM</span>
                </div>
                <div class="flex items-center justify-between py-1">
                  <span class="text-gray-400">Fluids Standard:</span>
                  <span class="font-bold text-white">Motul 100% Synthetic</span>
                </div>
              </div>

              <button
                (click)="isModalOpen = true"
                class="btn-laser w-full py-4 bg-[#00E676] hover:bg-[#00c864] text-[#0A0C10] font-black uppercase tracking-wider text-xs rounded-xl shadow-[0_0_25px_rgba(0,230,118,0.25)] transition-all font-['Outfit']"
              >
                Book This Service Bay
              </button>

              <a
                href="tel:+919840011223"
                class="w-full py-3.5 mt-3 bg-white/[0.06] hover:bg-white/[0.1] text-white font-bold text-xs uppercase tracking-wider rounded-xl border border-white/[0.1] flex items-center justify-center gap-2 font-mono transition-colors"
              >
                <svg class="w-4 h-4 text-[#00E676]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
                <span>Call Hotline: +91 98400 11223</span>
              </a>

              <div class="mt-4 text-center">
                <a routerLink="/contact" class="text-xs text-gray-400 hover:text-white transition-colors font-['Plus_Jakarta_Sans']">
                  Need a custom quote? Speak to our advisor →
                </a>
              </div>
            </div>
          </div>

        </div>

        <!-- Service Not Found -->
        <div *ngIf="!service" class="text-center py-24 bg-[#11151F] rounded-2xl border border-white/[0.08]">
          <h2 class="text-2xl font-black uppercase text-white mb-4 font-['Outfit']">Service Not Found</h2>
          <p class="text-gray-400 text-sm mb-6 font-['Plus_Jakarta_Sans']">The service package you are looking for does not exist or has been updated.</p>
          <a routerLink="/services" class="px-6 py-3 bg-[#00E676] text-[#0A0C10] text-xs font-black uppercase tracking-wider rounded-xl font-['Outfit']">
            Back to Catalog
          </a>
        </div>

      </div>

      <!-- Modal -->
      <app-enquiry-modal [isOpen]="isModalOpen" (close)="isModalOpen = false"></app-enquiry-modal>

    </div>
  `
})
export class ServiceDetailComponent implements OnInit {
  service?: WorkshopService;
  isModalOpen = false;

  constructor(private route: ActivatedRoute, private dataService: DataService) {}

  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      const id = params.get('id');
      if (id) {
        this.service = this.dataService.getServiceById(id);
      }
    });
  }
}
