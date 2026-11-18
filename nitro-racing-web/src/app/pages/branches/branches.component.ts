import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DataService } from '../../services/data.service';
import { Branch } from '../../models/service.model';
import { EnquiryModalComponent } from '../../components/enquiry-modal/enquiry-modal.component';

@Component({
  selector: 'app-branches',
  standalone: true,
  imports: [CommonModule, EnquiryModalComponent],
  template: `
    <div class="bg-[#0A0C10] text-white pt-24 sm:pt-28 pb-20 sm:pb-24 min-h-screen">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">

        <!-- Page Header -->
        <div class="text-center max-w-3xl mx-auto mb-10 sm:mb-16 animate-fade-in-down">
          <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-white/[0.04] border border-white/[0.08] mb-3 sm:mb-4">
            <span class="w-2 h-2 rounded-full bg-[#00E676] animate-pulse"></span>
            <span class="text-[11px] sm:text-xs font-['JetBrains_Mono'] uppercase tracking-widest text-gray-300">Dual Strategic Chennai Hubs</span>
          </div>
          <h1 class="text-3xl sm:text-5xl lg:text-6xl font-black uppercase text-white tracking-tight mb-3 sm:mb-5 font-['Outfit']">
            NITRO RACING <span class="text-[#00E676]">Showroom & Hubs</span>
          </h1>
          <p class="text-gray-400 text-xs sm:text-base lg:text-lg leading-relaxed font-['Plus_Jakarta_Sans'] max-w-2xl mx-auto">
            State-of-the-art superbike showrooms and integrated multi-bay service workshops across Ambattur SIDCO and Avadi.
          </p>

          <!-- Telemetry HUD Counters -->
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5 sm:gap-3 mt-6 sm:mt-8 scroll-reveal">
            <div class="p-3 sm:p-4 rounded-xl sm:rounded-2xl bg-[#11151F] border border-white/[0.08] hover:border-[#00E676]/30 transition-all text-center">
              <span class="text-xl sm:text-3xl font-black text-white font-['JetBrains_Mono'] block">10</span>
              <span class="text-[10px] sm:text-[11px] font-['JetBrains_Mono'] uppercase text-gray-400">Diagnostic Bays</span>
            </div>
            <div class="p-3 sm:p-4 rounded-xl sm:rounded-2xl bg-[#11151F] border border-white/[0.08] hover:border-[#00E676]/30 transition-all text-center">
              <span class="text-xl sm:text-3xl font-black text-[#00E676] font-['JetBrains_Mono'] block">300V</span>
              <span class="text-[10px] sm:text-[11px] font-['JetBrains_Mono'] uppercase text-gray-400">Motul Factory Line</span>
            </div>
            <div class="p-3 sm:p-4 rounded-xl sm:rounded-2xl bg-[#11151F] border border-white/[0.08] hover:border-[#00E676]/30 transition-all text-center">
              <span class="text-xl sm:text-3xl font-black text-white font-['JetBrains_Mono'] block">100%</span>
              <span class="text-[10px] sm:text-[11px] font-['JetBrains_Mono'] uppercase text-gray-400">Torque Calibrated</span>
            </div>
            <div class="p-3 sm:p-4 rounded-xl sm:rounded-2xl bg-[#11151F] border border-white/[0.08] hover:border-[#00E676]/30 transition-all text-center">
              <span class="text-xl sm:text-3xl font-black text-[#38BDF8] font-['JetBrains_Mono'] block">24/7</span>
              <span class="text-[10px] sm:text-[11px] font-['JetBrains_Mono'] uppercase text-gray-400">Flatbed Recovery</span>
            </div>
          </div>
        </div>

        <!-- ============================================================ -->
        <!-- 1. DEDICATED MOBILE & TABLET VIEW (block lg:hidden)          -->
        <!-- Streamlined layout, zero clutter, 1-tap dialer & navigation  -->
        <!-- ============================================================ -->
        <div class="block lg:hidden space-y-6 mb-14">
          <div
            *ngFor="let branch of branches"
            class="bg-[#11151F] border border-white/[0.08] rounded-2xl p-4 sm:p-6 shadow-xl scroll-reveal"
          >
            <!-- Clean Showroom Photo -->
            <div class="relative w-full aspect-[16/9] rounded-xl overflow-hidden bg-[#0A0C10] mb-4 border border-white/[0.08]">
              <img
                [src]="branch.imageUrl || (branch.id === 'ambattur' ? 'images/branches/branch_ambattur.jpg' : 'images/branches/branch_avadi.jpg')"
                [alt]="branch.name"
                class="w-full h-full object-cover object-center filter brightness-[0.95]"
              />
              <div class="absolute inset-0 bg-gradient-to-t from-black/50 via-transparent to-black/30 pointer-events-none"></div>

              <!-- Minimal Clean Top Tag -->
              <div class="absolute top-2.5 left-2.5 right-2.5 flex items-center justify-between pointer-events-none">
                <span class="px-2.5 py-1 rounded-md bg-black/85 backdrop-blur-md border border-white/10 text-[10px] font-['JetBrains_Mono'] text-[#00E676] font-bold flex items-center gap-1.5">
                  <span class="w-1.5 h-1.5 rounded-full bg-[#00E676] animate-pulse"></span>
                  <span>{{ branch.bayCountText }}</span>
                </span>
                <span class="px-2 py-0.5 rounded-md bg-black/85 backdrop-blur-md text-[10px] font-mono font-bold text-gray-300 border border-white/10">
                  {{ branch.code }}
                </span>
              </div>
            </div>

            <!-- Title & Subtitle -->
            <div class="mb-3">
              <span class="text-[10px] font-['JetBrains_Mono'] uppercase tracking-wider text-[#00E676] font-bold block mb-1">
                {{ branch.hubBadge }}
              </span>
              <h2 class="text-xl sm:text-2xl font-black text-white font-['Outfit'] leading-tight mb-1">
                {{ branch.name }}
              </h2>
              <p class="text-xs text-gray-400 font-['Plus_Jakarta_Sans']">
                {{ branch.tagline }}
              </p>
            </div>

            <!-- Address Strip -->
            <div class="p-3 rounded-xl bg-[#0A0C10] border border-white/[0.06] mb-3 text-xs">
              <div class="flex items-start gap-2 text-gray-200 font-['Plus_Jakarta_Sans'] leading-snug">
                <span class="text-[#00E676] font-bold">📍</span>
                <span>{{ branch.address }}</span>
              </div>
              <span class="text-[11px] text-gray-400 font-['JetBrains_Mono'] block mt-1.5 pl-5">
                Landmark: <strong class="text-gray-300">{{ branch.landmark }}</strong>
              </span>
            </div>

            <!-- Essential Specs Chips -->
            <div class="flex flex-wrap gap-1.5 mb-3.5">
              <span *ngFor="let s of branch.specialties?.slice(0, 3)" class="text-[10px] font-mono text-gray-300 bg-white/[0.04] px-2.5 py-1 rounded-md border border-white/[0.08]">
                ✓ {{ s }}
              </span>
            </div>

            <!-- Compact Supervisor & Timing Strip -->
            <div class="flex items-center justify-between p-2.5 rounded-xl bg-white/[0.02] border border-white/[0.05] mb-4 text-[11px] font-['JetBrains_Mono']">
              <div>
                <span class="text-gray-500 block text-[9px] uppercase">Supervisor</span>
                <span class="text-white font-semibold">{{ getShortManager(branch.managerName) }}</span>
              </div>
              <div class="text-right">
                <span class="text-gray-500 block text-[9px] uppercase">Hours</span>
                <span class="text-gray-200">8:30 AM – 8:00 PM</span>
              </div>
            </div>

            <!-- Mobile 1-Tap Actions (Big thumb targets) -->
            <div class="grid grid-cols-2 gap-2">
              <button
                (click)="openBranchBooking(branch.name)"
                class="btn-laser py-3 bg-[#00E676] active:bg-[#00c864] text-[#0A0C10] font-black text-xs uppercase tracking-wider rounded-xl transition-all shadow-[0_0_15px_rgba(0,230,118,0.25)] flex items-center justify-center gap-1.5 font-['Outfit']"
              >
                <span>Book Slot</span>
                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
              </button>

              <a
                [href]="'tel:' + branch.phone"
                class="py-3 bg-[#151A26] active:bg-[#1E2435] text-[#00E676] font-bold text-xs uppercase tracking-wider rounded-xl border border-[#00E676]/30 flex items-center justify-center gap-1.5 font-['JetBrains_Mono']"
              >
                <svg class="w-3.5 h-3.5 text-[#00E676]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
                <span>Call Hotline</span>
              </a>
            </div>

            <!-- Directions Link -->
            <div class="mt-2 text-center">
              <a
                [href]="branch.mapsUrl"
                target="_blank"
                rel="noopener noreferrer"
                class="text-[11px] text-gray-400 hover:text-white inline-flex items-center gap-1 font-['Plus_Jakarta_Sans'] py-1"
              >
                <span>Open in Google Maps Navigation</span>
                <span>↗</span>
              </a>
            </div>
          </div>
        </div>

        <!-- ============================================================ -->
        <!-- 2. DESKTOP WIDESCREEN VIEW (hidden lg:block)                 -->
        <!-- Full widescreen showroom presentation + 2-column breakdown  -->
        <!-- ============================================================ -->
        <div class="hidden lg:block space-y-16 mb-20">
          <div
            *ngFor="let branch of branches; let i = index"
            class="group bg-[#11151F] border border-white/[0.08] hover:border-[#00E676]/40 rounded-3xl p-8 lg:p-10 transition-all duration-300 shadow-2xl hover:shadow-[0_0_35px_rgba(0,230,118,0.12)] scroll-reveal"
          >
            <!-- Showroom Photo Card with Docked Telemetry Bar -->
            <div class="rounded-2xl overflow-hidden bg-[#0A0C10] mb-8 border border-white/[0.08]">
              <!-- Widescreen Image -->
              <div class="relative w-full aspect-[16/7] min-h-[300px] overflow-hidden bg-[#0A0C10]">
                <img
                  [src]="branch.imageUrl || (branch.id === 'ambattur' ? 'images/branches/branch_ambattur.jpg' : 'images/branches/branch_avadi.jpg')"
                  [alt]="branch.name + ' Showroom & Service Bay Floor'"
                  class="absolute inset-0 w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-700 filter brightness-[0.94] contrast-[1.06]"
                />

                <!-- Dark Vignettes -->
                <div class="absolute inset-0 bg-gradient-to-t from-[#0A0C10] via-black/20 to-black/60 pointer-events-none"></div>
                <div class="absolute inset-0 bg-gradient-to-r from-[#0A0C10]/40 via-transparent to-[#0A0C10]/40 pointer-events-none"></div>

                <!-- HUD Brackets -->
                <div class="absolute inset-4 pointer-events-none border border-white/[0.08] rounded-xl">
                  <div class="absolute top-0 left-0 w-3.5 h-3.5 border-t-2 border-l-2 border-[#00E676]"></div>
                  <div class="absolute top-0 right-0 w-3.5 h-3.5 border-t-2 border-r-2 border-[#00E676]"></div>
                  <div class="absolute bottom-0 left-0 w-3.5 h-3.5 border-b-2 border-l-2 border-[#00E676]"></div>
                  <div class="absolute bottom-0 right-0 w-3.5 h-3.5 border-b-2 border-r-2 border-[#00E676]"></div>
                </div>

                <!-- Top Telemetry Strip -->
                <div class="absolute top-5 left-5 right-5 flex items-center justify-between z-10 pointer-events-none">
                  <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-lg bg-black/80 backdrop-blur-md border border-white/10 text-xs font-['JetBrains_Mono'] text-white">
                    <span class="w-2 h-2 rounded-full bg-[#00E676] animate-pulse"></span>
                    <span class="font-bold tracking-wider">{{ branch.hubBadge || 'SHOWROOM & WORKSHOP FLOOR' }}</span>
                  </div>

                  <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-lg bg-black/80 backdrop-blur-md border border-white/10 text-xs font-['JetBrains_Mono'] text-[#38BDF8]">
                    <span class="font-bold">{{ branch.bayCountText }}</span>
                    <span class="text-gray-400">|</span>
                    <span class="text-white">{{ branch.code }}</span>
                  </div>
                </div>
              </div>

              <!-- Docked Telemetry Control Bar (Never overlaps the photo!) -->
              <div class="px-6 py-3.5 bg-[#0A0C10] border-t border-white/[0.08] flex items-center justify-between text-xs font-['JetBrains_Mono']">
                <div class="flex items-center gap-2.5">
                  <span class="w-2 h-2 rounded-full bg-[#00E676] animate-pulse"></span>
                  <span class="text-[#00E676] font-bold uppercase tracking-wider text-[11px]">SHOWROOM & REPAIR WORKSHOP LIVE</span>
                  <span class="text-gray-600">•</span>
                  <span class="text-gray-300 font-['Outfit'] font-medium text-xs">
                    {{ branch.id === 'ambattur' ? '6 SCISSOR LIFTS • MOTUL FLUID BAR • DYNO ROOM • RIDER LOUNGE' : '4 SCISSOR LIFTS • TIG WELDING • CUSTOM NITRO MODZ STUDIO' }}
                  </span>
                </div>

                <div class="text-right font-['JetBrains_Mono'] text-[11px] text-gray-400 hidden xl:block">
                  <span>Chennai Facility GPS Coordinates Verified</span>
                </div>
              </div>
            </div>

            <!-- Structured 2-Column Details -->
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
              
              <!-- Left Column: Location, Identity & Key Bay Stations -->
              <div class="lg:col-span-7 space-y-6">
                <div>
                  <div class="flex items-center gap-2 mb-2">
                    <span class="text-xs font-['JetBrains_Mono'] uppercase tracking-wider px-3 py-1 rounded-md bg-[#00E676]/10 text-[#00E676] border border-[#00E676]/25 font-bold">
                      {{ branch.hubBadge }}
                    </span>
                    <span class="text-xs text-gray-300 font-['JetBrains_Mono'] bg-white/[0.04] px-2.5 py-1 rounded border border-white/[0.06]">
                      {{ branch.code }}
                    </span>
                  </div>
                  <h2 class="text-3xl lg:text-4xl font-black text-white group-hover:text-[#00E676] transition-colors mb-2 font-['Outfit'] tracking-tight">
                    {{ branch.name }}
                  </h2>
                  <p class="text-sm font-['JetBrains_Mono'] text-[#00E676] font-semibold">
                    {{ branch.tagline }}
                  </p>
                </div>

                <!-- Physical Address Box -->
                <div class="p-4 rounded-2xl bg-[#0A0C10] border border-white/[0.06] flex items-start gap-3">
                  <div class="w-8 h-8 rounded-xl bg-[#00E676]/10 border border-[#00E676]/20 text-[#00E676] flex items-center justify-center shrink-0 mt-0.5">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
                  </div>
                  <div>
                    <span class="text-xs text-white font-medium block leading-relaxed font-['Plus_Jakarta_Sans']">
                      {{ branch.address }}
                    </span>
                    <span class="text-[11px] text-gray-400 font-['JetBrains_Mono'] block mt-1">
                      Landmark: <strong class="text-gray-300">{{ branch.landmark }}</strong>
                    </span>
                  </div>
                </div>

                <!-- Core Bay Stations & Capabilities Grid -->
                <div>
                  <span class="text-[10px] uppercase font-bold text-gray-400 tracking-wider block mb-3 font-['JetBrains_Mono']">
                    Core Bay Stations & Capabilities
                  </span>
                  <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
                    <div *ngFor="let eq of branch.keyEquipments" class="p-3.5 rounded-xl bg-white/[0.02] border border-white/[0.06]">
                      <span class="text-xs font-bold text-white flex items-center gap-1.5 font-['Outfit'] mb-1">
                        <span class="text-[#00E676]">✓</span>
                        <span>{{ eq.title }}</span>
                      </span>
                      <p class="text-[11px] text-gray-400 leading-snug font-['Plus_Jakarta_Sans']">
                        {{ eq.desc }}
                      </p>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Right Column: Operational Telemetry & Action Buttons -->
              <div class="lg:col-span-5 space-y-6">
                <!-- Operational Telemetry Card -->
                <div class="bg-[#0A0C10] rounded-2xl p-6 border border-white/[0.08] space-y-3.5 text-xs font-['JetBrains_Mono']">
                  <div class="flex justify-between items-center border-b border-white/[0.04] pb-2.5">
                    <span class="text-gray-400">Lead Supervisor:</span>
                    <span class="font-bold text-white">{{ branch.managerName }}</span>
                  </div>
                  <div class="flex justify-between items-center border-b border-white/[0.04] pb-2.5">
                    <span class="text-gray-400">Direct Workshop Hotline:</span>
                    <a [href]="'tel:' + branch.phone" class="font-bold text-[#00E676] hover:underline inline-flex items-center gap-1.5">
                      <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
                      <span>{{ branch.phone }}</span>
                    </a>
                  </div>
                  <div class="flex justify-between items-center border-b border-white/[0.04] pb-2.5">
                    <span class="text-gray-400">Operating Schedule:</span>
                    <span class="text-white font-medium">{{ branch.workingHours }}</span>
                  </div>
                  <div class="flex justify-between items-center border-b border-white/[0.04] pb-2.5">
                    <span class="text-gray-400">Sunday Status:</span>
                    <span class="text-gray-300 font-medium">{{ branch.hoursSunday }}</span>
                  </div>
                  <div class="flex justify-between items-center">
                    <span class="text-gray-400">GSTIN Registered:</span>
                    <span class="text-gray-400 font-mono text-[11px]">{{ branch.gstin }}</span>
                  </div>
                </div>

                <!-- Action Button Cluster -->
                <div class="space-y-3">
                  <button
                    (click)="openBranchBooking(branch.name)"
                    class="btn-laser w-full py-4 bg-[#00E676] hover:bg-[#00c864] text-[#0A0C10] font-black text-xs uppercase tracking-wider rounded-xl transition-all shadow-[0_0_20px_rgba(0,230,118,0.3)] flex items-center justify-center gap-2 font-['Outfit'] hover:-translate-y-0.5"
                  >
                    <span>Book Bay at {{ branch.id === 'ambattur' ? 'Ambattur' : 'Avadi' }}</span>
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
                  </button>

                  <div class="grid grid-cols-2 gap-3">
                    <a
                      [href]="'tel:' + branch.phone"
                      aria-label="Call branch directly"
                      class="py-3.5 bg-[#151A26] hover:bg-[#1E2435] text-[#00E676] text-xs font-bold rounded-xl border border-white/[0.1] flex items-center justify-center gap-2 font-['JetBrains_Mono'] transition-colors hover:-translate-y-0.5"
                    >
                      <svg class="w-3.5 h-3.5 text-[#00E676]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
                      <span>Direct Call</span>
                    </a>

                    <a
                      [href]="branch.mapsUrl"
                      target="_blank"
                      rel="noopener noreferrer"
                      class="py-3.5 bg-white/[0.05] hover:bg-white/[0.1] text-white text-xs font-bold uppercase tracking-wider rounded-xl border border-white/[0.1] transition-colors flex items-center justify-center gap-2 font-['Outfit'] hover:-translate-y-0.5"
                    >
                      <span>Directions</span>
                      <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
                    </a>
                  </div>
                </div>
              </div>

            </div>
          </div>
        </div>

        <!-- Full Workshop Amenities Matrix -->
        <div class="mb-14 sm:mb-16 scroll-reveal">
          <div class="text-center max-w-2xl mx-auto mb-8 sm:mb-10">
            <h3 class="text-2xl sm:text-3xl font-black uppercase text-white font-['Outfit'] mb-2 sm:mb-3">
              Standard Across Both <span class="text-[#00E676]">Workshops</span>
            </h3>
            <p class="text-xs sm:text-sm text-gray-400 font-['Plus_Jakarta_Sans']">
              Every Nitro Racing facility adheres to strict race-grade cleanliness, calibrated pneumatic equipment, and transparent digital workflows.
            </p>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4 sm:gap-6">
            <div class="p-5 sm:p-6 rounded-2xl bg-[#11151F] border border-white/[0.08] hover:border-[#00E676]/30 transition-all">
              <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-xl bg-[#00E676]/10 text-[#00E676] flex items-center justify-center font-bold mb-3 sm:mb-4 font-mono text-base sm:text-lg">
                01
              </div>
              <h4 class="text-sm sm:text-base font-bold text-white uppercase font-['Outfit'] mb-1.5 sm:mb-2">Pneumatic Scissor Lifts</h4>
              <p class="text-xs text-gray-400 leading-relaxed font-['Plus_Jakarta_Sans']">
                Heavy-duty hydraulic platform lifts with rubberized frame pads prevent underbody scratches on liter-class and adventure bikes.
              </p>
            </div>

            <div class="p-5 sm:p-6 rounded-2xl bg-[#11151F] border border-white/[0.08] hover:border-[#00E676]/30 transition-all">
              <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-xl bg-[#00E676]/10 text-[#00E676] flex items-center justify-center font-bold mb-3 sm:mb-4 font-mono text-base sm:text-lg">
                02
              </div>
              <h4 class="text-sm sm:text-base font-bold text-white uppercase font-['Outfit'] mb-1.5 sm:mb-2">Live CCTV AC Lounge</h4>
              <p class="text-xs text-gray-400 leading-relaxed font-['Plus_Jakarta_Sans']">
                Relax in air-conditioned comfort with complimentary high-speed Wi-Fi while watching your machine through glass partitions and live cameras.
              </p>
            </div>

            <div class="p-5 sm:p-6 rounded-2xl bg-[#11151F] border border-white/[0.08] hover:border-[#00E676]/30 transition-all">
              <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-xl bg-[#00E676]/10 text-[#00E676] flex items-center justify-center font-bold mb-3 sm:mb-4 font-mono text-base sm:text-lg">
                03
              </div>
              <h4 class="text-sm sm:text-base font-bold text-white uppercase font-['Outfit'] mb-1.5 sm:mb-2">Digital Torque Tooling</h4>
              <p class="text-xs text-gray-400 leading-relaxed font-['Plus_Jakarta_Sans']">
                Zero stripped threads. Every axle nut, caliper bolt, and engine case fastener is tightened using digital click torque wrenches to exact OEM Nm specifications.
              </p>
            </div>

            <div class="p-5 sm:p-6 rounded-2xl bg-[#11151F] border border-white/[0.08] hover:border-[#00E676]/30 transition-all">
              <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-xl bg-[#00E676]/10 text-[#00E676] flex items-center justify-center font-bold mb-3 sm:mb-4 font-mono text-base sm:text-lg">
                04
              </div>
              <h4 class="text-sm sm:text-base font-bold text-white uppercase font-['Outfit'] mb-1.5 sm:mb-2">Motul Factory Line Sealed Stock</h4>
              <p class="text-xs text-gray-400 leading-relaxed font-['Plus_Jakarta_Sans']">
                Direct authorized sourcing. Motul 300V, 7100, DOT 5.1 racing brake fluid, and Engine Ice coolant opened in front of the customer or shared on WhatsApp.
              </p>
            </div>

            <div class="p-5 sm:p-6 rounded-2xl bg-[#11151F] border border-white/[0.08] hover:border-[#00E676]/30 transition-all">
              <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-xl bg-[#00E676]/10 text-[#00E676] flex items-center justify-center font-bold mb-3 sm:mb-4 font-mono text-base sm:text-lg">
                05
              </div>
              <h4 class="text-sm sm:text-base font-bold text-white uppercase font-['Outfit'] mb-1.5 sm:mb-2">Ultrasonic Wash Bays</h4>
              <p class="text-xs text-gray-400 leading-relaxed font-['Plus_Jakarta_Sans']">
                Dedicated non-corrosive foam baths, high-pressure degreasers, and heated ultrasonic tanks for cleaning carburetors, throttle bodies, and brake pistons.
              </p>
            </div>

            <div class="p-5 sm:p-6 rounded-2xl bg-[#11151F] border border-white/[0.08] hover:border-[#00E676]/30 transition-all">
              <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-xl bg-[#00E676]/10 text-[#00E676] flex items-center justify-center font-bold mb-3 sm:mb-4 font-mono text-base sm:text-lg">
                06
              </div>
              <h4 class="text-sm sm:text-base font-bold text-white uppercase font-['Outfit'] mb-1.5 sm:mb-2">Hydraulic Flatbed Truck</h4>
              <p class="text-xs text-gray-400 leading-relaxed font-['Plus_Jakarta_Sans']">
                Punctures or mechanical breakdown? Our dedicated hydraulic motorcycle flatbed recovery vehicle picks up immobilized bikes safely across Chennai.
              </p>
            </div>
          </div>
        </div>

        <!-- Flatbed Recovery Direct Hotline Strip -->
        <div class="p-6 sm:p-10 lg:p-12 rounded-3xl bg-gradient-to-r from-[#11151F] via-[#151A26] to-[#11151F] border border-white/[0.1] flex flex-col md:flex-row items-center justify-between gap-6">
          <div class="text-center md:text-left">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded bg-[#00E676]/10 text-[#00E676] text-xs font-['JetBrains_Mono'] font-bold uppercase tracking-wider mb-2">
              <span class="w-1.5 h-1.5 rounded-full bg-[#00E676] animate-pulse"></span>
              Emergency Flatbed Pickup
            </div>
            <h3 class="text-xl sm:text-2xl lg:text-3xl font-black text-white font-['Outfit'] uppercase mb-1">
              Immobilized Or Need Workshop Transport?
            </h3>
            <p class="text-xs sm:text-sm text-gray-400 font-['Plus_Jakarta_Sans'] max-w-xl">
              Hydraulic motorcycle ramp recovery truck on standby across Ambattur, Avadi, Anna Nagar, Porur, and OMR.
            </p>
          </div>

          <div class="flex items-center justify-center shrink-0 w-full md:w-auto">
            <a
              href="tel:+919840011223"
              class="w-full sm:w-auto px-6 py-4 bg-[#00E676] hover:bg-[#00c864] text-[#0A0C10] font-black text-xs uppercase tracking-wider rounded-xl transition-all shadow-[0_0_25px_rgba(0,230,118,0.3)] flex items-center justify-center gap-2 font-['Outfit']"
            >
              <svg class="w-4 h-4 text-[#0A0C10]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
              <span>Call Flatbed: +91 98400 11223</span>
            </a>
          </div>
        </div>

      </div>

      <!-- Modal -->
      <app-enquiry-modal
        [isOpen]="isModalOpen"
        [preselectedService]="preselectedBranch"
        (close)="isModalOpen = false"
      ></app-enquiry-modal>

    </div>
  `
})
export class BranchesComponent implements OnInit {
  branches: Branch[] = [];
  isModalOpen = false;
  preselectedBranch = 'Superbike Precision Service';

  constructor(private dataService: DataService) {}

  ngOnInit(): void {
    this.branches = this.dataService.getBranches();
  }

  openBranchBooking(branchName: string): void {
    this.preselectedBranch = branchName.includes('Ambattur') ? 'Ambattur Branch Service' : 'Avadi Modz & Service';
    this.isModalOpen = true;
  }

  getShortManager(name?: string): string {
    if (!name) return 'Branch Supervisor';
    return name.split('(')[0].trim();
  }
}
