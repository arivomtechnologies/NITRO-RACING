import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';
import { DataService } from '../../services/data.service';
import { ServiceEnquiry } from '../../models/service.model';

interface FormErrors {
  customerName?: string;
  phoneNumber?: string;
  bikeModel?: string;
}

@Component({
  selector: 'app-contact',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterLink],
  template: `
    <div class="bg-[#0A0C10] text-white pt-28 pb-24 min-h-screen">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">

        <!-- Header -->
        <div class="text-center max-w-3xl mx-auto mb-16 animate-fade-in-down">
          <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-white/[0.04] border border-white/[0.08] mb-4">
            <span class="w-2 h-2 rounded-full bg-[#00E676] animate-pulse"></span>
            <span class="text-xs font-['JetBrains_Mono'] uppercase tracking-widest text-gray-300">Direct Workshop Desk</span>
          </div>
          <h1 class="text-4xl sm:text-6xl font-black uppercase text-white tracking-tight mb-5 font-['Outfit']">
            Service Booking & <span class="text-[#00E676]">Modz Inquiries</span>
          </h1>
          <p class="text-gray-400 text-base sm:text-lg leading-relaxed font-['Plus_Jakarta_Sans']">
            Have questions about superbike valve clearance or custom exhaust fabrication? Submit your vehicle details below and our service advisors will contact you promptly.
          </p>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-10">

          <!-- Left: Contact Form -->
          <div class="lg:col-span-7 premium-card p-8 sm:p-10 scroll-reveal">

            <!-- SUCCESS STATE -->
            <div *ngIf="submittedSuccess" class="text-center py-8 animate-scale-in">
              <div class="w-16 h-16 bg-[#00E676]/10 text-[#00E676] border border-[#00E676]/30 rounded-2xl flex items-center justify-center mx-auto mb-6 shadow-[0_0_25px_rgba(0,230,118,0.2)] animate-beacon">
                <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg>
              </div>
              <h2 class="text-3xl font-black text-white uppercase mb-3 font-['Outfit']">Enquiry Confirmed</h2>
              <p class="text-gray-400 text-sm max-w-md mx-auto mb-8 leading-relaxed font-['Plus_Jakarta_Sans']">
                Thank you <span class="font-bold text-white">{{ enquiryData.customerName }}</span>. Your request has been logged and assigned to the service supervisor at our <span class="font-bold text-[#00E676]">{{ enquiryData.preferredBranch | titlecase }}</span> workshop.
              </p>

              <div class="bg-[#0A0C10] border border-white/[0.08] rounded-xl p-6 mb-8 text-left max-w-md mx-auto space-y-3 font-['JetBrains_Mono']">
                <div class="flex justify-between text-xs py-1 border-b border-white/[0.04]">
                  <span class="text-gray-400">Tracking Reference:</span>
                  <span class="font-bold text-[#00E676]">{{ generatedId }}</span>
                </div>
                <div class="flex justify-between text-xs py-1 border-b border-white/[0.04]">
                  <span class="text-gray-400">Motorcycle:</span>
                  <span class="font-bold text-white">{{ enquiryData.bikeModel }}</span>
                </div>
                <div class="flex justify-between text-xs py-1 border-b border-white/[0.04]">
                  <span class="text-gray-400">Service Category:</span>
                  <span class="text-gray-300">{{ enquiryData.serviceType }}</span>
                </div>
                <div class="flex justify-between text-xs py-1">
                  <span class="text-gray-400">Workshop Direct Line:</span>
                  <span class="text-white font-bold">{{ enquiryData.preferredBranch === 'avadi' ? '+91 98401 22334' : '+91 98400 11223' }}</span>
                </div>
              </div>

              <div class="flex flex-col sm:flex-row justify-center gap-3">
                <button
                  (click)="resetForm()"
                  class="btn-laser px-6 py-3.5 bg-[#00E676] hover:bg-[#00c864] text-[#0A0C10] text-xs font-black uppercase tracking-wider rounded-xl transition-all shadow-[0_0_20px_rgba(0,230,118,0.25)] font-['Outfit']"
                >
                  Submit Another Enquiry
                </button>
                <a
                  routerLink="/"
                  class="px-6 py-3.5 bg-white/[0.05] text-white text-xs font-bold uppercase tracking-wider rounded-xl hover:bg-white/[0.1] transition-colors border border-white/[0.08] font-['Outfit']"
                >
                  Back to Home
                </a>
              </div>
            </div>

            <!-- FORM STATE -->
            <div *ngIf="!submittedSuccess">
              <div class="flex items-center justify-between mb-8 pb-4 border-b border-white/[0.06]">
                <h3 class="text-xl font-black uppercase text-white flex items-center gap-2 font-['Outfit']">
                  <span class="w-2.5 h-2.5 rounded-full bg-[#00E676]"></span>
                  <span>Workshop Service Request</span>
                </h3>
                <span class="text-xs text-gray-500 font-['JetBrains_Mono']">* Required fields</span>
              </div>

              <div class="p-4 rounded-xl bg-white/[0.02] border border-white/[0.06] mb-6">
                <p class="text-xs text-gray-300 font-['Plus_Jakarta_Sans'] leading-relaxed">
                  <strong class="text-[#00E676] font-['JetBrains_Mono']">Digital Check-in:</strong> Submitting this ticket registers your vehicle directly into our diagnostic queue. A supervisor will call to schedule your bay slot.
                </p>
              </div>

              <!-- General Error State -->
              <div *ngIf="errorMessage" class="mb-6 p-4 bg-red-950/40 border border-red-500/50 rounded-xl text-xs text-red-200 flex items-center gap-3 font-['Plus_Jakarta_Sans']">
                <svg class="w-5 h-5 shrink-0 text-red-400" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd"/></svg>
                <span>{{ errorMessage }}</span>
              </div>

              <form (ngSubmit)="onSubmit()" class="space-y-5">
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <!-- Name -->
                  <div>
                    <label class="block text-xs font-semibold uppercase tracking-wider text-gray-400 mb-2 font-['JetBrains_Mono']">
                      Your Name <span class="text-[#00E676]">*</span>
                    </label>
                    <input
                      type="text"
                      [(ngModel)]="enquiryData.customerName"
                      name="customerName"
                      placeholder="e.g. Vikram Raj"
                      required
                      class="w-full bg-[#0A0C10] border text-sm rounded-xl px-4 py-3 text-white placeholder-gray-600 focus:outline-none transition-colors font-['Plus_Jakarta_Sans']"
                      [ngClass]="errors.customerName ? 'border-red-500' : 'border-white/[0.1] focus:border-[#00E676]'"
                    />
                    <span *ngIf="errors.customerName" class="text-xs text-red-400 mt-1 block font-['JetBrains_Mono']">{{ errors.customerName }}</span>
                  </div>

                  <!-- Mobile -->
                  <div>
                    <label class="block text-xs font-semibold uppercase tracking-wider text-gray-400 mb-2 font-['JetBrains_Mono']">
                      Mobile Number <span class="text-[#00E676]">*</span>
                    </label>
                    <div class="relative">
                      <span class="absolute left-4 top-3 text-xs text-gray-500 font-['JetBrains_Mono']">+91</span>
                      <input
                        type="tel"
                        [(ngModel)]="enquiryData.phoneNumber"
                        name="phoneNumber"
                        placeholder="98400 11223"
                        maxlength="10"
                        required
                        class="w-full bg-[#0A0C10] border text-sm rounded-xl pl-12 pr-4 py-3 text-white placeholder-gray-600 focus:outline-none transition-colors font-['JetBrains_Mono']"
                        [ngClass]="errors.phoneNumber ? 'border-red-500' : 'border-white/[0.1] focus:border-[#00E676]'"
                      />
                    </div>
                    <span *ngIf="errors.phoneNumber" class="text-xs text-red-400 mt-1 block font-['JetBrains_Mono']">{{ errors.phoneNumber }}</span>
                  </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <!-- Email -->
                  <div>
                    <label class="block text-xs font-semibold uppercase tracking-wider text-gray-400 mb-2 font-['JetBrains_Mono']">
                      Email Address
                    </label>
                    <input
                      type="email"
                      [(ngModel)]="enquiryData.email"
                      name="email"
                      placeholder="vikram@domain.com"
                      class="w-full bg-[#0A0C10] border border-white/[0.1] text-sm rounded-xl px-4 py-3 text-white placeholder-gray-600 focus:outline-none focus:border-[#00E676] transition-colors font-['Plus_Jakarta_Sans']"
                    />
                  </div>

                  <!-- Motorcycle -->
                  <div>
                    <label class="block text-xs font-semibold uppercase tracking-wider text-gray-400 mb-2 font-['JetBrains_Mono']">
                      Motorcycle Make & Model <span class="text-[#00E676]">*</span>
                    </label>
                    <input
                      type="text"
                      [(ngModel)]="enquiryData.bikeModel"
                      name="bikeModel"
                      placeholder="e.g. Triumph Street Triple 765 RS"
                      required
                      class="w-full bg-[#0A0C10] border text-sm rounded-xl px-4 py-3 text-white placeholder-gray-600 focus:outline-none transition-colors font-['Plus_Jakarta_Sans']"
                      [ngClass]="errors.bikeModel ? 'border-red-500' : 'border-white/[0.1] focus:border-[#00E676]'"
                    />
                    <span *ngIf="errors.bikeModel" class="text-xs text-red-400 mt-1 block font-['JetBrains_Mono']">{{ errors.bikeModel }}</span>
                  </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <!-- Service Type -->
                  <div>
                    <label class="block text-xs font-semibold uppercase tracking-wider text-gray-400 mb-2 font-['JetBrains_Mono']">
                      Service Category <span class="text-[#00E676]">*</span>
                    </label>
                    <select
                      [(ngModel)]="enquiryData.serviceType"
                      name="serviceType"
                      class="w-full bg-[#0A0C10] border border-white/[0.1] text-sm rounded-xl px-4 py-3 text-white focus:outline-none focus:border-[#00E676] transition-colors font-['Plus_Jakarta_Sans']"
                    >
                      <option value="Superbike Precision Diagnostics">NITRO RACING Superbike Diagnostics (400cc+)</option>
                      <option value="Nitro Modz Exhaust & Tuning">Nitro Modz Performance Exhaust & Tuning</option>
                      <option value="Periodic Master Service">Periodic Master Service (Motul 7100)</option>
                      <option value="Desmo Valve Clearance">Desmodromic / Shim Valve Clearance</option>
                      <option value="Brembo Brakes & Suspension">Brakes & Front Fork Overhaul</option>
                      <option value="Ceramic Coating & Detailing">Ceramic Coating & Deep Wash</option>
                      <option value="General Inspection">General Inspection / Diagnostic Scan</option>
                    </select>
                  </div>

                  <!-- Preferred Branch -->
                  <div>
                    <label class="block text-xs font-semibold uppercase tracking-wider text-gray-400 mb-2 font-['JetBrains_Mono']">
                      Preferred Workshop <span class="text-[#00E676]">*</span>
                    </label>
                    <select
                      [(ngModel)]="enquiryData.preferredBranch"
                      name="preferredBranch"
                      class="w-full bg-[#0A0C10] border border-white/[0.1] text-sm rounded-xl px-4 py-3 text-white focus:outline-none focus:border-[#00E676] transition-colors font-['Plus_Jakarta_Sans']"
                    >
                      <option value="ambattur">Ambattur Main Hub (SIDCO Industrial Estate)</option>
                      <option value="avadi">Avadi Superbike Bay (New Military Rd)</option>
                    </select>
                  </div>
                </div>

                <!-- Message -->
                <div>
                  <label class="block text-xs font-semibold uppercase tracking-wider text-gray-400 mb-2 font-['JetBrains_Mono']">
                    Notes / Symptoms / Upgrades Requested
                  </label>
                  <textarea
                    [(ngModel)]="enquiryData.message"
                    name="message"
                    rows="3"
                    placeholder="Provide details about odometer reading, specific sounds, error indicators, or custom parts you want installed..."
                    class="w-full bg-[#0A0C10] border border-white/[0.1] text-sm rounded-xl px-4 py-3 text-white placeholder-gray-600 focus:outline-none focus:border-[#00E676] transition-colors font-['Plus_Jakarta_Sans']"
                  ></textarea>
                </div>

                <!-- Submit Button -->
                <button
                  type="submit"
                  [disabled]="isSubmitting"
                  class="btn-laser w-full py-4 bg-[#00E676] hover:bg-[#00c864] text-[#0A0C10] font-black text-sm uppercase tracking-wider rounded-xl transition-all flex items-center justify-center gap-3 shadow-[0_0_25px_rgba(0,230,118,0.25)] disabled:opacity-50 font-['Outfit']"
                >
                  <span *ngIf="isSubmitting" class="w-4 h-4 border-2 border-black border-t-transparent rounded-full animate-spin"></span>
                  <span>{{ isSubmitting ? 'Registering Booking...' : 'Confirm Workshop Bay Booking' }}</span>
                </button>
              </form>
            </div>

          </div>

          <!-- Right: Branch Contact Cards & Emergency Info -->
          <div class="lg:col-span-5 space-y-6">

            <!-- Ambattur Card -->
            <div class="premium-card p-6 space-y-3 scroll-reveal">
              <div class="flex items-center justify-between">
                <h4 class="text-lg font-black uppercase text-white font-['Outfit']">Ambattur Main Hub</h4>
                <span class="text-[10px] font-bold text-[#00E676] uppercase tracking-wider bg-[#00E676]/10 px-2.5 py-0.5 rounded border border-[#00E676]/20 font-['JetBrains_Mono']">HQ Branch</span>
              </div>
              <p class="text-xs text-gray-400 font-['Plus_Jakarta_Sans']">
                Plot 14/2A, SIDCO Industrial Estate Road, Ambattur, Chennai - 600058 (Near Ambattur Telephone Exchange)
              </p>
              <div class="pt-2 text-xs space-y-2 text-gray-400 font-['JetBrains_Mono']">
                <div class="flex justify-between py-1 border-b border-white/[0.04]">
                  <span>Direct Hotline:</span>
                  <a href="tel:+919840011223" class="text-[#00E676] font-bold hover:underline inline-flex items-center gap-1.5">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
                    <span>+91 98400 11223</span>
                  </a>
                </div>
                <div class="flex justify-between py-1 border-b border-white/[0.04]">
                  <span>Lead Supervisor:</span>
                  <span class="text-white">S. Ramanathan</span>
                </div>
                <div class="flex justify-between py-1">
                  <span>Operating Hours:</span>
                  <span class="text-white">Mon–Sat: 8:30 AM – 8:00 PM</span>
                </div>
              </div>
            </div>

            <!-- Avadi Card -->
            <div class="premium-card p-6 space-y-3 scroll-reveal">
              <div class="flex items-center justify-between">
                <h4 class="text-lg font-black uppercase text-white font-['Outfit']">Avadi Superbike Bay</h4>
                <span class="text-[10px] font-bold text-[#38BDF8] uppercase tracking-wider bg-[#38BDF8]/10 px-2.5 py-0.5 rounded border border-[#38BDF8]/20 font-['JetBrains_Mono']">Superbike Hub</span>
              </div>
              <p class="text-xs text-gray-400 font-['Plus_Jakarta_Sans']">
                Old No. 82, New No. 4, New Military Road, Avadi, Chennai - 600054 (Opposite Avadi Bus Terminus)
              </p>
              <div class="pt-2 text-xs space-y-2 text-gray-400 font-['JetBrains_Mono']">
                <div class="flex justify-between py-1 border-b border-white/[0.04]">
                  <span>Direct Hotline:</span>
                  <a href="tel:+919840122334" class="text-[#38BDF8] font-bold hover:underline inline-flex items-center gap-1.5">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
                    <span>+91 98401 22334</span>
                  </a>
                </div>
                <div class="flex justify-between py-1 border-b border-white/[0.04]">
                  <span>Lead Supervisor:</span>
                  <span class="text-white">M. Karthikeyan</span>
                </div>
                <div class="flex justify-between py-1">
                  <span>Operating Hours:</span>
                  <span class="text-white">Mon–Sat: 8:30 AM – 8:00 PM</span>
                </div>
              </div>
            </div>

            <!-- Flatbed Assistance Strip -->
            <div class="premium-card p-6 scroll-reveal">
              <div class="flex items-center gap-2 text-[#00E676] text-xs font-['JetBrains_Mono'] font-bold uppercase tracking-wider mb-2">
                <span>MOTORCYCLE FLATBED RECOVERY</span>
              </div>
              <p class="text-xs text-gray-400 mb-4 leading-relaxed font-['Plus_Jakarta_Sans']">
                Broke down or immobilized? Dedicated hydraulic motorcycle flatbed recovery available across Greater Chennai.
              </p>
              <a href="tel:+919840011223" class="inline-flex items-center gap-2 text-xs font-bold text-white hover:text-[#00E676] transition-colors font-['JetBrains_Mono']">
                <span>Hotline: +91 98400 11223</span>
                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
              </a>
            </div>

          </div>

        </div>

      </div>
    </div>
  `
})
export class ContactComponent {
  enquiryData: Partial<ServiceEnquiry> = {
    customerName: '',
    phoneNumber: '',
    email: '',
    bikeModel: '',
    serviceType: 'Superbike Precision Diagnostics',
    preferredBranch: 'ambattur',
    message: ''
  };

