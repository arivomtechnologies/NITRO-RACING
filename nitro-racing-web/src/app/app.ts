import { Component, signal, OnInit, AfterViewInit } from '@angular/core';
import { RouterOutlet, Router, NavigationEnd } from '@angular/router';
import { filter } from 'rxjs/operators';
import { NavbarComponent } from './components/navbar/navbar.component';
import { FooterComponent } from './components/footer/footer.component';
import { FloatingWidgetComponent } from './components/floating-widget/floating-widget.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, NavbarComponent, FooterComponent, FloatingWidgetComponent],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App implements OnInit, AfterViewInit {
  protected readonly title = signal('Nitro Racing');

  constructor(private router: Router) {}

  ngOnInit(): void {
    // Scroll to top and re-init observer on route changes
    this.router.events.pipe(
      filter(event => event instanceof NavigationEnd)
    ).subscribe(() => {
      if (typeof window !== 'undefined') {
        window.scrollTo({ top: 0, behavior: 'instant' });
        setTimeout(() => this.initScrollObserver(), 100);
      }
    });
  }

  ngAfterViewInit(): void {
    if (typeof window !== 'undefined') {
      setTimeout(() => this.initScrollObserver(), 150);
    }
  }

  private initScrollObserver(): void {
    if (typeof window === 'undefined' || typeof document === 'undefined') return;

    // Check if browser already supports native scroll-driven view timelines
    const supportsViewTimeline = typeof CSS !== 'undefined' && 
      CSS.supports && 
      CSS.supports('(animation-timeline: view()) and (animation-range: entry)');

    const prefersReducedMotion = typeof window.matchMedia === 'function' && 
      window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // If native view timeline is supported and user allows motion, native CSS handles it!
    if (supportsViewTimeline && !prefersReducedMotion) {
      return;
    }

    // High performance IntersectionObserver fallback
    if ('IntersectionObserver' in window) {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-revealed');
          }
        });
      }, {
        threshold: 0.05,
        rootMargin: '0px 0px -20px 0px'
      });

      const observeAll = () => {
        const elements = document.querySelectorAll('.scroll-reveal:not(.is-revealed)');
        elements.forEach(el => observer.observe(el));
      };

      observeAll();

      // Mutation observer to automatically track dynamically filtered cards (e.g. search, tabs)
      if ('MutationObserver' in window) {
        const mutObs = new MutationObserver(() => observeAll());
        mutObs.observe(document.body, { childList: true, subtree: true });
      }
    } else {
      // Direct fallback
      document.querySelectorAll('.scroll-reveal').forEach(el => el.classList.add('is-revealed'));
    }
  }
}
