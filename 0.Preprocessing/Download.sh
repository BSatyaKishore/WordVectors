#!/bin/bash

languages='en te hi'

for ln in $languages
do
    echo Downloading latest $ln wikipedia
    wget https://dumps.wikimedia.org/${ln}wiki/latest/${ln}wiki-latest-pages-articles.xml.bz2
done

echo All done
