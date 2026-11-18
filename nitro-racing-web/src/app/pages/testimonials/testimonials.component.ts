import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { DataService } from '../../services/data.service';
import { Testimonial } from '../../models/service.model';
import { EnquiryModalComponent } from '../../components/enquiry-modal/enquiry-modal.component';

@Component({
  selector: 'app-testimonials',
  standalone: true,
  imports: [CommonModule, FormsModule, EnquiryModalComponent],
  template: `
    <div class="bg-[#0A0C10] text-white pt-24 sm:pt-28 pb-20 sm:pb-24 min-h-screen">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">

        <!-- Page Header -->
        <div class="text-center max-w-3xl mx-auto mb-10 sm:mb-16 animate-fade-in-down">
          <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-white/[0.04] border border-white/[0.08] mb-3 sm:mb-4">
            <span class="w-2 h-2 rounded-full bg-[#00E676] animate-pulse"></span>
            <span class="text-[11px] sm:text-xs font-['JetBrains_Mono'] uppercase tracking-widest text-gray-300">Verified Rider Logbook</span>
          </div>
          <h1 class="text-3xl sm:text-5xl lg:text-6xl font-black uppercase text-white tracking-tight mb-3 sm:mb-5 font-['Outfit']">
            Customer <span class="text-[#00E676]">Reviews & Telemetry</span>
          </h1>
          <p class="text-gray-400 text-xs sm:text-base lg:text-lg leading-relaxed font-['Plus_Jakarta_Sans'] max-w-2xl mx-auto">
            Direct feedback from liter-class track riders, weekend tourers, and performance enthusiasts across Chennai workshops.
          </p>
        </div>

        <!-- Rating Highlight Showcase -->
        <div class="p-6 sm:p-10 rounded-3xl bg-[#11151F] border border-white/[0.08] mb-12 sm:mb-16 max-w-4xl mx-auto shadow-2xl scroll-reveal">
          <div class="flex flex-col md:flex-row items-center justify-between gap-6 pb-6 border-b border-white/[0.06]">
            <!-- Big Score -->
            <div class="flex items-center gap-4 text-center md:text-left">
              <div class="text-5xl sm:text-6xl font-black text-white font-['Outfit'] tracking-tight">4.9</div>
              <div>
                <div class="text-[#00E676] text-xl tracking-widest font-mono mb-1">★★★★★</div>
                <span class="text-xs text-gray-400 font-['JetBrains_Mono'] block">1,200+ Verified Digital Job Cards</span>
              </div>
            </div>

            <!-- Quick Trust Metrics -->
            <div class="flex flex-wrap items-center justify-center md:justify-end gap-3 text-xs font-['JetBrains_Mono']">
              <span class="px-3 py-1.5 rounded-xl bg-white/[0.03] border border-white/[0.08] text-gray-300">
                <strong class="text-[#00E676]">100%</strong> Genuine Motul Fluids
              </span>
              <span class="px-3 py-1.5 rounded-xl bg-white/[0.03] border border-white/[0.08] text-gray-300">
                <strong class="text-[#38BDF8]">0%</strong> Spliced Wiring
              </span>
              <span class="px-3 py-1.5 rounded-xl bg-white/[0.03] border border-white/[0.08] text-gray-300">
                <strong class="text-white">30 Days</strong> Service Warranty
              </span>
            </div>
          </div>

          <!-- Sub-ratings Grid -->
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 pt-6 text-center sm:text-left">
            <div class="p-3.5 rounded-2xl bg-[#0A0C10] border border-white/[0.04]">
              <span class="text-[10px] font-['JetBrains_Mono'] uppercase text-gray-400 block mb-1">Diagnostic Precision</span>
              <div class="flex items-center justify-center sm:justify-start gap-2">
                <span class="text-xl font-bold text-white font-mono">5.0</span>
                <span class="text-[#00E676] text-xs">★★★★★</span>
              </div>
            </div>

            <div class="p-3.5 rounded-2xl bg-[#0A0C10] border border-white/[0.04]">
              <span class="text-[10px] font-['JetBrains_Mono'] uppercase text-gray-400 block mb-1">WhatsApp Photo Reports</span>
              <div class="flex items-center justify-center sm:justify-start gap-2">
                <span class="text-xl font-bold text-white font-mono">5.0</span>
                <span class="text-[#00E676] text-xs">★★★★★</span>
              </div>
            </div>

            <div class="p-3.5 rounded-2xl bg-[#0A0C10] border border-white/[0.04]">
              <span class="text-[10px] font-['JetBrains_Mono'] uppercase text-gray-400 block mb-1">Dyno & Tuning Prowess</span>
              <div class="flex items-center justify-center sm:justify-start gap-2">
                <span class="text-xl font-bold text-white font-mono">4.9</span>
                <span class="text-[#00E676] text-xs">★★★★★</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Filter Tabs & Search Bar -->
        <div class="mb-10 flex flex-col md:flex-row items-center justify-between gap-4">
          <!-- Category Tabs -->
          <div class="flex flex-wrap items-center gap-2">
            <button
              *ngFor="let cat of categories"
              (click)="selectedCategory = cat"
              class="px-4 py-2 rounded-full text-xs font-semibold tracking-wider transition-all duration-200 font-['Outfit'] uppercase flex items-center gap-1.5"
              [ngClass]="selectedCategory === cat ? 'bg-[#00E676] text-[#0A0C10] font-black shadow-[0_0_20px_rgba(0,230,118,0.3)]' : 'bg-[#151A26] text-gray-300 hover:text-white border border-white/[0.08]'"
            >
              <span>{{ cat }}</span>
              <span class="text-[10px] px-1.5 py-0.2 rounded-full font-mono"
                    [ngClass]="selectedCategory === cat ? 'bg-black/20 text-black' : 'bg-white/10 text-gray-400'">
                {{ getCount(cat) }}
              </span>
            </button>
          </div>

          <!-- Branch Filter & Search -->
          <div class="flex items-center gap-2.5 w-full md:w-auto">
            <!-- Branch Filter -->
            <select
              [(ngModel)]="selectedBranch"
              class="bg-[#151A26] border border-white/[0.1] text-xs rounded-xl px-3 py-2.5 text-white focus:outline-none focus:border-[#00E676] font-['Plus_Jakarta_Sans']"
            >
              <option value="All">All Hubs</option>
              <option value="Ambattur">Ambattur Hub</option>
              <option value="Avadi">Avadi Hub</option>
            </select>

            <!-- Search Input -->
            <div class="relative flex-1 md:w-64">
              <input
                type="text"
                [(ngModel)]="searchQuery"
                placeholder="Search bike or rider..."
                class="w-full bg-[#151A26] border border-white/[0.1] text-xs rounded-xl pl-9 pr-3.5 py-2.5 text-white placeholder-gray-500 focus:outline-none focus:border-[#00E676] transition-all font-['Plus_Jakarta_Sans']"
              />
              <svg class="w-3.5 h-3.5 text-gray-400 absolute left-3 top-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
            </div>
          </div>
        </div>

        <!-- Testimonials Cards Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-16">
          <div
            *ngFor="let t of filteredTestimonials"
            class="group bg-[#11151F] border border-white/[0.08] hover:border-[#00E676]/40 rounded-3xl p-6 sm:p-7 flex flex-col justify-between transition-all duration-300 shadow-xl hover:shadow-[0_0_30px_rgba(0,230,118,0.12)] hover:-translate-y-1 scroll-reveal"
          >
            <div>
              <!-- Header: Avatar + Rider Info + Verified Badge -->
              <div class="flex items-start justify-between gap-3 mb-4">
                <div class="flex items-center gap-3">
                  <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-[#00E676]/20 to-[#38BDF8]/20 border border-[#00E676]/30 text-[#00E676] font-['Outfit'] font-black flex items-center justify-center text-sm shadow-md">
                    {{ t.avatarInitials || t.customerName.slice(0, 2).toUpperCase() }}
                  </div>
                  <div>
                    <h3 class="text-sm font-bold text-white font-['Outfit'] leading-tight">{{ t.customerName }}</h3>
                    <span class="text-[11px] text-gray-400 font-['Plus_Jakarta_Sans'] block">{{ t.neighborhood }}</span>
                  </div>
                </div>

                <span class="text-[10px] font-['JetBrains_Mono'] text-[#00E676] bg-[#00E676]/10 px-2 py-0.5 rounded font-bold border border-[#00E676]/25 shrink-0 flex items-center gap-1">
                  <span>✓</span>
                  <span>{{ t.jobCardNo || 'VERIFIED' }}</span>
                </span>
              </div>

              <!-- Bike Model & Service Category Banner -->
              <div class="p-3 rounded-xl bg-[#0A0C10] border border-white/[0.04] mb-4">
                <span class="text-xs font-black text-white font-['Outfit'] tracking-wide block mb-0.5">
                  🏍 {{ t.bikeModel }}
                </span>
                <span class="text-[11px] font-['JetBrains_Mono'] text-[#38BDF8] truncate block">
                  {{ t.serviceCategory }}
                </span>
              </div>

              <!-- Rating Stars & Date -->
              <div class="flex items-center justify-between mb-3 text-xs">
                <div class="flex items-center text-[#00E676] tracking-widest font-mono">
                  <span *ngFor="let s of [1,2,3,4,5]">★</span>
                </div>
                <span class="text-[11px] text-gray-500 font-['JetBrains_Mono']">{{ t.date }}</span>
              </div>

              <!-- Review Text Quote -->
              <p class="text-gray-300 text-xs sm:text-sm leading-relaxed mb-6 font-['Plus_Jakarta_Sans'] italic">
                "{{ t.review || t.feedback }}"
              </p>
            </div>

            <!-- Footer: Branch Tag + Certified Standard -->
            <div class="pt-4 border-t border-white/[0.06] flex items-center justify-between text-[11px] font-['JetBrains_Mono']">
              <span class="text-gray-400 flex items-center gap-1.5">
                <span class="w-1.5 h-1.5 rounded-full bg-[#00E676]"></span>
                <span>{{ t.branch }}</span>
              </span>
              <span class="text-gray-500 text-[10px] uppercase font-semibold">Job Card Closed</span>
            </div>
          </div>
        </div>

        <!-- No Results Fallback -->
        <div *ngIf="filteredTestimonials.length === 0" class="text-center py-16 bg-[#11151F] rounded-2xl border border-white/[0.08] mb-16">
          <p class="text-gray-400 text-sm mb-4 font-['Plus_Jakarta_Sans']">No reviews found matching your search "{{ searchQuery }}".</p>
          <button (click)="resetFilters()" class="px-5 py-2.5 bg-[#00E676] text-[#0A0C10] text-xs font-black uppercase tracking-wider rounded-xl font-['Outfit']">
            Reset Filters
          </button>
        </div>

        <!-- Bottom CTA Box -->
        <div class="p-8 sm:p-12 rounded-3xl bg-gradient-to-r from-[#11151F] via-[#151A26] to-[#11151F] border border-white/[0.1] text-center max-w-4xl mx-auto shadow-2xl scroll-reveal">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded bg-[#00E676]/10 text-[#00E676] text-xs font-['JetBrains_Mono'] font-bold uppercase tracking-wider mb-3">
            <span>Race-Grade Experience</span>
          </div>
          <h3 class="text-2xl sm:text-4xl font-black uppercase text-white mb-3 font-['Outfit']">
            Join The Nitro Racing Modz Rider Community
          </h3>
          <p class="text-gray-400 text-xs sm:text-base max-w-xl mx-auto mb-8 font-['Plus_Jakarta_Sans'] leading-relaxed">
            Experience computerized CAN-bus diagnostics, precision micrometer valve clearances, and transparent WhatsApp photo estimates.
          </p>
          
          <div class="flex flex-col sm:flex-row items-center justify-center gap-3.5">
            <button
              (click)="isModalOpen = true"
              class="btn-laser w-full sm:w-auto px-8 py-4 bg-[#00E676] hover:bg-[#00c864] text-[#0A0C10] text-xs font-black uppercase tracking-wider rounded-xl transition-all shadow-[0_0_20px_rgba(0,230,118,0.3)] font-['Outfit']"
            >
              Book Your Service Enquiry
            </button>
            <a
              href="tel:+919840011223"
              class="w-full sm:w-auto px-7 py-4 bg-[#151A26] hover:bg-[#1E2435] text-[#00E676] text-xs font-bold uppercase tracking-wider rounded-xl border border-white/[0.1] flex items-center justify-center gap-2 font-['JetBrains_Mono'] transition-colors"
            >
              <svg class="w-4 h-4 text-[#00E676]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
              <span>Call Workshop: +91 98400 11223</span>
            </a>
          </div>
        </div>

      </div>

      <!-- Enquiry Modal -->
      <app-enquiry-modal [isOpen]="isModalOpen" (close)="isModalOpen = false"></app-enquiry-modal>

    </div>
  `
})
export class TestimonialsComponent implements OnInit {
  testimonials: Testimonial[] = [];
  categories: string[] = ['All', 'Superbike Care', 'Nitro Modz', 'Periodic Service', 'Brakes'];
  selectedCategory = 'All';
  selectedBranch = 'All';
  searchQuery = '';
  isModalOpen = false;

