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
![Architecture Diagram](https://github.com/dhruvakashyap73/AWS-Dataflow/blob/main/1.%20AWS%20DataFlow%20Architecture/AWS-Dataflow%20Architecture.jpeg)

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

## Chapter 3: AWS Glue Job - ETL Operations and Data Quality

After ingesting raw data into S3, the next stage is **ETL processing** using **AWS Glue Studio**. This stage transforms raw data into clean, structured data suitable for analysis.

**Components:**

1. **Visual ETL in AWS Glue Studio**  
   - The ETL job `awsdataflowjob.py` performs transformations including:  
     - Removing duplicates  
     - Handling null values    
     - Aggregations 
     - Data type conversions 
     - Joining multiple datasets  

   **Visual ETL Flow Map:**  
   ![Visual ETL Flow Map](https://github.com/dhruvakashyap73/AWS-Dataflow/blob/main/3.%20AWS%20Glue%20ETL/AWS%20Glue%20ETL.png)

2. **Data Quality Validation**  
   - AWS Glue Data Quality jobs validate data against business rules, ensuring:  
     - No missing mandatory fields  
     - Correct data types  
     - Reasonable value ranges  
     - Consistency across related datasets  

   **Data Quality Report:**  
   ![Data Quality Report](https://github.com/dhruvakashyap73/AWS-Dataflow/blob/main/3.%20AWS%20Glue%20ETL/AWS%20Glue%20ETL%20DataQuality.png)

3. **Schema Management**  
   - After ETL, a **Glue Crawler** crawls the processed S3 zone.  
   - It updates the **AWS Glue Data Catalog** with schema and metadata for each dataset.  
   - This enables Athena and other AWS services to query the processed data efficiently.  

**Benefits:**

- Centralized and clean data storage in S3 (Processed Zone).  
- Production-grade data validation ensures high-quality analytics.  
- Metadata cataloging allows serverless SQL queries without manual schema management.  

---

## Chapter 4: Amazon Athena - Queries and Insights

After processing and cataloging the data using AWS Glue, **Amazon Athena** is used as a **serverless query engine** to analyze the cleaned data stored in S3. Athena enables ad-hoc queries and aggregations to extract meaningful insights from the processed OHLCV datasets.

### Key Insights from Athena Queries

1. **Aggregated Metrics**  
   - Daily and monthly aggregates of trading volume and prices were computed.  
   - **Insight:** Revealed trends in market activity, such as days with unusually high or low trading volume and periods of significant price changes.

2. **Time-Series Analysis**  
   - Daily changes in closing price and volume were tracked.  
   - **Insight:** Highlighted market volatility, showing peaks and drops on specific dates, which are critical for understanding trading behavior and risk assessment.

3. **Comparative Analysis**  
   - Sector-wise and category-wise aggregations were analyzed.  
   - **Insight:** Identified top-performing sectors or stocks and their contribution to overall market capitalization or trading activity. This helps in portfolio analysis and investment strategy planning.

4. **Risk and Performance Metrics**  
   - Daily rate of change and percentage returns were calculated.  
   - **Insight:** Pinpointed high-risk days with major price drops or spikes. This provides a better understanding of market stability and informs risk management strategies.

### Benefits of Using Athena

- **Serverless and Scalable:** No infrastructure setup required, scales automatically with data volume.  
- **Integration with Glue Data Catalog:** Allows immediate querying of processed data.  
- **Supports QuickSight Visualizations:** Provides the basis for dashboards and analytical insights.  
- **Real-Time Analysis:** Enables timely decisions based on updated processed datasets.  

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


