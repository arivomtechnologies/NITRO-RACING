import { Component, EventEmitter, Input, Output } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { DataService } from '../../services/data.service';
import { ServiceEnquiry } from '../../models/service.model';

interface FormErrors {
  customerName?: string;
  phoneNumber?: string;
  bikeModel?: string;
}

@Component({
  selector: 'app-enquiry-modal',
  standalone: true,
  imports: [CommonModule, FormsModule],
  template: `
    <div *ngIf="isOpen" class="fixed inset-0 z-50 overflow-y-auto" role="dialog" aria-modal="true" aria-labelledby="modal-title">
      <!-- Backdrop -->
      <div class="fixed inset-0 bg-[#0A0C10]/85 backdrop-blur-md transition-opacity" (click)="closeModal()"></div>

      <div class="flex min-h-full items-center justify-center p-4 text-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-2xl bg-[#11151F] border border-white/[0.1] text-left shadow-[0_20px_50px_rgba(0,0,0,0.8)] transition-all sm:my-8 sm:w-full sm:max-w-xl text-white animate-scale-in">

          <!-- Header Bar -->
          <div class="bg-[#151A26] px-6 py-4 flex items-center justify-between border-b border-white/[0.08]">
            <div class="flex items-center gap-2.5">
              <span class="w-2.5 h-2.5 rounded-full bg-[#00E676]"></span>
              <h3 id="modal-title" class="text-base font-black tracking-wider uppercase text-white flex items-center gap-2 font-['Outfit']">
                <span>Book Service Bay</span>
                <span class="text-[10px] text-[#0A0C10] bg-[#00E676] px-2 py-0.5 rounded font-black font-['Outfit']">NITRO MODZ</span>
              </h3>
            </div>
            <button (click)="closeModal()" type="button" aria-label="Close dialog" class="text-gray-400 hover:text-white p-1 rounded-lg hover:bg-white/[0.05] transition-colors">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
            </button>
          </div>

          <!-- SUCCESS STATE -->
          <div *ngIf="submittedSuccess" class="p-8 text-center">
            <div class="w-16 h-16 bg-[#00E676]/10 text-[#00E676] border border-[#00E676]/30 rounded-2xl flex items-center justify-center mx-auto mb-4 shadow-[0_0_20px_rgba(0,230,118,0.2)]">
              <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg>
            </div>
            <h4 class="text-2xl font-black text-white uppercase mb-2 font-['Outfit']">Enquiry Confirmed</h4>
            <p class="text-gray-400 text-sm mb-6 font-['Plus_Jakarta_Sans']">
              Thank you, <span class="font-bold text-white">{{ enquiryData.customerName }}</span>. Your request has been queued at our <span class="font-bold text-[#00E676]">{{ enquiryData.preferredBranch | titlecase }}</span> workshop.
            </p>

            <div class="bg-[#0A0C10] border border-white/[0.08] rounded-xl p-5 mb-6 text-left space-y-2.5 font-['JetBrains_Mono']">
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
                <span class="font-medium text-gray-300">{{ enquiryData.serviceType }}</span>
              </div>
              <div class="flex justify-between text-xs py-1">
                <span class="text-gray-400">Workshop Direct Line:</span>
                <span class="font-bold text-white">{{ enquiryData.preferredBranch === 'avadi' ? '+91 98401 22334' : '+91 98400 11223' }}</span>
              </div>
            </div>

            <p class="text-xs text-gray-400 mb-6 font-['Plus_Jakarta_Sans']">
              Our service supervisor will contact your mobile to confirm your scheduled vehicle drop-off and diagnostic slot.
            </p>

            <button (click)="resetAndClose()" class="w-full py-3.5 bg-[#00E676] hover:bg-[#00c864] text-[#0A0C10] font-black text-xs uppercase tracking-wider rounded-xl transition-all shadow-[0_0_20px_rgba(0,230,118,0.25)] font-['Outfit']">
              Done & Return
            </button>
          </div>

          <!-- FORM STATE -->
          <div *ngIf="!submittedSuccess" class="p-6">
            <div class="p-3.5 rounded-xl bg-white/[0.02] border border-white/[0.06] mb-6">
              <p class="text-xs text-gray-300 font-['Plus_Jakarta_Sans'] leading-relaxed">
                <strong class="text-[#00E676] font-['JetBrains_Mono']">Direct Booking:</strong> Reserving here places your machine immediately into our workshop digital queue.
              </p>
            </div>

            <!-- General Error Banner -->
            <div *ngIf="errorMessage" class="mb-4 p-3 bg-red-950/40 border border-red-500/50 rounded-xl text-xs text-red-200 flex items-center gap-2 font-['Plus_Jakarta_Sans']">
              <svg class="w-4 h-4 shrink-0 text-red-400" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd"/></svg>
              <span>{{ errorMessage }}</span>
            </div>

            <form (ngSubmit)="onSubmit()" class="space-y-4">
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <!-- Name -->
                <div>
                  <label class="block text-xs font-semibold uppercase tracking-wider text-gray-400 mb-1.5 font-['JetBrains_Mono']">
                    Your Name <span class="text-[#00E676]">*</span>
                  </label>
                  <input
                    type="text"
                    [(ngModel)]="enquiryData.customerName"
                    name="customerName"
                    placeholder="e.g. Vikram Raghavan"
                    required
                    class="w-full bg-[#0A0C10] border text-sm rounded-xl px-3.5 py-2.5 text-white placeholder-gray-600 focus:outline-none transition-colors font-['Plus_Jakarta_Sans']"
                    [ngClass]="errors.customerName ? 'border-red-500' : 'border-white/[0.1] focus:border-[#00E676]'"
                  />
                  <span *ngIf="errors.customerName" class="text-[11px] text-red-400 mt-1 block font-['JetBrains_Mono']">{{ errors.customerName }}</span>
                </div>

                <!-- Phone -->
                <div>
                  <label class="block text-xs font-semibold uppercase tracking-wider text-gray-400 mb-1.5 font-['JetBrains_Mono']">
                    Mobile Number <span class="text-[#00E676]">*</span>
                  </label>
                  <div class="relative">
                    <span class="absolute left-3.5 top-2.5 text-xs text-gray-500 font-['JetBrains_Mono']">+91</span>
                    <input
                      type="tel"
                      [(ngModel)]="enquiryData.phoneNumber"
                      name="phoneNumber"
                      placeholder="98400 11223"
                      maxlength="10"
                      required
                      class="w-full bg-[#0A0C10] border text-sm rounded-xl pl-11 pr-3.5 py-2.5 text-white placeholder-gray-600 focus:outline-none transition-colors font-['JetBrains_Mono']"
                      [ngClass]="errors.phoneNumber ? 'border-red-500' : 'border-white/[0.1] focus:border-[#00E676]'"
                    />
                  </div>
                  <span *ngIf="errors.phoneNumber" class="text-[11px] text-red-400 mt-1 block font-['JetBrains_Mono']">{{ errors.phoneNumber }}</span>
                </div>
              </div>

              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <!-- Email -->
                <div>
                  <label class="block text-xs font-semibold uppercase tracking-wider text-gray-400 mb-1.5 font-['JetBrains_Mono']">
                    Email Address
                  </label>
                  <input
                    type="email"
                    [(ngModel)]="enquiryData.email"
                    name="email"
                    placeholder="rider@example.com"
                    class="w-full bg-[#0A0C10] border border-white/[0.1] text-sm rounded-xl px-3.5 py-2.5 text-white placeholder-gray-600 focus:outline-none focus:border-[#00E676] transition-colors font-['Plus_Jakarta_Sans']"
                  />
                </div>

                <!-- Bike Model -->
                <div>
                  <label class="block text-xs font-semibold uppercase tracking-wider text-gray-400 mb-1.5 font-['JetBrains_Mono']">
                    Motorcycle Make & Model <span class="text-[#00E676]">*</span>
                  </label>
                  <input
                    type="text"
                    [(ngModel)]="enquiryData.bikeModel"
                    name="bikeModel"
                    placeholder="e.g. Kawasaki ZX-10R / Duke 390"
                    required
                    class="w-full bg-[#0A0C10] border text-sm rounded-xl px-3.5 py-2.5 text-white placeholder-gray-600 focus:outline-none transition-colors font-['Plus_Jakarta_Sans']"
                    [ngClass]="errors.bikeModel ? 'border-red-500' : 'border-white/[0.1] focus:border-[#00E676]'"
                  />
                  <span *ngIf="errors.bikeModel" class="text-[11px] text-red-400 mt-1 block font-['JetBrains_Mono']">{{ errors.bikeModel }}</span>
                </div>
              </div>

              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <!-- Service Type -->
                <div>
                  <label class="block text-xs font-semibold uppercase tracking-wider text-gray-400 mb-1.5 font-['JetBrains_Mono']">
                    Service Required <span class="text-[#00E676]">*</span>
                  </label>
                  <select
                    [(ngModel)]="enquiryData.serviceType"
                    name="serviceType"
                    class="w-full bg-[#0A0C10] border border-white/[0.1] text-sm rounded-xl px-3 py-2.5 text-white focus:outline-none focus:border-[#00E676] transition-colors font-['Plus_Jakarta_Sans']"
                  >
                    <option value="Superbike Precision Service">NITRO RACING Superbike Diagnostics (400cc+)</option>
                    <option value="Nitro Modz Exhaust & Tuning">Nitro Modz Tuning & Performance Exhaust</option>
                    <option value="Periodic Master Service">Periodic Routine Service & Fluids</option>
                    <option value="Engine Overhaul & Desmo">Engine Rebuild & Valve Clearance</option>
                    <option value="Brembo Brakes & Suspension">Brakes & Suspension Overhaul</option>
                    <option value="Ceramic Coating & Detailing">Ceramic Coating & Wash</option>
                    <option value="General Inspection / Other">General Inspection / Diagnostic Scan</option>
                  </select>
                </div>

                <!-- Preferred Branch -->
                <div>
                  <label class="block text-xs font-semibold uppercase tracking-wider text-gray-400 mb-1.5 font-['JetBrains_Mono']">
                    Preferred Workshop <span class="text-[#00E676]">*</span>
                  </label>
                  <select
                    [(ngModel)]="enquiryData.preferredBranch"
                    name="preferredBranch"
                    class="w-full bg-[#0A0C10] border border-white/[0.1] text-sm rounded-xl px-3 py-2.5 text-white focus:outline-none focus:border-[#00E676] transition-colors font-['Plus_Jakarta_Sans']"
                  >
                    <option value="ambattur">Ambattur Main Hub (SIDCO Industrial Estate)</option>
                    <option value="avadi">Avadi Superbike Bay (New Military Rd)</option>
                  </select>
                </div>
              </div>

              <!-- Message / Symptoms -->
              <div>
                <label class="block text-xs font-semibold uppercase tracking-wider text-gray-400 mb-1.5 font-['JetBrains_Mono']">
                  Describe Symptoms or Desired Upgrades
                </label>
                <textarea
                  [(ngModel)]="enquiryData.message"
                  name="message"
                  rows="2"
                  placeholder="e.g. Akrapovič slip-on installation, Stage 1 ECU remap, valve shimming..."
                  class="w-full bg-[#0A0C10] border border-white/[0.1] text-sm rounded-xl px-3.5 py-2 text-white placeholder-gray-600 focus:outline-none focus:border-[#00E676] transition-colors font-['Plus_Jakarta_Sans']"
                ></textarea>
              </div>

              <!-- Actions -->
              <div class="pt-4 flex items-center justify-end gap-3 border-t border-white/[0.08]">
                <button
                  type="button"
                  (click)="closeModal()"
                  class="px-5 py-2.5 text-xs font-semibold text-gray-400 hover:text-white transition-colors font-['Outfit']"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  [disabled]="isSubmitting"
                  class="btn-laser px-6 py-2.5 bg-[#00E676] hover:bg-[#00c864] text-[#0A0C10] font-black text-xs uppercase tracking-wider rounded-xl transition-all flex items-center gap-2 shadow-[0_0_20px_rgba(0,230,118,0.25)] disabled:opacity-50 font-['Outfit']"
                >
                  <span *ngIf="isSubmitting" class="w-4 h-4 border-2 border-black border-t-transparent rounded-full animate-spin"></span>
                  <span>{{ isSubmitting ? 'Registering...' : 'Confirm Bay Booking' }}</span>
                </button>
              </div>
            </form>
          </div>

        </div>
      </div>
    </div>
  `
})
export class EnquiryModalComponent {
  @Input() isOpen = false;
  @Input() set preselectedService(val: string | undefined) {
    if (val) {
      this.enquiryData.serviceType = val;
    }
  }
  @Output() close = new EventEmitter<void>();

