import zipfile
import xml.etree.ElementTree as ET

docx_path = r'D:\RACHE_TA\JUDUL TUGAS AKHIR.docx'
z = zipfile.ZipFile(docx_path)
doc_xml = z.read('word/document.xml')
root = ET.fromstring(doc_xml)

# Namespace
ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

# Extract ALL text paragraphs and tables with structure
print("=== DOCUMENT STRUCTURE ===\n")

for elem in root.iter():
    # Paragraphs
    if elem.tag == '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p':
        para_text = ''.join([t.text or '' for t in elem.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')])
        if para_text.strip():
            print(f"PARA: {para_text[:100]}")
    
    # Tables
    if elem.tag == '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tbl':
        rows = elem.findall('w:tr', ns)
        print(f"\nTABLE: {len(rows)} rows")
        for r_idx, row in enumerate(rows[:3]):
            cells = row.findall('w:tc', ns)
            print(f"  Row {r_idx}: {len(cells)} cells")
            for c_idx, cell in enumerate(cells):
                cell_text = ''.join([t.text or '' for t in cell.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')])
                if cell_text.strip():
                    print(f"    Cell {c_idx}: {cell_text[:60]}")
        print()
