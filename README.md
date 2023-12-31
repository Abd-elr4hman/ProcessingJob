# ProcessingJob
This porject illustrates a machine learning training pipeline. The main focus is the MLOPS Practices like Workflow Orchestration, Experiment tracking, Model versioning.
![image](https://github.com/Abd-elr4hman/ProcessingJob/assets/87248009/26f107c3-0df3-48fe-a0e2-a09c86294e05)




the project is split into 3 repositories:
* Processing job repo: This one.
* Training job repo: [here](https://github.com/Abd-elr4hman/TrainingJob)
* Orchestration repo: [here](https://github.com/Abd-elr4hman/ML-Training-Pipeline).
# To Do:
### Data Processing:
* [x] Process MNIST Raw dataset.
* [x] Define a SageMaker Processing Job.
* [x] Build a docker container to use with SageMaker,
* [x] Automate testing, building and pushing docker container to AWS ECR with github workflows.
### Model Training:
* [x] Use Tensorflow to train Mnist classification model.
* [x] Create a SageMaker Training Job using SageMaker Tensorflow deeplearning container.
### Experiment Tracking, Model versioning:
* [x] Perform Experiment tracking, model logging with MLflow, RDS Postgres db and S3.
### Orchestration:
* [x] Orchestrate the training process with AWS Step-functions.
