#!/bin/bash
./scrap.py http://so.gushiwen.org/gushi/sanbai.aspx ./data/gushi
./scrap.py http://so.gushiwen.org/gushi/songsan.aspx ./data/songci
./scrap.py http://so.gushiwen.org/gushi/tangshi.aspx ./data/tang
strfile ./data/gushi
strfile ./data/songci
strfile ./data/tang
