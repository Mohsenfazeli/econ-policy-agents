# Canadian and BC data and legal sources

A starting catalogue of public sources the team uses most. Each link was opened when this file was last updated (2026-10-31). Table IDs were confirmed against the Statistics Canada Web Data Service. Prefer the original producer; record table or series IDs, reference periods and retrieval dates every time.

## Statistics Canada

Licence: [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Programmatic access: [Web Data Service (WDS)](https://www.statcan.gc.ca/en/developers/wds).

| Topic | Source | ID | Notes |
| --- | --- | --- | --- |
| Consumer prices, monthly | [Consumer Price Index, monthly, not seasonally adjusted](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810000401) | 18-10-0004-01 | Canada, provinces, selected cities; product groups. Base 2002=100. |
| Consumer prices, annual | [Consumer Price Index, annual average, not seasonally adjusted](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810000501) | 18-10-0005-01 | Used in the [worked example](../../examples/cpi-fee-indexing/README.md). |
| CPI methodology | [The Canadian Consumer Price Index Reference Paper](https://www150.statcan.gc.ca/n1/en/catalogue/62-553-X) | 62-553-X | Scope, basket, weights, calculation. |
| Prices analysis | [Prices Analytical Series](https://www150.statcan.gc.ca/n1/en/catalogue/62F0014M) | 62F0014M | Technical papers on price measurement. |
| Labour force | [Labour force characteristics, monthly, seasonally adjusted and trend-cycle](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410028701) | 14-10-0287-01 | Labour Force Survey. Survey estimates: check quality flags. |
| Employment by industry | [Employment by industry, monthly](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410035501) | 14-10-0355-01 | Last five months only; use other LFS tables for history. |
| Labour Force Survey guide | [Guide to the Labour Force Survey](https://www150.statcan.gc.ca/n1/en/catalogue/71-543-G) | 71-543-G | Definitions and methodology. |
| Population | [Population estimates, quarterly](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710000901) | 17-10-0009-01 | Canada, provinces and territories. |
| Data quality | [Statistics Canada Quality Guidelines](https://www150.statcan.gc.ca/n1/en/catalogue/12-539-X) | 12-539-X | Reference for the data-quality audit skill. |

Other tables are found through the Statistics Canada site search or the WDS. Add them here when used more than once.

## BC government

| Topic | Source | Notes |
| --- | --- | --- |
| BC statistics | [BC Stats: data and statistics](https://www2.gov.bc.ca/gov/content/data/statistics) | Provincial statistics agency; population, economy, labour, trade. |
| BC economic statistics | [Economic statistics](https://www2.gov.bc.ca/gov/content/data/statistics/economy) | Provincial economic indicators and releases. |
| BC open data | [BC Data Catalogue](https://catalogue.data.gov.bc.ca/) | Check each dataset's licence. |
| BC budget and fiscal plan | [BC Budget](https://www.bcbudget.gov.bc.ca/) | Budget, fiscal plan, economic forecast. |

## Federal and national sources

| Topic | Source | Notes |
| --- | --- | --- |
| Interest and exchange rates | [Bank of Canada Valet API](https://www.bankofcanada.ca/valet/docs) | Programmatic access to Bank of Canada series. |
| Exchange rates | [Bank of Canada exchange rates](https://www.bankofcanada.ca/rates/exchange/) | Daily rates. |
| Interest rates | [Bank of Canada interest rates](https://www.bankofcanada.ca/rates/interest-rates/) | Policy rate and market rates. |
| Inflation measures | [Bank of Canada: consumer price index](https://www.bankofcanada.ca/rates/price-indexes/cpi/) | Core inflation measures. |
| Economic outlook | [Bank of Canada Monetary Policy Report](https://www.bankofcanada.ca/publications/mpr/) | Published projections; cite the edition. |
| Immigration | [IRCC statistics and open data](https://www.canada.ca/en/immigration-refugees-citizenship/corporate/reports-statistics/statistics-open-data.html) | Permanent and temporary residents, processing. |
| Immigration, monthly | [Permanent Residents: Monthly IRCC Updates](https://open.canada.ca/data/en/dataset/f7e5498e-0ad8-4417-85c9-9b8aff9b9eda) | Values are rounded and small counts suppressed; IRCC notes the rounded files are not for calculations. |
| Federal open data | [Open Government Portal](https://open.canada.ca/en/open-data) | Search across federal datasets. |
| Housing | [CMHC Housing Market Information Portal](https://www03.cmhc-schl.gc.ca/hmip-pimh/) | Starts, completions, rental market. |
| Fiscal analysis | [Parliamentary Budget Officer](https://www.pbo-dpb.ca/) | Independent federal costings and analysis. |
| Competition | [Competition Bureau Canada](https://competition-bureau.canada.ca/) | Market studies, guidance. |
| Federal publications | [Government of Canada Publications](https://publications.gc.ca/) | Archive of federal publications. |

## International

| Topic | Source | Notes |
| --- | --- | --- |
| US and international series | [FRED](https://fred.stlouisfed.org/) ([API](https://fred.stlouisfed.org/docs/api/fred/)) | Aggregator: cite the original source shown on each series. |
| OECD countries | [OECD Data Explorer](https://data-explorer.oecd.org/) | Cross-country comparisons. |
| Global | [World Bank Open Data](https://data.worldbank.org/) | Development indicators. |

## Legislation, regulation and decisions

| Topic | Source | Notes |
| --- | --- | --- |
| BC statutes and regulations | [BC Laws](https://www.bclaws.gov.bc.ca/) | Official consolidated BC legislation. Note the "current to" date. |
| Example: passenger transportation | [Passenger Transportation Act](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/04039_01) | Public statute; cite sections, not commentary. |
| Privacy (BC public bodies) | [Freedom of Information and Protection of Privacy Act](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96165_00) | Relevant to data handling. |
| BC Legislature | [Legislative Assembly of British Columbia](https://www.leg.bc.ca/) | Bills, Hansard. |
| Federal statutes and regulations | [Justice Laws Website](https://laws-lois.justice.gc.ca/) | Official consolidated federal legislation. |
| Federal regulations in progress | [Canada Gazette](https://gazette.gc.ca/) | Proposed and final regulations, with regulatory impact analysis statements. |
| Parliament | [House of Commons](https://www.ourcommons.ca/) | Bills, committee reports. |
| Court and tribunal decisions | [CanLII](https://www.canlii.org/) | Free access to Canadian decisions. |

## Adding a source

See [`library/README.md`](../README.md#how-to-add-context). Public sources only. Open every link before adding it.
