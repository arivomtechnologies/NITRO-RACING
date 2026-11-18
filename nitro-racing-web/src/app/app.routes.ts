import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { AboutComponent } from './pages/about/about.component';
import { ServicesComponent } from './pages/services/services.component';
import { ServiceDetailComponent } from './pages/service-detail/service-detail.component';
import { BranchesComponent } from './pages/branches/branches.component';
import { GalleryComponent } from './pages/gallery/gallery.component';
import { TestimonialsComponent } from './pages/testimonials/testimonials.component';
import { ContactComponent } from './pages/contact/contact.component';

export const routes: Routes = [
  { path: '', component: HomeComponent, title: 'Nitro Racing Modz | Lightning Speed Motorcycle Service & Tuning Studio' },
  { path: 'about', component: AboutComponent, title: 'About Us | Nitro Racing Modz Chennai' },
  { path: 'services', component: ServicesComponent, title: 'Services & Nitro Modz | Nitro Racing' },
  { path: 'services/:id', component: ServiceDetailComponent, title: 'Service Details | Nitro Racing' },
  { path: 'branches', component: BranchesComponent, title: 'Our Chennai Workshops | Ambattur & Avadi | Nitro Racing' },
  { path: 'gallery', component: GalleryComponent, title: 'Workshop Gallery | Nitro Racing' },
  { path: 'testimonials', component: TestimonialsComponent, title: 'Client Reviews | Nitro Racing' },
  { path: 'contact', component: ContactComponent, title: 'Book Service Enquiry | Nitro Racing' },
  { path: 'login', redirectTo: '' },
  { path: '**', redirectTo: '' }
];
