---
name: financial-model-build
description: Builds transparent financial models (NPV, IRR, payback, sensitivity and scenarios, budgets, cost and rate models) with inputs, calculations and outputs kept separate, built-in checks, and every assumption documented. Use when a request needs a cost, budget, rate or investment calculation that others must be able to follow and test.
license: MIT
metadata:
  owner: financial-modeller
  used-by: financial-modeller applied-economist
  version: "0.1.0"
---

# Financial model build

Good-practice references: the [ICAEW Financial Modelling Code](https://www.icaew.com/-/media/corporate/files/technical/technology/excel/financial-modelling-code.ashx) and the [FAST Standard](https://www.fast-standard.org/).

## Inputs

- The question and the decision the model supports.
- Parameters and assumptions from the Applied Economist and others, with sources.
- Data from the Data Engineer.

## Steps

1. **Agree the specification** with the Lead PM: purpose, users, outputs needed, time horizon, period length, units, currency, price basis (nominal or real, and base year), discount rate and its source.
2. **Lay out the structure:**
   - **Inputs:** every assumption, in one place, labelled with unit, source and assumptions log ID.
   - **Calculations:** formulas only, no typed numbers.
   - **Outputs:** the results users need.
   - **Checks:** tests that must hold (for example, totals agree, balances are zero, no negative quantities).
3. **Build calculations** with one consistent formula per row or column. Keep each step simple. Avoid circular references.
4. **Calculate key metrics** as relevant: NPV, IRR (and note where IRR is unreliable, such as with sign changes in cash flows), discounted payback, cost per unit, required rate or fee.
5. **Add checks** and a single master check that shows whether all checks pass.
6. **Run sensitivity analysis** on each important input (one at a time), and show which inputs move the result most.
7. **Run scenarios** with coherent sets of inputs (for example, low, base and high), each documented.
8. **Test the model:** change inputs to extreme values and confirm outputs behave sensibly; reproduce one result by hand.
9. **Write the model guide:** purpose, structure, how to update, limits.
10. **Version** the model file and record changes.

## Outputs

- The model (code or spreadsheet), stored according to its label.
- Inputs table with sources.
- Results: base case, scenarios, sensitivities.
- Model guide.

## Done when

- [ ] Inputs, calculations, outputs and checks are separate.
- [ ] No typed numbers in calculations.
- [ ] All checks pass and the master check shows it.
- [ ] Price basis and discount rate are stated.
- [ ] Sensitivity and scenarios are reported.
- [ ] A reviewer can trace any output to its inputs.
