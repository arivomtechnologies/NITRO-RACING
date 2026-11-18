import { Component, HostListener, signal } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-floating-widget',
  standalone: true,
  imports: [CommonModule],
  template: `
    <!-- Floating Bottom-Right Action Dock -->
    <div class="fixed bottom-6 right-6 z-40 flex flex-col items-end gap-3 select-none">
      
      <!-- Scroll To Top Button (Smooth Fade In on Scroll) -->
      <button
        *ngIf="showScrollTop()"
        (click)="scrollToTop()"
        type="button"
        aria-label="Scroll to top of page"
        class="w-11 h-11 rounded-full bg-[#11151F]/90 backdrop-blur-xl border border-white/15 text-gray-300 hover:text-[#00E676] hover:border-[#00E676]/50 transition-all duration-300 shadow-xl flex items-center justify-center transform hover:-translate-y-1 active:translate-y-0 group cursor-pointer"
      >
        <svg class="w-4 h-4 transition-transform group-hover:-translate-y-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 10l7-7m0 0l7 7m-7-7v18"/></svg>
      </button>

      <!-- Speed Dial Pill Stack -->
      <div class="flex items-center gap-2.5 bg-[#0A0C10]/90 backdrop-blur-xl border border-white/[0.12] p-1.5 rounded-full shadow-[0_10px_35px_rgba(0,0,0,0.85)] hover:border-[#00E676]/40 transition-all duration-300">
        
        <!-- Call Hotline Button with Pulse Indicator -->
        <a
          href="tel:+919840011223"
          aria-label="Call Nitro Racing Workshop Hotline"
          class="relative flex items-center gap-2 pl-3 pr-3.5 py-2 rounded-full bg-white/[0.04] hover:bg-[#00E676] text-white hover:text-black font-['JetBrains_Mono'] text-xs font-bold transition-all duration-300 group"
        >
          <span class="w-2 h-2 rounded-full bg-[#00E676] group-hover:bg-black animate-pulse"></span>
          <svg class="w-3.5 h-3.5 text-[#00E676] group-hover:text-black transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
          <span class="hidden sm:inline">Call Hotline</span>
        </a>

        <!-- WhatsApp Direct Chat Button -->
        <a
          href="https://wa.me/919840011223?text=Hi%20Nitro%20Racing%2C%20I%20would%20like%20to%20enquire%20about%20motorcycle%20service%20and%20dyno%20tuning."
          target="_blank"
          rel="noopener noreferrer"
          aria-label="Chat with Workshop Supervisor on WhatsApp"
          class="w-10 h-10 rounded-full bg-[#25D366] hover:bg-[#20ba5a] text-white flex items-center justify-center transition-all duration-300 shadow-[0_0_20px_rgba(37,211,102,0.4)] hover:shadow-[0_0_25px_rgba(37,211,102,0.6)] transform hover:scale-105 active:scale-95"
        >
          <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
        </a>

      </div>

    </div>
  `
})
export class FloatingWidgetComponent {
  showScrollTop = signal<boolean>(false);

  @HostListener('window:scroll', [])
  onScroll(): void {
    if (typeof window !== 'undefined') {
      const scrollY = window.scrollY || document.documentElement.scrollTop;
      this.showScrollTop.set(scrollY > 350);
    }
  }

  scrollToTop(): void {
    if (typeof window !== 'undefined') {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  }
}
