import sys
import os

def extract_docx(path):
    try:
        import docx
        doc = docx.Document(path)
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        return f"Error reading docx: {e}"

def extract_pptx(path):
    try:
        from pptx import Presentation
        prs = Presentation(path)
        text = []
        for slide in prs.slides:
            for shape in slide.shapes:
                if hasattr(shape, "text"):
                    text.append(shape.text)
        return "\n".join(text)
    except ImportError:
        return "python-pptx not installed"
    except Exception as e:
        return f"Error reading pptx: {e}"

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python extract.py <infile> <outfile>")
        sys.exit(1)
    
    path = sys.argv[1]
    outpath = sys.argv[2]
    ext = os.path.splitext(path)[1].lower()
    
    with open(outpath, 'w', encoding='utf-8') as f:
        f.write(f"--- Extracted text from {path} ---\n")
        if ext == ".docx":
            f.write(extract_docx(path))
        elif ext == ".pptx":
            f.write(extract_pptx(path))
        else:
            f.write("Unsupported format")
