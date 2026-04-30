#!/usr/bin/env bash
set -euo pipefail

if ! command -v mmdc >/dev/null 2>&1; then
  echo "Mermaid CLI not found. Install dependencies with: npm install" >&2
  echo "Then run: npm run render" >&2
  exit 1
fi

mmdc -i maps/source/v1-transcription.mmd -o maps/v1-transcription.svg
mmdc -i maps/source/v2-panel-critique.mmd -o maps/v2-panel-critique.svg
mmdc -i maps/source/v3-defense-and-substrate.mmd -o maps/v3-defense-and-substrate.svg

echo "Rendered maps."
