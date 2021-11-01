# 14848-final-project

## GUI for user to choose which application to run

<img width="1046" alt="Screen Shot 2021-10-31 at 9 52 48 PM" src="https://user-images.githubusercontent.com/60122319/139619105-2ea328f4-47cb-40c0-8cbf-c0a8a79e1b33.png">

## Docker files inclue:
user_interface_gui: elizxiong/user_interface_gui

Apache Hadoop: apache/hadoop

Apache Spark: bitnami/spark

Jupyter Notebook: jupyter/datascience-notebook

SonaQube & SonaScanner: zaquestion/sonarqube-scanner

## deployed to GCP Container Registry

<img width="793" alt="container_registry" src="https://user-images.githubusercontent.com/60122319/139619640-391997c3-8d45-491f-8ef7-ca4b458ea592.png">

## configuration

spark:
  ...
  environment:
    - SPARK_MODE=master
  ...
  
## docker run

spark:

$ docker run -d --name spark \
  --network=spark_network \
  -e SPARK_MODE=master \
  bitnami/spark
