import zipfile
import xml.etree.ElementTree as ET
import re

pptx_path = r"C:\Users\Gaurav\OneDrive\Desktop\SEM-2\ML-LAB\energy_optimizer\Energy_Consumption_Optimizer.pptx"

def extract_text_from_pptx(path):
    try:
        with zipfile.ZipFile(path, 'r') as zip_ref:
            # List all slide files
            slide_files = sorted(
                [f for f in zip_ref.namelist() if re.match(r'ppt/slides/slide\d+\.xml', f)],
                key=lambda x: int(re.search(r'\d+', x).group())
            )
            
            print(f"Found {len(slide_files)} slides in PowerPoint presentation.")
            
            for slide_file in slide_files:
                print(f"\n==================== {slide_file.upper()} ====================")
                slide_xml = zip_ref.read(slide_file)
                root = ET.fromstring(slide_xml)
                
                # Namespaces used in pptx files
                namespaces = {
                    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
                    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
                    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main'
                }
                
                # Find all text elements (a:t)
                text_runs = []
                # Simple traverse of XML to find text in order
                for elem in root.iter():
                    if elem.tag.endswith('}t'): # tags ending in }t like {http://schemas.openxmlformats.org/drawingml/2006/main}t
                        if elem.text:
                            text_runs.append(elem.text)
                
                # Combine runs into lines (usually runs are small, group them by paragraphs if possible, or just print them)
                # Let's print text elements separated by spaces or newlines
                print(" ".join(text_runs))
    except Exception as e:
        print("Error reading pptx:", e)

extract_text_from_pptx(pptx_path)
