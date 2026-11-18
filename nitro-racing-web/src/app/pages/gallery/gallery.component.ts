import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { DataService } from '../../services/data.service';
import { GalleryItem } from '../../models/service.model';
import { EnquiryModalComponent } from '../../components/enquiry-modal/enquiry-modal.component';

@Component({
  selector: 'app-gallery',
  standalone: true,
  imports: [CommonModule, FormsModule, EnquiryModalComponent],
  template: `
    <div class="bg-[#0A0C10] text-white pt-24 sm:pt-28 pb-20 sm:pb-24 min-h-screen">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">

        <!-- Page Header -->
        <div class="text-center max-w-3xl mx-auto mb-10 sm:mb-14 animate-fade-in-down">
          <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-white/[0.04] border border-white/[0.08] mb-3 sm:mb-4">
            <span class="w-2 h-2 rounded-full bg-[#00E676] animate-pulse"></span>
            <span class="text-[11px] sm:text-xs font-['JetBrains_Mono'] uppercase tracking-widest text-gray-300">Verified Workshop & Project Archive</span>
          </div>
          <h1 class="text-3xl sm:text-5xl lg:text-6xl font-black uppercase text-white tracking-tight mb-3 sm:mb-5 font-['Outfit']">
            Workshop & Custom Build <span class="text-[#00E676]">Gallery</span>
          </h1>
          <p class="text-gray-400 text-xs sm:text-base lg:text-lg leading-relaxed font-['Plus_Jakarta_Sans'] max-w-2xl mx-auto">
            High-resolution captures from our Ambattur multi-cylinder diagnostic bays and Avadi Nitro Modz fabrication studio. Liter-class engine overhauls, titanium welds, and dyno calibrations.
          </p>
        </div>

        <!-- Telemetry Stats Bar -->
        <div class="p-5 sm:p-7 rounded-2xl bg-[#11151F] border border-white/[0.08] mb-10 sm:mb-14 max-w-5xl mx-auto shadow-2xl scroll-reveal">
          <div class="grid grid-cols-2 md:grid-cols-4 gap-4 text-center">
            <div class="p-3 rounded-xl bg-[#0A0C10] border border-white/[0.04]">
              <span class="text-xl sm:text-2xl font-black text-[#00E676] font-['Outfit'] block">12+ Builds</span>
              <span class="text-[10px] sm:text-xs font-['JetBrains_Mono'] text-gray-400 uppercase">Documented Projects</span>
            </div>
            <div class="p-3 rounded-xl bg-[#0A0C10] border border-white/[0.04]">
              <span class="text-xl sm:text-2xl font-black text-white font-['Outfit'] block">100% Dyno</span>
              <span class="text-[10px] sm:text-xs font-['JetBrains_Mono'] text-gray-400 uppercase">Track & Street Tested</span>
            </div>
            <div class="p-3 rounded-xl bg-[#0A0C10] border border-white/[0.04]">
              <span class="text-xl sm:text-2xl font-black text-[#38BDF8] font-['Outfit'] block">Zero Splice</span>
              <span class="text-[10px] sm:text-xs font-['JetBrains_Mono'] text-gray-400 uppercase">IP67 Sealed Harnesses</span>
            </div>
            <div class="p-3 rounded-xl bg-[#0A0C10] border border-white/[0.04]">
              <span class="text-xl sm:text-2xl font-black text-white font-['Outfit'] block">Motul 300V</span>
              <span class="text-[10px] sm:text-xs font-['JetBrains_Mono'] text-gray-400 uppercase">Factory Line Fluids</span>
            </div>
          </div>
        </div>

        <!-- Filter Tabs & Search Controls -->
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

          <!-- Hub Filter & Search -->
          <div class="flex items-center gap-2.5 w-full md:w-auto">
            <select
              [(ngModel)]="selectedBranch"
              class="bg-[#151A26] border border-white/[0.1] text-xs rounded-xl px-3 py-2.5 text-white focus:outline-none focus:border-[#00E676] font-['Plus_Jakarta_Sans']"
            >
              <option value="All">All Hubs</option>
              <option value="Ambattur">Ambattur Hub</option>
              <option value="Avadi">Avadi Hub</option>
            </select>

            <div class="relative flex-1 md:w-60">
              <input
                type="text"
                [(ngModel)]="searchQuery"
                placeholder="Search bike, exhaust, dyno..."
                class="w-full bg-[#151A26] border border-white/[0.1] text-xs rounded-xl pl-9 pr-3.5 py-2.5 text-white placeholder-gray-500 focus:outline-none focus:border-[#00E676] transition-all font-['Plus_Jakarta_Sans']"
              />
              <svg class="w-3.5 h-3.5 text-gray-400 absolute left-3 top-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
            </div>
          </div>
        </div>

        <!-- Gallery Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 sm:gap-8 mb-16">
          <div
            *ngFor="let item of filteredItems"
            class="group bg-[#11151F] border border-white/[0.08] hover:border-[#00E676]/40 rounded-3xl overflow-hidden flex flex-col justify-between transition-all duration-300 shadow-xl hover:shadow-[0_0_30px_rgba(0,230,118,0.12)] hover:-translate-y-1 scroll-reveal"
          >
            <div>
              <!-- Image Container with Hover Inspect Prompt -->
              <div
                (click)="openInspector(item)"
                class="relative h-64 sm:h-72 bg-[#0A0C10] overflow-hidden cursor-pointer"
              >
                <img
                  [src]="item.imageUrl"
                  [alt]="item.title"
                  class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700"
                />
                <div class="absolute inset-0 bg-gradient-to-t from-[#11151F] via-[#11151F]/20 to-transparent"></div>

                <!-- Top Corner Badges -->
                <div class="absolute top-3.5 left-3.5 flex items-center gap-2">
                  <span class="text-[10px] font-['JetBrains_Mono'] font-bold uppercase tracking-wider px-2.5 py-1 rounded bg-[#0A0C10]/80 text-[#00E676] border border-[#00E676]/30 backdrop-blur-md">
                    {{ item.category }}
                  </span>
                </div>

                <div class="absolute top-3.5 right-3.5 flex items-center gap-1.5">
                  <span class="text-[10px] font-['JetBrains_Mono'] font-bold text-gray-300 px-2.5 py-1 rounded bg-[#0A0C10]/80 border border-white/[0.1] backdrop-blur-md">
                    {{ item.branch || 'Chennai Hub' }}
                  </span>
                </div>

                <!-- Floating Inspect Button Prompt -->
                <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity bg-black/40 backdrop-blur-[2px]">
                  <span class="px-4 py-2 rounded-xl bg-[#00E676] text-[#0A0C10] text-xs font-black uppercase tracking-wider font-['Outfit'] flex items-center gap-1.5 shadow-lg transform translate-y-2 group-hover:translate-y-0 transition-transform">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0zM10 7v3m0 0v3m0-3h3m-3 0H7"/></svg>
                    <span>Inspect Build</span>
                  </span>
                </div>

                <!-- Bottom Image Banner: Bike Model -->
                <div class="absolute bottom-3 left-4 right-4">
                  <span class="text-xs font-['JetBrains_Mono'] text-[#38BDF8] font-bold block mb-0.5">
                    🏍 {{ item.bikeModel }}
                  </span>
                  <span *ngIf="item.buildType" class="text-[10px] font-['JetBrains_Mono'] text-gray-400 block uppercase tracking-wider">
                    // {{ item.buildType }}
                  </span>
                </div>
              </div>

              <!-- Card Body -->
              <div class="p-5 sm:p-6">
                <h3 class="text-base sm:text-lg font-black text-white uppercase font-['Outfit'] mb-2.5 leading-snug group-hover:text-[#00E676] transition-colors">
                  {{ item.title }}
                </h3>

                <p class="text-xs text-gray-400 leading-relaxed font-['Plus_Jakarta_Sans'] mb-4">
                  {{ item.description || item.caption }}
                </p>

                <!-- Technical Specs Pills -->
                <div *ngIf="item.specs && item.specs.length" class="grid grid-cols-2 gap-2 mb-4">
                  <div *ngFor="let spec of item.specs" class="p-2 rounded-lg bg-[#0A0C10] border border-white/[0.04]">
                    <span class="text-[9px] font-['JetBrains_Mono'] text-gray-500 uppercase block">{{ spec.label }}</span>
                    <span class="text-[11px] font-bold text-white font-['JetBrains_Mono'] block truncate">{{ spec.value }}</span>
                  </div>
                </div>

                <!-- Tags -->
                <div *ngIf="item.tags && item.tags.length" class="flex flex-wrap gap-1.5 mb-2">
                  <span *ngFor="let tag of item.tags" class="text-[10px] font-['JetBrains_Mono'] text-gray-400 px-2 py-0.5 rounded bg-white/[0.03] border border-white/[0.06]">
                    #{{ tag }}
                  </span>
                </div>
              </div>
            </div>

            <!-- Card Footer: Actions -->
            <div class="p-5 sm:p-6 pt-0">
              <div class="pt-4 border-t border-white/[0.06] flex items-center justify-between gap-3">
                <button
                  (click)="openInspector(item)"
                  class="flex-1 py-2.5 rounded-xl bg-white/[0.04] hover:bg-white/[0.08] text-white text-xs font-bold font-['Outfit'] uppercase tracking-wider transition-colors border border-white/[0.08] flex items-center justify-center gap-1.5"
                >
                  <svg class="w-3.5 h-3.5 text-[#00E676]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
                  <span>Details</span>
                </button>

                <button
                  (click)="bookThisBuild(item)"
                  class="flex-1 py-2.5 rounded-xl bg-[#00E676] hover:bg-[#00c864] text-[#0A0C10] text-xs font-black font-['Outfit'] uppercase tracking-wider transition-all shadow-[0_0_15px_rgba(0,230,118,0.2)] flex items-center justify-center gap-1"
                >
                  <span>Enquire</span>
                  <span>→</span>
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- No Results Fallback -->
        <div *ngIf="filteredItems.length === 0" class="text-center py-16 bg-[#11151F] rounded-2xl border border-white/[0.08] mb-16">
          <p class="text-gray-400 text-sm mb-4 font-['Plus_Jakarta_Sans']">No builds or workshop photos found matching "{{ searchQuery }}".</p>
          <button (click)="resetFilters()" class="px-5 py-2.5 bg-[#00E676] text-[#0A0C10] text-xs font-black uppercase tracking-wider rounded-xl font-['Outfit']">
            Reset Filters
          </button>
        </div>

        <!-- Bottom CTA Box -->
        <div class="p-8 sm:p-12 rounded-3xl bg-gradient-to-r from-[#11151F] via-[#151A26] to-[#11151F] border border-white/[0.1] text-center max-w-4xl mx-auto shadow-2xl scroll-reveal">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded bg-[#00E676]/10 text-[#00E676] text-xs font-['JetBrains_Mono'] font-bold uppercase tracking-wider mb-3">
            <span>Custom Motorcycle Engineering</span>
          </div>
          <h3 class="text-2xl sm:text-4xl font-black uppercase text-white mb-3 font-['Outfit']">
            Have A Custom Build Or Superbike Project?
          </h3>
          <p class="text-gray-400 text-xs sm:text-base max-w-xl mx-auto mb-8 font-['Plus_Jakarta_Sans'] leading-relaxed">
            From bespoke stainless 2-into-1 exhausts to liter-class desmodromic valve servicing and dyno Stage 2 fuel mapping. Speak directly with our master technicians.
          </p>
          
          <div class="flex flex-col sm:flex-row items-center justify-center gap-3.5">
            <button
              (click)="isModalOpen = true"
              class="btn-laser w-full sm:w-auto px-8 py-4 bg-[#00E676] hover:bg-[#00c864] text-[#0A0C10] text-xs font-black uppercase tracking-wider rounded-xl transition-all shadow-[0_0_20px_rgba(0,230,118,0.3)] font-['Outfit']"
            >
              Book Your Build Consultation
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

      <!-- Fullscreen Build Inspector Lightbox Modal -->
      <div
        *ngIf="selectedItem"
        class="fixed inset-0 z-50 bg-black/90 backdrop-blur-md flex items-center justify-center p-4 sm:p-6 overflow-y-auto"
        (click)="closeInspector()"
      >
        <div
          class="bg-[#11151F] border border-white/[0.12] rounded-3xl max-w-4xl w-full overflow-hidden shadow-2xl relative my-8"
          (click)="$event.stopPropagation()"
        >
          <!-- Close Button -->
          <button
            (click)="closeInspector()"
            class="absolute top-4 right-4 z-20 w-9 h-9 rounded-full bg-black/70 border border-white/20 text-white flex items-center justify-center hover:bg-[#00E676] hover:text-black transition-colors"
          >
            ✕
          </button>

          <div class="grid grid-cols-1 md:grid-cols-2">
            <!-- Modal Image View -->
            <div class="relative bg-[#0A0C10] min-h-[300px] md:min-h-[460px] flex items-center justify-center overflow-hidden">
              <img
                [src]="selectedItem.imageUrl"
                [alt]="selectedItem.title"
                class="w-full h-full object-cover"
              />
              <div class="absolute inset-0 bg-gradient-to-t from-[#11151F] via-transparent to-transparent opacity-80 md:hidden"></div>
              
              <div class="absolute top-4 left-4 flex flex-wrap gap-2">
                <span class="text-[10px] font-['JetBrains_Mono'] font-bold uppercase tracking-wider px-2.5 py-1 rounded bg-[#0A0C10]/90 text-[#00E676] border border-[#00E676]/30">
                  {{ selectedItem.category }}
                </span>
                <span *ngIf="selectedItem.jobCardNo" class="text-[10px] font-['JetBrains_Mono'] font-bold px-2 py-1 rounded bg-black/80 text-white border border-white/10">
                  ✓ {{ selectedItem.jobCardNo }}
                </span>
              </div>
            </div>

            <!-- Modal Content & Specs -->
            <div class="p-6 sm:p-8 flex flex-col justify-between">
              <div>
                <div class="flex items-center gap-2 mb-2 text-xs font-['JetBrains_Mono'] text-[#38BDF8]">
                  <span>🏍 {{ selectedItem.bikeModel }}</span>
                  <span class="text-gray-500">•</span>
                  <span class="text-gray-400">{{ selectedItem.branch }}</span>
                </div>

                <h3 class="text-xl sm:text-2xl font-black text-white uppercase font-['Outfit'] mb-3">
                  {{ selectedItem.title }}
                </h3>

                <p class="text-xs sm:text-sm text-gray-300 leading-relaxed font-['Plus_Jakarta_Sans'] mb-6">
                  {{ selectedItem.description || selectedItem.caption }}
                </p>

                <!-- Technical Specs Table -->
                <div *ngIf="selectedItem.specs && selectedItem.specs.length" class="space-y-2 mb-6">
                  <span class="text-[10px] font-['JetBrains_Mono'] uppercase tracking-widest text-gray-400 block mb-2">Build Telemetry & Components</span>
                  <div *ngFor="let spec of selectedItem.specs" class="flex items-center justify-between p-2.5 rounded-xl bg-[#0A0C10] border border-white/[0.04]">
                    <span class="text-xs font-['JetBrains_Mono'] text-gray-400">{{ spec.label }}</span>
                    <span class="text-xs font-bold text-white font-['JetBrains_Mono']">{{ spec.value }}</span>
                  </div>
                </div>

                <!-- Tags -->
                <div *ngIf="selectedItem.tags && selectedItem.tags.length" class="flex flex-wrap gap-1.5 mb-6">
                  <span *ngFor="let tag of selectedItem.tags" class="text-[10px] font-['JetBrains_Mono'] text-gray-400 px-2 py-0.5 rounded bg-white/[0.04] border border-white/[0.08]">
                    #{{ tag }}
                  </span>
                </div>
              </div>

              <!-- Actions in Modal -->
              <div class="pt-4 border-t border-white/[0.08] flex flex-col sm:flex-row gap-3">
                <button
                  (click)="bookThisBuild(selectedItem)"
                  class="flex-1 py-3 px-4 bg-[#00E676] hover:bg-[#00c864] text-[#0A0C10] text-xs font-black uppercase tracking-wider rounded-xl transition-all shadow-[0_0_15px_rgba(0,230,118,0.2)] font-['Outfit'] text-center"
                >
                  Enquire About Similar Build
                </button>
                <a
                  href="tel:+919840011223"
                  class="py-3 px-4 bg-[#151A26] hover:bg-[#1E2435] text-white text-xs font-bold uppercase tracking-wider rounded-xl border border-white/[0.1] font-['JetBrains_Mono'] flex items-center justify-center gap-1.5"
                >
                  <svg class="w-3.5 h-3.5 text-[#00E676]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
                  <span>Call Workshop</span>
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Enquiry Modal -->
      <app-enquiry-modal [isOpen]="isModalOpen" (close)="isModalOpen = false"></app-enquiry-modal>

    </div>
  `
})
export class GalleryComponent implements OnInit {
  items: GalleryItem[] = [];
  categories: string[] = ['All', 'Superbikes', 'Nitro Modz', 'Track & Dyno', 'Workshop Life', 'Detailing'];
  selectedCategory = 'All';
  selectedBranch = 'All';
  searchQuery = '';
  isModalOpen = false;
  selectedItem: GalleryItem | null = null;

