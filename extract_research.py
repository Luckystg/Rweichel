with open('plaintext.txt', 'r', encoding='latin-1') as f:
    lines = f.readlines()

# Find markers
start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if 'PT Kereta Api Indonesia' in line and start_idx == -1:
        start_idx = i
        print(f'Found start at line {i+1}')
    if ('DAFTAR PUSTAKA' in line or 'REFERENSI' in line) and i > 100:
        end_idx = i
        print(f'Found end at line {i+1}')
        break

print(f'Total lines: {len(lines)}')

if end_idx < 0:
    for i in range(len(lines)-1, 100, -1):
        if 'Referensi' in lines[i] or 'Pustaka' in lines[i]:
            end_idx = i
            print(f'Found end at line {i+1}')
            break

if start_idx > 0 and end_idx > 0:
    research_lines = lines[start_idx:end_idx]
    with open('research_chapter_content.txt', 'w', encoding='utf-8') as f:
        f.writelines(research_lines)
    print(f'Saved {len(research_lines)} lines')
else:
    print(f'Error: Start={start_idx}, End={end_idx}')
