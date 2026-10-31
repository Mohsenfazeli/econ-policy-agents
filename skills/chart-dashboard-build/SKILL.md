---
name: chart-dashboard-build
description: Designs and builds charts, maps and dashboards from data in code, with a takeaway title, the source and date on every chart, and an accessible, minimal design. Use whenever a deliverable needs a visual, or a request asks for a dashboard in tools such as Shiny, Plotly, Streamlit or a Power BI-style tool.
license: MIT
metadata:
  owner: dataviz-builder
  used-by: dataviz-builder data-engineer automation-engineer
  version: "0.1.0"
---

# Chart and dashboard build

Useful references: the UK Government Analysis Function's [data visualisation guidance](https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-charts/) and [WCAG 2.2](https://www.w3.org/TR/WCAG22/) for accessibility.

## Inputs

- The message each chart must convey, and the audience.
- Processed data with its documentation card.

## Steps for a chart

1. **State the message** in one sentence. If there is no single message, reconsider whether a chart is needed.
2. **Choose the chart type:**

   | Message | Chart |
   | --- | --- |
   | Change over time | Line |
   | Compare categories | Horizontal bar (sorted) |
   | Part of a whole | Stacked bar; avoid pie charts with many slices |
   | Estimates with uncertainty | Dot with interval, or a fan chart for forecasts |
   | Relationship between two variables | Scatter |
   | Geography matters | Map; otherwise use a bar chart |

3. **Build from the data in code.** Never type values in.
4. **Label it:**
   - Title states the takeaway ("BC inflation was above Canada's in each year from 2016 to 2019"), not just the topic.
   - Axis labels with units.
   - Direct labels on lines where possible, instead of a legend.
   - Source line: source, table or series ID, reference period, and retrieval date. Example: "Source: Statistics Canada, Table 18-10-0005-01. Annual averages, 2015 to 2025. Retrieved 2026-10-31."
5. **Design minimally:** no 3D, no heavy gridlines, no decoration. Bar charts start at zero.
6. **Make it accessible:** colour-blind-safe palette, enough contrast, meaning not carried by colour alone, readable font size, and alt text that states the message and key values.
7. **Check every value** shown against the data.

## Additional steps for a dashboard

1. **Specify before building:** users, the questions they need answered, data sources, refresh frequency, and the handling label of the data.
2. **Confirm the tool is approved** for the data's label. Dashboards on Internal or Confidential data stay in approved environments only, and never appear in this repo.
3. **Sketch the layout:** most important view first; filters only where users need them.
4. **Document data lineage** from source to each view.
5. **Build as code** where the tool allows (for example, Shiny, Plotly Dash or Streamlit), on a branch through the Automation Engineer's pull request process.
6. **Test** with sample questions from the users, and check accessibility.

## Outputs

- Chart files and the code that produces them.
- Chart notes: message, source line, alt text, method notes.
- For dashboards: specification, lineage note, and a link to the pull request.

## Done when

- [ ] Every chart has a takeaway title, axis labels, units and a source line with dates.
- [ ] Every value matches the data.
- [ ] Alt text is written.
- [ ] The chart reads correctly in greyscale.
- [ ] Dashboards: specification approved, tool approved for the label, and code reviewed.
