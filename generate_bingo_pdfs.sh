#!/bin/bash

# generate bingo pdfs
mkdir pdfs
for i in {1..10}
do
    python3 generate_bingo_tex.py --fields_file=fields.txt --template_file=bingo.tex.template | xelatex -c --jobname bingo"$i" --output-directory=pdfs
done

# cleanup
rm pdfs/*.log
rm pdfs/*.aux
