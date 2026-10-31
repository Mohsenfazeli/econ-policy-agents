---
name: regression-analysis
description: Plans, estimates and diagnoses regression models, including causal designs (difference-in-differences, instrumental variables, regression discontinuity, synthetic control), discrete choice, fractional outcome and survey-weighted models. Use when a request needs an estimated relationship or effect with stated assumptions, uncertainty and diagnostics.
license: MIT
metadata:
  owner: econometrician
  used-by: econometrician applied-economist
  version: "0.1.0"
---

# Regression analysis

## Inputs

- The question, from the handoff.
- Processed data with its data documentation card and data-quality audit.
- Prior estimates and methods from the Research Librarian, if any.

## Steps

1. **Classify the question.**
   - Descriptive: "How does Y vary with X?"
   - Predictive: "What will Y be?" (use the [forecasting skill](../forecasting/SKILL.md))
   - Causal: "What is the effect of X on Y?"
   Only causal designs support causal language.
2. **Choose the model** to fit the outcome and design:

   | Situation | Typical approach |
   | --- | --- |
   | Continuous outcome | Linear regression with robust or clustered standard errors |
   | Binary or multinomial choice | Logit or probit; multinomial or conditional logit for discrete choice |
   | Outcome is a share between 0 and 1 | Fractional response model (for example, fractional logit), not a linear model on the share |
   | Counts | Poisson or negative binomial |
   | Policy change affecting some units at a known time | Difference-in-differences; for staggered timing, a method robust to heterogeneous effects |
   | Endogenous regressor with a valid instrument | Instrumental variables, with first-stage strength reported |
   | Treatment assigned by a cut-off | Regression discontinuity |
   | One or few treated units with a long pre-period | Synthetic control |
   | Survey data | Use survey weights and design (strata, clusters) |

3. **Write down the specification before estimating:** outcome, key regressors, controls, fixed effects, sample, standard errors, and for causal designs the identifying assumptions.
4. **Estimate in code.** Save code and outputs together. Set seeds where randomness is involved.
5. **Diagnose:**
   - Residual patterns, influential observations, multicollinearity.
   - Heteroskedasticity and serial correlation; choose standard errors accordingly.
   - Difference-in-differences: plot pre-trends; run an event-study version.
   - Instrumental variables: first-stage F-statistic or equivalent; discuss the exclusion restriction.
   - Regression discontinuity: density test at the cut-off; bandwidth sensitivity.
   - Synthetic control: pre-period fit; placebo tests.
   - Discrete and fractional models: report marginal effects, not only coefficients.
6. **Test robustness:** alternative specifications, samples, and control sets. Report all that were run.
7. **Interpret** in plain language: size, direction, uncertainty, and what the result does not show.

## Outputs

- Method note (question type, model, rationale, assumptions).
- Results table (estimates, standard errors or intervals, sample size, specification).
- Diagnostics and robustness summary.
- Plain-language interpretation and limitations.
- Code location.

## Done when

- [ ] The specification was written before estimation.
- [ ] Every reported number comes from saved code.
- [ ] Diagnostics appropriate to the method were run and reported.
- [ ] At least one robustness check is reported for each headline estimate.
- [ ] Causal language is used only where the design supports it.

## References

See [methods references](../../library/methods/references.md), including *Causal Inference: The Mixtape*, *The Effect*, *Discrete Choice Methods with Simulation*, and the difference-in-differences and synthetic control papers listed there.
