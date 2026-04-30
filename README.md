# AI Web Atlas

> A critical, versioned atlas of the AI-agent web: reconstructing Parallel Web Systems’ April 2026 market-map poster, then expanding it to show the customers, peers, infrastructure layers, and physical substrate that corporate logo maps usually blur together.

![AI Web Atlas v3](./maps/v3-defense-and-substrate.svg)

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Code & Data: MIT](https://img.shields.io/badge/Code%20%26%20Data-MIT-blue.svg)](./LICENSE-MIT)
[![Atlas Version](https://img.shields.io/badge/Atlas-v3-red.svg)](./maps/v3-defense-and-substrate.svg)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](#contributing)

---

## What this is

AI Web Atlas is an independent, versioned map of the emerging agentic web: the layer of AI agents, retrieval systems, browser operators, model tools, infrastructure companies, defense systems, and physical dependencies now forming around the open web.

The starting artifact is Parallel Web Systems’ April 2026 market-map-style poster and its framing that “the web’s second user is online.” This repository treats that claim as a serious primary source, then asks what a more analytically honest map would need to add, remove, qualify, or separate.

It is not an official Parallel document. It is not a vendor landscape slide. It is a public research artifact for people who want to reason clearly about the agentic web.

---

## Why this exists

Corporate market maps are useful, but they are not neutral.

They often:

- flatten customers, partners, peers, suppliers, and infrastructure dependencies into one visual field;
- make revenue concentration look like ecosystem breadth;
- overstate category ownership;
- hide physical constraints such as compute, energy, datacenters, minerals, cables, and export controls;
- omit inconvenient adjacent powers.

AI Web Atlas separates the layers so the map becomes harder to use as marketing and more useful as analysis.

---

## The maps

### v1 — Transcription layer

[`maps/v1-transcription.svg`](./maps/v1-transcription.svg)  
[`maps/source/v1-transcription.mmd`](./maps/source/v1-transcription.mmd)

A structured approximation of the original poster’s visible topology. This version preserves the source artifact’s broad categories and approximate layout. Unclear or unverified slots are marked as uncertain rather than silently presented as fact.

### v2 — Panel critique

[`maps/v2-panel-critique.svg`](./maps/v2-panel-critique.svg)  
[`maps/source/v2-panel-critique.mmd`](./maps/source/v2-panel-critique.mmd)  
[`debates/v2-panel-critique.md`](./debates/v2-panel-critique.md)

A critique pass generated through simulated expert archetypes with deliberately conflicting perspectives: AI infrastructure, venture-market analysis, product strategy, security, and web architecture.

v2 separates confirmed customers, probable customers, peers, infrastructure providers, uncertain guesses, and category markers.

### v3 — Defense and physical substrate

[`maps/v3-defense-and-substrate.svg`](./maps/v3-defense-and-substrate.svg)  
[`maps/source/v3-defense-and-substrate.mmd`](./maps/source/v3-defense-and-substrate.mmd)  
[`debates/v3-defense-and-substrate.md`](./debates/v3-defense-and-substrate.md)

v3 adds two structural omissions from a software-only agent map:

1. **Defense and national-security AI**
2. **The physical substrate**

The physical substrate layer shows what the agent web depends on but does not necessarily buy from directly: semiconductors, accelerators, datacenters, power, cooling, water, fiber, subsea cables, critical minerals, and export controls.

---

## Key findings

### 1. “The web’s second user” is rhetorically powerful but analytically incomplete

Automated traffic existed long before LLM agents. The stronger claim is that AI agents may be the first large-scale web users that operate recursively, conversationally, and task-continuously rather than as simple crawlers.

See: [`findings/second-user-claim.md`](./findings/second-user-claim.md)

### 2. Customer-versus-peer confusion is the central map failure mode

A logo map can imply that every entity shown has the same relationship to the company making the map. This atlas distinguishes customer, probable customer, peer, supplier, substrate, category marker, and uncertain nodes.

See: [`findings/customer-vs-peer.md`](./findings/customer-vs-peer.md)

### 3. The mesh hides concentration

A map with 100+ logos can still be commercially dominated by a small number of accounts. Logo presence is ecosystem evidence, not proof of revenue scale.

See: [`findings/revenue-concentration.md`](./findings/revenue-concentration.md)

### 4. The physical substrate is not optional

The agentic web is usually described as software. Its binding constraints are physical: compute supply, power, chips, datacenters, water, cooling, networks, minerals, and export controls.

See: [`findings/physical-substrate.md`](./findings/physical-substrate.md)

---

## Visual grammar

| Convention | Meaning |
|---|---|
| Light box | Original poster category or confirmed ecosystem node |
| Orange dashed box | Uncertain reconstruction or educated guess |
| Blue box | Panel addition |
| Red box | Defense or national-security expansion |
| Dark substrate band | Physical dependency, not a customer relationship |
| Strikethrough | Removed or challenged classification |
| Heavy border | Structural hub |
| Dotted link | Uncertain or indirect relationship |

Topology is approximate. Positioning reflects interpretive clustering, not validated market distance.

---

## Methodology

The atlas is built through three steps.

1. **Reconstruct** — preserve the source artifact as faithfully as possible from public material.
2. **Stress-test** — run simulated expert archetypes against the map to surface omissions, category errors, and structural disagreements.
3. **Version** — preserve each stage instead of silently overwriting old interpretations.

The panels are simulated. They are analytical devices, not real quotes from named public figures and not sources of proprietary knowledge.

See: [`methodology/expert-panel-simulation.md`](./methodology/expert-panel-simulation.md)

---

## Repository structure

```text
Ai-web-atlas/
├── README.md
├── LICENSE
├── LICENSE-MIT
├── LICENSE-CC-BY-4.0
├── NOTICE
├── CITATION.cff
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── CHANGELOG.md
├── DISCLAIMER.md
├── ROADMAP.md
├── package.json
├── Makefile
├── maps/
│   ├── v1-transcription.svg
│   ├── v2-panel-critique.svg
│   ├── v3-defense-and-substrate.svg
│   └── source/
│       ├── v1-transcription.mmd
│       ├── v2-panel-critique.mmd
│       └── v3-defense-and-substrate.mmd
├── data/
│   └── companies.json
├── findings/
├── debates/
├── methodology/
├── docs/
├── sources/
├── scripts/
└── .github/
```

---

## Working with the maps

The rendered maps are SVG files in [`maps/`](./maps/). Mermaid source files are stored in [`maps/source/`](./maps/source/).

To edit a map:

1. Edit the relevant `.mmd` file.
2. Render to SVG with Mermaid CLI or Mermaid Live.
3. Update the matching SVG.
4. Open a pull request explaining the change and citing evidence.

---

## Contributing

Useful contributions include:

- evidence-backed corrections;
- better customer-versus-peer classifications;
- new sourced nodes;
- improved map rendering;
- structured data additions;
- new version proposals.

Good evidence includes public customer case studies, company announcements, product documentation, procurement records, public filings, earnings-call transcripts, and credible reporting. Anonymous claims are not accepted as evidence.

This repository does not accept unsourced logo additions, promotional copy, speculative customer claims, or simulated quotes attributed to real people who did not say them.

---

## Sources

Primary and background sources are collected in [`sources/bibliography.md`](./sources/bibliography.md).

Core source categories include Parallel announcements, official protocol documentation, bot-traffic reports, defense technology announcements, semiconductor and datacenter infrastructure sources, and public filings or procurement records where available.

---

## Citation

```bibtex
@misc{ai-web-atlas,
  title        = {AI Web Atlas},
  author       = {Contributors},
  year         = {2026},
  howpublished = {\url{https://github.com/myceldigital/Ai-web-atlas}},
  note         = {A critical, versioned atlas of the AI-agent web}
}
```

---

## License

Maps, findings, debate transcripts, and prose documentation are released under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).

Code, structured data, and rendering scripts are released under the [MIT License](./LICENSE-MIT).

---

## Disclaimer

This repository is independent. It is not affiliated with, endorsed by, or sponsored by Parallel Web Systems or any company shown in the maps.

The presence of a company on a map does not imply a commercial relationship unless explicitly marked and sourced.

---

*Last updated: April 30, 2026 · Atlas version 3*