  errors: FormErrors = {};
  errorMessage = '';
  isSubmitting = false;
  submittedSuccess = false;
  generatedId = '';

  constructor(private dataService: DataService) {}

  validate(): boolean {
    this.errors = {};
    if (!this.enquiryData.customerName?.trim()) {
      this.errors.customerName = 'Customer name is required';
    }
    const phone = this.enquiryData.phoneNumber?.replace(/\D/g, '') || '';
    if (!phone || phone.length < 10) {
      this.errors.phoneNumber = 'Valid 10-digit mobile number required';
    }
    if (!this.enquiryData.bikeModel?.trim()) {
      this.errors.bikeModel = 'Please enter your motorcycle make & model';
    }
    return Object.keys(this.errors).length === 0;
  }

  async onSubmit(): Promise<void> {
    if (!this.validate()) return;

    this.isSubmitting = true;
    this.errorMessage = '';

    try {
      const result = await this.dataService.submitEnquiry(this.enquiryData as any);
      this.generatedId = result.id;
      this.submittedSuccess = true;
    } catch (e: any) {
      this.errorMessage = e?.message || 'Network timeout. Could not submit enquiry. Please call us directly.';
    } finally {
      this.isSubmitting = false;
    }
  }

  resetForm(): void {
    this.submittedSuccess = false;
    this.enquiryData = {
      customerName: '',
      phoneNumber: '',
      email: '',
      bikeModel: '',
      serviceType: 'Superbike Precision Diagnostics',
      preferredBranch: 'ambattur',
      message: ''
    };
    this.errors = {};
    this.errorMessage = '';
  }
}
