from pptx import Presentation
from pptx.util import Inches
import slides_sec_a_b
import slides_sec_c
import slides_sec_d_e
import slides_sec_f
import slides_sec_g_h_i

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

print("Assembling Slide Deck...")
slides_sec_a_b.build_slides_1_to_9(prs, blank_layout)
slides_sec_c.build_slides_10_to_19(prs, blank_layout)
slides_sec_d_e.build_slides_20_to_25(prs, blank_layout)
slides_sec_f.build_slides_26_to_39(prs, blank_layout)
slides_sec_g_h_i.build_slides_40_to_52(prs, blank_layout)

print(f"Total Slides Generated: {len(prs.slides)}")
prs.save("Nitro_Racing_Complete_BRD.pptx")
print("Saved Nitro_Racing_Complete_BRD.pptx successfully!")
