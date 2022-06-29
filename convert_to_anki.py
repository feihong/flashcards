"""
Convert all .txt files to a format accepted by Anki
"""

from pathlib import Path

def get_cards(txt_file: Path):
  with txt_file.open('r') as fp:
    while True:
        front = fp.readline().strip()
        back = fp.readline().strip()
        fp.readline() # skip a line
        if not front or not back:
          break
        yield (front, back)


for txt_file in Path('.').glob('*.txt'):
  if txt_file.name.endswith('.anki.txt'):
    continue

  output_file = txt_file.with_suffix('.anki.txt')
  count = 0

  with output_file.open('w') as fp:
    for front, back in get_cards(txt_file):
      fp.write(f'{front};{back}\n')
      count +=1

  print(f'Wrote {count} flashcards to {output_file}')
