export interface MotorcycleService {
  id: string;
  code: string;
  name: string;
  category: 'routine' | 'superbike' | 'modz' | 'engine' | 'detailing' | string;
  categoryLabel?: string;
  shortDesc: string;
  shortDescription?: string;
  fullDesc: string;
  description?: string;
  duration: string;
  estimatedDuration?: string;
  startingPrice: number;
  basePrice?: string;
  featured: boolean;
  includedList: string[];
  includedItems?: string[];
  recommendedInterval?: string;
  applicableModels?: string;
  imageUrl?: string;
  badge?: string;
  telemetryTag?: string;
  divisionTag?: string;
}

export type WorkshopService = MotorcycleService;

export interface Branch {
  id: string;
  code: string;
  name: string;
  doorNo: string;
  street: string;
  landmark: string;
  area: string;
  city: string;
  state: string;
  pincode: string;
  phone: string;
  email: string;
  manager: string;
  managerName?: string;
  bays: number;
  hoursWeekday: string;
  hoursSunday: string;
  workingHours?: string;
  gstin: string;
  status: 'ACTIVE' | 'PLANNED';
  mapUrl?: string;
  mapsUrl?: string;
  address?: string;
  specialties?: string[];
  imageUrl?: string;
  tagline?: string;
  hubBadge?: string;
  bayCountText?: string;
  keyEquipments?: { title: string; desc: string }[];
}

export interface Testimonial {
  id: string;
  customerName: string;
  neighborhood?: string;
  bikeModel: string;
  serviceCategory?: string;
  rating: number;
  date: string;
  review: string;
  feedback?: string;
  branch: string;
  jobCardNo?: string;
  avatarInitials?: string;
  verified?: boolean;
  categoryKey?: string;
}

export interface GalleryItem {
  id: string;
  title: string;
  category: 'superbikes' | 'workshop' | 'modz' | 'engine' | 'dyno' | 'detailing' | string;
  imageUrl: string;
  caption: string;
  description?: string;
  bikeModel?: string;
  branch?: string;
  buildType?: string;
  specs?: { label: string; value: string }[];
  tags?: string[];
  date?: string;
  jobCardNo?: string;
}

export interface ServiceEnquiry {
  id?: string;
  customerName: string;
  phoneNumber?: string;
  mobileNumber?: string;
  email?: string;
  bikeModel?: string;
  serviceType?: string;
  serviceRequired?: string;
  preferredBranch?: string;
  message?: string;
  createdAt?: Date;
}

export type EnquirySubmission = ServiceEnquiry;
