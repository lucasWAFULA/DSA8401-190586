from zipfile import ZipFile
from pathlib import Path
pptx = Path(r'C:\Users\hp\OneDrive\Dokumenter\MSC. DSA\AML-DSA8401-REPEAT\DSA8401_Lab_Setup.pptx')
print('exists', pptx.exists())
if not pptx.exists():
    raise SystemExit(1)
with ZipFile(pptx, 'r') as z:
    slides=[n for n in z.namelist() if n.startswith('ppt/slides/slide')]
    print('slides', len(slides))
    for s in slides[:10]:
        print('---', s)
        data=z.read(s).decode('utf-8', errors='ignore')
        lines=data.splitlines()
        for i,l in enumerate(lines[:80],1):
            if 't>' in l or 'a:t' in l:
                print(i, l.strip())
print('done')