  constructor(private dataService: DataService) {}

  ngOnInit(): void {
    this.items = this.dataService.getGallery();
  }

  getCount(cat: string): number {
    if (cat === 'All') return this.items.length;
    return this.items.filter(i => i.category === cat).length;
  }

  get filteredItems(): GalleryItem[] {
    return this.items.filter(item => {
      // Category filter
      const matchesCat = this.selectedCategory === 'All' || item.category === this.selectedCategory;

      // Hub filter
      const matchesBranch = this.selectedBranch === 'All' || (item.branch || '').toLowerCase().includes(this.selectedBranch.toLowerCase());

      // Search query
      const q = this.searchQuery.toLowerCase().trim();
      const matchesSearch = !q ||
        item.title.toLowerCase().includes(q) ||
        (item.bikeModel || '').toLowerCase().includes(q) ||
        (item.caption || '').toLowerCase().includes(q) ||
        (item.description || '').toLowerCase().includes(q) ||
        (item.buildType || '').toLowerCase().includes(q) ||
        (item.tags || []).some(t => t.toLowerCase().includes(q));

      return matchesCat && matchesBranch && matchesSearch;
    });
  }

  openInspector(item: GalleryItem): void {
    this.selectedItem = item;
  }

  closeInspector(): void {
    this.selectedItem = null;
  }

  bookThisBuild(item: GalleryItem): void {
    this.selectedItem = null;
    this.isModalOpen = true;
  }

  resetFilters(): void {
    this.selectedCategory = 'All';
    this.selectedBranch = 'All';
    this.searchQuery = '';
  }
}
