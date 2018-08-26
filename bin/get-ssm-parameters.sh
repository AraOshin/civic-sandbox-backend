#! /bin/bash

# Pulls in HackO API env var values as parameters from AWS Parameter Store
# Depends on pre-installed awscli

# Modelled on https://aws.amazon.com/blogs/compute/managing-secrets-for-amazon-ecs-applications-using-parameter-store-and-iam-roles-for-tasks/

EC2_REGION="us-west-2" # unfortunately cannot rely on dynamic env var values that this script is meant to pull in
NAMESPACE="/production/2018/API" # future-proofing this script for subsequent or past containers
PROJECT_CANONICAL_NAME="civic_sandbox" # must be set to each project's "Final naming convention" from here https://github.com/hackoregon/civic-devops/issues/1

# Get unencrypted values
NEIGHBORHOOD_DEVELOPMENT_18_POSTGRES_HOST=`aws ssm get-parameters --names "$NAMESPACE"/"$PROJECT_CANONICAL_NAME"/NEIGHBORHOOD_DEVELOPMENT_18_POSTGRES_HOST --no-with-decryption --region $EC2_REGION --output text | awk '{print $4}'`
NEIGHBORHOOD_DEVELOPMENT_18_POSTGRES_NAME=`aws ssm get-parameters --names "$NAMESPACE"/"$PROJECT_CANONICAL_NAME"/NEIGHBORHOOD_DEVELOPMENT_18_POSTGRES_NAME --no-with-decryption --region $EC2_REGION --output text | awk '{print $4}'`
NEIGHBORHOOD_DEVELOPMENT_18_POSTGRES_PORT=`aws ssm get-parameters --names "$NAMESPACE"/"$PROJECT_CANONICAL_NAME"/NEIGHBORHOOD_DEVELOPMENT_18_POSTGRES_PORT --no-with-decryption --region $EC2_REGION --output text | awk '{print $4}'`
NEIGHBORHOOD_DEVELOPMENT_18_POSTGRES_USER=`aws ssm get-parameters --names "$NAMESPACE"/"$PROJECT_CANONICAL_NAME"/NEIGHBORHOOD_DEVELOPMENT_18_POSTGRES_USER --no-with-decryption --region $EC2_REGION --output text | awk '{print $4}'`


TRANSPORTATION_SYSTEMS_18_POSTGRES_HOST=`aws ssm get-parameters --names "$NAMESPACE"/"$PROJECT_CANONICAL_NAME"/TRANSPORTATION_SYSTEMS_18_POSTGRES_HOST --no-with-decryption --region $EC2_REGION --output text | awk '{print $4}'`
TRANSPORTATION_SYSTEMS_18_POSTGRES_NAME=`aws ssm get-parameters --names "$NAMESPACE"/"$PROJECT_CANONICAL_NAME"/TRANSPORTATION_SYSTEMS_18_POSTGRES_NAME --no-with-decryption --region $EC2_REGION --output text | awk '{print $4}'`
TRANSPORTATION_SYSTEMS_18_POSTGRES_PORT=`aws ssm get-parameters --names "$NAMESPACE"/"$PROJECT_CANONICAL_NAME"/TRANSPORTATION_SYSTEMS_18_POSTGRES_PORT --no-with-decryption --region $EC2_REGION --output text | awk '{print $4}'`
TRANSPORTATION_SYSTEMS_18_POSTGRES_USER=`aws ssm get-parameters --names "$NAMESPACE"/"$PROJECT_CANONICAL_NAME"/TRANSPORTATION_SYSTEMS_18_POSTGRES_USER --no-with-decryption --region $EC2_REGION --output text | awk '{print $4}'`


DISASTER_RESILIENCE_18_POSTGRES_HOST=`aws ssm get-parameters --names "$NAMESPACE"/"$PROJECT_CANONICAL_NAME"/DISASTER_RESILIENCE_18_POSTGRES_HOST --no-with-decryption --region $EC2_REGION --output text | awk '{print $4}'`
DISASTER_RESILIENCE_18_POSTGRES_NAME=`aws ssm get-parameters --names "$NAMESPACE"/"$PROJECT_CANONICAL_NAME"/DISASTER_RESILIENCE_18_POSTGRES_NAME --no-with-decryption --region $EC2_REGION --output text | awk '{print $4}'`
DISASTER_RESILIENCE_18_POSTGRES_PORT=`aws ssm get-parameters --names "$NAMESPACE"/"$PROJECT_CANONICAL_NAME"/DISASTER_RESILIENCE_18_POSTGRES_PORT --no-with-decryption --region $EC2_REGION --output text | awk '{print $4}'`
DISASTER_RESILIENCE_18_POSTGRES_USER=`aws ssm get-parameters --names "$NAMESPACE"/"$PROJECT_CANONICAL_NAME"/DISASTER_RESILIENCE_18_POSTGRES_USER --no-with-decryption --region $EC2_REGION --output text | awk '{print $4}'`

