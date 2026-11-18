import { Component, OnInit, OnDestroy, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { DataService } from '../../services/data.service';
import { WorkshopService, Branch, Testimonial } from '../../models/service.model';
import { EnquiryModalComponent } from '../../components/enquiry-modal/enquiry-modal.component';

export interface HeroSlide {
  id: number;
  tag: string;
  tagColor: string;
  title: string;
  highlight: string;
  description: string;
  specs: string[];
  image: string;
  alt: string;
  telemetry: string;
  primaryCtaText: string;
  serviceCategory: string;
  secondaryCtaText: string;
  secondaryRoute: string;
}

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, RouterLink, EnquiryModalComponent],
  template: `
    <div class="bg-[#0A0C10] text-[#CBD5E1]">

      <!-- ============================================================== -->
      <!-- MOBILE HERO DESIGN (block lg:hidden)                           -->
      <!-- Letters in Front & Background Handles Image Cleanly            -->
      <!-- ============================================================== -->
      <section class="block lg:hidden relative min-h-[92vh] flex flex-col justify-between overflow-hidden border-b border-white/[0.08] bg-[#0A0C10] select-none">
        
        <!-- BACK: Handled Background Image Layer with Depth Vignettes -->
        <div class="absolute inset-0 z-0">
          <div
            *ngFor="let s of slides; let i = index"
            class="absolute inset-0 transition-all duration-1000 ease-in-out"
            [ngClass]="i === currentSlide ? 'opacity-100 scale-100 z-10' : 'opacity-0 scale-105 pointer-events-none z-0'"
          >
            <img
              [src]="s.image"
              [alt]="s.alt"
              class="w-full h-full object-cover object-[center_35%] filter brightness-[0.70] contrast-[1.15]"
            />
            <!-- Top Dark Gradient (softens overhead ceiling lamps) -->
            <div class="absolute inset-x-0 top-0 h-44 bg-gradient-to-b from-[#0A0C10] via-[#0A0C10]/75 to-transparent"></div>
            <!-- Bottom Deep Gradient providing solid backdrop for front letters -->
            <div class="absolute inset-x-0 bottom-0 h-[65%] bg-gradient-to-t from-[#0A0C10] via-[#0A0C10]/95 via-50% to-transparent"></div>
          </div>
        </div>

        <!-- TOP: Floating Minimalist Tag & Auto-Moving Dots -->
        <div class="relative z-20 pt-20 px-5 flex items-center justify-between">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#0A0C10]/85 border border-white/[0.1] backdrop-blur-md">
            <span class="w-2 h-2 rounded-full bg-[#00E676] animate-pulse"></span>
            <span class="text-[10px] font-['JetBrains_Mono'] font-bold tracking-wider text-gray-200 uppercase">
              NITRO RACING • 2 HUBS
            </span>
          </div>

          <!-- Slide Indicator Dots -->
          <div class="flex items-center gap-1.5 bg-[#0A0C10]/85 px-2.5 py-1 rounded-full border border-white/[0.1] backdrop-blur-md">
            <button
              *ngFor="let s of slides; let i = index"
              (click)="goToSlide(i)"
              [attr.aria-label]="'Go to slide ' + (i + 1)"
              class="h-1 rounded-full transition-all duration-500"
              [ngClass]="i === currentSlide ? 'w-5 bg-[#00E676]' : 'w-1.5 bg-white/30'"
            ></button>
          </div>
        </div>

        <!-- FRONT: Letters & Typography in High-Contrast Foreground -->
        <div class="relative z-20 px-5 pb-8 pt-10 flex flex-col justify-end text-left">
          
          <!-- Category Division Tag -->
          <div class="mb-2.5">
            <span class="text-[11px] font-['JetBrains_Mono'] font-bold uppercase tracking-wider text-[#00E676] bg-[#00E676]/10 px-2.5 py-1 rounded border border-[#00E676]/20">
              {{ currentSlideData.tag }}
            </span>
          </div>

          <!-- Letters Headline (Clean, Bold, High Legibility) -->
          <h1 class="text-3xl sm:text-4xl font-black tracking-tight text-white font-['Outfit'] leading-[1.08] mb-3">
            <span>{{ currentSlideData.title }}</span> <br />
            <span class="text-[#00E676]">
              {{ currentSlideData.highlight }}
            </span>
          </h1>

          <!-- Letters Subtitle -->
          <p class="text-xs sm:text-sm text-gray-300 font-normal leading-relaxed mb-4 font-['Plus_Jakarta_Sans'] line-clamp-2">
            {{ currentSlideData.description }}
          </p>

          <!-- Specs Badges in Front (Solid Dark Backing for Sharp Readability) -->
          <div class="flex flex-wrap gap-2 mb-6">
            <span
              *ngFor="let spec of currentSlideData.specs.slice(0, 2)"
              class="text-[10px] font-['JetBrains_Mono'] px-2.5 py-1 rounded-lg bg-[#0A0C10] border border-white/[0.12] text-gray-200 flex items-center gap-1.5 shadow-md"
            >
              <span class="w-1.5 h-1.5 rounded-full bg-[#00E676]"></span>
              <span>{{ spec }}</span>
            </span>
            <span class="text-[10px] font-['JetBrains_Mono'] px-2.5 py-1 rounded-lg bg-[#0A0C10] border border-white/[0.12] text-gray-200 flex items-center gap-1.5 shadow-md">
              <span class="w-1.5 h-1.5 rounded-full bg-[#38BDF8]"></span>
              <span>Ambattur & Avadi</span>
            </span>
          </div>

          <!-- 1-Tap Mobile Actions -->
          <div class="flex flex-col gap-2.5 w-full">
            <button
              (click)="openEnquiryModal(currentSlideData.serviceCategory)"
              class="w-full py-4 bg-[#00E676] active:bg-[#00c864] text-[#0A0C10] font-black text-xs font-['Outfit'] uppercase tracking-wider rounded-xl transition-all shadow-[0_0_25px_rgba(0,230,118,0.35)] flex items-center justify-center gap-2"
            >
              <span>{{ currentSlideData.primaryCtaText }}</span>
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
            </button>

            <div class="grid grid-cols-2 gap-2">
              <a
                [routerLink]="currentSlideData.secondaryRoute"
                class="py-3 bg-white/[0.06] text-white font-bold text-xs font-['Outfit'] uppercase tracking-wider rounded-xl border border-white/[0.1] text-center transition-all flex items-center justify-center gap-1"
              >
                <span>Details →</span>
              </a>
              <a
                href="tel:+919840011223"
                class="py-3 bg-white/[0.06] hover:bg-white/[0.1] text-white font-bold text-xs font-['Outfit'] uppercase tracking-wider rounded-xl border border-white/[0.1] text-center transition-all flex items-center justify-center gap-1.5 font-mono"
              >
                <svg class="w-3.5 h-3.5 text-[#00E676]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
                <span>Call Hotline</span>
              </a>
            </div>
          </div>

          <!-- Micro Trust Strip -->
          <div class="mt-4 pt-3 border-t border-white/[0.08] flex items-center justify-between text-[10px] font-['JetBrains_Mono'] text-gray-400">
            <span>✓ Master Techs</span>
            <span>✓ Motul Sealed</span>
            <span>✓ Live WhatsApp</span>
          </div>

        </div>

      </section>

      <!-- ============================================================== -->
      <!-- DESKTOP HERO DESIGN (hidden lg:flex)                           -->
      <!-- Full-Fit Split Screen Luxury Automotive                        -->
      <!-- ============================================================== -->
      <section class="hidden lg:flex relative min-h-[85vh] lg:min-h-[88vh] items-center overflow-hidden border-b border-white/[0.08] bg-[#0A0C10]">
        
        <!-- RIGHT SIDE: Full-Fit Hero Images With Continuous Auto-Moving Fade -->
        <div class="w-full h-full absolute top-0 bottom-0 right-0 w-[50%] xl:w-[54%] z-0 overflow-hidden">
          <div
            *ngFor="let s of slides; let i = index"
            class="absolute inset-0 transition-all duration-1000 ease-in-out"
            [ngClass]="i === currentSlide ? 'opacity-100 scale-100 z-10' : 'opacity-0 scale-105 pointer-events-none z-0'"
          >
            <img
              [src]="s.image"
              [alt]="s.alt"
              class="w-full h-full object-cover object-center filter brightness-[0.88] contrast-[1.12]"
            />
            <!-- Gradient Blend: Seamlessly fades into matte black on the left on desktop -->
            <div class="absolute inset-0 bg-gradient-to-r from-[#0A0C10] via-[#0A0C10]/40 to-transparent"></div>
            <!-- Vertical Vignette -->
            <div class="absolute inset-0 bg-gradient-to-t from-[#0A0C10] via-transparent to-transparent"></div>
          </div>

          <!-- Right Bottom Telemetry Badge (Auto-updates with current slide) -->
          <div class="absolute bottom-6 right-6 z-20 flex items-center gap-3 font-['JetBrains_Mono'] pointer-events-none">
            <div class="relative bg-[#0A0C10]/90 border border-white/[0.12] backdrop-blur-md px-4 py-2.5 rounded-xl text-xs flex items-center gap-3 text-white shadow-2xl">
              <span class="w-2 h-2 rounded-full bg-[#00E676] animate-pulse"></span>
              <div class="flex flex-col text-left">
                <span class="text-[9px] uppercase tracking-widest text-[#00E676] font-bold">LIVE WORKSHOP TELEMETRY</span>
                <span class="text-xs text-gray-200 font-semibold">{{ currentSlideData.telemetry }}</span>
              </div>
              <!-- Mini HUD Brackets -->
              <div class="absolute -top-1 -left-1 w-2.5 h-2.5 border-t-2 border-l-2 border-[#00E676]"></div>
              <div class="absolute -bottom-1 -right-1 w-2.5 h-2.5 border-b-2 border-r-2 border-[#00E676]"></div>
            </div>
          </div>
        </div>

        <!-- LEFT SIDE: Content, Dynamic Specs & Actions (Auto-Moving) -->
        <div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 lg:py-20 w-full pointer-events-auto">
          <div class="grid grid-cols-1 lg:grid-cols-12 items-center">
            
            <div class="lg:col-span-7 xl:col-span-6 text-left flex flex-col justify-between">
              
              <!-- Clean Eyebrow Badge -->
              <div class="inline-flex items-center gap-2.5 px-3.5 py-1.5 rounded-full bg-white/[0.05] border border-white/[0.1] backdrop-blur-md mb-6 w-fit transition-all duration-500">
                <span class="w-2 h-2 rounded-full transition-colors duration-500" [style.backgroundColor]="currentSlideData.tagColor"></span>
                <span class="text-xs font-['JetBrains_Mono'] font-bold tracking-wider text-gray-200 uppercase">
                  {{ currentSlideData.tag }}
                </span>
              </div>

              <!-- Main Headline with Outfit Luxury Typography -->
              <div class="min-h-[140px] sm:min-h-[160px] flex flex-col justify-center mb-4">
                <h1 class="text-3xl sm:text-5xl lg:text-6xl font-black tracking-tight text-white font-['Outfit'] leading-[1.08] transition-opacity duration-500">
                  <span>{{ currentSlideData.title }}</span> <br />
                  <span class="text-transparent bg-clip-text bg-gradient-to-r from-white via-slate-200 to-[#00E676]">
                    {{ currentSlideData.highlight }}
                  </span>
                </h1>
              </div>

              <!-- Subtitle / Narrative -->
              <p class="text-sm sm:text-base text-gray-300 font-normal leading-relaxed mb-6 max-w-xl font-['Plus_Jakarta_Sans'] min-h-[72px] transition-opacity duration-500">
                {{ currentSlideData.description }}
              </p>

              <!-- Dynamic Specification Badges -->
              <div class="flex flex-wrap gap-2.5 mb-8 min-h-[42px]">
                <span
                  *ngFor="let spec of currentSlideData.specs"
                  class="text-xs font-['JetBrains_Mono'] px-3.5 py-1.5 rounded-xl bg-white/[0.05] border border-white/[0.1] text-gray-200 flex items-center gap-2 shadow-sm transition-all duration-500"
                >
                  <span class="w-1.5 h-1.5 rounded-full bg-[#00E676]"></span>
                  <span>{{ spec }}</span>
                </span>
              </div>

              <!-- Modern Action Buttons Suite -->
              <div class="flex flex-wrap items-center gap-3.5 mb-8">
                <!-- Primary Action Button -->
                <button
                  (click)="openEnquiryModal(currentSlideData.serviceCategory)"
                  class="group relative px-7 py-4 bg-[#00E676] hover:bg-[#00c864] text-[#0A0C10] font-black text-xs font-['Outfit'] uppercase tracking-wider rounded-xl transition-all duration-300 shadow-[0_0_25px_rgba(0,230,118,0.35)] hover:shadow-[0_0_35px_rgba(0,230,118,0.5)] flex items-center justify-center gap-2.5 overflow-hidden transform hover:-translate-y-0.5 active:translate-y-0"
                >
                  <span class="w-1.5 h-1.5 rounded-full bg-[#0A0C10] animate-pulse"></span>
                  <span>{{ currentSlideData.primaryCtaText }}</span>
                  <svg class="w-4 h-4 transition-transform group-hover:translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
                </button>

                <!-- Secondary Route Button -->
                <a
                  [routerLink]="currentSlideData.secondaryRoute"
                  class="px-6 py-4 bg-white/[0.05] hover:bg-white/[0.1] text-white font-bold text-xs font-['Outfit'] uppercase tracking-wider rounded-xl border border-white/[0.1] hover:border-white/[0.25] transition-all flex items-center justify-center gap-2 group backdrop-blur-sm"
                >
                  <span>{{ currentSlideData.secondaryCtaText }}</span>
                  <span class="text-[#00E676] transition-transform group-hover:translate-x-0.5">→</span>
                </a>

                <!-- Workshop Direct Hotline Call Button -->
                <a
                  href="tel:+919840011223"
                  class="px-5 py-4 bg-[#151A26]/80 hover:bg-[#1E2435] text-gray-200 hover:text-white font-bold text-xs font-['JetBrains_Mono'] uppercase tracking-wider rounded-xl border border-white/[0.1] hover:border-[#00E676]/40 transition-all flex items-center justify-center gap-2.5 backdrop-blur-sm shadow-lg group"
                >
                  <div class="w-6 h-6 rounded-lg bg-[#00E676]/10 border border-[#00E676]/30 flex items-center justify-center group-hover:bg-[#00E676] transition-colors">
                    <svg class="w-3.5 h-3.5 text-[#00E676] group-hover:text-black transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
                  </div>
                  <span>+91 98400 11223</span>
                </a>
              </div>

              <!-- Modern Segmented Slide Control Cards (Bottom of Hero Left) -->
              <div class="grid grid-cols-3 gap-3 pt-6 border-t border-white/[0.08]">
                <button
                  *ngFor="let s of slides; let i = index"
                  (click)="goToSlide(i)"
                  class="text-left p-3 rounded-xl border transition-all duration-300 relative overflow-hidden group cursor-pointer"
                  [ngClass]="i === currentSlide 
                    ? 'bg-[#151A26] border-[#00E676]/50 shadow-[0_0_20px_rgba(0,230,118,0.15)]' 
                    : 'bg-white/[0.02] border-white/[0.06] hover:bg-white/[0.05] hover:border-white/[0.15]'"
                >
                  <!-- Active Top Highlight Line -->
                  <div 
                    class="absolute top-0 left-0 h-[2px] transition-all duration-500"
                    [ngClass]="i === currentSlide ? 'w-full bg-[#00E676]' : 'w-0 group-hover:w-1/2 bg-white/20'"
                  ></div>
                  <div class="flex items-center justify-between mb-1">
                    <span class="text-[10px] font-['JetBrains_Mono'] font-bold uppercase tracking-wider"
                          [ngClass]="i === currentSlide ? 'text-[#00E676]' : 'text-gray-500 group-hover:text-gray-400'">
                      0{{ i + 1 }} // {{ i === 0 ? 'SUPERBIKE' : (i === 1 ? 'MODZ' : 'WORKSHOP') }}
                    </span>
                    <span *ngIf="i === currentSlide" class="w-1.5 h-1.5 rounded-full bg-[#00E676] animate-pulse"></span>
                  </div>
                  <span class="text-xs font-bold text-white font-['Outfit'] block truncate">
                    {{ s.highlight }}
                  </span>
                </button>
              </div>

              <!-- Key Credentials Strip -->
              <div class="mt-6 pt-4 border-t border-white/[0.06] grid grid-cols-2 sm:grid-cols-4 gap-3 text-[11px] font-['JetBrains_Mono'] text-gray-400">
                <div class="flex items-center gap-1.5">
                  <span class="text-[#00E676] font-bold">✓</span>
                  <span>Master Techs</span>
                </div>
                <div class="flex items-center gap-1.5">
                  <span class="text-[#00E676] font-bold">✓</span>
                  <span>Motul 300V</span>
                </div>
                <div class="flex items-center gap-1.5">
                  <span class="text-[#00E676] font-bold">✓</span>
                  <span>WhatsApp Reports</span>
                </div>
                <div class="flex items-center gap-1.5">
                  <span class="text-[#00E676] font-bold">✓</span>
                  <span>30-Day Warranty</span>
                </div>
              </div>

            </div>

          </div>
        </div>
      </section>

      <!-- STATS & WORKSHOP TELEMETRY DOCK (Modern Glass Cards) -->
      <section class="bg-[#0A0C10] border-b border-white/[0.08] py-8 sm:py-10 scroll-reveal">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="grid grid-cols-2 lg:grid-cols-4 gap-3.5 sm:gap-6">
            
            <div class="p-5 sm:p-6 rounded-2xl bg-[#11151F] border border-white/[0.06] hover:border-[#00E676]/30 transition-all shadow-xl group hover:-translate-y-1">
              <div class="flex items-center justify-between mb-2">
                <span class="text-[10px] font-['JetBrains_Mono'] text-gray-400 uppercase tracking-widest">Digital Job Cards</span>
                <span class="w-1.5 h-1.5 rounded-full bg-[#00E676] group-hover:animate-ping"></span>
              </div>
              <span class="block text-2xl sm:text-4xl font-black text-white font-['Outfit'] mb-1">12,500+</span>
              <span class="text-xs text-gray-400 font-['Plus_Jakarta_Sans'] block">Motorcycles Calibrated</span>
            </div>

            <div class="p-5 sm:p-6 rounded-2xl bg-[#11151F] border border-white/[0.06] hover:border-[#00E676]/30 transition-all shadow-xl group hover:-translate-y-1">
              <div class="flex items-center justify-between mb-2">
                <span class="text-[10px] font-['JetBrains_Mono'] text-[#00E676] uppercase tracking-widest font-semibold">Litre-Class Bay</span>
                <span class="w-1.5 h-1.5 rounded-full bg-[#00E676] group-hover:animate-ping"></span>
              </div>
              <span class="block text-2xl sm:text-4xl font-black text-[#00E676] font-['Outfit'] mb-1">450+</span>
              <span class="text-xs text-gray-400 font-['Plus_Jakarta_Sans'] block">Superbikes Tuned & Dyno'd</span>
            </div>

            <div class="p-5 sm:p-6 rounded-2xl bg-[#11151F] border border-white/[0.06] hover:border-[#38BDF8]/30 transition-all shadow-xl group hover:-translate-y-1">
              <div class="flex items-center justify-between mb-2">
                <span class="text-[10px] font-['JetBrains_Mono'] text-gray-400 uppercase tracking-widest">Diagnostics</span>
                <span class="w-1.5 h-1.5 rounded-full bg-[#38BDF8] group-hover:animate-ping"></span>
              </div>
              <span class="block text-2xl sm:text-4xl font-black text-white font-['Outfit'] mb-1">99.2%</span>
              <span class="text-xs text-gray-400 font-['Plus_Jakarta_Sans'] block">First-Time Resolution Rate</span>
            </div>

            <div class="p-5 sm:p-6 rounded-2xl bg-[#11151F] border border-white/[0.06] hover:border-white/[0.2] transition-all shadow-xl group hover:-translate-y-1">
              <div class="flex items-center justify-between mb-2">
                <span class="text-[10px] font-['JetBrains_Mono'] text-[#38BDF8] uppercase tracking-widest font-semibold">Workshop Network</span>
                <span class="w-1.5 h-1.5 rounded-full bg-[#38BDF8] group-hover:animate-ping"></span>
              </div>
              <span class="block text-2xl sm:text-4xl font-black text-[#38BDF8] font-['Outfit'] mb-1">2 Hubs</span>
              <span class="text-xs text-gray-400 font-['Plus_Jakarta_Sans'] block">Ambattur Flagship & Avadi Studio</span>
            </div>

          </div>
        </div>
      </section>

      <!-- DUAL CAPABILITIES BREAKDOWN -->
      <section class="py-24 bg-[#0A0C10] scroll-reveal">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center max-w-3xl mx-auto mb-16">
            <span class="text-xs font-mono font-bold uppercase tracking-wider text-[#00E676] block mb-2">WORKSHOP CAPABILITIES</span>
            <h2 class="text-3xl sm:text-5xl font-extrabold text-white tracking-tight font-['Outfit']">
              Engineered For Every Cylinder Count.
            </h2>
            <p class="text-slate-400 text-sm sm:text-base mt-4 leading-relaxed font-['Plus_Jakarta_Sans']">
              Equipped with computerized diagnostic scanners, pneumatic lifts, and high-temp fabrication gear to handle everyday commuters as well as track-focused superbikes.
            </p>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Pillar 1 -->
            <div class="premium-card p-8 flex flex-col justify-between scroll-reveal">
              <div>
                <div class="w-12 h-12 rounded-xl bg-white/[0.04] border border-white/10 flex items-center justify-center text-white mb-6">
                  <svg class="w-6 h-6 text-[#38BDF8]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
                </div>
                <span class="text-xs font-mono text-[#38BDF8] uppercase tracking-wider font-semibold block mb-1">Division 01</span>
                <h3 class="text-2xl font-bold text-white mb-3 font-['Outfit']">NITRO RACING Superbike Bay</h3>
                <p class="text-slate-400 text-sm leading-relaxed mb-6 font-['Plus_Jakarta_Sans']">
                  Dedicated master technician care for Kawasaki, Triumph, Ducati, BMW Motorrad, Yamaha & Honda. Shimming valve clearances, ECU diagnostics, and Engine Ice coolant flushing.
                </p>
                <ul class="space-y-2.5 text-xs text-slate-300 mb-8 border-t border-white/[0.06] pt-4 font-mono">
                  <li class="flex items-center gap-2">
                    <span class="text-[#38BDF8]">›</span>
                    <span>OBD-II Multi-Protocol ECU Scanning</span>
                  </li>
                  <li class="flex items-center gap-2">
                    <span class="text-[#38BDF8]">›</span>
                    <span>Laser Wheel Alignment & Chain Sag Caliper</span>
                  </li>
                  <li class="flex items-center gap-2">
                    <span class="text-[#38BDF8]">›</span>
                    <span>Brembo Sintered Pad Caliper Overhaul</span>
                  </li>
                </ul>
              </div>
              <a routerLink="/services" fragment="superbike" class="w-full py-3 bg-white/[0.05] hover:bg-white/[0.1] text-white text-xs font-bold font-['Outfit'] uppercase tracking-wider rounded-xl text-center transition-colors border border-white/10">
                Explore Superbike Care
              </a>
            </div>

            <!-- Pillar 2 -->
            <div class="premium-card p-8 border-[#00E676]/30 flex flex-col justify-between relative scroll-reveal">
              <div class="absolute top-4 right-4 bg-[#00E676] text-[#0A0C10] text-[10px] font-mono font-bold uppercase tracking-wider px-2.5 py-0.5 rounded-full shadow-md">
                Featured
              </div>
              <div>
                <div class="w-12 h-12 rounded-xl bg-[#00E676]/10 border border-[#00E676]/30 flex items-center justify-center text-[#00E676] mb-6">
                  <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"/></svg>
                </div>
                <span class="text-xs font-mono text-[#00E676] uppercase tracking-wider font-semibold block mb-1">Division 02</span>
                <h3 class="text-2xl font-bold text-white mb-3 font-['Outfit']">NITRO RACING Modz Studio</h3>
                <p class="text-slate-400 text-sm leading-relaxed mb-6 font-['Plus_Jakarta_Sans']">
                  Akrapovič & Austin Racing slip-ons, Stage 1 ECU remaps, high-candela auxiliary pod lighting with relay harnesses, heavy-gauge crash cages, and carbon body kit fitments.
                </p>
                <ul class="space-y-2.5 text-xs text-slate-300 mb-8 border-t border-white/[0.06] pt-4 font-mono">
                  <li class="flex items-center gap-2">
                    <span class="text-[#00E676]">›</span>
                    <span>Performance Exhaust Fitment & Decat Headers</span>
                  </li>
                  <li class="flex items-center gap-2">
                    <span class="text-[#00E676]">›</span>
                    <span>Auxiliary Touring Lights with Relay Harness</span>
                  </li>
                  <li class="flex items-center gap-2">
                    <span class="text-[#00E676]">›</span>
                    <span>Quickshifter & Dynojet Flash Tuning</span>
                  </li>
                </ul>
              </div>
              <a routerLink="/services" fragment="modz" class="btn-laser w-full py-3 bg-[#00E676] hover:bg-[#00C853] text-[#0A0C10] text-xs font-bold font-['Outfit'] uppercase tracking-wider rounded-xl text-center transition-all shadow-md">
                Explore Nitro Modz
              </a>
            </div>

            <!-- Pillar 3 -->
            <div class="premium-card p-8 flex flex-col justify-between scroll-reveal">
              <div>
                <div class="w-12 h-12 rounded-xl bg-white/[0.04] border border-white/10 flex items-center justify-center text-white mb-6">
                  <svg class="w-6 h-6 text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
                </div>
                <span class="text-xs font-mono text-gray-400 uppercase tracking-wider font-semibold block mb-1">Division 03</span>
                <h3 class="text-2xl font-bold text-white mb-3 font-['Outfit']">NITRO RACING Workshop Care</h3>
                <p class="text-slate-400 text-sm leading-relaxed mb-6 font-['Plus_Jakarta_Sans']">
                  50-point precision mechanical inspection, ultrasonic injector flushes, Motul synthetic oils, and chain lube. Routine servicing executed with motorsport cleanliness.
                </p>
                <ul class="space-y-2.5 text-xs text-slate-300 mb-8 border-t border-white/[0.06] pt-4 font-mono">
                  <li class="flex items-center gap-2">
                    <span class="text-gray-400">›</span>
                    <span>100% Motul 7100 / 300V Ester Synthetics</span>
                  </li>
                  <li class="flex items-center gap-2">
                    <span class="text-gray-400">›</span>
                    <span>Ultrasonic Fuel Injector Cleaning & Flow Test</span>
                  </li>
                  <li class="flex items-center gap-2">
                    <span class="text-gray-400">›</span>
                    <span>Digital Tire Depth & Front Fork Seal Inspection</span>
                  </li>
                </ul>
              </div>
              <a routerLink="/services" fragment="routine" class="w-full py-3 bg-white/[0.05] hover:bg-white/[0.1] text-white text-xs font-bold font-['Outfit'] uppercase tracking-wider rounded-xl text-center transition-colors border border-white/10">
                Explore Routine Care
              </a>
            </div>
          </div>
        </div>
      </section>

      <!-- FEATURED WORKSHOP CATALOG -->
      <section class="py-24 bg-[#0D111A] border-t border-b border-white/[0.06] scroll-reveal">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="flex flex-col md:flex-row md:items-end justify-between mb-16 gap-6">
            <div>
              <span class="text-xs font-mono font-bold uppercase tracking-wider text-[#00E676] block mb-2">SERVICE DIRECTORY</span>
              <h2 class="text-3xl sm:text-5xl font-extrabold text-white tracking-tight font-['Outfit']">
                NITRO RACING Packages
              </h2>
              <p class="text-slate-400 text-sm sm:text-base mt-2 font-['Plus_Jakarta_Sans']">
                Transparent starting labor rates with verified manufacturer torque specs.
              </p>
            </div>
            <a routerLink="/services" class="inline-flex items-center gap-2 text-sm font-bold text-[#00E676] hover:underline font-['Outfit'] uppercase tracking-wider">
              <span>View Full Catalog</span>
              <span>→</span>
            </a>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div *ngFor="let s of featuredServices" class="premium-card p-7 flex flex-col justify-between group scroll-reveal">
              <div>
                <div class="flex items-center justify-between mb-4">
                  <span class="text-[10px] font-mono font-bold uppercase tracking-wider px-2.5 py-1 rounded bg-[#00E676]/10 text-[#00E676] border border-[#00E676]/20">
                    {{ s.category }}
                  </span>
                  <span class="text-xs text-slate-400 font-mono">
                    {{ s.estimatedDuration }}
                  </span>
                </div>

                <h3 class="text-xl font-bold text-white group-hover:text-[#00E676] transition-colors mb-2 font-['Outfit']">
                  {{ s.name }}
                </h3>
                <p class="text-slate-400 text-xs sm:text-sm leading-relaxed mb-6 font-['Plus_Jakarta_Sans']">
                  {{ s.shortDescription }}
                </p>

                <!-- Inclusions Preview -->
                <div class="space-y-2 mb-6 border-t border-white/[0.06] pt-4 text-xs text-slate-300 font-mono">
                  <div *ngFor="let item of (s.includedItems || s.includedList).slice(0, 3)" class="flex items-center gap-2">
                    <span class="text-[#00E676]">✓</span>
                    <span>{{ item }}</span>
                  </div>
                </div>
              </div>

              <!-- Price & CTA -->
              <div class="pt-4 border-t border-white/[0.06] flex items-center justify-between">
                <div>
                  <span class="text-[10px] uppercase font-mono text-slate-400 block">Starting Labor</span>
                  <span class="text-xl font-extrabold text-white font-mono">{{ s.basePrice }}</span>
                </div>
                <a [routerLink]="['/services', s.id]" class="px-5 py-2.5 bg-white/[0.05] hover:bg-white/[0.1] text-white text-xs font-bold font-['Outfit'] uppercase tracking-wider rounded-xl transition-colors border border-white/10">
                  Details
                </a>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- BRANCH LOCATIONS SECTION -->
      <section class="py-24 bg-[#0A0C10] scroll-reveal">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center max-w-3xl mx-auto mb-16">
            <span class="text-xs font-mono font-bold uppercase tracking-wider text-[#00E676] block mb-2">WORKSHOP HUBS</span>
            <h2 class="text-3xl sm:text-5xl font-extrabold text-white tracking-tight font-['Outfit']">
              Visit Our Chennai Workshops
            </h2>
            <p class="text-slate-400 text-sm sm:text-base mt-4 font-['Plus_Jakarta_Sans']">
              Dual strategic locations in Ambattur and Avadi with dedicated customer reception lounges and clean diagnostic bays.
            </p>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div *ngFor="let b of branches" class="premium-card p-8 flex flex-col justify-between scroll-reveal">
              <div>
                <div class="flex items-center justify-between mb-4">
                  <span class="text-xs font-mono font-bold uppercase text-[#00E676] tracking-wider">{{ b.code }}</span>
                  <span class="text-xs text-slate-400 font-mono">Mon–Sat: 8:30 AM – 8:00 PM</span>
                </div>
                <h3 class="text-2xl font-bold text-white mb-2 font-['Outfit']">{{ b.name }}</h3>
                <p class="text-slate-400 text-xs sm:text-sm leading-relaxed mb-6 font-['Plus_Jakarta_Sans']">
                  {{ b.address }}
                </p>

                <div class="space-y-2 mb-6 text-xs text-slate-300 font-mono border-t border-white/[0.06] pt-4">
                  <div class="flex justify-between">
                    <span class="text-slate-400">Supervisor:</span>
                    <span class="text-white font-semibold">{{ b.managerName }}</span>
                  </div>
                  <div class="flex justify-between">
                    <span class="text-slate-400">Hotline:</span>
                    <a [href]="'tel:' + b.phone" class="text-[#00E676] hover:underline">{{ b.phone }}</a>
                  </div>
                </div>
              </div>

              <div class="flex items-center gap-3 pt-4 border-t border-white/[0.06]">
                <button
                  (click)="openEnquiryModal()"
                  class="btn-laser flex-1 py-3 bg-[#00E676] hover:bg-[#00c864] text-[#0A0C10] font-bold text-xs font-['Outfit'] uppercase tracking-wider rounded-xl text-center transition-colors shadow-md"
                >
                  Book Slot At {{ b.name.includes('Ambattur') ? 'Ambattur' : 'Avadi' }}
                </button>
                <a
                  [href]="b.mapsUrl"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="px-5 py-3 bg-white/[0.05] hover:bg-white/[0.1] text-white text-xs font-semibold rounded-xl border border-white/10 transition-colors font-mono"
                >
                  Maps ↗
                </a>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- TESTIMONIALS STRIP -->
      <section class="py-20 bg-[#0D111A] border-t border-white/[0.06] scroll-reveal">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center max-w-2xl mx-auto mb-14">
            <span class="text-xs font-mono font-bold uppercase tracking-wider text-[#00E676] block mb-2">VERIFIED REVIEWS</span>
            <h2 class="text-3xl sm:text-4xl font-extrabold text-white tracking-tight font-['Outfit']">
              What Riders Say
            </h2>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div *ngFor="let t of testimonials" class="premium-card p-7 flex flex-col justify-between scroll-reveal">
              <div>
                <div class="flex items-center text-[#00E676] text-sm tracking-wider mb-4 font-mono">
                  <span>★★★★★</span>
                </div>
                <p class="text-slate-300 text-sm leading-relaxed mb-6 font-['Plus_Jakarta_Sans'] italic">
                  "{{ t.feedback }}"
                </p>
              </div>

              <div class="pt-4 border-t border-white/[0.06] flex items-center justify-between">
                <div>
                  <span class="text-white font-bold text-sm block font-['Outfit']">{{ t.customerName }}</span>
                  <span class="text-xs text-[#38BDF8] font-mono">{{ t.bikeModel }}</span>
                </div>
                <span class="text-[10px] font-mono text-slate-400 uppercase bg-white/[0.04] px-2 py-0.5 rounded">
                  {{ t.branch }}
                </span>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- CALL TO ACTION BANNER -->
      <section class="bg-[#121622] border-t border-white/[0.08] py-20 scroll-reveal">
        <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <span class="text-xs font-mono font-bold uppercase tracking-wider text-[#00E676] block mb-3">SCHEDULE SERVICE</span>
          <h2 class="text-3xl sm:text-5xl font-extrabold text-white tracking-tight mb-4 font-['Outfit']">
            Ready to Give Your Bike The Care It Deserves?
          </h2>
          <p class="text-sm sm:text-base text-slate-400 max-w-xl mx-auto mb-8 leading-relaxed font-['Plus_Jakarta_Sans']">
            Submit a service enquiry in under 60 seconds. Our workshop supervisor will review your bike's symptoms and call to schedule drop-off.
          </p>
          <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
            <button
              (click)="openEnquiryModal()"
              class="btn-laser px-8 py-4 bg-[#00E676] hover:bg-[#00c864] text-[#0A0C10] font-bold text-sm font-['Outfit'] uppercase tracking-wider rounded-xl transition-all shadow-xl shadow-[#00E676]/20 flex items-center gap-2"
            >
              <span>Submit Service Enquiry</span>
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
            </button>
            <a
              href="tel:+919840011223"
              class="px-8 py-4 bg-white/[0.06] hover:bg-white/[0.1] text-white font-semibold text-sm font-['Outfit'] tracking-wide rounded-xl border border-white/10 transition-colors flex items-center gap-2 font-mono"
            >
              <svg class="w-4 h-4 text-[#00E676]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
              <span>Call Ambattur: +91 98400 11223</span>
            </a>
          </div>
        </div>
      </section>

      <!-- MODAL COMPONENT -->
      <app-enquiry-modal
        [isOpen]="isModalOpen"
        [preselectedService]="selectedServiceCategory"
        (close)="closeEnquiryModal()"
      ></app-enquiry-modal>

    </div>
  `
})
export class HomeComponent implements OnInit, OnDestroy {
  featuredServices: WorkshopService[] = [];
  branches: Branch[] = [];
  testimonials: Testimonial[] = [];
  isModalOpen = false;
  selectedServiceCategory?: string;

