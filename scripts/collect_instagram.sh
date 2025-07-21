#!/bin/bash

# Set season based on user input
SEASON=$1  # Usage: ./collect_instagram.sh winter

HASHTAGS=$(cat config/hashtags_by_season.json | \
  python3 -c "import sys, json; print(' '.join(['#'+tag for tag in json.load(sys.stdin)['$SEASON']]))")

OUTDIR="data/instagram/$SEASON"
mkdir -p $OUTDIR

for tag in $HASHTAGS; do
    instaloader "$tag" --no-pictures --no-videos --fast-update --comments --dirname-pattern=$OUTDIR
done
