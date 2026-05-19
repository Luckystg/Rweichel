import zipfile
import xml.etree.ElementTree as ET
import re

def extract_docx_content(docx_path, start_marker="BAB I", end_marker="DAFTAR PUSTAKA"):
    """Extract content between start and end markers from DOCX file"""
    z = zipfile.ZipFile(docx_path)
    doc_xml = z.read('word/document.xml')
    root = ET.fromstring(doc_xml)
    
    # Define namespace
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    
    # Extract all paragraphs
    paragraphs = []
    for p in root.findall('.//w:p', ns):
        text_elements = []
        for t in p.findall('.//w:t', ns):
            if t.text:
                text_elements.append(t.text)
        para_text = ''.join(text_elements)
        if para_text:
            paragraphs.append(para_text)
    
    # Find start and end indices
    start_idx = -1
    end_idx = len(paragraphs)
    
    for i, para in enumerate(paragraphs):
        if start_marker in para and start_idx == -1:
            start_idx = i
            print(f"[INFO] Found start marker at index {i}: {para[:50]}")
        if end_marker in para and start_idx != -1:
            end_idx = i
            print(f"[INFO] Found end marker at index {i}: {para[:50]}")
            break
    
    if start_idx == -1:
        print(f"[ERROR] Start marker '{start_marker}' not found!")
        return None
    
    extracted = paragraphs[start_idx:end_idx]
    
    print(f"\n[SUCCESS] Extracted {len(extracted)} paragraphs")
    print(f"Content preview (first 10 lines):")
    for i, line in enumerate(extracted[:10]):
        print(f"  {line[:80]}")
    
    return extracted

def clean_and_structure_content(paragraphs):
    """Clean and structure extracted paragraphs"""
    content = "\n\n".join(paragraphs)
    
    # Clean special characters
    content = content.replace('â€œ', '"').replace('â€\x9d', '"')
    content = content.replace('â€"', '—')
    content = content.replace('â€˜', "'").replace('â€™', "'")
    
    return content

if __name__ == "__main__":
    docx_file = r"d:\RACHE_TA\JUDUL TUGAS AKHIR.docx"
    
    print("=" * 80)
    print("EXTRACTING BAB I-III CONTENT FROM DOCX")
    print("=" * 80)
    
    paragraphs = extract_docx_content(docx_file)
    
    if paragraphs:
        # Save raw content
        with open(r"d:\RACHE_TA\chapter_content_raw.txt", "w", encoding="utf-8") as f:
            for para in paragraphs:
                f.write(para + "\n\n")
        
        # Save cleaned content
        cleaned = clean_and_structure_content(paragraphs)
        with open(r"d:\RACHE_TA\chapter_content_cleaned.txt", "w", encoding="utf-8") as f:
            f.write(cleaned)
        
        print(f"\n[SAVED] Raw content: d:\\RACHE_TA\\chapter_content_raw.txt")
        print(f"[SAVED] Cleaned content: d:\\RACHE_TA\\chapter_content_cleaned.txt")
