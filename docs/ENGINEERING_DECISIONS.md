# Engineering decision and evidence register

**Status:** Retrospective portfolio-level engineering review (28 October 2026). This document summarizes public repository contents. It is **not** a contemporaneous project design diary, proof of solo authorship, or independent verification of production use.

**Interactive equivalents:** [Engineering Notebook](../engineering.html) · [Evidence Ledger](../evidence.html) · [Five case studies](../work.html).

## How to read the evidence

Every project claim must include its denominator, data source, test boundary, or known limitation. Numbers from synthetic data are not actual company revenue, commercial ROI, fraud prevention, or future demand forecasts. Source links below are canonical and are preferable to repeating unsupported numerical claims in social media summaries.

| ID | Problem | Implementation trade-off | Test boundary | Main evidence | Explicit limit |
|---|---|---|---|---|---|
| ADR-01 | Revenue and distinct customer metrics can be inflated by invalid lines and returns | Completed-line recognition, SQL/Pandas reconciliation | Seeded, fictional e-commerce orders | [Source and setup](https://github.com/harshakavali81-collab/E-Commerse-Sales-and-Customers-Analytics/blob/main/README.md) | No external revenue impact |
| ADR-02 | Accuracy obscures fraud class imbalance | Chronological split, validation F2 threshold and held-out PR-AUC | 4,000 simulated events, 800 held-out | [Held-out results](https://github.com/harshakavali81-collab/TransactionShield-a-Real-Time-Fraud-Detection-and-Risk-Scoring-Platform./blob/main/docs/RESULTS.md) | Test PR-AUC 0.0319 is inadequate for deployment |
| ADR-03 | Time leakage makes demand forecasts misleading | Past-only lags, chronological validation and weekly naive baseline | Simulated one-step holdout | [Model card](https://github.com/harshakavali81-collab/DemandPilot-AI-Enterprise-AI-Demand-Forecasting-Inventory-Optimization-Platform/blob/main/docs/model_card.md) | No calibrated intervals or multi-horizon validation |
| ADR-04 | Retrieved answers can hallucinate or lack evidence | Chunk metadata, lexical TF-IDF, citations and abstention | 30 authored questions and 16 recorded tests | [Validation](https://github.com/harshakavali81-collab/AI-Document-Q-A-RAG-Knowledge-Assistant/blob/main/docs/VALIDATION.md) | Not independent LLM answer accuracy |
| ADR-05 | Restaurant totals can be incorrectly interpreted as live business outcomes | Power BI model, KPI cards, maps and slicers | Project workbook/README summary | [Dataset and dashboard](https://github.com/harshakavali81-collab/Zomato-Insights-Dashboard-project-with-PowerBI/blob/main/README.md) | Live PBIX refresh and binary availability not independently verified |

## ADR-01 — Consistent revenue population

**Decision represented by the implementation:** Quarantine invalid lines, deduplicate IDs and count completed transactions toward revenue. The e-commerce README reports 72,388 raw lines, 100 duplicated identifiers removed, 60 invalid records quarantined and 31,581 completed orders with valid lines. SQL and Pandas revenue and profit reconcile within INR 0.01.

**Reasoning:** Mixed status populations lead to false revenue and AOV. Recognition rules must be defined before summing metrics. **Next check:** add a status-change fixture and verify both implementations still agree. Do not infer actual retailer revenue from this fictional dataset.

Documented commands (run from repository root following its install guide):

```bash
python src/pipeline.py
python -m unittest discover -s tests
```

## ADR-02 — Fraud decisions are a precision/recall trade-off

**Observed:** Held-out PR-AUC 0.0319, precision 0.0246, recall 0.1429, 800 test records, 21 fraud labels. The source reports a validation-F2 threshold of 0.03 which generates many false alarms.

**Reasoning:** The review threshold trades recall for manual review volume. Large synthetic model scores cannot be advertised as real banking protection, and the poor documented results are especially important. **Next check:** representative ground truth, calibrated operating points and operational cost/safety review.

Documented synthetic training command:

```bash
python -m ml.training.train --fast
```

## ADR-03 — Use time-aware forecasting evaluation

**Observed:** One-step held-out WAPE 18.469% (LightGBM) vs 29.012% (weekly seasonal naive) in the documented simulated experiment.

**Reasoning:** Random train/test splits or future-derived lags would leak information. Recursive forecasts compound error; the repository explicitly says its displayed uncertainty range is uncalibrated and incorporates test residuals. **Next check:** proper rolling-origin multi-step evaluation and separately calibrated confidence bounds.

## ADR-04 — Prioritize testable source-grounded retrieval

**Observed:** 16 passing local pytest tests, 23/25 answerable evidence hits, 3/5 correct abstentions on authored fixture questions.

**Reasoning:** An offline lexical baseline and explicit citations make behavior inspectable; the reported fraction does not measure correctness of free-form LLM answers. **Next check:** independent documents, contradictory evidence and separately tested optional model integrations.

Documented validation commands:

```bash
python -m pytest -q
python -m evaluation.evaluate
```

## ADR-05 — Dashboard scope and reproducibility

**Observed:** Zomato project README lists 9,551 restaurants, 250 cuisines, 15 countries, 141 cities and average rating 2.89.

**Reasoning:** Country, city and cuisine filters can make project data easier to explore. These counts are sample properties, not real-time Zomato statistics or proof of financial impact. **Next check:** open the actual workbook and PBIX in Power BI Desktop when available and compare filter-level counts with source rows.

## Test/evidence grading used in this portfolio

1. **Repository documented:** a public README or technical record contains a method/measurement. This is not independent reproduction.
2. **Locally recorded test:** a repository includes a written test command and recorded result. It does not establish execution in the current session.
3. **Independent portfolio-site QA:** browser and link checks execute in GitHub Actions against the portfolio site. This does not validate underlying ML/banking/healthcare claims.
4. **Production verified:** requires genuine deployment, real authorized data, security review, operational monitoring and domain validation. **No listed project is promoted into this category without separate source evidence.**

## How to update this document

- Inspect the current project source first.
- Amend `data/project-evidence.json` and the matching case-study text.
- If a numeric figure changes, preserve denominator, unit, data provenance and test split.
- Explain regressions; do not silently overwrite a weak result with a marketing number.
- Run `python scripts/audit_site.py` and review GitHub Actions live QA on publication.

See [Portfolio Maintenance](PORTFOLIO_MAINTENANCE.md) for release steps.
