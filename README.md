# Notification Service
- Simple [Python] notification service, used to send push notification and sms.
- Here I have used two external platforms Twilio to send sms and Firebase Cloud Messaging "FCM" for the push notifications.
## About
```
    * Simple application support service container to be simple as possible.
    * Also, has a simple integration with multiple platforms "Twilio and FCM".
    * Also, application has two services "Producer and Consumer" so, application
        contains a simple queueing technique manage communication between two services.
    * Code supports configurability rather than hard-coding to achieve the simplicity and readability.
    * Each service has it's own dockerfile and application has docker-compose
        file contains multiple services.
```
## Getting Started
These instructions will make the project up and running on your local machine for development purposes.
### Prerequisites
* Docker 19.03.5
* Docker Compose 1.23.1
### Setup
* Dive into notification-service directory.
```
    $ cd notification-service
```
* Copy .env.example to .env file.
```
    $ cp .env.example .env
```
* Update apps keys into .env file used into integration with external platforms.
* Run docker-compose.yml file.
```
    $ docker-compose up -d --build
```
### Containers created and their ports are as follows:
* Main-service "Producer" :8080
* MongoDB :27018
* RabbitMQ :5672
## Built With
* [Python3](https://www.python.org/doc/)
* [RabbitMQ](https://www.rabbitmq.com/documentation.html)
* [MongoDB](https://docs.mongodb.com/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Twilio](https://www.twilio.com/)
* [Firebase Cloud Messaging "FCM"](https://firebase.google.com/docs/cloud-messaging)
* [Docker](https://docs.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)
## Running Service Tests
```
    $ docker-compose exec app sh -c "python -m unittest discover -s . -p '*_test.py'"
    $ docker-compose exec notification_consumer sh -c "python -m unittest discover -s . -p '*_test.py'"
```
## Endpoints
```
    * A [POST] api used to create group contains multiple users.
    * A [POST] api used to create bulk of users without any groups.
    * A [POST] api used to update user device token "FCM token used for push notification".
    * A [POST] api used to create notification for group or single user.
```
## Calling Endpoint
#### Create Group Endpoint
* API Endpoint
```
   [POST] http://127.0.0.1:8000/groups
```
* Request Headers
```
    'Accept' => 'application/json'
```
* Request Body
```
    {
        "name": "Test Group",
        "users": [
            {"name": "Example 2", "phone": "+20111111111", "fcm_token": ""},
            {"name": "Example 1", "phone": "+20222222222", "fcm_token": ""}
        ]
    }
```
* Response sample
```
    {
        "status": true, 
        "group_id": "6019e7f979b3130006f60ef5"
    }
```
#### Update User FCM Token Endpoint
* API Endpoint
```
   [POST] http://127.0.0.1:8000/user/update-fcm-token
```
* Request Headers
```
    'Accept' => 'application/json'
```
* Request Body
```
    {
        "phone": "+20111111111",
        "fcm_token": "FCM TOKEN GENERATED INTO WEB FOR TESTING CAUSE I DON'T HAVE OTHER DEVICES"
    }
```
* Response sample
```
    {
        "updated": true,
         "message": "User updated successfully"
    }
```
#### Create Notification Endpoint
* API Endpoint
```
   [POST] http://127.0.0.1:8000/notifications
```
* Request Headers
```
    'Accept' => 'application/json'
```
* Request Body
```
    {
        "title": "notification example 1",
        "body": " notification body example 1",
        "group_id": "",
        "user": "+20111111111",
        "provider": "SMS" OR "FCM"
    }
```
* Response sample
```
    {
        "created": true, 
        "published": true, 
        "notification_id": "6019ef77d116e40006768f11"
    }
```
## Service Challenges
* Handling external services down "External integrated systems exceptions such as rate limit exceeded"
* I couldn't send or receive notifications with multiple users "devices" using FCM, 
    I made a tricky and already implemented scenario to 
    generate a web device token to use it into the FCM push notification.
## Features
* Service container.
* Apply adequate design patterns.
* Applying simple design principles.
* Apply simple queueing technique manage communication between services.
* Scalable system design.
* Apply simple request validation using FastAPI validator and Models schema.
* Implement simple integration with FCM and Twilio.
* Simple handling for services down or rate-limit exceeded exception by retrying pushing notification.
* Implement some simple test cases.
## Applied Design Patterns
* Factory Design Pattern.
* Strategy Design Pattern.
* Repository Design Pattern.
* Dependency Injection.
## Missing Features
* Apply centralized logging and monitoring system.
* Sending notification via emails and support multiple email platforms "Email Service".
* Apply a simple web interface helps us into creating groups and sending notifications.
* ADD more test cases.