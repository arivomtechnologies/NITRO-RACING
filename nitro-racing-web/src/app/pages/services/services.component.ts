import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink, ActivatedRoute } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { DataService } from '../../services/data.service';
import { WorkshopService } from '../../models/service.model';
import { EnquiryModalComponent } from '../../components/enquiry-modal/enquiry-modal.component';

@Component({
  selector: 'app-services',
  standalone: true,
  imports: [CommonModule, RouterLink, FormsModule, EnquiryModalComponent],
  template: `
    <div class="bg-[#0A0C10] text-white pt-28 pb-24 min-h-screen">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">

        <!-- Page Header -->
        <div class="text-center max-w-3xl mx-auto mb-16 animate-fade-in-down">
          <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-white/[0.04] border border-white/[0.08] mb-4">
            <span class="w-2 h-2 rounded-full bg-[#00E676] animate-pulse"></span>
            <span class="text-xs font-['JetBrains_Mono'] uppercase tracking-widest text-gray-300">Engineering & Tuning Menu</span>
          </div>
          <h1 class="text-4xl sm:text-6xl font-black uppercase text-white tracking-tight mb-5 font-['Outfit']">
            NITRO RACING Workshop & <span class="text-[#00E676]">Modz</span> Catalog
          </h1>
          <p class="text-gray-400 text-base sm:text-lg leading-relaxed font-['Plus_Jakarta_Sans']">
            From factory-calibrated routine maintenance to high-compression engine rebuilds, dyno mapping, and bespoke Nitro Modz titanium exhaust fabrication.
          </p>

          <!-- Quick Hub Pills -->
          <div class="flex flex-wrap items-center justify-center gap-3 mt-6">
            <span class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-[#11151F] border border-white/[0.08] text-xs font-['JetBrains_Mono'] text-gray-300 hover:border-[#00E676]/30 transition-colors">
              <span class="w-1.5 h-1.5 rounded-full bg-[#00E676] animate-pulse"></span>
              <span>Ambattur Hub: 6 Hydraulic Diagnostic Bays</span>
            </span>
            <span class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-[#11151F] border border-white/[0.08] text-xs font-['JetBrains_Mono'] text-gray-300 hover:border-[#38BDF8]/30 transition-colors">
              <span class="w-1.5 h-1.5 rounded-full bg-[#38BDF8] animate-pulse"></span>
              <span>Avadi Hub: Superbike & Nitro Modz Studio</span>
            </span>
          </div>
        </div>

        <!-- Filter Tabs & Search Bar -->
        <div class="mb-12 flex flex-col md:flex-row items-center justify-between gap-4">
          <!-- Category Tabs -->
          <div class="flex flex-wrap items-center gap-2">
            <button
              *ngFor="let cat of categories"
              (click)="selectedCategory = cat"
              class="px-5 py-2.5 rounded-full text-xs font-semibold tracking-wider transition-all duration-200 font-['Outfit'] uppercase flex items-center gap-2"
              [ngClass]="selectedCategory === cat ? 'bg-[#00E676] text-[#0A0C10] font-black shadow-[0_0_20px_rgba(0,230,118,0.3)]' : 'bg-[#151A26] text-gray-300 hover:text-white border border-white/[0.08] hover:border-white/[0.2]'"
            >
              <span>{{ cat }}</span>
              <span class="text-[10px] px-1.5 py-0.2 rounded-full font-mono"
                    [ngClass]="selectedCategory === cat ? 'bg-black/20 text-black' : 'bg-white/10 text-gray-400'">
                {{ getCount(cat) }}
              </span>
            </button>
          </div>

          <!-- Search Input -->
          <div class="w-full md:w-80 relative">
            <input
              type="text"
              [(ngModel)]="searchQuery"
              placeholder="Search services, exhausts, dyno..."
              class="w-full bg-[#151A26] border border-white/[0.1] text-xs rounded-xl pl-10 pr-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:border-[#00E676] focus:ring-1 focus:ring-[#00E676] transition-all font-['Plus_Jakarta_Sans']"
            />
            <svg class="w-4 h-4 text-gray-400 absolute left-3.5 top-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
          </div>
        </div>

        <!-- Division Highlights Banner -->
        <div *ngIf="selectedCategory === 'Superbike Care'" class="mb-10 p-6 rounded-2xl bg-[#11151F] border border-white/[0.08] border-l-4 border-l-[#38BDF8]">
          <div class="flex items-center gap-3 mb-2">
            <span class="w-2.5 h-2.5 rounded-full bg-[#38BDF8]"></span>
            <h3 class="text-lg font-black uppercase text-white font-['Outfit']">NITRO RACING Superbike Diagnostics & Valve Clearances</h3>
          </div>
          <p class="text-sm text-gray-400 leading-relaxed max-w-3xl font-['Plus_Jakarta_Sans']">
            Our Avadi and Ambattur superbike bays feature dedicated diagnostic pods for Kawasaki Ninja/Z series, Ducati Panigale/Monster, Triumph Street/Speed Triple, Honda CBR, and BMW S1000RR. All fluids used are Motul 300V Factory Line.
          </p>
        </div>

        <div *ngIf="selectedCategory === 'Nitro Modz'" class="mb-10 p-6 rounded-2xl bg-[#11151F] border border-white/[0.08] border-l-4 border-l-[#00E676]">
          <div class="flex items-center gap-3 mb-2">
            <span class="w-2.5 h-2.5 rounded-full bg-[#00E676]"></span>
            <h3 class="text-lg font-black uppercase text-white font-['Outfit']">Nitro Modz Performance & Styling Studio</h3>
          </div>
          <p class="text-sm text-gray-400 leading-relaxed max-w-3xl font-['Plus_Jakarta_Sans']">
            Custom exhaust bend pipe welding, decat headers, Stage 1/2 ECU flash tuning, high-candela auxiliary pod wiring with IP67 relays, heavy-gauge crash cages, and carbon body kit fitments.
          </p>
        </div>

        <!-- Split Left & Right Services Showcase -->
        <div class="space-y-10">
          <div
            *ngFor="let s of filteredServices; let i = index"
            class="group bg-[#11151F] border border-white/[0.08] hover:border-[#00E676]/40 rounded-3xl overflow-hidden transition-all duration-300 shadow-2xl hover:shadow-[0_0_35px_rgba(0,230,118,0.12)] scroll-reveal"
          >
            <div
              class="flex flex-col"
              [ngClass]="i % 2 === 1 ? 'lg:flex-row-reverse' : 'lg:flex-row'"
            >
              <!-- DETAILS EXPLANATION (Left or Right based on alternating row) -->
              <div class="w-full lg:w-7/12 p-6 sm:p-8 lg:p-10 flex flex-col justify-between">
                <div>
                  <!-- Meta Header: Division Tag + Duration + Interval -->
                  <div class="flex flex-wrap items-center gap-2.5 mb-4">
                    <span class="text-xs font-['JetBrains_Mono'] uppercase tracking-wider px-3 py-1 rounded-md bg-[#00E676]/10 text-[#00E676] border border-[#00E676]/25 font-bold">
                      {{ s.badge || s.categoryLabel || s.category }}
                    </span>
                    <span class="text-xs text-gray-300 font-['JetBrains_Mono'] flex items-center gap-1.5 bg-white/[0.04] px-2.5 py-1 rounded border border-white/[0.06]">
                      <svg class="w-3.5 h-3.5 text-[#00E676]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                      {{ s.estimatedDuration }}
                    </span>
                    <span *ngIf="s.recommendedInterval" class="text-xs text-gray-300 font-['JetBrains_Mono'] hidden sm:inline-flex items-center gap-1.5 bg-white/[0.04] px-2.5 py-1 rounded border border-white/[0.06]">
                      <span class="w-1.5 h-1.5 rounded-full bg-[#38BDF8]"></span>
                      {{ s.recommendedInterval }}
                    </span>
                  </div>

                  <!-- Title -->
                  <h2 class="text-2xl sm:text-3xl font-black text-white group-hover:text-[#00E676] transition-colors mb-3 font-['Outfit'] tracking-tight leading-tight">
                    {{ s.name }}
                  </h2>

                  <!-- Explanations -->
                  <p class="text-sm sm:text-base text-gray-200 font-medium leading-relaxed mb-3 font-['Plus_Jakarta_Sans']">
                    {{ s.shortDescription }}
                  </p>
                  <p class="text-xs sm:text-sm text-gray-400 leading-relaxed mb-6 font-['Plus_Jakarta_Sans']">
                    {{ s.description }}
                  </p>

                  <!-- Key Deliverables Checklist -->
                  <div class="mb-6 bg-[#0A0C10] border border-white/[0.06] rounded-2xl p-5">
                    <span class="text-[10px] font-['JetBrains_Mono'] uppercase font-bold text-gray-400 tracking-wider block mb-3 flex items-center justify-between">
                      <span>Inspection & Engineering Deliverables</span>
                      <span class="text-[#00E676] text-[10px]">{{ (s.includedItems || s.includedList).length }} Checkpoints</span>
                    </span>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
                      <div
                        *ngFor="let inc of (s.includedItems || s.includedList).slice(0, 6)"
                        class="text-xs text-gray-300 flex items-start gap-2 font-['Plus_Jakarta_Sans']"
                      >
                        <span class="text-[#00E676] font-bold text-xs mt-0.5">✓</span>
                        <span class="leading-snug">{{ inc }}</span>
                      </div>
                    </div>
                  </div>

                  <!-- Compatible Models / Equipment Specs -->
                  <div *ngIf="s.applicableModels" class="flex flex-wrap items-center gap-2 mb-6">
                    <span class="text-[10px] uppercase font-['JetBrains_Mono'] text-gray-400 font-semibold">Suitable For:</span>
                    <span class="text-xs font-['JetBrains_Mono'] text-gray-200 bg-white/[0.04] px-3 py-1 rounded-lg border border-white/[0.08]">
                      {{ s.applicableModels }}
                    </span>
                  </div>
                </div>

                <!-- Footer: Pricing + Action Buttons + Call Hotline Icon -->
                <div class="pt-6 border-t border-white/[0.08] flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                  <div>
                    <span class="text-[10px] font-['JetBrains_Mono'] uppercase text-gray-400 block font-semibold">Starting Labor Base</span>
                    <div class="flex items-baseline gap-2">
                      <span class="text-3xl font-black text-white font-['JetBrains_Mono']">{{ s.basePrice }}</span>
                      <span class="text-[10px] text-gray-500 font-['JetBrains_Mono']">*Excludes parts & oils</span>
                    </div>
                  </div>

                  <div class="flex flex-wrap items-center gap-2.5">
                    <button
                      (click)="openEnquiry(s.name)"
                      class="px-6 py-3 bg-[#00E676] hover:bg-[#00c864] text-[#0A0C10] text-xs font-black uppercase tracking-wider rounded-xl transition-all shadow-[0_0_20px_rgba(0,230,118,0.3)] flex items-center gap-2 font-['Outfit'] hover:-translate-y-0.5"
                    >
                      <span>Book Bay</span>
                      <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
                    </button>

                    <a
                      [routerLink]="['/services', s.id]"
                      class="px-5 py-3 bg-white/[0.05] hover:bg-white/[0.1] text-white text-xs font-bold uppercase tracking-wider rounded-xl transition-colors border border-white/[0.1] font-['Outfit'] hover:-translate-y-0.5"
                    >
                      Details →
                    </a>

                    <a
                      href="tel:+919840011223"
                      aria-label="Call Nitro Racing Hotline"
                      class="px-4 py-3 bg-[#151A26] hover:bg-[#1E2435] text-[#00E676] text-xs font-bold rounded-xl border border-white/[0.1] flex items-center gap-2 font-['JetBrains_Mono'] transition-colors hover:-translate-y-0.5"
                    >
                      <svg class="w-3.5 h-3.5 text-[#00E676]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
                      <span class="hidden sm:inline">Call Hotline</span>
                    </a>
                  </div>
                </div>
              </div>

              <!-- IMAGES SIDE (Right or Left based on alternating row) -->
              <div class="w-full lg:w-5/12 relative min-h-[320px] sm:min-h-[420px] lg:min-h-full overflow-hidden bg-[#0A0C10]">
                <!-- High-Resolution Dedicated Image with Smooth Zoom -->
                <img
                  [src]="s.imageUrl"
                  [alt]="s.name"
                  class="absolute inset-0 w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-700 filter brightness-[0.92] contrast-[1.08]"
                />

                <!-- Top & Bottom Cinematic Vignette Gradients -->
                <div class="absolute inset-0 bg-gradient-to-t from-[#0A0C10] via-black/20 to-black/60"></div>
                <div class="absolute inset-0 bg-gradient-to-r from-[#0A0C10]/60 via-transparent to-[#0A0C10]/60"></div>

                <!-- HUD Framing Brackets -->
                <div class="absolute inset-3 pointer-events-none border border-white/[0.08] rounded-2xl">
                  <div class="absolute top-0 left-0 w-3 h-3 border-t-2 border-l-2 border-[#00E676]"></div>
                  <div class="absolute top-0 right-0 w-3 h-3 border-t-2 border-r-2 border-[#00E676]"></div>
                  <div class="absolute bottom-0 left-0 w-3 h-3 border-b-2 border-l-2 border-[#00E676]"></div>
                  <div class="absolute bottom-0 right-0 w-3 h-3 border-b-2 border-r-2 border-[#00E676]"></div>
                </div>

                <!-- Top Telemetry Tag -->
                <div class="absolute top-5 left-5 right-5 flex items-center justify-between z-10 pointer-events-none">
                  <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-lg bg-black/80 backdrop-blur-md border border-white/10 text-[10px] font-['JetBrains_Mono'] text-white">
                    <span class="w-2 h-2 rounded-full bg-[#00E676] animate-pulse"></span>
                    <span class="font-bold tracking-wider">{{ s.divisionTag || 'DIVISION 01 // WORKSHOP' }}</span>
                  </div>

                  <span class="text-[10px] font-['JetBrains_Mono'] font-bold uppercase tracking-wider bg-black/80 backdrop-blur-md px-2.5 py-1 rounded-lg border border-white/10 text-[#38BDF8]">
                    {{ s.code }}
                  </span>
                </div>

                <!-- Bottom Image HUD Overlay -->
                <div class="absolute bottom-5 left-5 right-5 z-10 p-4 rounded-xl bg-[#0A0C10]/90 backdrop-blur-md border border-white/10 shadow-lg">
                  <div class="flex items-center justify-between text-[10px] sm:text-[11px] font-['JetBrains_Mono'] mb-1">
                    <span class="text-gray-400 uppercase tracking-wider font-semibold">Diagnostic Telemetry</span>
                    <span class="text-[#00E676] font-bold flex items-center gap-1.5">
                      <span class="w-1.5 h-1.5 rounded-full bg-[#00E676]"></span>
                      CALIBRATED & VERIFIED
                    </span>
                  </div>
                  <div class="text-[11px] font-mono text-gray-200 truncate">
                    {{ s.telemetryTag || 'OBD-II LIVE • SHIM MICROMETER CALIBRATION' }}
                  </div>
                </div>
              </div>

            </div>
          </div>
        </div>

        <!-- No Results Fallback -->
        <div *ngIf="filteredServices.length === 0" class="text-center py-16 bg-[#11151F] rounded-2xl border border-white/[0.08]">
          <p class="text-gray-400 text-sm mb-4 font-['Plus_Jakarta_Sans']">No services match your search "{{ searchQuery }}".</p>
          <button (click)="resetFilters()" class="px-5 py-2.5 bg-[#00E676] text-[#0A0C10] text-xs font-black uppercase tracking-wider rounded-xl font-['Outfit']">
            Reset Filters
          </button>
        </div>

        <!-- ============================================================ -->
        <!-- INTERACTIVE SERVICE COST & BAY TIME ESTIMATOR               -->
        <!-- ============================================================ -->
        <div class="mt-24 bg-[#11151F] border border-white/[0.08] rounded-3xl p-6 sm:p-10 lg:p-12 relative overflow-hidden shadow-2xl scroll-reveal">
          <div class="absolute top-0 right-0 w-96 h-96 bg-[#00E676]/5 rounded-full blur-3xl pointer-events-none"></div>

          <div class="max-w-3xl mb-8">
            <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-white/[0.04] border border-white/[0.08] mb-3">
              <span class="w-2 h-2 rounded-full bg-[#00E676] animate-pulse"></span>
              <span class="text-xs font-['JetBrains_Mono'] uppercase tracking-widest text-[#00E676] font-bold">Interactive Calculator</span>
            </div>
            <h2 class="text-2xl sm:text-4xl font-black text-white font-['Outfit'] tracking-tight mb-2">
              Instant Service Cost & Bay Time Estimator
            </h2>
            <p class="text-xs sm:text-sm text-gray-400 font-['Plus_Jakarta_Sans']">
              Select your motorcycle displacement class and desired service package for real-time labor, factory fluid specifications, and bay turnaround estimates.
            </p>
          </div>

          <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
            <!-- Left Configurator Options (7 cols) -->
            <div class="lg:col-span-7 space-y-6">
              
              <!-- 1. Displacement CC Class -->
              <div>
                <label class="block text-xs font-['JetBrains_Mono'] uppercase text-gray-400 font-bold mb-2.5">
                  1. Motorcycle Displacement Class
                </label>
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5">
                  <button
                    *ngFor="let cc of ccClasses; let i = index"
                    (click)="selectedCcIndex = i"
                    type="button"
                    class="p-3.5 rounded-2xl text-left border transition-all text-xs"
                    [ngClass]="selectedCcIndex === i ? 'bg-[#00E676]/10 border-[#00E676] text-white shadow-[0_0_15px_rgba(0,230,118,0.2)]' : 'bg-[#0A0C10] border-white/[0.08] text-gray-400 hover:border-white/20'"
                  >
                    <div class="font-black text-sm font-['Outfit']" [ngClass]="selectedCcIndex === i ? 'text-[#00E676]' : 'text-white'">
                      {{ cc.label }}
                    </div>
                    <div class="text-[10px] text-gray-400 mt-1 line-clamp-1">
                      {{ cc.sub }}
                    </div>
                  </button>
                </div>
              </div>

              <!-- 2. Service Package Selection -->
              <div>
                <label class="block text-xs font-['JetBrains_Mono'] uppercase text-gray-400 font-bold mb-2.5">
                  2. Desired Service Package
                </label>
                <div class="space-y-2.5">
                  <button
                    *ngFor="let pkg of servicePackages; let i = index"
                    (click)="selectedPackageIndex = i"
                    type="button"
                    class="w-full p-4 rounded-2xl text-left border transition-all flex items-center justify-between"
                    [ngClass]="selectedPackageIndex === i ? 'bg-[#00E676]/10 border-[#00E676] text-white shadow-[0_0_15px_rgba(0,230,118,0.2)]' : 'bg-[#0A0C10] border-white/[0.08] text-gray-400 hover:border-white/20'"
                  >
                    <div>
                      <div class="font-bold text-sm text-white font-['Outfit'] flex items-center gap-2">
                        <span>{{ pkg.name }}</span>
                        <span *ngIf="selectedPackageIndex === i" class="text-[10px] px-2 py-0.5 rounded bg-[#00E676] text-[#0A0C10] font-black uppercase font-mono">Selected</span>
                      </div>
                      <div class="text-xs text-gray-400 mt-0.5 font-['Plus_Jakarta_Sans']">
                        {{ pkg.inspectionPoints }} Checklist Points • Standard Turnaround ~ {{ pkg.baseTime }}
                      </div>
                    </div>
                    <div class="text-right">
                      <span class="text-xs font-mono font-bold text-gray-300">Base</span>
                      <div class="text-sm font-black font-['JetBrains_Mono'] text-[#00E676]">₹{{ pkg.baseLabor }}</div>
                    </div>
                  </button>
                </div>
              </div>

            </div>

            <!-- Right Telemetry Summary Card (5 cols) -->
            <div class="lg:col-span-5 bg-[#0A0C10] border border-white/[0.1] rounded-2xl p-6 relative">
              <div class="flex items-center justify-between border-b border-white/[0.08] pb-4 mb-4">
                <div>
                  <span class="text-[10px] font-mono uppercase tracking-wider text-gray-400 block">Bay Telemetry Estimate</span>
                  <span class="text-base font-black text-white font-['Outfit']">{{ currentPackage.name }}</span>
                </div>
                <span class="text-xs font-['JetBrains_Mono'] text-[#38BDF8] bg-[#38BDF8]/10 px-2.5 py-1 rounded border border-[#38BDF8]/20 font-bold">
                  {{ currentCc.label }}
                </span>
              </div>

              <!-- Metrics -->
              <div class="space-y-3.5 mb-6 text-xs">
                <div class="flex items-center justify-between">
                  <span class="text-gray-400 font-['Plus_Jakarta_Sans']">Estimated Bay Labor</span>
                  <span class="font-black font-['JetBrains_Mono'] text-white text-base">₹{{ estimatedLabor }}</span>
                </div>
                <div class="flex items-center justify-between">
                  <span class="text-gray-400 font-['Plus_Jakarta_Sans']">Diagnostics & Checklist</span>
                  <span class="font-bold font-['JetBrains_Mono'] text-[#00E676]">{{ currentPackage.inspectionPoints }} Multi-Point Inspection</span>
                </div>
                <div class="flex items-center justify-between">
                  <span class="text-gray-400 font-['Plus_Jakarta_Sans']">Turnaround Bay Duration</span>
                  <span class="font-bold font-['JetBrains_Mono'] text-white">{{ currentPackage.baseTime }}</span>
                </div>
                <div class="pt-2 border-t border-white/[0.06]">
                  <span class="text-[11px] text-gray-400 block mb-1">Recommended Factory Fluid Spec:</span>
                  <span class="text-xs font-['JetBrains_Mono'] text-[#38BDF8] font-bold block bg-white/[0.03] p-2 rounded-lg border border-white/[0.06]">
                    {{ currentCc.fluid }}
                  </span>
                </div>
              </div>

              <!-- Action Button -->
              <button
                (click)="openEnquiry(currentPackage.name + ' (' + currentCc.label + ')')"
                class="btn-laser w-full py-3.5 bg-[#00E676] hover:bg-[#00c864] text-[#0A0C10] font-black text-xs uppercase tracking-wider rounded-xl transition-all shadow-[0_0_20px_rgba(0,230,118,0.3)] flex items-center justify-center gap-2 font-['Outfit']"
              >
                <span>Book Bay for this Setup</span>
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
              </button>
              <p class="text-[10px] text-gray-400 text-center mt-2.5 font-['JetBrains_Mono']">
                *Fluids and OEM parts billed additionally at factory list price with warranty.
              </p>
            </div>
          </div>
        </div>

        <!-- ============================================================ -->
        <!-- RIDERS FAQ ACCORDION                                         -->
        <!-- ============================================================ -->
        <div class="mt-24 mb-16 scroll-reveal">
          <div class="text-center max-w-2xl mx-auto mb-12">
            <span class="text-xs font-['JetBrains_Mono'] text-[#00E676] uppercase tracking-widest font-bold block mb-2">Knowledge Base</span>
            <h2 class="text-3xl sm:text-4xl font-black text-white font-['Outfit'] tracking-tight mb-3">
              Frequently Asked Rider Questions
            </h2>
            <p class="text-xs sm:text-sm text-gray-400 font-['Plus_Jakarta_Sans']">
              Clear answers regarding our Motul fluid specifications, OEM spare parts, Dyno sessions, and bay scheduling.
            </p>
          </div>

          <div class="max-w-3xl mx-auto space-y-3.5">
            <div
              *ngFor="let faq of faqs; let i = index"
              class="rounded-2xl border transition-all duration-200 overflow-hidden"
              [ngClass]="expandedFaq === i ? 'bg-[#11151F] border-[#00E676]/40 shadow-[0_0_20px_rgba(0,230,118,0.1)]' : 'bg-[#11151F]/60 border-white/[0.08] hover:border-white/[0.2]'"
            >
              <button
                (click)="toggleFaq(i)"
                type="button"
                class="w-full p-5 text-left flex items-center justify-between gap-4 font-['Outfit'] font-bold text-sm sm:text-base text-white"
              >
                <span class="flex items-center gap-3">
                  <span class="text-xs font-mono font-bold" [ngClass]="expandedFaq === i ? 'text-[#00E676]' : 'text-gray-500'">0{{ i + 1 }}</span>
                  <span>{{ faq.question }}</span>
                </span>
                <span class="w-7 h-7 rounded-full bg-white/[0.04] border border-white/[0.1] flex items-center justify-center shrink-0 text-sm transition-transform duration-200"
                      [ngClass]="expandedFaq === i ? 'rotate-180 text-[#00E676] border-[#00E676]/30' : 'text-gray-400'">
                  ↓
                </span>
              </button>

              <div *ngIf="expandedFaq === i" class="px-5 pb-5 pt-1 text-xs sm:text-sm text-gray-300 font-['Plus_Jakarta_Sans'] leading-relaxed border-t border-white/[0.04]">
                {{ faq.answer }}
              </div>
            </div>
          </div>
        </div>

      </div>

      <!-- ENQUIRY MODAL -->
      <app-enquiry-modal
        [isOpen]="isModalOpen"
        [preselectedService]="selectedService"
        (close)="isModalOpen = false"
      ></app-enquiry-modal>

    </div>
  `
})
export class ServicesComponent implements OnInit {
  services: WorkshopService[] = [];
  categories: string[] = ['All', 'Superbike Care', 'Nitro Modz', 'Routine Care', 'Engine & Brakes', 'Detailing'];
  selectedCategory = 'All';
  searchQuery = '';
  isModalOpen = false;
  selectedService = '';

