# Finding: customer-versus-peer confusion

The central failure mode of corporate market maps is relationship flattening.

A logo can mean many different things:

- confirmed customer;
- probable customer;
- partner;
- integration target;
- peer;
- competitor;
- supplier;
- infrastructure dependency;
- category marker;
- speculative inclusion.

These relationships should not be visually treated as equivalent.

## Classification model

AI Web Atlas uses the following relationship types in `data/companies.json`:

- `customer`
- `probable_customer`
- `peer`
- `supplier`
- `substrate`
- `category_marker`
- `uncertain`

## Why this matters

A company can be central to the agentic web while not being a customer of a given vendor. Conversely, a real customer may be commercially small. A serious atlas must therefore distinguish ecosystem importance from commercial relationship.

## Atlas treatment

Where public evidence does not prove a relationship, the atlas preserves ambiguity rather than implying certainty.
