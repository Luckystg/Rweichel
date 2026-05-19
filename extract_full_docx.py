import zipfile
import xml.etree.ElementTree as ET
import re

docx_path = r'D:\RACHE_TA\JUDUL TUGAS AKHIR.docx'
z = zipfile.ZipFile(docx_path)
doc_xml = z.read('word/document.xml')
root = ET.fromstring(doc_xml)

ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

# Find where BAB III starts
output = []
in_bab_iii = False
capture = False

for elem in root.iter():
    if elem.tag == '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p':
        para_text = ''.join([t.text or '' for t in elem.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')])
        
        # Start capture at BAB III
        if 'BAB III' in para_text or 'ANALISIS' in para_text:
            capture = True
            in_bab_iii = True
        
        if capture and para_text.strip():
            output.append(para_text)

# Save to file
with open('D:\\RACHE_TA\\extracted_content.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output[:500]))  # First 500 paragraphs after BAB III

print(f"Extracted {len(output)} paragraphs from BAB III onwards")
print("\nFirst 50 lines:")
for i, line in enumerate(output[:50]):
    print(f"{i+1}. {line[:100]}")
