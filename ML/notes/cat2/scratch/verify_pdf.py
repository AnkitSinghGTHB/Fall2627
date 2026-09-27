import fitz

doc = fitz.open('pdf/ML_CAT2_CALCULATIONS_MASTER_BOOKLET.pdf')
print('Total pages:', len(doc))
for i, page in enumerate(doc):
    text = page.get_text()
    for term in ['Dendrogram Structure', 'Markov Blanket', 'Pruning Lattice', 'Task A9']:
        if term in text:
            clean_term = term.replace(' ', '_')
            out_file = f'scratch/verify_{clean_term}_p{i+1}.png'
            print(f'Term "{term}" found on Page {i+1} -> saving to {out_file}')
            pix = page.get_pixmap(dpi=150)
            pix.save(out_file)