  // Auto-Moving Slider Configuration
  currentSlide = 0;
  private timer: any = null;
  private readonly SLIDE_DURATION = 4000; // Auto-moves every 4 seconds

  slides: HeroSlide[] = [
    {
      id: 1,
      tag: 'NITRO RACING // SUPERBIKE CARE BAY',
      tagColor: '#38BDF8',
      title: 'NITRO RACING Superbike Engineering.',
      highlight: 'Tuned For The Apex.',
      description: 'Dedicated multi-cylinder diagnostics bay for litre-class superbikes (Kawasaki, Ducati, BMW, Yamaha, Triumph). Digital valve clearance calibration, Motul 300V fluids, and dyno-matched throttle mapping.',
      specs: ['400cc – 1400cc Multi-Cylinder', 'Motul 300V Factory Line', 'OBD-II CAN-Bus Scanners'],
      image: 'images/hero_superbike.jpg',
      alt: 'Nitro Racing Superbike Bay',
      telemetry: 'OBD-II LIVE • SHIM MICROMETER CALIBRATION',
      primaryCtaText: 'Book Superbike Bay',
      serviceCategory: 'Superbike Precision Diagnostics',
      secondaryCtaText: 'Superbike Specs',
      secondaryRoute: '/services/superbike-diagnostics'
    },
    {
      id: 2,
      tag: 'NITRO RACING // MODZ PERFORMANCE STUDIO',
      tagColor: '#00E676',
      title: 'NITRO RACING Exhaust & ECU Tuning.',
      highlight: 'Maximum Flow & Acoustic Roar.',
      description: 'Handcrafted titanium & stainless steel exhaust systems, decat manifolds, acoustic resonator tuning, and Stage 1/2 ECU flash remaps for blistering throttle response and race-grade power delivery.',
      specs: ['TIG Titanium Bend Piping', 'Stage 1 & 2 ECU Remaps', 'Auxiliary Touring Relays'],
      image: 'images/engine_detail.jpg',
      alt: 'Nitro Racing Exhaust & Tuning',
      telemetry: 'DECAT HEADERS • ACOUSTIC TUNED • STAGE 1/2',
      primaryCtaText: 'Request Modz Quote',
      serviceCategory: 'Nitro Modz Performance Exhaust & Tuning',
      secondaryCtaText: 'View Modz Gallery',
      secondaryRoute: '/gallery'
    },
    {
      id: 3,
      tag: 'NITRO RACING // WORKSHOP CARE',
      tagColor: '#00E676',
      title: 'NITRO RACING Workshop Bays.',
      highlight: 'Zero Guesswork Calibration.',
      description: 'Pneumatic scissor lifts, calibrated digital torque wrenches, ultrasonic fuel injector cleaning, and computerized OBD-II telemetry. Every single bolt fastened to strict factory engineering tolerances.',
      specs: ['Digital Torque Tooling', 'Ultrasonic Injector Cleaning', '30-Day / 1,000km Warranty'],
      image: 'images/service_bay.jpg',
      alt: 'Nitro Racing State-of-the-Art Bay',
      telemetry: '50-POINT DIAGNOSTIC • DIGITAL JOB CARD',
      primaryCtaText: 'Book Master Inspection',
      serviceCategory: 'Periodic Master Service',
      secondaryCtaText: 'Explore Both Hubs',
      secondaryRoute: '/branches'
    }
  ];

