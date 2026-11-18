import { Injectable } from '@angular/core';
import { MotorcycleService, Branch, Testimonial, GalleryItem, EnquirySubmission } from '../models/service.model';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  private services: MotorcycleService[] = [
    {
      id: 'general-service',
      code: 'SRV-GEN-01',
      name: 'General Periodic Service',
      category: 'routine',
      categoryLabel: 'Periodic Maintenance',
      shortDesc: 'Routine 50-point precision care and comprehensive safety inspection for your motorcycle.',
      fullDesc: 'Our flagship 50-point comprehensive periodic maintenance package covers complete fluid inspection, chain tensioning & lube, spark plug cleaning, air filter service, battery load test, brake cleaning, cable lubrication, and fastener torque checks.',
      duration: '90 Mins',
      startingPrice: 650,
      featured: true,
      includedList: [
        '50-point thorough mechanical & safety checklist',
        'Engine oil & oil filter replacement (fluids extra)',
        'Drive chain degreasing, tensioning & high-temp lubrication',
        'Front & rear brake pad cleaning and caliper inspection',
        'Spark plug gap inspection & ultrasonic cleaning',
        'Clutch, throttle and choke cable free-play adjustment',
        'Battery voltage & charging circuit load test',
        'High-pressure foam wash and dry polish'
      ],
      recommendedInterval: 'Every 3,000 km or 3 Months',
      applicableModels: 'All commuter & sports motorcycles (100cc – 300cc)'
    },
    {
      id: 'superbike-major-service',
      code: 'SRV-SBK-01',
      name: 'Superbike Major Service & Valve Clearance',
      category: 'superbike',
      categoryLabel: 'Superbike Care Division',
      shortDesc: 'Dedicated master technician service for high-CC performance machines (400cc – 1000cc+).',
      fullDesc: 'NITRO RACING race-grade maintenance specifically designed for multi-cylinder performance superbikes (Inline-4, V-Twin, Triple). Includes shimming / valve clearance inspection, computerized diagnostic health check, throttle synchronization, and chassis torqueing.',
      duration: '240 Mins',
      startingPrice: 3500,
      featured: true,
      includedList: [
        'Valve clearance / shim measurement and precision adjustment',
        'Electronic throttle body synchronization and TPS calibration',
        'OBD-2 ECU fault code scan and live sensor diagnostic logs',
        'Motul 300V Factory Line racing fluid service',
        'Brembo sintered brake caliper overhaul & DOT 5.1 fluid flush',
        'Slipper clutch friction plate wear measurement',
        'Swingarm pivot & steering head bearing greasing',
        'Dyno health check & high-speed chassis stability inspection'
      ],
      recommendedInterval: 'Every 6,000 km or 6 Months',
      applicableModels: 'Kawasaki Ninja, ZX-10R, Yamaha R1/R3, Ducati, Triumph, BMW, Honda CBR, RE 650'
    },
    {
      id: 'superbike-obd-diagnostics',
      code: 'SRV-SBK-02',
      name: 'Superbike OBD-2 Diagnostic & Throttle Sync',
      category: 'superbike',
      categoryLabel: 'Superbike Care Division',
      shortDesc: 'Digital electronic ECU fault scanning, sensor mapping, and electronic throttle calibration.',
      fullDesc: 'Modern electronic motorcycles require specialized diagnostic computers. We plug directly into your bike’s CAN-bus to diagnose check-engine lights, recalibrate ride-by-wire throttles, and clear false error codes.',
      duration: '60 Mins',
      startingPrice: 1200,
      featured: false,
      includedList: [
        'Direct OBD-2 CAN-bus computerized diagnostic connection',
        'Full ECU fault code read, analysis, and clearing',
        'Ride-by-wire electronic throttle body calibration',
        'O2 sensor, MAP sensor, and coolant temp sensor live testing',
        'ABS and traction control unit diagnostic check'
      ],
      recommendedInterval: 'On check-engine warning or annual service',
      applicableModels: 'All fuel-injected and ECU-managed motorcycles'
    },
    {
      id: 'superbike-coolant-flush',
      code: 'SRV-SBK-03',
      name: 'Radiator Engine Ice Coolant Flush',
      category: 'superbike',
      categoryLabel: 'Superbike Care Division',
      shortDesc: 'Complete cooling system chemical flush and refill with Engine Ice racing coolant.',
      fullDesc: 'High-compression engines produce extreme heat in city traffic. We completely flush old acidic coolant, reverse-flush the radiator core, inspect thermostat operation, and refill with non-toxic Engine Ice high-performance coolant for up to 10°C lower running temperatures.',
      duration: '45 Mins',
      startingPrice: 650,
      featured: false,
      includedList: [
        'Complete drainage of old radiator and reservoir coolant',
        'Chemical flush to remove scale and internal corrosion',
        'Radiator cap pressure test & radiator fan relay test',
        'Engine Ice USA racing coolant refill with vacuum bleed'
      ],
      recommendedInterval: 'Every 12 Months or 10,000 km',
      applicableModels: 'All liquid-cooled motorcycles & superbikes'
    },
    {
      id: 'performance-exhaust-mod',
      code: 'SRV-MOD-01',
      name: 'Performance Exhaust Installation',
      category: 'modz',
      categoryLabel: 'Nitro Modz & Tuning',
      shortDesc: 'Slip-on and full-system exhaust fitment with custom header alignment and heat shielding.',
      fullDesc: 'Transform your motorcycle’s acoustic note, drop up to 6 kg of weight, and unleash top-end horsepower with precision exhaust installation. We fit genuine Akrapovič, Arrow, Austin Racing, SC Project, and custom performance headers with leak-proof copper gaskets.',
      duration: '90 Mins',
      startingPrice: 1500,
      featured: true,
      includedList: [
        'OEM exhaust removal and manifold inspection',
        'Precision slip-on or full-system stainless/titanium fitment',
        'High-temperature copper gasket sealing (zero exhaust leaks)',
        'O2 sensor bung adaptation or delete harness',
        'Sound decibel measurement and customer tuning approval'
      ],
      recommendedInterval: 'One-time upgrade',
      applicableModels: 'All performance sports bikes, cafe racers & roadsters'
    },
    {
      id: 'ecu-remapping-dyno',
      code: 'SRV-MOD-02',
      name: 'ECU Stage 1 / Stage 2 Fuel Map Flashing',
      category: 'modz',
      categoryLabel: 'Nitro Modz & Tuning',
      shortDesc: 'Custom fuel and ignition map flashing for improved throttle response and torque.',
      fullDesc: 'Stock factory ECU maps are overly lean to pass emissions. Our Stage 1 and Stage 2 flashes optimize air-fuel ratios, smoothen on-off throttle snatchiness, eliminate factory speed limiters, and lower radiator fan activation temperature.',
      duration: '120 Mins',
      startingPrice: 2800,
      featured: true,
      includedList: [
        'Stock ECU ROM extraction and cloud backup',
        'Stage 1 / Stage 2 optimized fuel and ignition advance mapping',
        'Deceleration popping / backfire tuning or elimination',
        'Top speed limiter removal and RPM limiter adjustment',
        'Lowered radiator fan turn-on threshold (8°C cooler)'
      ],
      recommendedInterval: 'Recommended after exhaust or air filter upgrades',
      applicableModels: 'KTM 390/250, Yamaha R15/MT15, RE 650 Twins, Kawasaki, Triumph'
    },
    {
      id: 'auxiliary-fog-lights',
      code: 'SRV-MOD-03',
      name: 'Auxiliary Lights & Custom Wiring Harness',
      category: 'modz',
      categoryLabel: 'Nitro Modz & Tuning',
      shortDesc: 'Professional high-lumen auxiliary LED fog light installation with dedicated relay protection.',
      fullDesc: 'Never splice stock wiring! We build custom plug-and-play wiring harnesses with waterproof 40A relays, waterproof fuse taps, and ergonomic handlebar-mounted switches to power Maddog, Baja Designs, or Clearwater LED lights safely.',
      duration: '75 Mins',
      startingPrice: 850,
      featured: false,
      includedList: [
        'Custom heavy-duty wiring harness with 40A sealed automotive relay',
        'Inline waterproof blade fuse protection',
        'CNC aluminum crash guard or fork mounting clamps',
        'Handlebar waterproof toggle switch with LED indicator',
        'Precision headlight beam alignment (spot / flood combination)'
      ],
      recommendedInterval: 'One-time upgrade',
      applicableModels: 'Adventure bikes, Royal Enfield, touring motorcycles'
    },
    {
      id: 'crash-guard-sliders',
      code: 'SRV-MOD-04',
      name: 'Crash Guard & Frame Sliders Fitment',
      category: 'modz',
      categoryLabel: 'Nitro Modz & Tuning',
      shortDesc: 'Heavy-duty tubular engine guards and Delrin frame sliders to protect critical components.',
      fullDesc: 'Protect your engine casing, radiator, and fairings from costly drop damage. We fit precision-engineered tubular crash guards and Delrin frame sliders using high-tensile Grade 8.8 / 10.9 chassis mounting bolts.',
      duration: '60 Mins',
      startingPrice: 500,
      featured: false,
      includedList: [
        'Chassis mounting point inspection and thread preparation',
        'Grade 10.9 high-tensile steel mounting hardware with Loctite',
        'Tubular guard alignment with zero engine vibration transfer',
        'Replaceable high-density Delrin slider pucks'
      ],
      recommendedInterval: 'Essential protection upgrade',
      applicableModels: 'All naked, sport, and adventure motorcycles'
    },
    {
      id: 'engine-repair',
      code: 'SRV-ENG-01',
      name: 'Engine Diagnostic & Overhaul',
      category: 'engine',
      categoryLabel: 'Engine Operations',
      shortDesc: 'In-depth diagnostic inspection and repair for engine noise, smoke, or power loss.',
      fullDesc: 'Our engine specialists diagnose tapping noises, white/blue exhaust smoke, compression loss, and piston ring wear. We perform precision cylinder honing, piston replacement, valve lapping, and crankshaft truing.',
      duration: '180 Mins',
      startingPrice: 1800,
      featured: false,
      includedList: [
        'Cylinder head compression test & leak-down diagnostic',
        'Borescope inspection of combustion chamber & cylinder walls',
        'Tappet / valve clearance setting',
        'Timing chain tensioner inspection and replacement',
        'Engine oil pressure measurement'
      ],
      recommendedInterval: 'When experiencing noise, oil consumption, or smoke',
      applicableModels: 'All four-stroke two-wheelers'
    },
    {
      id: 'brake-caliper-overhaul',
      code: 'SRV-BRK-01',
      name: 'Brake Caliper Overhaul & Fluid Bleeding',
      category: 'routine',
      categoryLabel: 'Brake Care',
      shortDesc: 'Restore razor-sharp stopping power with caliper rebuilding and fresh DOT 4 fluid.',
      fullDesc: 'Spongy brake levers and uneven pad wear endanger rider safety. We dismantle brake calipers, clean pistons ultrasonically, replace rubber dust seals, lubricate slide pins with silicone grease, and bleed fresh hydraulic fluid.',
      duration: '45 Mins',
      startingPrice: 350,
      featured: false,
      includedList: [
        'Caliper removal, piston extraction, and degreasing',
        'Slide pin cleaning and high-temp silicone lubrication',
        'Brake rotor runout measurement with dial gauge',
        'Vacuum bleeding with fresh DOT 4 synthetic brake fluid',
        'Bed-in procedure and emergency stop testing'
      ],
      recommendedInterval: 'Every 6 Months or 6,000 km',
      applicableModels: 'All disc-brake motorcycles & scooters'
    },
    {
      id: 'washing-detailing',
      code: 'SRV-WSH-01',
      name: 'Premium Foam Wash & Ceramic Polish',
      category: 'detailing',
      categoryLabel: 'Detailing & Polish',
      shortDesc: 'pH-neutral foam bath, engine degreasing, chain shine, and hydrophobic paint sealant.',
      fullDesc: 'Give your ride that showroom race finish. We use pH-neutral carnauba shampoo, non-corrosive engine bay degreasers, plastic trim restorative sealants, and spray ceramic hydrophobic protection.',
      duration: '45 Mins',
      startingPrice: 300,
      featured: false,
      includedList: [
        'High-pressure pre-rinse to remove road grit',
        'Snow foam bath with ultra-soft microfiber mitts',
        'Alloy wheel de-tarring and sprocket degreasing',
        'Heated warm-air blowout drying (no water spots)',
        'Hydrophobic paint sealant & matte vinyl dressing'
      ],
      recommendedInterval: 'Monthly or post-monsoon',
      applicableModels: 'All motorcycles & scooters'
    }
  ];

  private branches: Branch[] = [
    {
      id: 'ambattur',
      code: 'BR-AMB-01',
      name: 'Nitro Racing – Ambattur Branch',
      doorNo: 'Plot 14/2A',
      street: 'SIDCO Industrial Estate Road',
      landmark: 'Near Ambattur Telephone Exchange',
      area: 'Ambattur',
      city: 'Chennai',
      state: 'Tamil Nadu',
      pincode: '600058',
      phone: '+91 98400 11223',
      email: 'ambattur@nitroracing.in',
      manager: 'S. Ramanathan (Operations Head)',
      bays: 6,
      hoursWeekday: 'Monday – Saturday: 8:30 AM – 8:00 PM',
      hoursSunday: 'Sunday: 9:00 AM – 2:00 PM',
      gstin: '33AABCN1234D1Z2',
      status: 'ACTIVE',
      mapUrl: 'https://maps.google.com/?q=Ambattur+Industrial+Estate+Chennai'
    },
    {
      id: 'avadi',
      code: 'BR-AVD-02',
      name: 'Nitro Racing – Avadi Branch',
      doorNo: 'Old No. 82, New No. 4',
      street: 'New Military Road',
      landmark: 'Opposite Avadi Bus Terminus',
      area: 'Avadi',
      city: 'Chennai',
      state: 'Tamil Nadu',
      pincode: '600054',
      phone: '+91 98401 22334',
      email: 'avadi@nitroracing.in',
      manager: 'M. Karthikeyan (Branch Manager)',
      bays: 4,
      hoursWeekday: 'Monday – Saturday: 8:30 AM – 8:00 PM',
      hoursSunday: 'Sunday: Closed (Track Events)',
      gstin: '33AABCN1234D1Z2',
      status: 'ACTIVE',
      mapUrl: 'https://maps.google.com/?q=New+Military+Road+Avadi+Chennai'
    }
  ];

  private testimonials: Testimonial[] = [
    {
      id: 't1',
      customerName: 'Rajesh Kumar',
      neighborhood: 'Anna Nagar West',
      bikeModel: 'Yamaha R15 V4',
      serviceCategory: 'Periodic Service & Brakes',
      categoryKey: 'routine',
      rating: 5,
      date: 'November 2026',
      jobCardNo: 'JC-8821',
      avatarInitials: 'RK',
      verified: true,
      review: 'Brought my R15 V4 with spongy front brakes and a dry rattling chain. The digital check-in on the tablet was lightning fast, estimate was shared on WhatsApp with clear parts breakdown, and bike rides like new.',
      branch: 'Ambattur Branch'
    },
    {
      id: 't2',
      customerName: 'Siddharth Menon',
      neighborhood: 'Thiruvanmiyur',
      bikeModel: 'Kawasaki Ninja ZX-10R',
      serviceCategory: 'Superbike Major Service',
      categoryKey: 'superbike',
      rating: 5,
      date: 'November 2026',
      jobCardNo: 'JC-8844',
      avatarInitials: 'SM',
      verified: true,
      review: 'Finding a workshop in Chennai that truly understands liter-class superbikes is tough. Master tech Hari handled my ZX-10R valve clearance and Engine Ice flush with extreme care using proper paddock stands. Best superbike garage!',
      branch: 'Ambattur Branch'
    },
    {
      id: 't3',
      customerName: 'Karthik Raja',
      neighborhood: 'Anna Nagar',
      bikeModel: 'Royal Enfield Continental GT 650',
      serviceCategory: 'Nitro Modz Customization',
      categoryKey: 'modz',
      rating: 5,
      date: 'November 2026',
      jobCardNo: 'JC-8809',
      avatarInitials: 'KR',
      verified: true,
      review: 'Fitted an Akrapovič slip-on exhaust and got the ECU Stage 1 tuned at Nitro Modz Avadi. The difference in mid-range torque and deceleration sound is phenomenal. Zero backfires, 100% professional fitment.',
      branch: 'Avadi Branch'
    },
    {
      id: 't4',
      customerName: 'Praveen Chandran',
      neighborhood: 'Avadi',
      bikeModel: 'KTM 390 Duke',
      serviceCategory: 'Fork Overhaul & Brake Pads',
      categoryKey: 'brakes',
      rating: 5,
      date: 'October 2026',
      jobCardNo: 'JC-8762',
      avatarInitials: 'PC',
      verified: true,
      review: 'My front WP inverted forks were leaking oil badly. The Avadi team rebuilt them with genuine seals, fitted Brembo ceramic pads, and had my bike ready by 4 PM as promised. Very transparent pricing!',
      branch: 'Avadi Branch'
    },
    {
      id: 't5',
      customerName: 'Vikramaditya Rao',
      neighborhood: 'ECR Chennai',
      bikeModel: 'Ducati Panigale V2',
      serviceCategory: 'Desmo Valve Clearance & Slipper Clutch',
      categoryKey: 'superbike',
      rating: 5,
      date: 'October 2026',
      jobCardNo: 'JC-8715',
      avatarInitials: 'VR',
      verified: true,
      review: 'Had my Panigale V2 Desmo service completed at Ambattur. They used calibrated micrometers for every valve shim and Motul 300V Factory Line oil. The throttle response and engine smoothness are unmatched.',
      branch: 'Ambattur Branch'
    },
    {
      id: 't6',
      customerName: 'Arun Prasath',
      neighborhood: 'Velachery',
      bikeModel: 'BMW S1000RR',
      serviceCategory: 'OBD-2 CAN-Bus Diagnostics',
      categoryKey: 'superbike',
      rating: 5,
      date: 'October 2026',
      jobCardNo: 'JC-8690',
      avatarInitials: 'AP',
      verified: true,
      review: 'Check-engine light popped up during a track day. The Ambattur team plugged directly into the CAN-bus port, pinpointed a faulty O2 sensor immediately, cleared the ghost codes, and recalibrated the quickshifter.',
      branch: 'Ambattur Branch'
    },
    {
      id: 't7',
      customerName: 'Deepak Sundaram',
      neighborhood: 'Mogappair',
      bikeModel: 'Royal Enfield Himalayan 450',
      serviceCategory: 'Nitro Modz Auxiliary Lighting & Relay',
      categoryKey: 'modz',
      rating: 5,
      date: 'September 2026',
      jobCardNo: 'JC-8641',
      avatarInitials: 'DS',
      verified: true,
      review: 'Got Baja Designs auxiliary pods installed before my Ladakh ride. Zero wire cutting! They constructed a bespoke plug-and-play wiring harness with a waterproof 40A sealed automotive relay. Outstanding build quality.',
      branch: 'Avadi Branch'
    },
    {
      id: 't8',
      customerName: 'Gautham Balaji',
      neighborhood: 'Adyar',
      bikeModel: 'Triumph Street Triple 765 RS',
      serviceCategory: 'Brembo Caliper Rebuild & Bleed',
      categoryKey: 'brakes',
      rating: 5,
      date: 'September 2026',
      jobCardNo: 'JC-8608',
      avatarInitials: 'GB',
      verified: true,
      review: 'Brembo Stylema calipers were ultrasonically cleaned, new high-temp silicone seals installed, and bled with DOT 5.1 racing fluid using their vacuum purge bleeder. Brake feel is razor-sharp now.',
      branch: 'Ambattur Branch'
    },
    {
      id: 't9',
      customerName: 'Naveen Krishnan',
      neighborhood: 'Porur',
      bikeModel: 'Honda CBR 650R',
      serviceCategory: 'Titanium SC Project Exhaust & Dyno Tune',
      categoryKey: 'modz',
      rating: 5,
      date: 'August 2026',
      jobCardNo: 'JC-8550',
      avatarInitials: 'NK',
      verified: true,
      review: 'Full system titanium exhaust fitment done at Nitro Modz Avadi. Perfect weld alignment, zero gas leaks, copper gaskets used, and the Stage 2 ECU flash gave me a crisp +6.2 HP increase on the dyno.',
      branch: 'Avadi Branch'
    },
    {
      id: 't10',
      customerName: 'Harish Raghavan',
      neighborhood: 'Kolathur',
      bikeModel: 'Bajaj Dominar 400',
      serviceCategory: '50-Point General Periodic Service',
      categoryKey: 'routine',
      rating: 5,
      date: 'August 2026',
      jobCardNo: 'JC-8512',
      avatarInitials: 'HR',
      verified: true,
      review: 'Regular periodic maintenance is handled with showroom precision. Spark plugs cleaned, chain degreased and lubed, Motul 7100 engine oil refilled, and received a complete WhatsApp photo report of old parts.',
      branch: 'Ambattur Branch'
    },
    {
      id: 't11',
      customerName: 'Sanjay Varadarajan',
      neighborhood: 'Ambattur OT',
      bikeModel: 'Yamaha MT-15 V2',
      serviceCategory: 'Ultrasonic Injector Clean & Drive Chain',
      categoryKey: 'routine',
      rating: 5,
      date: 'July 2026',
      jobCardNo: 'JC-8467',
      avatarInitials: 'SV',
      verified: true,
      review: 'Had low-end jerking issues in bumper-to-bumper traffic. They ultrasonically cleaned the fuel injector, reset the throttle position sensor, and tensioned the chain. Bike feels factory-fresh and revs effortlessly.',
      branch: 'Ambattur Branch'
    },
    {
      id: 't12',
      customerName: 'Anand Chidambaram',
      neighborhood: 'Kilpauk',
      bikeModel: 'Kawasaki Z900',
      serviceCategory: 'Radiator Engine Ice Flush & Ceramic Detail',
      categoryKey: 'superbike',
      rating: 5,
      date: 'July 2026',
      jobCardNo: 'JC-8420',
      avatarInitials: 'AC',
      verified: true,
      review: 'Chennai summer heat was pushing my Z900 engine temp past 105°C. Did a complete chemical radiator flush and Engine Ice refill at Ambattur. Runs a solid 8-10°C cooler now, plus the snow foam wash made it look brand new.',
      branch: 'Ambattur Branch'
    }
  ];

  private gallery: GalleryItem[] = [
    {
      id: 'g1',
      title: 'BMW S1000RR M-Performance Track Calibration',
      category: 'Superbikes',
      imageUrl: 'images/gallery/gallery_bmw_s1000rr.jpg',
      caption: 'Full electronic throttle sync, quickshifter micro-calibration, and Brembo Stylema fluid flush.',
      description: 'Pre-track inspection and diagnostics for Chennai MMRT track day. Digital CAN-bus health scan, TPS angle recalibration, and Motul 300V 15W50 Factory Line flush.',
      bikeModel: 'BMW S1000RR M-Sport',
      branch: 'Ambattur Hub',
      buildType: 'Race Prep & OBD-2 Calibration',
      jobCardNo: 'JC-9042',
      date: 'October 2026',
      specs: [
        { label: 'Electronics', value: 'BOSCH 6-Axis IMU' },
        { label: 'Fluids', value: 'Motul 300V 15W50' },
        { label: 'Brakes', value: 'Motul RBF 660' }
      ],
      tags: ['1000cc', 'Inline-4', 'Track Setup', 'Superbike Bay']
    },
    {
      id: 'g2',
      title: 'Continental GT 650 Custom 2-Into-1 Race Exhaust',
      category: 'Nitro Modz',
      imageUrl: 'images/gallery/gallery_continental_gt650.jpg',
      caption: 'Custom 304 stainless steel 2-into-1 bend pipe fabrication paired with dyno Stage 1 fuel remap.',
      description: 'Complete bespoke fabrication at Avadi Studio. Purge-welded 2-into-1 collector eliminating the heavy OEM catalytic converter box, matched with BMC high-flow air filter.',
      bikeModel: 'Royal Enfield Continental GT 650',
      branch: 'Avadi Hub',
      buildType: 'Bespoke Exhaust & Dyno Map',
      jobCardNo: 'JC-8910',
      date: 'September 2026',
      specs: [
        { label: 'Power Gain', value: '+5.4 BHP Dyno' },
        { label: 'Exhaust', value: 'Custom 2-into-1 TIG' },
        { label: 'Filter', value: 'BMC High-Flow' }
      ],
      tags: ['650cc Twin', 'Custom Exhaust', 'Dyno Tuned', 'Avadi Modz']
    },
    {
      id: 'g3',
      title: 'Ducati Panigale V2 Desmodromic Micrometer Calibration',
      category: 'Superbikes',
      imageUrl: 'images/gallery/gallery_ducati_panigale.jpg',
      caption: 'Opening and closing valve shim tolerance checks using digital micrometer and Motul 300V Factory Line refill.',
      description: 'Major desmodromic timing maintenance on Ducati 955cc Superquadro. 8-shim digital micrometer measurement, timing belt tensioning, and Engine Ice USA chemical coolant flush.',
      bikeModel: 'Ducati Panigale V2',
      branch: 'Ambattur Hub',
      buildType: 'Desmo Service & Thermal Overhaul',
      jobCardNo: 'JC-8821',
      date: 'August 2026',
      specs: [
        { label: 'Engine', value: '955cc Superquadro' },
        { label: 'Tolerance', value: '0.05mm - 0.10mm' },
        { label: 'Coolant', value: 'Engine Ice USA' }
      ],
      tags: ['V-Twin', 'Desmo Valve', 'Track Ready', 'Ambattur Hub']
    },
    {
      id: 'g4',
      title: 'Inertia Chassis Dyno Stage 2 Map Calibration',
      category: 'Track & Dyno',
      imageUrl: 'images/gallery/gallery_dyno_cell.jpg',
      caption: 'Wideband O2 lambda datalogging across 3,000 - 10,000 RPM eliminating low-end throttle snatch.',
      description: 'Chassis dynamometer mapping in Ambattur soundproof cell. Step-by-step fuel and ignition advance adjustments providing linear torque curve and crisp quickshifter autoblip.',
      bikeModel: 'KTM Duke 390 Gen-3',
      branch: 'Ambattur Hub',
      buildType: 'AFR Telemetry & Throttle Response',
      jobCardNo: 'JC-9180',
      date: 'October 2026',
      specs: [
        { label: 'Wheel Output', value: '44.8 WHP' },
        { label: 'AFR Target', value: '13.2 : 1' },
        { label: 'RPM Limit', value: '10,500 RPM' }
      ],
      tags: ['Dyno Cell', 'Wideband AFR', 'ECU Remap', 'Performance']
    },
    {
      id: 'g5',
      title: 'Kawasaki Ninja ZX-10R Brembo Race Caliper Rebuild',
      category: 'Superbikes',
      imageUrl: 'images/services/service_brakes.jpg',
      caption: 'Ultrasonic piston decarbonization, high-temp silicone seals, and stainless steel braided brake lines.',
      description: 'Braking overhaul for liter-class superbike. Stripped down Brembo Stylema monobloc calipers, replaced with high-temp racing fluid seals, and vacuum bled with Motul RBF 660.',
      bikeModel: 'Kawasaki Ninja ZX-10R',
      branch: 'Ambattur Hub',
      buildType: 'Hydraulic Brake Bleed & Pad Setup',
      jobCardNo: 'JC-9450',
      date: 'November 2026',
      specs: [
        { label: 'Calipers', value: 'Brembo Stylema' },
        { label: 'Fluid', value: 'Motul RBF 660' },
        { label: 'Pads', value: 'EBC Double-H' }
      ],
      tags: ['Liter Class', 'Brembo', 'Track Spec', 'Hydraulic Care']
    },
    {
      id: 'g6',
      title: 'Ambattur Flagship 6 Pneumatic Scissor Lifts',
      category: 'Workshop Life',
      imageUrl: 'images/branches/branch_ambattur.jpg',
      caption: 'Pneumatic tool feeds, torque wrenches calibrated monthly, and oil-proof epoxy flooring.',
      description: 'Inside our main engineering facility in SIDCO Ambattur. 6 dedicated heavy-duty scissor bays with dedicated diagnostic consoles, live CCTV telemetry, and customer viewing lounge.',
      bikeModel: 'Multi-Cylinder Diagnostic Bays',
      branch: 'Ambattur Hub',
      buildType: 'Zero-Tolerance Workshop Environment',
      jobCardNo: 'BAY-AMB-01',
      date: 'Active Daily',
      specs: [
        { label: 'Bays', value: '6 Scissor Lifts' },
        { label: 'Scanners', value: 'CAN-Bus Multi-Brand' },
        { label: 'Lounge', value: 'AC Glass Viewing Bay' }
      ],
      tags: ['Epoxy Bay', 'Pneumatic Lifts', 'Torque Calibrated', 'Ambattur']
    },
    {
      id: 'g7',
      title: 'Yamaha R15 V4 Custom Underbelly Exhaust & Header',
      category: 'Nitro Modz',
      imageUrl: 'images/services/service_exhaust.jpg',
      caption: 'Back-purged TIG welded stainless header with tuned expansion chamber and carbon fiber end cap.',
      description: 'Handcrafted link pipe and tuned collector designed to increase mid-range scavenge efficiency. Finished with high-temperature electrochemical heat coloring.',
      bikeModel: 'Yamaha YZF-R15 V4 Track Mod',
      branch: 'Avadi Hub',
      buildType: 'TIG Weld & Purge Rig',
      jobCardNo: 'JC-9620',
      date: 'October 2026',
      specs: [
        { label: 'Weight Saving', value: '-3.8 kg' },
        { label: 'dB Rating', value: '92 dB with Decibel Killer' },
        { label: 'Finish', value: 'Heat-Treated Blue Titanium' }
      ],
      tags: ['TIG Welded', 'Lightweight', 'Exhaust Mod', 'Avadi Studio']
    },
    {
      id: 'g8',
      title: 'Avadi Performance Studio & Custom Fabrication Bay',
      category: 'Workshop Life',
      imageUrl: 'images/branches/branch_avadi.jpg',
      caption: 'Dedicated chassis armor jig for Delrin frame sliders, auxiliary light wiring rigs, and express fluid care.',
      description: 'Our Avadi hub specializes in quick-turnaround routine maintenance, specialized custom bracket fabrication, auxiliary lighting relays, and bespoke motorcycle aesthetics.',
      bikeModel: 'Performance Armor Station',
      branch: 'Avadi Hub',
      buildType: 'Fabrication & Express Modz',
      jobCardNo: 'BAY-AVD-01',
      date: 'Active Daily',
      specs: [
        { label: 'Lifts', value: '4 Hydraulic Scissor Bays' },
        { label: 'Fabrication', value: 'TIG & Tube Bender' },
        { label: 'Electrical', value: 'IP67 Sealed Crimping' }
      ],
      tags: ['Studio', 'Custom Jig', 'Modz Bay', 'Avadi']
    },
    {
      id: 'g9',
      title: 'Triumph 765 RS Electronic Diagnostics & MAP Sensor Sync',
      category: 'Superbikes',
      imageUrl: 'images/services/service_diagnostics.jpg',
      caption: 'Direct CAN-bus connection analyzing fuel trim short/long term data, clearing phantom check engine codes.',
      description: 'Connected via computerized multi-brand scanner to analyze live throttle position sensor (TPS) voltage, intake manifold pressure, and ride-by-wire servo response.',
      bikeModel: 'Triumph Street Triple 765 RS',
      branch: 'Ambattur Hub',
      buildType: 'Computerized Sensor Calibration',
      jobCardNo: 'JC-9310',
      date: 'September 2026',
      specs: [
        { label: 'Diagnostics', value: 'OBD-2 CAN-Bus' },
        { label: 'Sensors Checked', value: 'TPS, MAP, O2 Lambda' },
        { label: 'Report', value: 'Digital Telemetry PDF' }
      ],
      tags: ['Triple 765', 'ECU Scan', 'Sensor Calibration', 'Ambattur Hub']
    },
    {
      id: 'g10',
      title: 'Himalayan 450 IP67 Sealed Auxiliary Harness & Baja Pods',
      category: 'Nitro Modz',
      imageUrl: 'images/services/service_lights.jpg',
      caption: 'Direct battery tap with 40A waterproof relay, braided heat-shrink sleeve, and handlebar waterproof backlit switch.',
      description: 'Engineered adventure-touring electrical setup. Zero spliced factory wires, military-spec Deutsch connectors, fuse box isolation, and vibration-damped bracket mounts.',
      bikeModel: 'Royal Enfield Himalayan 450',
      branch: 'Avadi Hub',
      buildType: 'Zero-Splice Tourer Electricals',
      jobCardNo: 'JC-9521',
      date: 'November 2026',
      specs: [
        { label: 'Relay', value: '40A IP67 Sealed' },
        { label: 'Wiring', value: '100% Uncut OEM Loom' },
        { label: 'Draw', value: '60W High-Efficiency LED' }
      ],
      tags: ['Tourer Modz', 'No Wire Splice', 'IP67 Waterproof', 'Avadi']
    },
    {
      id: 'g11',
      title: 'Kawasaki Z900 High-Capacity Thermal Vacuum Purge',
      category: 'Track & Dyno',
      imageUrl: 'images/services/service_coolant.jpg',
      caption: 'Chemical cooling passage descaling, thermostat valve check, vacuum refill ensuring zero trapped air pockets.',
      description: 'High-temperature cooling overhaul preventing engine heat soaking during hot Chennai rides. Full chemical flush followed by high-performance Engine Ice USA coolant refill.',
      bikeModel: 'Kawasaki Z900 Multi-Cylinder',
      branch: 'Ambattur Hub',
      buildType: 'Chemical Flush & Engine Ice USA',
      jobCardNo: 'JC-8420',
      date: 'July 2026',
      specs: [
        { label: 'Coolant', value: 'Engine Ice USA' },
        { label: 'Temp Reduction', value: '-8°C Operating Temp' },
        { label: 'Boiling Point', value: '124°C High Boiling' }
      ],
      tags: ['Inline-4', 'Cooling System', 'Thermal Management', 'Engine Ice']
    },
    {
      id: 'g12',
      title: 'Ducati Streetfighter V4 9H Ceramic Graphene Shield',
      category: 'Detailing',
      imageUrl: 'images/services/service_detailing.jpg',
      caption: '3-stage DA rotary paint correction removing swirl marks, topped with 9H Graphene matrix coating.',
      description: 'Precision cosmetic restoration for Ducati Panigale/Streetfighter bodywork. Multi-stage machine polish with silicone-free compounds and 9H hydrophobic ceramic finish.',
      bikeModel: 'Ducati Streetfighter V4',
      branch: 'Ambattur Hub',
      buildType: 'Paint Correction & 9H Graphene',
      jobCardNo: 'JC-9770',
      date: 'October 2026',
      specs: [
        { label: 'Hardness', value: '9H Ceramic Graphene' },
        { label: 'Hydrophobic Angle', value: '115° Water Contact' },
        { label: 'Longevity', value: '2-Year Coating Warranty' }
      ],
      tags: ['Detailing', 'Graphene 9H', 'Swirl Removal', 'Paint Protection']
    }
  ];

  constructor() {
    const serviceImages: { [id: string]: { image: string; tag: string; badge: string; division: string } } = {
      'general-service': {
        image: 'images/services/service_routine.jpg',
        tag: 'HYDRAULIC SCISSOR BAY // 50-POINT MECHANICAL SCAN',
        badge: 'ROUTINE CARE',
        division: 'DIVISION 01 // FACTORY MAINTENANCE'
      },
      'superbike-major-service': {
        image: 'images/services/service_superbike.jpg',
        tag: 'VALVE MICROMETER CALIBRATION // MOTUL 300V RACING FLUID',
        badge: 'SUPERBIKE CARE',
        division: 'DIVISION 02 // SUPERBIKE CARE BAY'
      },
      'superbike-obd-diagnostics': {
        image: 'images/services/service_diagnostics.jpg',
        tag: 'OBD-II CAN-BUS // LIVE ECU TELEMETRY & THROTTLE SYNC',
        badge: 'SUPERBIKE DIAGNOSTICS',
        division: 'DIVISION 02 // ELECTRONIC DIAGNOSTICS'
      },
      'superbike-coolant-flush': {
        image: 'images/services/service_coolant.jpg',
        tag: 'ENGINE ICE USA // VACUUM PURGE & THERMAL MANAGEMENT',
        badge: 'THERMAL CARE',
        division: 'DIVISION 02 // THERMAL CALIBRATION'
      },
      'performance-exhaust-mod': {
        image: 'images/services/service_exhaust.jpg',
        tag: 'BESPOKE TITANIUM WELDING // COPPER GASKET SEAL',
        badge: 'NITRO MODZ',
        division: 'DIVISION 03 // PERFORMANCE FABRICATION'
      },
      'ecu-remapping-dyno': {
        image: 'images/services/service_dyno.jpg',
        tag: 'STAGE 1/2 FUEL FLASH // DYNO-MATCHED THROTTLE RESPONSE',
        badge: 'NITRO MODZ',
        division: 'DIVISION 03 // DYNO & ECU REMAPPING'
      },
      'auxiliary-fog-lights': {
        image: 'images/services/service_lights.jpg',
        tag: '40A SEALED RELAY // PLUG & PLAY WIRING HARNESS',
        badge: 'NITRO MODZ',
        division: 'DIVISION 03 // ELECTRICAL STUDIO'
      },
      'crash-guard-sliders': {
        image: 'images/services/service_superbike.jpg',
        tag: 'GRADE 10.9 HIGH TENSILE // DELRIN CRASH PUCKS',
        badge: 'CHASSIS ARMOR',
        division: 'DIVISION 03 // STRUCTURAL PROTECTION'
      },
      'engine-repair': {
        image: 'images/services/service_engine.jpg',
        tag: 'BORESCOPE INSPECTION // PRECISION CYLINDER HONING',
        badge: 'ENGINE OPERATIONS',
        division: 'DIVISION 04 // ENGINE SPECIALTY'
      },
      'brake-caliper-overhaul': {
        image: 'images/services/service_brakes.jpg',
        tag: 'BREMBO MONOBLOC CALIPER // VACUUM FLUID BLEED & PADS',
        badge: 'BRAKE PRECISION',
        division: 'DIVISION 04 // HYDRAULIC BRAKING'
      },
      'washing-detailing': {
        image: 'images/services/service_detailing.jpg',
        tag: 'PH-NEUTRAL SNOW FOAM BATH // CERAMIC HYDROPHOBIC SEAL',
        badge: 'STUDIO DETAILING',
        division: 'DIVISION 05 // DETAILING & COATING'
      }
    };

    this.services.forEach(s => {
      s.shortDescription = s.shortDesc;
      s.description = s.fullDesc;
      s.estimatedDuration = s.duration;
      s.basePrice = '₹' + s.startingPrice.toLocaleString('en-IN');
      s.includedItems = [...s.includedList];

      const meta = serviceImages[s.id] || {
        image: 'images/services/service_superbike.jpg',
        tag: 'NITRO RACING WORKSHOP CALIBRATION',
        badge: 'PERFORMANCE',
        division: 'DIVISION 01 // WORKSHOP'
      };
      s.imageUrl = meta.image;
      s.telemetryTag = meta.tag;
      s.badge = meta.badge;
      s.divisionTag = meta.division;
    });

    this.branches.forEach(b => {
      b.address = `${b.doorNo}, ${b.street}, ${b.landmark}, ${b.area}, ${b.city} - ${b.pincode}`;
      b.managerName = b.manager;
      b.workingHours = `${b.hoursWeekday}`;
      b.mapsUrl = b.mapUrl;
      if (b.id === 'ambattur') {
        b.imageUrl = 'images/branches/branch_ambattur.jpg';
        b.tagline = 'Main Diagnostics & Multi-Cylinder Engineering Hub';
        b.hubBadge = 'FLAGSHIP WORKSHOP // 6 BAYS';
        b.bayCountText = '6 Pneumatic Hydraulic Diagnostic Bays';
        b.specialties = ['Superbike Diagnostics Bay', '6 Hydraulic Lifts', 'Dyno Tuning Room', 'Customer AC Lounge', 'Motul Fluid Bar'];
        b.keyEquipments = [
          { title: 'CAN-Bus Diagnostic Pods', desc: 'Direct computerized scanner for Kawasaki, Ducati, BMW, Honda, Triumph' },
          { title: 'Dyno Tuning Room', desc: 'Inertia chassis dyno for ECU Stage 1 / Stage 2 throttle mapping' },
          { title: 'Motul Fluid Bar', desc: 'Factory Line sealed 300V, 7100, DOT 5.1 & Engine Ice on tap' },
          { title: 'Rider AC Lounge', desc: 'Live CCTV glass viewing bay, espresso bar, high-speed Wi-Fi' }
        ];
      } else {
        b.imageUrl = 'images/branches/branch_avadi.jpg';
        b.tagline = 'Superbike Care Bay & Bespoke Nitro Modz Studio';
        b.hubBadge = 'PERFORMANCE STUDIO // 4 BAYS';
        b.bayCountText = '4 Pneumatic Scissor Lifts + Modz Pod';
        b.specialties = ['Nitro Modz Studio', '4 Hydraulic Lifts', 'Custom Pipe Fabrication', 'Exhaust Dyno Check', 'Express Bay'];
        b.keyEquipments = [
          { title: 'Titanium TIG Fabrication', desc: 'Custom bend pipe, link pipes & Akrapovič / SC Project exhaust fitment' },
          { title: 'IP67 Electrical Rig', desc: '40A sealed relay harnesses for Maddog / Baja Designs auxiliary pods' },
          { title: 'Crash Armor Jig', desc: 'Precision fitment of Delrin sliders & heavy-gauge engine cages' },
          { title: 'Express Service Pod', desc: 'Quick 45-min brake bleeding, Motul chain service, and oil flush' }
        ];
      }
    });

    this.testimonials.forEach(t => {
      t.feedback = t.review;
    });

    this.gallery.forEach(g => {
      g.description = g.description || g.caption;
      g.bikeModel = g.bikeModel || 'Performance Motorcycle';
    });
  }

  getServices(): MotorcycleService[] {
    return this.services;
  }

  getServiceById(id: string): MotorcycleService | undefined {
    return this.services.find(s => s.id === id);
  }

  getFeaturedServices(): MotorcycleService[] {
    return this.services.filter(s => s.featured);
  }

  getBranches(): Branch[] {
    return this.branches;
  }

  getBranchById(id: string): Branch | undefined {
    return this.branches.find(b => b.id === id);
  }

  getTestimonials(): Testimonial[] {
    return this.testimonials;
  }

  getGallery(category?: string): GalleryItem[] {
    if (!category || category === 'all') {
      return this.gallery;
    }
    return this.gallery.filter(g => g.category === category);
  }

  submitEnquiry(enquiry: Omit<EnquirySubmission, 'createdAt'>): Promise<{ success: boolean; id: string }> {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        const phone = enquiry.mobileNumber || enquiry.phoneNumber;
        // Validate required fields
        if (!enquiry.customerName?.trim() || !phone?.trim()) {
          reject(new Error('Name and Mobile Number are required.'));
          return;
        }

        const newSubmission: EnquirySubmission = {
          ...enquiry,
          mobileNumber: phone,
          phoneNumber: phone,
          createdAt: new Date()
        };

        try {
          const stored = localStorage.getItem('nitro_enquiries');
          const list = stored ? JSON.parse(stored) : [];
          list.unshift(newSubmission);
          localStorage.setItem('nitro_enquiries', JSON.stringify(list));
        } catch {
          // Fallback if localStorage disabled
        }

        const enquiryId = 'ENQ-' + Math.floor(100000 + Math.random() * 900000);
        resolve({ success: true, id: enquiryId });
      }, 700); // Simulate network latency
    });
  }
}
