#!/bin/bash
mkdir -p build;
./main.py > build/brothers.dot;
dot -Tsvg build/brothers.dot -o build/brothers.svg;
