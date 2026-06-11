# AWS Serverless API Lab

## Overview

This project demonstrates how to build and test a serverless API using AWS Lambda, API Gateway, CloudWatch Logs, Python, and Node.js.

The application uses API Gateway to route HTTP requests to separate Lambda functions written in Python and Node.js. CloudWatch Logs were used to validate successful execution and troubleshoot issues during development.

---

## What Did I Build?

I built a simple serverless API that exposes two endpoints through Amazon API Gateway:

* `/python` → Invokes a Python Lambda function
* `/node` → Invokes a Node.js Lambda function

Each Lambda function processes incoming requests and returns a JSON response. CloudWatch Logs capture execution details and provide visibility into function behavior.

---

## Why Did I Build It?

The purpose of this lab was to gain hands-on experience with AWS serverless services and understand how API Gateway interacts with Lambda functions.

This project helped me learn:

* How API Gateway routes requests to Lambda functions
* How Lambda functions process event data
* How to test API endpoints
* How to use CloudWatch Logs for monitoring and troubleshooting
* Differences between Python and Node.js Lambda implementations

---

## Architecture

Client Request

↓

Amazon API Gateway

↓

├── GET /python → Python Lambda Function

└── GET /node → Node.js Lambda Function

↓

Amazon CloudWatch Logs

---

## Technologies Used

* AWS Lambda
* Amazon API Gateway
* Amazon CloudWatch
* Python
* Node.js
* JSON

---

## Testing and Validation

The API was tested by invoking both endpoints through API Gateway.

Example Python Response:

```json
{
  "message": "Hello Ted from Python!",
  "timestamp": "2026-04-29T04:57:17.998254+00:00"
}
```

Example Node.js Response:

```json
{
  "message": "HELLO TED FROM NODE!"
}
```

Successful execution was verified through CloudWatch Logs and Lambda invocation records.

---

## Challenges Encountered

### 1. Node.js Runtime Error

While testing the Node.js Lambda function, I encountered an `exports is not defined` error.

#### Resolution

I updated the code to use the proper module syntax required by the Node.js runtime and redeployed the function.

---

### 2. Query Parameters Not Passing Correctly

Initial API Gateway requests were not forwarding parameters to the Lambda functions as expected.

#### Resolution

I reviewed the API Gateway integration settings and enabled proxy integration so request data would be passed through correctly.

---

### 3. Verifying Lambda Execution

When requests did not return the expected output, it was difficult to determine where the issue occurred.

#### Resolution

I used CloudWatch Logs to inspect incoming events, validate execution flow, and identify configuration issues.

---

## What I Learned

Through this project I learned how to:

* Build and test serverless APIs using AWS services
* Connect API Gateway routes to Lambda functions
* Process incoming event data within Lambda
* Use CloudWatch Logs for troubleshooting and monitoring
* Debug API Gateway and Lambda integration issues
* Deploy and test both Python and Node.js serverless functions

This project strengthened my understanding of event-driven and serverless application architectures in AWS.

---

## Screenshots

The repository includes screenshots showing:

* API Gateway creation
* Python route success
* Node route success
* Lambda invocation results
* CloudWatch Log Groups
* Successful CloudWatch executions

These screenshots provide evidence of successful deployment and testing of the serverless application.