  constructor(private dataService: DataService, private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.services = this.dataService.getServices();

    this.route.fragment.subscribe(frag => {
      if (frag === 'superbike') this.selectedCategory = 'Superbike Care';
      else if (frag === 'modz') this.selectedCategory = 'Nitro Modz';
      else if (frag === 'routine') this.selectedCategory = 'Routine Care';
      else if (frag === 'brakes') this.selectedCategory = 'Engine & Brakes';
    });
  }

  getCount(cat: string): number {
    if (cat === 'All') return this.services.length;
    return this.services.filter(s => s.category === cat).length;
  }

  get filteredServices(): WorkshopService[] {
    return this.services.filter(s => {
      const matchesCat = this.selectedCategory === 'All' || s.category === this.selectedCategory;
      const q = this.searchQuery.toLowerCase().trim();
      const matchesSearch = !q ||
        s.name.toLowerCase().includes(q) ||
        (s.shortDescription || s.shortDesc || '').toLowerCase().includes(q) ||
        (s.includedItems || s.includedList || []).some((item: string) => item.toLowerCase().includes(q));
      return matchesCat && matchesSearch;
    });
  }

  resetFilters(): void {
    this.selectedCategory = 'All';
    this.searchQuery = '';
  }

  openEnquiry(serviceName?: string): void {
    this.selectedService = serviceName || 'General Service';
    this.isModalOpen = true;
  }

