# Components

![Alt text](./images/components.png)


This document explains the architecture of the CryptApp system, which is designed to handle the collection and processing of cryptocurrency data. The application uses modern technologies such as **FastAPI**, **Redis**, **Celery**, and **Gunicorn** to offer a scalable and efficient service. Below is a detailed explanation of each component in the diagram.


### 1. **Users**

Users interact with the CryptApp application via HTTP requests. These users can be end clients or other systems/services that consume the API to retrieve cryptocurrency data.

### 2. **CryptApp (FastAPI and Gunicorn)**

- **FastAPI**: A Python web framework used to build the API for CryptApp. FastAPI is known for its high performance and ease of use, allowing developers to quickly create RESTful APIs.

- **Gunicorn**: A WSGI (Web Server Gateway Interface) server that serves the FastAPI application. Gunicorn handles concurrency, allowing CryptApp to manage multiple requests simultaneously, thereby improving the system's performance and responsiveness.

### 3. **Cache (Redis)**

Redis acts as the caching system in the CryptApp architecture. Its primary purpose is to enhance the application's response time by storing temporary data that can be accessed quickly. Common use cases include:

- Temporary storage of frequently accessed cryptocurrency data.
- Caching API responses to reduce server load and decrease user wait times.

### 4. **Task Queue (Celery and Redis)**

The application utilizes **Celery** for managing asynchronous background tasks, allowing CryptApp to handle long-running and complex processes without blocking the main execution of the API. Redis is also used here as a message broker, managing the task queue.

- **Celery**: A distributed task queue system that enables asynchronous execution of tasks. In this context, Celery schedules and dispatches tasks to workers for processing.

- **Redis**: Besides its role as a cache, Redis acts as the broker for Celery, storing and managing tasks that need to be processed by workers.

#### Example of Tasks

- `CollectProcessCryptos`: A scheduled task that might be responsible for collecting cryptocurrency data from external sources, processing it, and storing it for future use.

### 5. **Workers**

Workers are components of the system that execute background tasks. In this architecture, workers can perform different types of processing:

- **ETL (Extract, Transform, Load)**: This process involves extracting data from various sources, transforming it into a usable format, and loading it into a database or file system.

- **Worker**: Generic workers that handle various tasks assigned by Celery. These workers consume tasks from the queue and process them according to the system's requirements.

## Data Flow

1. **User Interaction**: 
   - Users send requests to the CryptApp API via HTTP.
   - The requests are handled by Gunicorn, which routes them to the FastAPI application.

2. **CryptApp Processing**:
   - The FastAPI application processes user requests, interacting with Redis for caching purposes to improve performance.
   - If a request requires data processing or retrieval from external sources, CryptApp may trigger a task in Celery.

3. **Task Queue**:
   - Celery manages tasks that need to be processed in the background. These tasks are queued in Redis, which acts as a broker.
   - Tasks like `CollectProcessCryptos` are sent to workers for execution.

4. **Workers**:
   - Workers pick up tasks from the Redis queue and execute them asynchronously.
   - Tasks can include data extraction, transformation, or any other background processing required by the application.

5. **Cache and Response**:
   - Processed data can be cached in Redis for quick access in future requests.
   - FastAPI sends the response back to the user, completing the request cycle.

## Conclusion

This architecture provides a robust and efficient way to handle high-volume data processing and API interactions, leveraging FastAPI for performance, Redis for caching and task queuing, and Celery for asynchronous task management. This setup allows CryptApp to scale effectively and handle complex tasks without affecting the user experience.
