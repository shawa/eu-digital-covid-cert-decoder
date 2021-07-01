#!/bin/zsh

set -euo pipefail

zbarimg - 2>/dev/null \
 | sed 's/^QR-Code://' \
 | python3 decode-cert.py \
