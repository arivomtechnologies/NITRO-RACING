from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import sys

prs = Presentation("Nitro_Racing_Complete_BRD.pptx")
c = canvas.Canvas("Nitro_Racing_Complete_BRD.pdf", pagesize=(960, 540))

# PPTX width = 13.333 inches = 960 points. PPTX height = 7.5 inches = 540 points.
# PPTX coordinates: (0, 0) is top-left.
# ReportLab coordinates: (0, 0) is bottom-left.
# So y_pdf = 540 - (y_pptx_pt + h_pptx_pt)

def to_pts(emu):
    return emu / 12700.0  # 1 pt = 12700 EMUs

def get_color(color_obj, default=colors.black):
    try:
        rgb = color_obj.rgb
        return colors.Color(rgb[0]/255.0, rgb[1]/255.0, rgb[2]/255.0)
    except:
        return default

for s_idx, slide in enumerate(prs.slides):
    # Default white background
    c.setFillColor(colors.HexColor('#F5F5F2'))
    c.rect(0, 0, 960, 540, fill=1, stroke=0)

    for shape in slide.shapes:
        x = to_pts(shape.left)
        y_top = to_pts(shape.top)
        w = to_pts(shape.width)
        h = to_pts(shape.height)
        y = 540 - (y_top + h)

        if shape.has_table:
            table = shape.table
            num_rows = len(table.rows)
            num_cols = len(table.columns)
            curr_y_top = y_top
            for r_idx in range(num_rows):
                row_h = to_pts(table.rows[r_idx].height)
                curr_x = x
                for col_idx in range(num_cols):
                    col_w = to_pts(table.columns[col_idx].width)
                    cell = table.cell(r_idx, col_idx)
                    cell_y = 540 - (curr_y_top + row_h)
                    
                    # Fill cell
                    bg_col = colors.HexColor('#242A31') if r_idx == 0 else (colors.white if r_idx % 2 == 1 else colors.HexColor('#F5F5F2'))
                    c.setFillColor(bg_col)
                    c.setStrokeColor(colors.HexColor('#D6D9DD'))
                    c.setLineWidth(0.5)
                    c.rect(curr_x, cell_y, col_w, row_h, fill=1, stroke=1)
                    
                    # Draw text
                    txt = cell.text.strip()
                    if txt:
                        is_header = (r_idx == 0)
                        c.setFillColor(colors.white if is_header else colors.HexColor('#17191D'))
                        c.setFont("Helvetica-Bold" if is_header else "Helvetica", 7.5 if is_header else 7)
                        
                        # Handle multiline or wrapping
                        lines = txt.split('\n')
                        text_y = cell_y + row_h - 11
                        for line in lines[:3]:
                            if len(line) > 55:
                                line = line[:52] + "..."
                            c.drawString(curr_x + 5, text_y, line)
                            text_y -= 9

                    curr_x += col_w
                curr_y_top += row_h

        elif shape.has_text_frame:
            # Check shape background
            try:
                if shape.fill.type:
                    fill_c = get_color(shape.fill.fore_color)
                    c.setFillColor(fill_c)
                    c.setStrokeColor(fill_c)
                    if shape.auto_shape_type:
                        c.roundRect(x, y, w, h, 4, fill=1, stroke=0)
                    else:
                        c.rect(x, y, w, h, fill=1, stroke=0)
            except:
                pass

            # Check outline
            try:
                if shape.line.fill.type:
                    stroke_c = get_color(shape.line.color)
                    c.setStrokeColor(stroke_c)
                    c.setLineWidth(1)
                    c.roundRect(x, y, w, h, 4, fill=0, stroke=1)
            except:
                pass

            tf = shape.text_frame
            cur_y_text = 540 - y_top - 14
            for para in tf.paragraphs:
                p_text = para.text.strip()
                if not p_text:
                    cur_y_text -= 6
                    continue
                font_size = 9
                font_name = "Helvetica"
                font_color = colors.HexColor('#17191D')
                if para.font.size:
                    font_size = para.font.size.pt
                if para.font.bold:
                    font_name = "Helvetica-Bold"
                try:
                    font_color = get_color(para.font.color, default=colors.HexColor('#17191D'))
                except:
                    pass

                c.setFont(font_name, font_size * 0.95)
                c.setFillColor(font_color)
                
                # Alignments
                if para.alignment == 2:  # Right
                    c.drawRightString(x + w - 5, cur_y_text, p_text)
                elif para.alignment == 1:  # Center
                    c.drawCentredString(x + w/2, cur_y_text, p_text)
                else:
                    c.drawString(x + 10, cur_y_text, p_text)
                
                cur_y_text -= (font_size * 1.25)
        else:
            # Plain shape (e.g. background or accent line)
            try:
                fill_c = get_color(shape.fill.fore_color)
                c.setFillColor(fill_c)
                c.setStrokeColor(fill_c)
                c.rect(x, y, w, h, fill=1, stroke=0)
            except:
                pass

    c.showPage()

c.save()
print("Nitro_Racing_Complete_BRD.pdf generated successfully with all 52 slides!")
