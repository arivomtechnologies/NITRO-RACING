from pptx import Presentation
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import sys

prs = Presentation("Nitro_Racing_Complete_BRD.pptx")
print(f"Read {len(prs.slides)} slides from PPTX.")
