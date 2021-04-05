# Project 4: Serverless Data Engineering Pipeline
- Reproduce the architecture of the example serverless data engineering project.
- Enhance the project by extending the functionality of the NLP analysis: adding entity extraction, key phrase extraction, or some other NLP feature.

# Reference
https://www.youtube.com/watch?v=zXxdbtamoa4

# Takeaways
- I recommend, in advance, creating resources, such as Dynamo DB, S3, SQS, and IAM role to make debug process easir.
- From the AWS icon in cloud9 IDE, I can create "SAM lambda application," and the directory whose name corresponds to the lambda function is created.
- After creating the lambda function based on the guidance, can modify the app.py in that directory.
- Then, can build the application as a container and deploy it using the command below.
```command
sam build --use-container
sam deploy --guided
```
  - I failed to build "producer" several times because of a lack of enough storage space. Check the room in the environment.
- I could confirm the deployed functions in "AWS Lambda". On this page, I could change their roles and set triggers.
