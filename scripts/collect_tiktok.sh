#!/bin/bash

SEASON=$1 # Usage: ./collect_tiktok.sh summer

HASHTAGS=$(cat config/hashtags_by_season.json | \
  python3 -c "import sys, json; print(' '.join(json.load(sys.stdin)['$SEASON']))")

OUTDIR="data/tiktok/$SEASON"
mkdir -p $OUTDIR

for tag in $HASHTAGS; do
    tiktok-scraper hashtag $tag -n 100 --filepath "$OUTDIR" --filetype json
done
