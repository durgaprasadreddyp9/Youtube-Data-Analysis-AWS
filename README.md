# 📊 YouTube Data Analytics Pipeline with AWS

## 📌 Overview
This project focuses on **securely managing, streamlining, and analyzing** structured and semi-structured **YouTube video data** based on **video categories** and **trending metrics**. The system is designed to **ingest, transform, and store** data efficiently while ensuring scalability and reliability.

Key functionalities include:
- **Data ingestion mechanism** to collect data from multiple sources.
- **ETL pipeline** to transform raw data into a structured format.
- **Centralized Data Lake** for optimized storage and querying.
- **Scalable AWS architecture** to handle growing data volumes.
- **Interactive visualizations** for meaningful insights.

---

### 🔹 **Tech Stack**
- **📦 AWS S3** - Stores raw and processed data.
- **🔐 AWS IAM** - Manages secure access control.
- **🔗 AWS Glue** - Facilitates data integration and transformation.
- **🔍 AWS Athena** - Performs SQL-based querying on the dataset.
- **⚡ AWS Lambda** - Automates ETL and compute tasks.
- **📊 AWS QuickSight** - Provides interactive data visualizations.
- **📜 Kaggle Dataset** - Contains trending YouTube video data across regions.

### 🔄 **Workflow**
1️⃣ **Ingest Data**:  
   - Extract trending video data from Kaggle.
   - Store raw CSV/JSON files in **AWS S3**.

2️⃣ **Transform Data (ETL)**:  
   - Use **AWS Glue** to clean, normalize, and format data.
   - Convert semi-structured JSON into a structured schema.

3️⃣ **Load Data into Data Lake**:  
   - Store the transformed data back in **S3**.
   - Register tables in **AWS Glue Data Catalog**.

4️⃣ **Query & Analyze Data**:  
   - Use **AWS Athena** to run SQL queries on structured data.
   - Optimize query performance with partitioning.

5️⃣ **Visualize Insights**:  
   - Connect **AWS QuickSight** to Athena.
   - Create dashboards for metrics like trending video patterns, top categories, and engagement trends.

---

## 🚀 Getting Started

### 🔧 **Prerequisites**
Ensure you have:
- **AWS Account** with IAM permissions for S3, Glue, Athena, Lambda, and QuickSight.
- **Python (>=3.8)** 🐍
- **Boto3 & AWS CLI** installed and configured.