  constructor(private dataService: DataService) {}

  ngOnInit(): void {
    this.testimonials = this.dataService.getTestimonials();
  }

  getCount(cat: string): number {
    if (cat === 'All') return this.testimonials.length;
    if (cat === 'Superbike Care') return this.testimonials.filter(t => t.categoryKey === 'superbike').length;
    if (cat === 'Nitro Modz') return this.testimonials.filter(t => t.categoryKey === 'modz').length;
    if (cat === 'Periodic Service') return this.testimonials.filter(t => t.categoryKey === 'routine').length;
    if (cat === 'Brakes') return this.testimonials.filter(t => t.categoryKey === 'brakes').length;
    return 0;
  }

  get filteredTestimonials(): Testimonial[] {
    return this.testimonials.filter(t => {
      // Category Filter
      let matchesCat = true;
      if (this.selectedCategory === 'Superbike Care') matchesCat = t.categoryKey === 'superbike';
      else if (this.selectedCategory === 'Nitro Modz') matchesCat = t.categoryKey === 'modz';
      else if (this.selectedCategory === 'Periodic Service') matchesCat = t.categoryKey === 'routine';
      else if (this.selectedCategory === 'Brakes') matchesCat = t.categoryKey === 'brakes';

      // Branch Filter
      const matchesBranch = this.selectedBranch === 'All' || t.branch.toLowerCase().includes(this.selectedBranch.toLowerCase());

      // Search Query
      const q = this.searchQuery.toLowerCase().trim();
      const matchesSearch = !q ||
        t.customerName.toLowerCase().includes(q) ||
        t.bikeModel.toLowerCase().includes(q) ||
        (t.serviceCategory || '').toLowerCase().includes(q) ||
        (t.neighborhood || '').toLowerCase().includes(q) ||
        (t.review || '').toLowerCase().includes(q);

      return matchesCat && matchesBranch && matchesSearch;
    });
  }

  resetFilters(): void {
    this.selectedCategory = 'All';
    this.selectedBranch = 'All';
    this.searchQuery = '';
  }
}
