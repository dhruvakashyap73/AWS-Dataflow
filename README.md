# AWS-Dataflow: Serverless ETL Pipeline 

## Introduction

This project demonstrates the design and implementation of a **Fully Automated Serverless ETL & Analytics Pipeline** using AWS services. The goal of this project is to collect data from external APIs, process and clean it, store it in a structured format, and provide analytical insights via SQL queries and visualizations, all while maintaining observability and monitoring.

The pipeline implements industry-standard cloud-native practices and ensures:

- Automated data ingestion from external APIs.
- Data cleaning, transformation, and validation.
- Metadata management and cataloging for query optimization.
- Analytical queries using serverless query engines.
- Visualization and monitoring for business insights and reliability.

The workflow is as follows:  

**API → Raw Storage → ETL → Clean Data → Metadata Catalog → Query → Dashboard → Monitoring**  

---

## Chapter 1: Architecture

The architecture of this pipeline leverages **AWS Serverless Services** to achieve scalability, reliability, and cost-efficiency. The major components are:

1. **Data Ingestion**: Data is collected from external APIs and stored in Amazon S3 (Raw Zone).  
2. **ETL Processing**: AWS Glue Studio performs Extract, Transform, Load (ETL) operations, cleaning and structuring the data.  
3. **Data Validation**: AWS Glue Data Quality jobs verify data accuracy, completeness, and consistency.  
4. **Schema Management**: Glue Crawler updates the AWS Glue Data Catalog with processed schema and metadata.  
5. **Query Engine**: Amazon Athena allows running SQL queries on the cleaned and cataloged data.  
6. **Visualization**: Amazon QuickSight dashboards visualize key insights for stakeholders.  
7. **Monitoring**: Amazon CloudWatch tracks pipeline performance, logs, and metrics.  

**Architecture Diagram:**  
![Architecture Diagram](INSERT_IMAGE_LINK_HERE)

**Key Advantages:**

- Fully serverless, eliminating the need for provisioning servers.
- Scalable to handle large datasets.
- Observability and logging via CloudWatch.
- Real-world production-level design.

---

## Chapter 2: Data Ingestion

Data ingestion is the first critical stage of the pipeline. The goal is to fetch raw data from **Twelve Data API** and store it in Amazon S3 (Raw Zone) for further processing.

**Implementation Details:**

1. **Data Source**: Twelve Data API, which provides time-series and financial data.  
2. **Data Retrieval**: Python script `DataIngestion.py` is used to fetch data from 12 different APIs.  
3. **Storage**: Raw data is stored in **Amazon S3 Raw Zone**, organized by source and date for traceability.  
4. **Automation**: Data ingestion can be scheduled to run at regular intervals using orchestration tools (optional enhancement: EventBridge Scheduler).  

**Python Script Example (`DataIngestion.py`):**
