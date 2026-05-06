# Data enrichment
This repository contains the enriched version of the data extracted during the second step of the workflow ([2-DataExtraction](https://github.com/FNS-Spurgeon/2-DataExtraction)).

## Data cleaning
Data are cleaned using OpenRefine. Spaces, line breaks, hyphens and ellipsis are normalised. Bibliographical information, quotation and Spurgeon’s notes are split. New CSV files are stored in the repository [1-DataCorrected](https://github.com/FNS-Spurgeon/3-DataEnrichment/tree/main/1-DataCorrected).

## Data enrichment
Data are augmented with new information:

- **Date certainty**: Spurgeon uses different symbols to assess the certainty of a date (i.e. c, a, n.a, n.b, \[] or ?). Depending on these symbols, we automatically attribute to each date a level of certainty: high, medium or low.
- **Author certainty**: Similarly to dates, a level of certainty for authors attribution is automatically assigned.
- **Name reconciliation**: Each author name is reconciled with Wikidata. From Wikidata, we get their gender and their VIAF ID (if there is one).
- **Index classification**: Each entry in the volumes is enriched with the 10-categories classification provided by the [index](https://github.com/FNS-Spurgeon/2-DataExtraction/tree/main/index/index-csv) (Vol. 3), using authors' names, dates, part and page numbers as key to match entries listed in the index with their correspondences in the volumes. This is done with the script [indexAddition.py](https://github.com/FNS-Spurgeon/3-DataEnrichment/blob/main/scripts/indexAddition.py).
- **Language detection**: The language of quotations is detected with the [langid](https://github.com/saffsd/langid.py) Python library. The script used can be found here: [languageDetection.py](https://github.com/FNS-Spurgeon/3-DataEnrichment/blob/main/scripts/languageDetection.py). 

The enriched CSV files are stored in [2-DataEnriched](https://github.com/FNS-Spurgeon/3-DataEnrichment/tree/main/2-DataEnriched).

## Licence
All data are published under the licence [CC-BY](https://creativecommons.org/licenses/by/4.0/).