  enquiryData: Partial<ServiceEnquiry> = {
    customerName: '',
    phoneNumber: '',
    email: '',
    bikeModel: '',
    serviceType: 'Superbike Precision Service',
    preferredBranch: 'ambattur',
    message: ''
  };

  errors: FormErrors = {};
  errorMessage = '';
  isSubmitting = false;
  submittedSuccess = false;
  generatedId = '';

  constructor(private dataService: DataService) {}

  closeModal(): void {
    this.close.emit();
  }

  validate(): boolean {
    this.errors = {};
    if (!this.enquiryData.customerName?.trim()) {
      this.errors.customerName = 'Name is required';
    }
    const phone = this.enquiryData.phoneNumber?.replace(/\D/g, '') || '';
    if (!phone || phone.length < 10) {
      this.errors.phoneNumber = 'Valid 10-digit mobile required';
    }
    if (!this.enquiryData.bikeModel?.trim()) {
      this.errors.bikeModel = 'Motorcycle model required';
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
      this.errorMessage = e?.message || 'Submission error. Please call our hotline.';
    } finally {
      this.isSubmitting = false;
    }
  }

  resetAndClose(): void {
    this.submittedSuccess = false;
    this.enquiryData = {
      customerName: '',
      phoneNumber: '',
      email: '',
      bikeModel: '',
      serviceType: 'Superbike Precision Service',
      preferredBranch: 'ambattur',
      message: ''
    };
    this.errors = {};
    this.errorMessage = '';
    this.closeModal();
  }
}
