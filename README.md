# OCI Language and Batch Translation 

[![License: UPL](https://img.shields.io/badge/license-UPL-green)](https://img.shields.io/badge/license-UPL-green) [![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=oracle-devrel_oci-language-translation)](https://sonarcloud.io/dashboard?id=oracle-devrel_oci-language-translation)

## Introduction

The OCI Language Service is a serverless, multitenant service that provides users with pretrained and custom models to analyze *unstructured text* and extract insights without the need for Data Science or Machine Learning expertise.

The Language service can be accessed via REST API, SDK, or  CLI, and is suitable for tasks requiring text analysis at scale.

These are the following available features:

- [Language Detection](https://docs.oracle.com/en-us/iaas/language/using/lang-detect.htm#lang-detect): detecting languages based on the provided text - with a confidence score.
- [Text Classification](https://docs.oracle.com/en-us/iaas/language/using/ner.htm#ner): identifying document category and subcategories, to which the text belongs to.
- [Named Entity Recognition](https://docs.oracle.com/en-us/iaas/language/using/ner.htm#ner) (NER): identify entities, places, locations, emails... within text.
- [Key Phrase Extraction](https://docs.oracle.com/en-us/iaas/language/using/key_ref.htm#key_ref): extracts the most important set of phrases from a text or a block of text.
- [Sentiment Analysis](https://docs.oracle.com/en-us/iaas/language/using/sentment.htm#sentiment): analyzes the sentiment score from provided text: it can be positive, neutral, or negative.
- [Text Translation](https://docs.oracle.com/en-us/iaas/language/using/translate-text.htm): batch translate text into any language of choice (as long as it's [in the supported list of languages](https://docs.oracle.com/en-us/iaas/language/using/translate-text.htm)).
- [Personal Identifiable Information (PII)](https://docs.oracle.com/en-us/iaas/language/using/pii.htm#translate): detects private information in the text (credit cards, IP addresses, phone numbers, emails, telephone numbers, names,...) and **obscures/hides** it.

With all these features available, the Language service automates sophisticated text analysis, saving you time and resources.

We will use OCI's Python SDK to access OCI Language, and once we have some code ready, we will invoke it in a pipeline to create an AI-Enhanced Wall Street Market Analyzer.

There's the possibility to create your own custom models for Text Classification and Named Entity Recognition, although we will not explore their benefits in this use case. [Have a look here](https://docs.oracle.com/en-us/iaas/language/using/custom-models.htm#custom-models) if you're interested.

## 0. Prerequisites and setup

- Oracle Cloud Infrastructure (OCI) Account with available credits to spend
- [OCI Language Overview](https://docs.oracle.com/en-us/iaas/language/using/overview.htm#language)
- [Oracle Cloud Infrastructure (OCI) Language Documentation](https://docs.oracle.com/en-us/iaas/language/using/home.htm)
- [Python 3.10](https://www.python.org/downloads/release/python-3100/)
- [Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)
- [OCI SDK](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm)

First, we install dependencies:

```bash
pip install -r requirements.txt
```

We can run some of our code: 

After, we can run `data_generator.py`:

```bash
cd scripts/
python data_generator.py
```

The console will ask for how many synthetic users' data you want. For testing purposes, this can be any small value that will let us test; for your own use case in practice, your only job is to select which data will go into the vector database, and in which form (JSON, structured data, raw text... and their properties (if any)).

## 1. Create data sources

## 2. Create endpoint to consume data

## 3. Create agent to point to data source and identity domain

## 4. Talk to your new agent

## Demo

[OCI Vision Overview - Exploring the Service](https://www.youtube.com/watch?v=eyJm7OlaRBk&list=PLPIzp-E1msraY9To-BB-vVzPsK08s4tQD&index=4)

## Tutorial

Here’s an use case being solved with OCI Vision + Python:

[App Pattern: OCI Vision Customized Object Detector in Python](https://www.youtube.com/watch?v=B9EmMkqnoGQ&list=PLPIzp-E1msraY9To-BB-vVzPsK08s4tQD&index=2)

[This is a tutorial](https://docs.oracle.com/en/learn/oci-opensearch/index.html#introduction) about OCI OpenSearch if you're interested in learning more about vectorization, connecting to the cluster, ingesting data, searching for data and visualizing it.

## Physical Architecture

![arch](./img/arch.PNG)

## Contributing

This project is open source. Please submit your contributions by forking this repository and submitting a pull request! Oracle appreciates any contributions that are made by the open source community.

## License

Copyright (c) 2022 Oracle and/or its affiliates.

Licensed under the Universal Permissive License (UPL), Version 1.0.

See [LICENSE](LICENSE) for more details.

ORACLE AND ITS AFFILIATES DO NOT PROVIDE ANY WARRANTY WHATSOEVER, EXPRESS OR IMPLIED, FOR ANY SOFTWARE, MATERIAL OR CONTENT OF ANY KIND CONTAINED OR PRODUCED WITHIN THIS REPOSITORY, AND IN PARTICULAR SPECIFICALLY DISCLAIM ANY AND ALL IMPLIED WARRANTIES OF TITLE, NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A PARTICULAR PURPOSE.  FURTHERMORE, ORACLE AND ITS AFFILIATES DO NOT REPRESENT THAT ANY CUSTOMARY SECURITY REVIEW HAS BEEN PERFORMED WITH RESPECT TO ANY SOFTWARE, MATERIAL OR CONTENT CONTAINED OR PRODUCED WITHIN THIS REPOSITORY. IN ADDITION, AND WITHOUT LIMITING THE FOREGOING, THIRD PARTIES MAY HAVE POSTED SOFTWARE, MATERIAL OR CONTENT TO THIS REPOSITORY WITHOUT ANY REVIEW. USE AT YOUR OWN RISK.
