#!/bin/bash
python3 substitute.py $1
surge ./ scientific-afterthought.surge.sh
