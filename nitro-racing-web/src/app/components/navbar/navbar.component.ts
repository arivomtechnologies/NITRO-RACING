import { Component, signal, HostListener, OnInit } from '@angular/core';
import { RouterLink, RouterLinkActive } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [CommonModule, RouterLink, RouterLinkActive],
  template: `
    <header 
      class="sticky top-0 z-50 transition-all duration-300 ease-out"
      [ngClass]="isScrolled() 
        ? 'bg-[#0A0C10]/95 backdrop-blur-2xl border-b border-[#00E676]/25 shadow-[0_10px_35px_rgba(0,0,0,0.85)] py-0' 
        : 'bg-[#0A0C10]/80 backdrop-blur-md border-b border-white/[0.07] py-0'"
    >
      <!-- Topmost Scroll Progress Telemetry Beam -->
      <div 
        id="scroll-progress-bar" 
        [style.transform]="'scaleX(' + scrollProgress() + ')'"
        class="absolute top-0 left-0 right-0 h-[2.5px] bg-gradient-to-r from-[#00E676] via-[#38BDF8] to-[#00E676] origin-left z-50 transition-transform duration-75 ease-out"
      ></div>

      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div 
          class="flex items-center justify-between transition-all duration-300 ease-out"
          [ngClass]="isScrolled() ? 'h-16' : 'h-20'"
        >
          
          <!-- Logo & Brand Identity with Gentle Hover Glow -->
          <a routerLink="/" class="flex items-center gap-3 group">
            <div 
              class="rounded-xl overflow-hidden bg-[#11151F] border border-white/10 p-1 group-hover:border-[#00E676] group-hover:shadow-[0_0_18px_rgba(0,230,118,0.4)] transition-all duration-300 transform group-hover:scale-105"
              [ngClass]="isScrolled() ? 'w-9 h-9' : 'w-11 h-11'"
            >
              <img src="images/logo.jpg" alt="Nitro Racing Modz" class="w-full h-full object-contain" />
            </div>
            <div>
              <div class="flex items-center gap-1.5 font-['Outfit']">
                <span class="font-bold tracking-tight text-white transition-all duration-300" [ngClass]="isScrolled() ? 'text-lg' : 'text-xl'">NITRO</span>
                <span class="font-bold tracking-tight text-[#00E676] transition-all duration-300" [ngClass]="isScrolled() ? 'text-lg' : 'text-xl'">RACING</span>
                <span class="text-[9px] font-mono font-bold text-gray-300 bg-white/[0.06] px-1.5 py-0.5 rounded border border-white/10 uppercase tracking-widest group-hover:border-[#00E676]/40 transition-colors">MODZ</span>
              </div>
              <span 
                *ngIf="!isScrolled()"
                class="text-[10px] tracking-wider text-gray-400 font-medium uppercase block font-['Plus_Jakarta_Sans'] transition-opacity duration-300"
              >
                Superbike Care & Tuning Studio
              </span>
            </div>
          </a>

          <!-- Modern Clean Desktop Navigation with Spring Trackers -->
          <nav class="hidden lg:flex items-center gap-8 text-sm font-medium">
            <a routerLink="/" routerLinkActive="text-[#00E676] font-semibold is-active-nav" [routerLinkActiveOptions]="{exact: true}" 
               class="text-gray-300 hover:text-white transition-colors py-2 relative group flex items-center gap-1">
              <span>Home</span>
              <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-[#00E676] transition-all duration-300 ease-out group-hover:w-full group-[.is-active-nav]:w-full shadow-[0_0_8px_#00E676]"></span>
            </a>

            <a routerLink="/about" routerLinkActive="text-[#00E676] font-semibold is-active-nav" 
               class="text-gray-300 hover:text-white transition-colors py-2 relative group flex items-center gap-1">
              <span>About</span>
              <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-[#00E676] transition-all duration-300 ease-out group-hover:w-full group-[.is-active-nav]:w-full shadow-[0_0_8px_#00E676]"></span>
            </a>

            <a routerLink="/services" routerLinkActive="text-[#00E676] font-semibold is-active-nav" 
               class="text-gray-300 hover:text-white transition-colors py-2 flex items-center gap-1.5 relative group">
              <span>Services</span>
              <span class="text-[9px] px-1.5 py-0.2 rounded bg-[#00E676]/15 text-[#00E676] font-mono font-semibold border border-[#00E676]/30 animate-pulse">MODZ</span>
              <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-[#00E676] transition-all duration-300 ease-out group-hover:w-full group-[.is-active-nav]:w-full shadow-[0_0_8px_#00E676]"></span>
            </a>

            <a routerLink="/branches" routerLinkActive="text-[#00E676] font-semibold is-active-nav" 
               class="text-gray-300 hover:text-white transition-colors py-2 relative group flex items-center gap-1">
              <span>Branches</span>
              <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-[#00E676] transition-all duration-300 ease-out group-hover:w-full group-[.is-active-nav]:w-full shadow-[0_0_8px_#00E676]"></span>
            </a>

            <a routerLink="/gallery" routerLinkActive="text-[#00E676] font-semibold is-active-nav" 
               class="text-gray-300 hover:text-white transition-colors py-2 relative group flex items-center gap-1">
              <span>Gallery</span>
              <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-[#00E676] transition-all duration-300 ease-out group-hover:w-full group-[.is-active-nav]:w-full shadow-[0_0_8px_#00E676]"></span>
            </a>

            <a routerLink="/testimonials" routerLinkActive="text-[#00E676] font-semibold is-active-nav" 
               class="text-gray-300 hover:text-white transition-colors py-2 relative group flex items-center gap-1">
              <span>Reviews</span>
              <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-[#00E676] transition-all duration-300 ease-out group-hover:w-full group-[.is-active-nav]:w-full shadow-[0_0_8px_#00E676]"></span>
            </a>
          </nav>

          <!-- Right Header CTAs with Radar Pulse & Laser Shimmer -->
          <div class="hidden sm:flex items-center gap-4">
            <!-- Call Button with Animated Radar Ring -->
            <a 
              href="tel:+919840011223" 
              class="relative text-xs font-mono font-medium text-gray-300 hover:text-white flex items-center gap-2.5 transition-colors group px-3 py-1.5 rounded-xl hover:bg-white/[0.04]"
            >
              <div class="relative w-8 h-8 rounded-lg bg-[#00E676]/10 border border-[#00E676]/30 flex items-center justify-center text-[#00E676] group-hover:bg-[#00E676] group-hover:text-black transition-all">
                <!-- Radar Pulse Ring -->
                <span class="absolute inset-0 rounded-lg bg-[#00E676]/30 animate-ping opacity-75"></span>
                <svg class="w-3.5 h-3.5 relative z-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
              </div>
              <span>+91 98400 11223</span>
            </a>

            <!-- Book Service CTA with Laser Shimmer -->
            <a 
              routerLink="/contact" 
              class="btn-laser px-5 py-2.5 rounded-xl bg-[#00E676] hover:bg-[#00C853] text-[#0A0C10] text-xs font-black font-['Outfit'] uppercase tracking-wider transition-all duration-300 shadow-lg shadow-[#00E676]/25 flex items-center gap-2 transform hover:-translate-y-0.5 active:translate-y-0"
            >
              <span>Book Service</span>
              <svg class="w-3.5 h-3.5 transition-transform group-hover:translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
            </a>
          </div>

          <!-- Mobile Menu Button -->
          <div class="lg:hidden flex items-center gap-2.5">
            <a href="tel:+919840011223" 
               aria-label="Call Nitro Racing"
               class="relative px-3 py-1.5 rounded-lg bg-[#00E676]/10 border border-[#00E676]/30 text-xs font-mono text-[#00E676] flex items-center gap-1.5 font-bold hover:bg-[#00E676] hover:text-black transition-all">
              <span class="w-2 h-2 rounded-full bg-[#00E676] animate-pulse"></span>
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
              <span>Call</span>
            </a>
            <button (click)="toggleMobileMenu()" type="button" 
                    aria-label="Toggle Navigation Menu" 
                    [attr.aria-expanded]="mobileMenuOpen()"
                    class="p-2.5 rounded-xl bg-[#151A26] text-gray-300 hover:text-white border border-white/10 transition-transform active:scale-95">
              <svg *ngIf="!mobileMenuOpen()" class="w-5 h-5 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"/></svg>
              <svg *ngIf="mobileMenuOpen()" class="w-5 h-5 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
            </button>
          </div>

        </div>
      </div>

      <!-- Mobile Navigation Drawer with Smooth Slide Transition -->
      <div 
        *ngIf="mobileMenuOpen()" 
        class="lg:hidden bg-[#0D1017]/98 backdrop-blur-2xl border-b border-white/10 px-5 pt-3 pb-6 space-y-2 animate-fade-in-down"
      >
        <a (click)="closeMobileMenu()" routerLink="/" routerLinkActive="text-[#00E676] bg-[#151A26]" [routerLinkActiveOptions]="{exact: true}" 
           class="block px-4 py-3 rounded-xl text-sm text-gray-300 font-medium hover:bg-[#151A26] hover:text-white transition-all">Home</a>
        <a (click)="closeMobileMenu()" routerLink="/about" routerLinkActive="text-[#00E676] bg-[#151A26]" 
           class="block px-4 py-3 rounded-xl text-sm text-gray-300 font-medium hover:bg-[#151A26] hover:text-white transition-all">About</a>
        <a (click)="closeMobileMenu()" routerLink="/services" routerLinkActive="text-[#00E676] bg-[#151A26]" 
           class="block px-4 py-3 rounded-xl text-sm text-gray-300 font-medium hover:bg-[#151A26] hover:text-white transition-all flex items-center justify-between">
          <span>Services & Nitro Modz</span>
          <span class="text-[9px] bg-[#00E676] text-black font-bold px-1.5 py-0.5 rounded font-mono">MODZ</span>
        </a>
        <a (click)="closeMobileMenu()" routerLink="/branches" routerLinkActive="text-[#00E676] bg-[#151A26]" 
           class="block px-4 py-3 rounded-xl text-sm text-gray-300 font-medium hover:bg-[#151A26] hover:text-white transition-all">Our Branches</a>
        <a (click)="closeMobileMenu()" routerLink="/gallery" routerLinkActive="text-[#00E676] bg-[#151A26]" 
           class="block px-4 py-3 rounded-xl text-sm text-gray-300 font-medium hover:bg-[#151A26] hover:text-white transition-all">Gallery</a>
        <a (click)="closeMobileMenu()" routerLink="/testimonials" routerLinkActive="text-[#00E676] bg-[#151A26]" 
           class="block px-4 py-3 rounded-xl text-sm text-gray-300 font-medium hover:bg-[#151A26] hover:text-white transition-all">Reviews</a>
        
        <div class="pt-3 border-t border-white/10 space-y-2">
          <a href="tel:+919840011223" class="w-full flex items-center justify-center gap-2 px-4 py-3 rounded-xl bg-white/[0.05] border border-white/10 text-white text-xs font-bold uppercase tracking-wider font-mono hover:bg-white/10 transition-colors">
            <svg class="w-4 h-4 text-[#00E676]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
            <span>Call Hotline: +91 98400 11223</span>
          </a>
          <a (click)="closeMobileMenu()" routerLink="/contact" class="btn-laser w-full text-center block px-4 py-3 rounded-xl bg-[#00E676] text-[#0A0C10] text-xs font-black uppercase tracking-wider shadow-lg">
            Book Service Enquiry
          </a>
        </div>
      </div>
    </header>
  `
})
export class NavbarComponent implements OnInit {
  mobileMenuOpen = signal<boolean>(false);
  isScrolled = signal<boolean>(false);
  scrollProgress = signal<number>(0);

  ngOnInit(): void {
    this.updateScrollState();
  }

  @HostListener('window:scroll', [])
  onWindowScroll(): void {
    this.updateScrollState();
  }

  private updateScrollState(): void {
    if (typeof window !== 'undefined') {
      const scrollY = window.scrollY || document.documentElement.scrollTop;
      this.isScrolled.set(scrollY > 25);

      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const progress = docHeight > 0 ? Math.min(1, Math.max(0, scrollY / docHeight)) : 0;
      this.scrollProgress.set(progress);
    }
  }

  toggleMobileMenu(): void {
    this.mobileMenuOpen.update(v => !v);
  }

  closeMobileMenu(): void {
    this.mobileMenuOpen.set(false);
  }
}
