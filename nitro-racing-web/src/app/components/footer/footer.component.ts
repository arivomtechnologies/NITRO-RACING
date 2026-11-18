import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-footer',
  standalone: true,
  imports: [CommonModule, RouterLink],
  template: `
    <footer class="bg-[#080A0E] text-slate-400 border-t border-white/[0.08] pt-16 pb-12 font-['Plus_Jakarta_Sans']">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <!-- Top Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10 mb-12">
          <!-- Col 1: Brand Info -->
          <div>
            <div class="flex items-center gap-3 mb-4">
              <div class="w-10 h-10 rounded-xl overflow-hidden bg-[#121622] border border-white/10 p-0.5">
                <img src="images/logo.jpg" alt="Nitro Racing Crest" class="w-full h-full object-contain" />
              </div>
              <div class="font-['Outfit']">
                <span class="text-lg font-bold text-white tracking-tight">NITRO <span class="text-[#00E676]">RACING</span></span>
                <span class="block text-[10px] text-slate-500 font-mono tracking-widest uppercase">TUNING STUDIO</span>
              </div>
            </div>
            <p class="text-xs text-slate-400 mb-6 leading-relaxed">
              Chennai's premier multi-brand motorcycle workshop specializing in routine mechanical service, dedicated superbike diagnostics, and Nitro Modz performance fabrication.
            </p>
            <div class="flex items-center gap-3">
              <a href="https://instagram.com" target="_blank" rel="noopener noreferrer" aria-label="Instagram" class="w-8 h-8 rounded-lg bg-white/[0.04] border border-white/10 flex items-center justify-center text-slate-400 hover:text-white hover:border-white/20 transition-colors">
                <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
              </a>
              <a href="https://wa.me/919840011223" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp" class="w-8 h-8 rounded-lg bg-white/[0.04] border border-white/10 flex items-center justify-center text-slate-400 hover:text-[#00E676] hover:border-[#00E676]/30 transition-colors">
                <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
              </a>
            </div>
          </div>

          <!-- Col 2: Services -->
          <div>
            <h4 class="text-white font-bold text-xs font-['Outfit'] tracking-wider uppercase mb-4">
              Specialized Services
            </h4>
            <ul class="space-y-2.5 text-xs text-slate-400">
              <li><a routerLink="/services" class="hover:text-white transition-colors">NITRO RACING Superbike Diagnostics</a></li>
              <li><a routerLink="/services" class="hover:text-white transition-colors">Desmo & Shim Valve Tuning</a></li>
              <li><a routerLink="/services" class="hover:text-white transition-colors">Nitro Modz Custom Exhausts</a></li>
              <li><a routerLink="/services" class="hover:text-white transition-colors">ECU Remap & Dyno Calibration</a></li>
              <li><a routerLink="/services" class="hover:text-white transition-colors">Periodic 50-Point Master Service</a></li>
              <li><a routerLink="/services" class="hover:text-white transition-colors">Ceramic Coating & Deep Wash</a></li>
              <li><a routerLink="/services" class="hover:text-white transition-colors">Brembo Brake Overhaul</a></li>
            </ul>
          </div>

          <!-- Col 3: Workshops -->
          <div>
            <h4 class="text-white font-bold text-xs font-['Outfit'] tracking-wider uppercase mb-4">
              Chennai Workshops
            </h4>
            <div class="space-y-3.5 text-xs">
              <div class="p-3 bg-white/[0.02] rounded-xl border border-white/[0.05]">
                <span class="text-white font-semibold block mb-1">Ambattur Main Hub</span>
                <p class="text-[11px] text-slate-400 mb-1.5">Plot 14/2A, SIDCO Industrial Estate, Ambattur, Chennai - 600058</p>
                <a href="tel:+919840011223" class="text-[#00E676] font-mono hover:underline inline-flex items-center gap-1.5">
                  <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
                  <span>+91 98400 11223</span>
                </a>
              </div>

              <div class="p-3 bg-white/[0.02] rounded-xl border border-white/[0.05]">
                <span class="text-white font-semibold block mb-1">Avadi Superbike Bay</span>
                <p class="text-[11px] text-slate-400 mb-1.5">Old No. 82, New No. 4, New Military Road, Avadi, Chennai - 600054</p>
                <a href="tel:+919840122334" class="text-[#38BDF8] font-mono hover:underline inline-flex items-center gap-1.5">
                  <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
                  <span>+91 98401 22334</span>
                </a>
              </div>
            </div>
          </div>

          <!-- Col 4: Operating Hours -->
          <div>
            <h4 class="text-white font-bold text-xs font-['Outfit'] tracking-wider uppercase mb-4">
              Hours & Booking
            </h4>
            <div class="space-y-3 text-xs text-slate-400">
              <div>
                <span class="text-white font-medium block">Monday – Saturday</span>
                <span>08:30 AM – 08:00 PM</span>
              </div>
              <div>
                <span class="text-white font-medium block">Sunday Express Bay</span>
                <span>09:00 AM – 02:00 PM</span>
              </div>
              <div class="pt-2">
                <a routerLink="/contact" class="inline-flex items-center gap-2 px-4 py-2.5 bg-[#00E676] hover:bg-[#00C853] text-[#0A0C10] rounded-xl font-bold font-['Outfit'] text-xs uppercase tracking-wider transition-colors shadow-md">
                  <span>Submit Service Enquiry</span>
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
                </a>
              </div>
            </div>
          </div>
        </div>

        <!-- Bottom Line -->
        <div class="border-t border-white/[0.06] pt-6 flex flex-col md:flex-row items-center justify-between text-xs text-slate-500 gap-4">
          <p>© 2026 Nitro Racing Modz. All rights reserved. NITRO RACING motorcycle engineering.</p>
          <div class="flex items-center gap-6">
            <a routerLink="/" class="hover:text-slate-300">Home</a>
            <a routerLink="/about" class="hover:text-slate-300">About</a>
            <a routerLink="/services" class="hover:text-slate-300">Services</a>
            <a routerLink="/branches" class="hover:text-slate-300">Branches</a>
            <a routerLink="/contact" class="hover:text-slate-300">Contact</a>
          </div>
        </div>
      </div>
    </footer>
  `
})
export class FooterComponent {}
