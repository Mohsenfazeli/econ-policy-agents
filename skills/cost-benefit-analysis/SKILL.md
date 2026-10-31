---
name: cost-benefit-analysis
description: Structures and carries out a cost-benefit analysis of a policy, program or regulatory option, following Canadian guidance. Use when a request asks whether an option's benefits justify its costs, to compare options on net benefit, or to describe who gains and who loses.
license: MIT
metadata:
  owner: applied-economist
  used-by: applied-economist financial-modeller policy-designer
  version: "0.1.0"
---

# Cost-benefit analysis

This skill follows the structure of the Treasury Board of Canada Secretariat's [Canada's Cost-Benefit Analysis Guide for Regulatory Proposals](https://www.publications.gc.ca/collections/collection_2022/sct-tbs/BT58-5-2022-eng.pdf) (2022), which supports the federal [Policy on Cost-Benefit Analysis](https://www.canada.ca/en/government/system/laws/developing-improving-federal-regulations/requirements-developing-managing-reviewing-regulations/policy-cost-benefit-analysis.html). For BC work, check whether provincial guidance or the requesting ministry sets different parameters (for example, the discount rate), and record what was used. The UK [Green Book](https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government) is a useful comparison.

## Inputs

- The options from the Policy Designer, including the status quo.
- Evidence, data and parameters from the team.
- The audience's required parameters, if any (discount rate, time horizon, price base year).

## Steps

1. **Define the baseline** (what happens without action) and each option, concretely.
2. **Set the frame:** standing (whose costs and benefits count, for example, British Columbians or Canadians), time horizon, price base year, real or nominal values, and discount rate. Record each choice and its source in the assumptions log.
3. **Identify impacts** for each option relative to the baseline: costs and benefits to government, businesses, consumers, workers and others. Separate **transfers** (one group's loss is another's gain) from real resource costs and benefits.
4. **Quantify and monetize** where there is a defensible basis. Cite every unit value and parameter. Where an impact cannot be monetized, quantify it; where it cannot be quantified, describe it qualitatively. Never drop an impact because it is hard to measure.
5. **Calculate** present values of costs and benefits, net present value, and benefit-cost ratio. Hand detailed modelling to the Financial Modeller using the [financial model build skill](../financial-model-build/SKILL.md).
6. **Analyse uncertainty:** sensitivity on key parameters, including the discount rate; scenarios; break-even values where useful.
7. **Analyse distribution:** who gains and who loses, by group and region where data allow. Include GBA+ considerations.
8. **Summarize** in an accounting statement: monetized, quantified and qualitative impacts for each option, side by side.

## Outputs

- Accounting statement by option.
- Assumptions and parameters table with sources.
- Sensitivity and scenario results.
- Distributional analysis.
- Plain-language summary of what the analysis shows and its limits.

## Done when

- [ ] Baseline, standing, horizon, price base, discount rate are stated with sources.
- [ ] Transfers are identified and not counted as net benefits or costs.
- [ ] No double counting.
- [ ] Non-monetized impacts are listed.
- [ ] Sensitivity to the discount rate and key parameters is shown.
- [ ] Distributional effects are described.