  // Estimator Data
  ccClasses = [
    { label: '150cc – 250cc', sub: 'KTM RC200, R15 V4, MT-15, Gixxer SF250', multiplier: 1.0, fluid: 'Motul 7100 10W40 (1.2L – 1.5L)' },
    { label: '300cc – 450cc', sub: 'Duke 390, Ninja 400, Himalayan 450, Aprilia 457', multiplier: 1.35, fluid: 'Motul 300V Factory Line 15W50 (1.7L – 2.0L)' },
    { label: '650cc – 1400cc', sub: 'Continental GT650, ZX-10R, S1000RR, Hayabusa', multiplier: 2.1, fluid: 'Motul 300V² 4T 10W50 Ester Core (3.2L – 4.0L)' }
  ];

  servicePackages = [
    { id: 'routine', name: 'Factory Routine Bay Service', baseLabor: 1499, baseTime: '2.5 Hours', inspectionPoints: 42 },
    { id: 'track', name: 'Track-Spec Diagnostic & Brake Flush', baseLabor: 3499, baseTime: '4.5 Hours', inspectionPoints: 68 },
    { id: 'rebuild', name: 'Comprehensive Engine Rebuild & Shims', baseLabor: 7999, baseTime: '2 – 3 Days', inspectionPoints: 95 }
  ];

