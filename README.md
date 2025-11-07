Designed and implemented an end-to-end data pipeline that automates data ingestion, transformation, and analytics using Snowflake, Apache Airflow, and dbt.

Data Ingestion: Extracted structured CSV datasets and loaded them into Snowflake as raw tables inside raw schema.

Data Modeling & Transformation: Built a robust staging layer and fact models using dbt, following best practices of modular SQL and data lineage tracking.

Orchestration & Automation: Configured Airflow DAGs to orchestrate dbt runs and dbt tests, ensuring automated scheduling, dependency management, and monitoring of pipeline tasks.

Analytics Layer: Developed a fact table (fct_daily_orders_revenue) combining multiple staging models to provide insights into daily revenue trends and customer behavior.

Best Practices: Implemented data quality tests, schema evolution handling, and a clear data warehouse architecture separating raw, staging, and analytics layers.

This project demonstrates building a scalable, cloud-native ELT pipeline that transforms raw CSV files into meaningful analytics-ready datasets, enabling downstream reporting and BI dashboards
