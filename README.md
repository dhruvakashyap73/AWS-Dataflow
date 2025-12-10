# AWS-Dataflow: Serverless ETL Pipeline 

## Introduction

This project demonstrates the design and implementation of a **Fully Automated Serverless ETL & Analytics Pipeline** using AWS services. The goal of this project is to collect data from external APIs, process and clean it, store it in a structured format, and provide analytical insights via SQL queries and visualizations, all while maintaining observability and monitoring.

The pipeline implements industry-standard cloud-native practices and ensures:
- Data ingestion from external APIs using Databricks Workspace and Notebook (manual or scheduled via script).  
- Data cleaning, transformation, and validation using AWS Glue Studio (ETL & Data Validation)  
- Metadata management and cataloging for query optimization using Glue Crawler and Glue Data Catalog.  
- Analytical queries using serverless query engines like Amazon Athena.  
- Visualization and monitoring for business insights and reliability via Amazon QuickSight and CloudWatch.

---

## Chapter 1: Architecture
## Workflow
This project implements a **Serverless ETL and Analytics Pipeline** on AWS. Data is collected from the **Twelve Data API** using a **Databricks Notebook** and a Python script (`DataIngestion.py`) and stored in **Amazon S3 (Raw Zone)**. The raw data is then processed in **AWS Glue Studio**, where it is cleaned, transformed, and structured by removing duplicates, handling missing values, aggregating, and converting data types. **AWS Glue Data Quality** jobs check the data for accuracy and consistency. A **Glue Crawler** updates the **Glue Data Catalog** with schema and metadata, making the data ready for queries. **Amazon Athena** runs SQL queries on the processed data to extract insights such as trading volumes, price changes, and risk metrics. These insights are visualized in **Amazon QuickSight** dashboards, showing trends, correlations, and market volatility. Finally, **Amazon CloudWatch** monitors the pipeline, collecting logs and metrics to ensure reliability and detect issues. This pipeline shows a complete, cloud-native approach for analyzing financial data.

