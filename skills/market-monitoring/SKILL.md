---
name: market-monitoring
description: Sets up and runs recurring monitoring of a market or sector using public indicators for prices, costs, supply, demand, labour and structure. Use when a request asks how a market is performing, what has changed since the last period, or to build a repeatable indicator set and commentary.
license: MIT
metadata:
  owner: applied-economist
  used-by: applied-economist data-engineer dataviz-builder
  version: "0.1.0"
---

# Market monitoring

## Inputs

- The market or sector, geography and the questions decision-makers care about (from the handoff).
- Available public data (see the [data sources catalogue](../../library/data-sources/canada-bc.md)).
- Approved private data, where the charter allows. Anything built on private data stays out of public outputs.

## Steps

1. **Frame the market.** Define the product or service, geography, and the main groups of buyers and sellers. Describe how prices are set (competitive, regulated, negotiated).
2. **Pick indicators** in five groups, using only those with reliable data:
   - **Prices:** price levels or indices, relevant CPI components.
   - **Costs:** input cost indices (fuel, labour, insurance, capital), wages.
   - **Supply and capacity:** number of providers, capacity measures, entry and exit.
   - **Demand:** volumes, trips or usage, population and income drivers.
   - **Labour:** employment, hours, earnings, and the share of non-standard or platform-based work where measured.
3. **Document each indicator:** definition, source, table or series ID, frequency, lag, and known limits.
4. **Build the pipeline** with the Data Engineer so each update is a rerun, not a rebuild.
5. **Set comparisons:** change from the previous period, from a year earlier, and against a relevant benchmark (for example, overall CPI, or Canada versus BC).
6. **Write commentary:** what changed, the likely reasons (with evidence), and what to watch. Separate observation from interpretation.
7. **Flag signals** that may warrant attention, with the threshold or reasoning used.
8. **Schedule** the next update based on data release dates.

## Outputs

- Indicator catalogue (definition, source, frequency, limits).
- Indicator table and charts for the period.
- Commentary of one to two pages, bottom line first.
- Next update date.

## Done when

- [ ] Every indicator has a documented source and definition.
- [ ] The update can be rerun from the pipeline.
- [ ] Commentary separates what the data show from interpretation.
- [ ] Nothing in a public output names a regulated company or uses internal figures.

## Common pitfalls

- Reading a monthly blip as a trend.
- Comparing nominal prices across years without adjusting for inflation where that matters.
- Inferring market power from price levels alone.
