#!/usr/bin/env bash
set -euo pipefail

gprof2dot -f pstats "$1" | dot -Tpng -o "${1%.*}".png