**AWS Dataflow Architecture**  
![Architecture Diagram](https://github.com/dhruvakashyap73/AWS-Dataflow/blob/main/1.%20AWS%20DataFlow%20Architecture/AWS-Dataflow%20Architecture.jpeg)

---

## Chapter 2: Data Ingestion

Data ingestion is the first critical stage of the pipeline. The goal is to fetch raw data from **Twelve Data API** and store it in Amazon S3 (Raw Zone) for further processing. The ingestion process is implemented using **Databricks Workspace and Notebook**, which allows scalable, interactive data processing before storing it in S3.

**Implementation Details:**
1. **Data Source**: Twelve Data API, providing financial and time-series data (OHLCV).  
2. **Data Retrieval**: Data is ingested via a **Databricks Notebook**, which runs a Python script (`DataIngestion.py`) to fetch data from the Twelve Data API. Databricks provides an interactive environment to process, validate, and prepare the data before storage.  
3. **Storage**: Raw data is stored in **Amazon S3 Raw Zone**, organized by source and date for traceability and easy access for downstream ETL processes.  
4. **Automation (Optional)**: The ingestion process can be scheduled using orchestration tools (e.g., EventBridge Scheduler) to ensure regular updates without manual intervention.  

**Python Script (`DataIngestion.py`)**  
[Access the DataIngestion.py file here](https://github.com/dhruvakashyap73/AWS-Dataflow/blob/main/2.%20Data_Ingestion/DataIngestion.py)

---

## Chapter 3: AWS Glue Job - ETL Operations and Data Quality

After ingesting raw data into S3, the next stage is **ETL processing** using **AWS Glue Studio**. The ETL job, implemented as `awsdataflowjob.py`, performs multiple transformations on the raw data, including duplicate removal, null handling, aggregations, data type conversions, and joining multiple datasets to produce clean, structured data ready for analysis.  

**Visual ETL Flow Map:**  
![Visual ETL Flow Map](https://github.com/dhruvakashyap73/AWS-Dataflow/blob/main/3.%20AWS%20Glue%20ETL/AWS%20Glue%20ETL.png)

Once the data is processed, **AWS Glue Data Quality** jobs validate it against business rules to ensure completeness, correctness, and consistency across related datasets. This includes checks for mandatory fields, correct data types, and reasonable value ranges.  

**Data Quality Report:**  
![Data Quality Report](https://github.com/dhruvakashyap73/AWS-Dataflow/blob/main/3.%20AWS%20Glue%20ETL/AWS%20Glue%20ETL%20DataQuality.png)

Finally, a **Glue Crawler** scans the processed S3 zone and updates the **AWS Glue Data Catalog** with schema and metadata for each dataset. This enables efficient querying of the processed data using Amazon Athena or other AWS services, completing the ETL and validation cycle.

---

## Chapter 4: Amazon Athena - Queries and Insights

After processing and cataloging the data using AWS Glue, **Amazon Athena** is used as a **serverless query engine** to analyze the cleaned datasets stored in S3. Athena enables ad-hoc queries, aggregations, and analytics on the processed OHLCV data.

**Athena Queries File:**  
[Access athena_queries.sql here](INSERT_LINK_TO_ATHENA_QUERIES_HERE)

### Key Insights from Athena Queries
1. **Aggregated Metrics**  
   Daily and monthly aggregates of trading volume and prices were computed.  
   **Insight:** Revealed trends in market activity, highlighting days with unusually high or low trading volumes and significant price changes.
2. **Time-Series Analysis**  
   Daily changes in closing price and trading volume were tracked.  
   **Insight:** Showed market volatility with peaks and drops on specific dates, essential for understanding trading behavior and risk.
3. **Comparative Analysis**  
   Sector-wise and category-wise aggregations were analyzed.  
   **Insight:** Identified top-performing stocks or sectors and their contribution to overall market activity, aiding investment and portfolio analysis.
4. **Risk and Performance Metrics**  
   Daily rate of change and percentage returns were calculated.  
   **Insight:** Pinpointed high-risk days with major price spikes or drops, providing insights into market stability and informing risk management strategies 

---

## Chapter 5: Amazon QuickSight - Visualization

In this stage, the processed **OHLCV (Open, High, Low, Close, Volume)** data is visualized using **Amazon QuickSight**. The visualizations provide insights into market trends, daily price movements, trading activity, and price-volume correlations.

### Visualizations

1. **Daily Price Change**  
   - **File:** ![1.png](INSERT_IMAGE_LINK_HERE)  
   - **Insight:** This line chart shows daily price changes for the selected time period. It highlights **market volatility**, helping to identify days with significant gains or losses and assess overall price stability.

2. **Daily Volume**  
   - **File:** ![2.png](INSERT_IMAGE_LINK_HERE)  
   - **Insight:** This bar chart tracks **daily trading activity** by displaying the total trading volume per day. Peaks in the chart indicate high activity days, which can correlate with major market events.

3. **Monthly Volume**  
   - **File:** ![4.png](INSERT_IMAGE_LINK_HERE)  
   - **Insight:** This bar chart summarizes **long-term trading trends** by aggregating volume over the month. It helps to understand whether trading activity is increasing, decreasing, or stable over time.

4. **Price vs Volume**  
   - **File:** ![6.png](INSERT_IMAGE_LINK_HERE)  
   - **Insight:** This bubble/scatter chart analyzes the **correlation between price and trading volume**. The X-axis represents price, Y-axis represents trading volume, and bubble size indicates the relative market impact. It helps identify anomalies and relationships between price movements and trading activity.

### Key Benefits

- Provides interactive dashboards for easy data interpretation.  
- Supports trend analysis, risk assessment, and market activity insights.  
- Seamlessly integrated with Athena queries and Glue Data Catalog for real-time analytics.  
- Enables stakeholders to make data-driven decisions without writing SQL or code.  

---

## Chapter 6: Amazon CloudWatch - Monitoring and Logs

Monitoring is a critical part of any production-grade ETL pipeline. **Amazon CloudWatch** provides centralized monitoring, logging, and alerting for the entire serverless ETL and analytics workflow.

### Key Monitoring Components

1. **Logs**  
   - All AWS Glue ETL job runs, API ingestion events, and pipeline activities are logged.  
   - Logs provide detailed information on job execution status, errors, warnings, and performance metrics.  
   - **Insight:** Enables quick troubleshooting, error tracking, and validation of ETL execution.  

   **Example Log Dashboard:**  
   ![CloudWatch Logs](INSERT_IMAGE_LINK_HERE)

2. **Metrics & Dashboards**  
   - Custom dashboards track key performance indicators such as:  
     - ETL job duration and success/failure rate  
     - Data ingestion volume  
     - API response times  
     - S3 storage growth in raw and processed zones  
   - **Insight:** Provides real-time observability into pipeline health, ensures SLA compliance, and helps optimize resource usage.  

   **Example Metrics Dashboard:**  
   ![CloudWatch Metrics Dashboard](INSERT_IMAGE_LINK_HERE)

### Benefits

- Centralized monitoring across all AWS services used in the pipeline.  
- Early detection of failures and anomalies through logs and metrics.  
- Supports automation via alarms and notifications (optional SNS integration).  
- Enhances reliability, observability, and operational efficiency of the data pipeline.


