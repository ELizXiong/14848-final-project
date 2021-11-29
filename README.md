# 14848-final-project

## GUI for user to choose which application to run
<img width="1068" alt="Screen Shot 2021-11-28 at 8 39 20 PM" src="https://user-images.githubusercontent.com/60122319/143796000-25930b29-8594-4b17-90e8-a32361abb5b3.png">

### Usage: users can choose the desired application by using either drop-down option list or typing in the corresponding number (1,2,3,4) in the input box. Press the confirm (for the drop-down list) or submit button (for the input box) to access to the desired application interface.

### Please see details in the walkthrough demo video

## Docker Images

### Apache Hadoop: 

Namenode docker image: bde2020/hadoop-namenode

https://hub.docker.com/r/bde2020/hadoop-namenode

Datanode docker image: bde2020/hadoop-datanode

https://hub.docker.com/r/bde2020/hadoop-datanode

### Apache Spark: bitnami/spark

https://hub.docker.com/r/bitnami/spark/

### Jupyter Notebook: jupyter/datascience-notebook

https://hub.docker.com/r/jupyter/datascience-notebook/

### SonaQube & SonaScanner: sonarqube

https://hub.docker.com/_/sonarqube

### Toolbox User Interface: elizxiong/toolbox-interface:v2

https://hub.docker.com/layers/179555090/elizxiong/toolbox-interface/v2/images/sha256-6bbc4be9866a4d47a3a6e540fbdf4a8f41c0061d93b256b001908c646df08ec8?context=repo

## Push above docker images to Google Container Registry

<img width="554" alt="Screen Shot 2021-11-28 at 9 04 32 PM" src="https://user-images.githubusercontent.com/60122319/143797774-f1cd4dc1-5cbf-47d3-baa1-53097f20199c.png">

Codes used [use sonarqube as an example]:

docker pull sonarqube

docker tag sonarqube gcr.i0/final-project-330803/sonarqube:latest

docker push gcr.i0/final-project-330803/sonarqube:latest

## Deploy docker images to Kubernetes Engine

<img width="989" alt="Screen Shot 2021-11-28 at 9 06 21 PM" src="https://user-images.githubusercontent.com/60122319/143797965-7ae1099d-4c81-4a32-9010-6c6ee55549d0.png">

For Apache Hadoop App, deploy Namenode first, yml and environment variables needed can be found here in https://github.com/big-data-europe/docker-hadoop. Please see docker-compose.yml and hadoop.env. Added CLUSTER_NAME=test and other environment variables to yaml file. Please see files in configuration folder for details. 

After successfully deploying namenode, deploy datanode in a similiar way. Added SERVICE_PRECONDITION: "hadoop-namenode-qw94b:9000" and other environment variables to yaml file. Please see files in configuration folder for details. 

Other docker images can be deployed using Deploy to GKE option and default settings.

## Expose to Services & Ingress

<img width="1063" alt="Screen Shot 2021-11-28 at 9 19 32 PM" src="https://user-images.githubusercontent.com/60122319/143799002-e15192ee-fabc-42fa-9250-088cb621f02e.png">

Endpoint: http://35.239.106.172/[#PORT]

Apache Hadoop:  TCP Ports Used 9870, 9000

Spark: TCP Port Used 8080

Juypter: TCP Port Used 8888

Sonar-qube: TCP Port Used 9000

## Run the User Interface GUI

Method 1: run using Docker Image elizxiong/toolbox-interface:v2 with proper environment $DISPLAY specified

Method 2: run using command$ python User_Interface_GUI.py in terminal with required package installed (!pip install tk)

## Outputs 

### 1. Apache Hadoop

#### NameNode
<img width="1236" alt="Screen Shot 2021-11-28 at 5 48 11 PM" src="https://user-images.githubusercontent.com/60122319/143799723-7be9f7d2-b541-4341-bcfd-51c9bfbede57.png">

#### DataNode
<img width="1236" alt="Screen Shot 2021-11-28 at 5 47 56 PM" src="https://user-images.githubusercontent.com/60122319/143799730-7bd2ee90-4494-4475-9cfd-b837d6b05cd6.png">

### 2. Spark
<img width="1267" alt="Screen Shot 2021-11-28 at 5 32 31 PM" src="https://user-images.githubusercontent.com/60122319/143799780-fc751712-48c9-4523-a1eb-3ab9ddf4a649.png">

### 3. Jupyter 
<img width="933" alt="Screen Shot 2021-11-28 at 5 31 48 PM" src="https://user-images.githubusercontent.com/60122319/143799793-2e0dab70-bffe-4bff-92b6-645f8b825341.png">

### 4. SonarQube 
<img width="844" alt="Screen Shot 2021-11-28 at 5 32 04 PM" src="https://user-images.githubusercontent.com/60122319/143799801-f39636ca-99b5-432b-810d-2ec15a2ae4b8.png">



