import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-about',
  standalone: true,
  imports: [CommonModule, RouterLink],
  template: `
    <div class="bg-[#0A0C10] text-white pt-28 pb-24 min-h-screen">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">

        <!-- Header with Official Logo Crest Badge -->
        <div class="text-center max-w-3xl mx-auto mb-20">
          <div class="w-24 h-24 mx-auto mb-8 rounded-2xl overflow-hidden bg-[#0A0C10] border border-white/[0.1] p-1.5 shadow-[0_0_40px_rgba(0,230,118,0.2)]">
            <img src="images/logo.jpg" alt="Nitro Racing Modz Crest" class="w-full h-full object-contain" />
          </div>
          <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-white/[0.04] border border-white/[0.08] mb-4">
            <span class="w-2 h-2 rounded-full bg-[#00E676]"></span>
            <span class="text-xs font-['JetBrains_Mono'] uppercase tracking-widest text-gray-300">Motorsport Heritage & Engineering</span>
          </div>
          <h1 class="text-4xl sm:text-6xl font-black uppercase text-white tracking-tight mb-6 font-['Outfit']">
            Engineered For The <span class="text-[#00E676]">Obsessed.</span>
          </h1>
          <p class="text-gray-400 text-base sm:text-lg leading-relaxed font-['Plus_Jakarta_Sans']">
            Nitro Racing Modz was established to give Chennai motorcyclists an uncompromising alternative to standard dealership garages. We treat every motorcycle—from street commuters to litre-class superbikes—as high-precision machinery.
          </p>
        </div>

        <!-- High-End Photography Showcase -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-24">
          <div class="rounded-2xl overflow-hidden border border-white/[0.08] relative group scroll-reveal">
            <img
              src="images/service_bay.jpg"
              alt="Nitro Racing State-of-the-Art Bay"
              class="w-full h-[400px] object-cover group-hover:scale-105 transition-transform duration-700"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-[#0A0C10] via-transparent to-transparent"></div>
            <div class="absolute bottom-6 left-6 right-6">
              <span class="text-[10px] font-['JetBrains_Mono'] font-bold text-[#00E676] uppercase tracking-wider block mb-1">FACILITY</span>
              <h3 class="text-2xl font-black text-white uppercase font-['Outfit']">NITRO RACING Climate-Controlled Bays</h3>
              <p class="text-xs text-gray-300 mt-1 font-['Plus_Jakarta_Sans']">Hydraulic scissor lifts, Italian computerized diagnostic scanners, and specialized paddock gear.</p>
            </div>
          </div>

          <div class="rounded-2xl overflow-hidden border border-white/[0.08] relative group scroll-reveal">
            <img
              src="images/engine_detail.jpg"
              alt="Nitro Racing Engine Tuning"
              class="w-full h-[400px] object-cover group-hover:scale-105 transition-transform duration-700"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-[#0A0C10] via-transparent to-transparent"></div>
            <div class="absolute bottom-6 left-6 right-6">
              <span class="text-[10px] font-['JetBrains_Mono'] font-bold text-[#38BDF8] uppercase tracking-wider block mb-1">CRAFTSMANSHIP</span>
              <h3 class="text-2xl font-black text-white uppercase font-['Outfit']">Engine Rebuilds & Desmo Clearance</h3>
              <p class="text-xs text-gray-300 mt-1 font-['Plus_Jakarta_Sans']">Micrometer shim calibration, titanium valve adjustments, and factory torque specifications.</p>
            </div>
          </div>
        </div>

        <!-- Core Values / Philosophy -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-24">
          <div class="premium-card p-8 scroll-reveal">
            <div class="w-12 h-12 rounded-xl bg-white/[0.04] text-[#00E676] flex items-center justify-center font-black text-xl mb-6 border border-white/[0.08] font-['JetBrains_Mono']">
              01
            </div>
            <h3 class="text-xl font-black text-white uppercase mb-3 font-['Outfit']">100% Genuine Fluids & Spares</h3>
            <p class="text-sm text-gray-400 leading-relaxed font-['Plus_Jakarta_Sans']">
              We never compromise on consumables. From Motul 300V / 7100 ester synthetic oils to Brembo sintered pads and NGK Iridium spark plugs, all parts are factory authentic with verifiable batch seals.
            </p>
          </div>

          <div class="premium-card p-8 scroll-reveal">
            <div class="w-12 h-12 rounded-xl bg-white/[0.04] text-[#38BDF8] flex items-center justify-center font-black text-xl mb-6 border border-white/[0.08] font-['JetBrains_Mono']">
              02
            </div>
            <h3 class="text-xl font-black text-white uppercase mb-3 font-['Outfit']">Transparent Digital Job Cards</h3>
            <p class="text-sm text-gray-400 leading-relaxed font-['Plus_Jakarta_Sans']">
              No surprise estimates. Our technicians photograph vehicle symptoms upon check-in and log all replaced parts digitally. Customers receive real-time WhatsApp updates before any extra work begins.
            </p>
          </div>

          <div class="premium-card p-8 scroll-reveal">
            <div class="w-12 h-12 rounded-xl bg-white/[0.04] text-[#00E676] flex items-center justify-center font-black text-xl mb-6 border border-white/[0.08] font-['JetBrains_Mono']">
              03
            </div>
            <h3 class="text-xl font-black text-white uppercase mb-3 font-['Outfit']">Track-Trained Technicians</h3>
            <p class="text-sm text-gray-400 leading-relaxed font-['Plus_Jakarta_Sans']">
              Our mechanics are certified for multi-cylinder superbikes, Bosch fuel injection, and CAN-bus electrical networks. They ride, race, and understand how bikes behave at 10,000+ RPM.
            </p>
          </div>
        </div>

        <!-- Master Technicians -->
        <div class="mb-24 scroll-reveal">
          <div class="text-center max-w-2xl mx-auto mb-12">
            <span class="text-xs font-['JetBrains_Mono'] font-bold uppercase tracking-widest text-[#00E676] block mb-2">MASTER WORKSHOP LEADS</span>
            <h2 class="text-3xl sm:text-4xl font-black uppercase text-white tracking-tight font-['Outfit']">Certified Technicians</h2>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div class="premium-card p-6 text-center scroll-reveal">
              <div class="w-20 h-20 rounded-2xl bg-white/[0.03] border border-white/[0.1] mx-auto mb-4 flex items-center justify-center text-2xl font-black text-[#00E676] font-['JetBrains_Mono']">
                SK
              </div>
              <h4 class="text-lg font-black text-white uppercase font-['Outfit']">Suresh Kumar</h4>
              <span class="text-xs text-[#00E676] font-['JetBrains_Mono'] font-bold block mb-2">Chief Superbike Lead</span>
              <p class="text-xs text-gray-400 leading-relaxed font-['Plus_Jakarta_Sans']">14+ years specializing in Kawasaki, Yamaha inline-4, and Ducati Desmo valvetrains.</p>
            </div>

            <div class="premium-card p-6 text-center scroll-reveal">
              <div class="w-20 h-20 rounded-2xl bg-white/[0.03] border border-white/[0.1] mx-auto mb-4 flex items-center justify-center text-2xl font-black text-[#38BDF8] font-['JetBrains_Mono']">
                KP
              </div>
              <h4 class="text-lg font-black text-white uppercase font-['Outfit']">Karthik Pandian</h4>
              <span class="text-xs text-[#38BDF8] font-['JetBrains_Mono'] font-bold block mb-2">Nitro Modz Custom Fabricator</span>
              <p class="text-xs text-gray-400 leading-relaxed font-['Plus_Jakarta_Sans']">TIG welding expert, custom stainless/titanium exhaust manifolds, and crash armor.</p>
            </div>

            <div class="premium-card p-6 text-center scroll-reveal">
              <div class="w-20 h-20 rounded-2xl bg-white/[0.03] border border-white/[0.1] mx-auto mb-4 flex items-center justify-center text-2xl font-black text-[#00E676] font-['JetBrains_Mono']">
                AR
              </div>
              <h4 class="text-lg font-black text-white uppercase font-['Outfit']">Arun R.</h4>
              <span class="text-xs text-[#00E676] font-['JetBrains_Mono'] font-bold block mb-2">Diagnostics & Electrical</span>
              <p class="text-xs text-gray-400 leading-relaxed font-['Plus_Jakarta_Sans']">OBD-II scanner diagnostics, CAN-bus harness repair, and high-output auxiliary lighting.</p>
            </div>
          </div>
        </div>

        <!-- Bottom CTA -->
        <div class="premium-card p-12 text-center max-w-3xl mx-auto scroll-reveal">
          <h3 class="text-3xl font-black uppercase text-white mb-4 font-['Outfit']">Ready To Experience True Engineering?</h3>
          <p class="text-gray-400 text-sm sm:text-base max-w-lg mx-auto mb-8 font-['Plus_Jakarta_Sans']">
            Book an inspection at our Ambattur or Avadi workshops and receive a thorough digital health report for your machine.
          </p>
          <a routerLink="/contact" class="btn-laser inline-block px-8 py-4 bg-[#00E676] hover:bg-[#00c864] text-[#0A0C10] text-xs font-black uppercase tracking-wider rounded-xl transition-all shadow-[0_0_20px_rgba(0,230,118,0.25)] font-['Outfit']">
            Book Workshop Inspection
          </a>
        </div>

      </div>
    </div>
  `
})
export class AboutComponent {}
