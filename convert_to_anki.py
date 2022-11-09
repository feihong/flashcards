"""
Convert all .txt files to a format accepted by Anki
"""

import re
from pathlib import Path

def get_cards(txt_file: Path):
  text = txt_file.read_text()
  chunks = re.split(r'\n{2,}', text)

  for chunk in chunks:
    chunk = chunk.strip()
    if chunk == '':
      continue

    front, back = chunk.splitlines(1)
    yield front.strip(), back


for txt_file in Path('.').glob('*.txt'):
  if txt_file.name.endswith('.anki.txt'):
    continue

  output_file = txt_file.with_suffix('.anki.txt')
  count = 0

  with output_file.open('w') as fp:
    for front, back in get_cards(txt_file):
      fp.write(f'{front}\t{back}\n')
      count +=1

  print(f'Wrote {count} flashcards to {output_file}')
