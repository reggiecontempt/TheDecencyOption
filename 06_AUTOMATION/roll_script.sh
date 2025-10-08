#!/usr/bin/env bash
set -euo pipefail
DATE=$(date +"%Y%m%d_%H%M")
zip -r "The_Decency_Option_${DATE}.zip" The_Decency_Option
sha256sum "The_Decency_Option_${DATE}.zip" >> The_Decency_Option/00_README/HASH_LEDGER.txt