  get currentSlideData(): HeroSlide {
    return this.slides[this.currentSlide];
  }

  constructor(private dataService: DataService, private cdr: ChangeDetectorRef) {}

  ngOnInit(): void {
    this.featuredServices = this.dataService.getFeaturedServices();
    this.branches = this.dataService.getBranches();
    this.testimonials = this.dataService.getTestimonials().slice(0, 3);
    this.startAutoMoving();
  }

  ngOnDestroy(): void {
    this.stopAutoMoving();
  }

  startAutoMoving(): void {
    this.stopAutoMoving();
    this.timer = setInterval(() => {
      this.currentSlide = (this.currentSlide + 1) % this.slides.length;
      this.cdr.detectChanges();
    }, this.SLIDE_DURATION);
  }

  stopAutoMoving(): void {
    if (this.timer) {
      clearInterval(this.timer);
      this.timer = null;
    }
  }

  goToSlide(index: number): void {
    this.currentSlide = index;
    this.startAutoMoving(); // Reset timer so it stays for full duration
    this.cdr.detectChanges();
  }

  openEnquiryModal(serviceCategory?: string): void {
    this.selectedServiceCategory = serviceCategory || 'Superbike Precision Diagnostics';
    this.isModalOpen = true;
  }

  closeEnquiryModal(): void {
    this.isModalOpen = false;
  }
}
