# Prototyping a Financial RAG Chatbot: FinSightAI
## Problem Statement
Off-the-shelf large language models (LLMs), while highly capable in solving general problems and generating human-like responses, are inherently constrained by their static training data and lack of access to real-time or domain-specific knowledge. These models excel at understanding broad topics but struggle to address time-sensitive or domain-specific queries. Without access to real-time or specialized data, their responses can lack accuracy, depth, and relevance, making them unsuitable for use cases where up-to-date and domain-specific information is critical.

In the financial domain, these limitations become particularly pronounced. Answering questions about publicly traded companies often requires the ability to interpret dynamic and detailed information such as SEC filings, company presentations, and real-time market news. Off-the-shelf LLMs, which lack access to such data and are unable to access the latest financial tables or contextualize the latest corporate developments, frequently produce incomplete or outdated answers. This makes them unreliable for stakeholders like investors, analysts, and corporate decision-makers who rely on timely and precise financial insights.

Retrieval-Augmented Generation (RAG) offers a domain-specific solution by enhancing LLMs with real-time access to external, specialized data sources. For example, in the financial domain, RAG enables LLMs to retrieve and analyze the most recent SEC filings, balance sheets, earnings call transcripts, and breaking news articles. By combining retrieval-based search with generative capabilities, RAG ensures that responses are not only accurate but also timely and contextually relevant.

This project explores the potential of Retrieval-Augmented Generation (RAG) to develop FinSightAI, a financial chatbot prototype that aims to deliver accurate and timely answers to complex financial questions. The tool demonstrates how real-time data retrieval, such as SEC filings and company news, can enhance large language models (LLMs). For example, FinSightAI can fetch and analyze a company’s most recent quarterly revenue and expenses, addressing limitations of static training data. While building an accurate financial chatbot is challenging due to the complexity of financial data, this project serves as a proof of concept for integrating RAG to handle nuanced and time-sensitive queries.

## Methodology
The methodology for building a Retrieval-Augmented Generation (RAG) pipeline for a financial chatbot involves several key steps, as illustrated in Figures 1 and 2. These steps ensure the system retrieves relevant context and generates accurate, coherent responses.

Figure 1 illustrates the conceptual workflow of an LLM using RAG. The system combines the generative capabilities of large language models with the retrieval of domain-specific, up-to-date data to address complex and time-sensitive queries effectively.

![image](https://github.com/user-attachments/assets/0a87c2b4-191a-4cff-81f6-b92eb1c10f07)

Figure 1 - How an LLM using RAG works

Figure 2 illustrates the step-by-step process of implementing the RAG pipeline for the financial chatbot. Each step, described below, contributes to the system's ability to retrieve and process data efficiently.

![image](https://github.com/user-attachments/assets/936bae0a-b62d-4dbb-905e-039a293e4197)

Figure 2 - Process Overview

## Using This Repository
### Folders
```datasets``` folder contains documents downloaded for the prototype. It includes the following subfolders and files:
* ```news``` folder contains company news in PDF format.
* ```sec_filings``` folder contains recent 10-K and 10-Q files in HTML format downloaded from the SEC EDGAR API.
* ```pickle_files``` stores pickled documents with metadata.
* ```news_list.csv``` This CSV file records URLs and information of news articles to be crawled.

```eval``` folder contains evaluation-related files:
* ```Eval_QA_Bank.xlsx``` includes queries, corresponding ground-truth answers, and final evaluation results.

```chroma_database``` folder contains 18 Chroma vector stores.


### Notebooks
```1_data_collection_a_SEC_filings_metadata.ipynb```: Notebook for downloading SEC filings such as 10-K and 10-Q.

```1_data_collection_b_news_crawler.ipynb```: Notebook for downloading company news.

```2_data_preprocessing.ipynb```: Notebook for loading documents and adding metadata.

```3_vector_store_creation.ipynb```: Notebook for creating and persisting vector stores using different chunking methods, chunk sizes, and embedding models.

```4_RAG_LLM_evaluation.ipynb```: Notebook for evaluating response accuracy and efficiency across different vector stores and LLMs.

```5_RAG_deployment_UI.ipynb```: Notebook for configuring the final RAG LLM and building a user interface (UI).



