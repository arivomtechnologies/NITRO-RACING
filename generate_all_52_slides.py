import sys
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

C_GRAPHITE = RGBColor(23, 25, 29)     # #17191D
C_CHARCOAL = RGBColor(36, 42, 49)     # #242A31
C_ORANGE   = RGBColor(244, 119, 33)   # #F47721
C_SILVER   = RGBColor(214, 217, 221)  # #D6D9DD
C_OFFWHITE = RGBColor(245, 245, 242)  # #F5F5F2
C_WHITE    = RGBColor(255, 255, 255)  # #FFFFFF
C_GREEN    = RGBColor(34, 155, 98)    # #229B62
C_GOLD     = RGBColor(233, 162, 59)   # #E9A23B
C_MUTED    = RGBColor(124, 134, 145)  # #7C8691
C_CARD_BG  = RGBColor(255, 255, 255)
C_DARK_CARD= RGBColor(30, 35, 42)

def set_bg(slide, color):
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = color
    bg.line.fill.background()
    return bg

def add_header(slide, title_text, category_text="BUSINESS REQUIREMENTS DOCUMENT", is_dark=False):
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.12))
    bar.fill.solid()
    bar.fill.fore_color.rgb = C_ORANGE
    bar.line.fill.background()

    cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.25), Inches(11.7), Inches(0.35))
    tf_c = cat_box.text_frame
    tf_c.word_wrap = True
    p_c = tf_c.paragraphs[0]
    p_c.text = category_text.upper()
    p_c.font.size = Pt(9.5)
    p_c.font.bold = True
    p_c.font.color.rgb = C_ORANGE

    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.55), Inches(11.7), Inches(0.7))
    tf_t = title_box.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = title_text
    p_t.font.size = Pt(19)
    p_t.font.bold = True
    p_t.font.color.rgb = C_WHITE if is_dark else C_GRAPHITE

def add_footer(slide, slide_num, total_slides=52, is_dark=False):
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(7.0), Inches(11.733), Inches(0.02))
    line.fill.solid()
    line.fill.fore_color.rgb = C_CHARCOAL if is_dark else C_SILVER
    line.line.fill.background()

    f_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.05), Inches(9.0), Inches(0.35))
    p_f = f_box.text_frame.paragraphs[0]
    p_f.text = "Nitro Racing Automobile Service Center Management System | Arivom Technologies, Chennai"
    p_f.font.size = Pt(8.5)
    p_f.font.color.rgb = C_MUTED

    p_box = slide.shapes.add_textbox(Inches(10.5), Inches(7.05), Inches(2.0), Inches(0.35))
    p_p = p_box.text_frame.paragraphs[0]
    p_p.alignment = PP_ALIGN.RIGHT
    p_p.text = f"Slide {slide_num} of {total_slides}"
    p_p.font.size = Pt(8.5)
    p_p.font.bold = True
    p_p.font.color.rgb = C_ORANGE if is_dark else C_CHARCOAL

def add_badge(slide, left, top, text, badge_type="CONFIRMED"):
    colors_map = {
        "CONFIRMED": (C_GREEN, C_WHITE),
        "RECOMMENDED": (C_GOLD, C_WHITE),
        "OPTIONAL": (C_MUTED, C_WHITE),
        "PENDING": (C_ORANGE, C_WHITE),
        "MUST": (C_CHARCOAL, C_ORANGE),
    }
    bg_col, txt_col = colors_map.get(badge_type, (C_CHARCOAL, C_WHITE))
    badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, Inches(2.0), Inches(0.32))
    badge.fill.solid()
    badge.fill.fore_color.rgb = bg_col
    badge.line.fill.background()
    p = badge.text_frame.paragraphs[0]
    p.text = text
    p.font.size = Pt(8)
    p.font.bold = True
    p.alignment = PP_ALIGN.CENTER
    p.font.color.rgb = txt_col
    return badge

def create_card(slide, left, top, width, height, title, items, is_dark_card=False, title_color=None):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = C_DARK_CARD if is_dark_card else C_CARD_BG
    card.line.color.rgb = C_CHARCOAL if is_dark_card else C_SILVER
    card.line.width = Pt(1)

    tf = card.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.2)
    tf.margin_right = Inches(0.2)
    tf.margin_top = Inches(0.18)
    tf.margin_bottom = Inches(0.18)

    p_title = tf.paragraphs[0]
    p_title.text = title
    p_title.font.size = Pt(11)
    p_title.font.bold = True
    p_title.font.color.rgb = title_color if title_color else (C_ORANGE if is_dark_card else C_CHARCOAL)
    p_title.space_after = Pt(6)

    for item in items:
        p = tf.add_paragraph()
        p.text = f"•  {item}"
        p.font.size = Pt(8.5)
        p.font.color.rgb = C_SILVER if is_dark_card else C_GRAPHITE
        p.space_after = Pt(3)
        p.line_spacing = 1.15
    return card

def create_table_card(slide, left, top, width, height, headers, rows_data, col_widths=None):
    num_rows = len(rows_data) + 1
    num_cols = len(headers)
    table_shape = slide.shapes.add_table(num_rows, num_cols, left, top, width, height)
    table = table_shape.table

    if col_widths and len(col_widths) == num_cols:
        for idx, w in enumerate(col_widths):
            table.columns[idx].width = w

    for c_idx, h_text in enumerate(headers):
        cell = table.cell(0, c_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = C_CHARCOAL
        p = cell.text_frame.paragraphs[0]
        p.text = h_text
        p.font.size = Pt(9)
        p.font.bold = True
        p.font.color.rgb = C_WHITE
        p.alignment = PP_ALIGN.CENTER

    for r_idx, r_data in enumerate(rows_data, start=1):
        for c_idx, val in enumerate(r_data):
            cell = table.cell(r_idx, c_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = C_WHITE if r_idx % 2 == 1 else C_OFFWHITE
            p = cell.text_frame.paragraphs[0]
            p.text = str(val)
            p.font.size = Pt(8.5)
            p.font.color.rgb = C_GRAPHITE
            if c_idx == 0:
                p.font.bold = True
                p.alignment = PP_ALIGN.CENTER
    return table_shape

print("Definitions complete. Writing 52 slide builders...")