# Note: this env var value is for the WSGI startup - corresponds to the folder name where the base Django project is stored in the repo
PROJECT_NAME=`aws ssm get-parameters --names "$NAMESPACE"/"$PROJECT_CANONICAL_NAME"/PROJECT_NAME --no-with-decryption --region $EC2_REGION --output text | awk '{print $4}'`

# Get encrypted values
DJANGO_SECRET_KEY=`aws ssm get-parameters --names "$NAMESPACE"/"$PROJECT_CANONICAL_NAME"/DJANGO_SECRET_KEY --with-decryption --region $EC2_REGION --output text | awk '{print $4}'`
NEIGHBORHOOD_DEVELOPMENT_18_POSTGRES_PASSWORD=`aws ssm get-parameters --names "$NAMESPACE"/"$PROJECT_CANONICAL_NAME"/NEIGHBORHOOD_DEVELOPMENT_18_POSTGRES_PASSWORD --with-decryption --region $EC2_REGION --output text | awk '{print $4}'`
TRANSPORTATION_SYSTEMS_18_POSTGRES_PASSWORD=`aws ssm get-parameters --names "$NAMESPACE"/"$PROJECT_CANONICAL_NAME"/TRANSPORTATION_SYSTEMS_18_POSTGRES_PASSWORD --with-decryption --region $EC2_REGION --output text | awk '{print $4}'`
DISASTER_RESILIENCE_18_POSTGRES_PASSWORD=`aws ssm get-parameters --names "$NAMESPACE"/"$PROJECT_CANONICAL_NAME"/DISASTER_RESILIENCE_18_POSTGRES_PASSWORD --with-decryption --region $EC2_REGION --output text | awk '{print $4}'`

# Set environment variables in the container
export DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY
export PROJECT_NAME=$PROJECT_NAME
export POSTGRES_PORT=$POSTGRES_PORT

export NEIGHBORHOOD_DEVELOPMENT_18_POSTGRES_HOST=$NEIGHBORHOOD_DEVELOPMENT_18_POSTGRES_HOST
export NEIGHBORHOOD_DEVELOPMENT_18_POSTGRES_NAME=$NEIGHBORHOOD_DEVELOPMENT_18_POSTGRES_NAME
export NEIGHBORHOOD_DEVELOPMENT_18_POSTGRES_PASSWORD=$NEIGHBORHOOD_DEVELOPMENT_18_POSTGRES_PASSWORD
export NEIGHBORHOOD_DEVELOPMENT_18_POSTGRES_USER=$NEIGHBORHOOD_DEVELOPMENT_18_POSTGRES_USER


export TRANSPORTATION_SYSTEMS_18_POSTGRES_HOST=$TRANSPORTATION_SYSTEMS_18_POSTGRES_HOST
export TRANSPORTATION_SYSTEMS_18_POSTGRES_NAME=$TRANSPORTATION_SYSTEMS_18_POSTGRES_NAME
export TRANSPORTATION_SYSTEMS_18_POSTGRES_PASSWORD=$TRANSPORTATION_SYSTEMS_18_POSTGRES_PASSWORD
export TRANSPORTATION_SYSTEMS_18_POSTGRES_USER=$TRANSPORTATION_SYSTEMS_18_POSTGRES_USER


export DISASTER_RESILIENCE_18_POSTGRES_HOST=$DISASTER_RESILIENCE_18_POSTGRES_HOST
export DISASTER_RESILIENCE_18_POSTGRES_NAME=$DISASTER_RESILIENCE_18_POSTGRES_NAME
export DISASTER_RESILIENCE_18_POSTGRES_PASSWORD=$DISASTER_RESILIENCE_18_POSTGRES_PASSWORD
export DISASTER_RESILIENCE_18_POSTGRES_USER=$DISASTER_RESILIENCE_18_POSTGRES_USER