  selectedCcIndex = 0;
  selectedPackageIndex = 0;

  get currentCc() {
    return this.ccClasses[this.selectedCcIndex];
  }

  get currentPackage() {
    return this.servicePackages[this.selectedPackageIndex];
  }

  get estimatedLabor(): number {
    return Math.round(this.currentPackage.baseLabor * this.currentCc.multiplier);
  }

  // FAQ Accordion State
  expandedFaq: number | null = 0; // Default first open

  faqs = [
    {
      question: 'How frequently should I schedule Motul 300V Factory Line oil changes?',
      answer: 'For high-revving track bikes and aggressive street riding, we recommend fluid replacement every 3,000 km or 6 months. 300V Ester Core provides unmatched shear resistance and high-temperature film stability under intense thermal loads.'
    },
    {
      question: 'Do you provide genuine OEM spare parts for European & Japanese superbikes?',
      answer: 'Yes. Both our Ambattur and Avadi hubs maintain verified supplier pipelines for genuine OEM Brembo pads, NGK Iridium plugs, K&N / BMC air filters, and factory clutch assemblies for Kawasaki, Ducati, BMW Motorrad, Honda, Yamaha, Triumph, and Royal Enfield twins.'
    },
    {
      question: 'Can I wait in the Rider Lounge while my motorcycle is being serviced in the bay?',
      answer: 'Absolutely. Our Ambattur Flagship Hub features a sound-insulated, air-conditioned Rider Lounge with direct viewing glass into the 6 diagnostic bays, high-speed Wi-Fi, Motul espresso bar, and live digital bay status monitors.'
    },
    {
      question: 'What is included in the 68-Point Superbike Diagnostic Bay inspection?',
      answer: 'Our technicians perform computerized OBD-II fault logging, digital throttle body synchronization, micrometer valve clearance shimming, fork seal stiction analysis, laser wheel alignment, steering head bearing torque check, and hydraulic DOT 5.1 brake bleeding.'
    },
    {
      question: 'Do you offer emergency towing and recovery if my bike breaks down in Chennai?',
      answer: 'Yes, our 24/7 dedicated motorcycle recovery flatbed is equipped with pneumatic soft-tie wheel chocks that protect fairings and anodized finishes. Call our emergency hotline at +91 98400 11223 for immediate dispatch across Chennai and outer corridors.'
    }
  ];

  toggleFaq(index: number): void {
    this.expandedFaq = this.expandedFaq === index ? null : index;
  }
}
