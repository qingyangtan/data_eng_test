# Data Engineering Test Documentation

## Section 1

- Airflow is deployed to handle the scheduling
- The schedule is set at 1am daily
- The 4 data processing steps are executed and save to the output folder

## Section 2

- The dockerfile will pull the latest Postgres image with necessary settings
- The init.sql will create the required tables based on DDL
- Refer to the pdf for the Entity-Relationship Diagram

## Section 3

- The Data Architecture is based off AWS Cloud
- Kafka streams the images uploaded by customers to the S3 Data Lake in real time
- The scripts prepared by the Software Engineers (SE) will be placed in the glue jobs to be executed
- The processed images are then flow into S3 for the web application to fetch it when the customers send a request
- Glacier is used to reduce the costs of storing heavy bytes images while meeting the 7 days or more archive regulation
- The metadata generated upon processing the images will be stored into S3 as well
- AWS Quicksight is chosen as to keep BI in the AWS ecosystem, reduce licensing costs, reduce the need to find another data store for analytics
- Refer to the pdf for the data architecture
