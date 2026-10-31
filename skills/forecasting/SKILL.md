---
name: forecasting
description: Produces forecasts and projections with intervals or scenarios, evaluated against simple benchmarks. Use when a request needs future values of a series (prices, demand, labour, population, costs), or a projection to feed a cost-benefit or financial model.
license: MIT
metadata:
  owner: econometrician
  used-by: econometrician applied-economist financial-modeller
  version: "0.1.0"
---

# Forecasting

## Inputs

- The series to forecast, horizon and frequency (from the handoff).
- Historical data with documentation card.
- Any published forecasts from authoritative sources (for example, the Bank of Canada's [Monetary Policy Report](https://www.bankofcanada.ca/publications/mpr/) for inflation outlooks, or the BC budget's economic forecast in [BC Budget](https://www.bcbudget.gov.bc.ca/) documents).

## Steps

1. **Define the target:** series, units, geography, frequency, horizon, and how the forecast will be used.
2. **Check for an existing authoritative forecast.** If one exists and fits, consider using it (with citation) rather than building a new one. Record the choice.
3. **Look at the data.** Plot it. Note trend, seasonality, breaks, outliers and recent shocks.
4. **Set benchmarks.** At least one simple method: naive (last value), seasonal naive, or drift.
5. **Fit candidate models** suited to the data, for example exponential smoothing (ETS), ARIMA, regression with predictors, or a judgment-based scenario where data are thin.
6. **Evaluate out of sample.** Use a holdout period or time-series cross-validation. Compare accuracy (for example, MAE, RMSE, MASE) against the benchmarks. A model that does not beat a benchmark needs a reason to be used.
7. **Produce the forecast with uncertainty:** prediction intervals (state the level, for example 80% and 95%) or a set of named scenarios with their assumptions.
8. **Stress-test** against a plausible downside and upside.
9. **Document** the method, assumptions, data vintage, and when the forecast should be refreshed.

## Outputs

- Forecast table: period, point forecast, interval bounds or scenario values.
- Chart with history and forecast, interval shown.
- Accuracy comparison against benchmarks.
- Method and assumptions note, including the data vintage.

## Done when

- [ ] At least one benchmark was evaluated.
- [ ] Out-of-sample accuracy is reported.
- [ ] Every forecast has an interval or scenario range.
- [ ] Data vintage and refresh date are recorded.
- [ ] Any authoritative published forecast was considered and cited.

## Common pitfalls

- Reporting a single number as "the forecast".
- Evaluating only in sample.
- Extrapolating a recent shock as a trend.

## References

Hyndman and Athanasopoulos, [*Forecasting: Principles and Practice* (3rd edition)](https://otexts.com/fpp3/).
