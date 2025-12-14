 1) What this project does (User Flow)

minimal Notes API.

**User Flow:**

1. A client (browser or curl) sends a request to the application.
2. NGINX acts as a reverse proxy and forwards traffic to the Flask API.
3. The Flask API handles requests:

   * **POST /notes** → creates a note (write path)
   * **GET /notes** → retrieves all notes (read path)
4. Notes are stored in application memory (used to validate end-to-end cloud flow).

This proves compute, networking, containerization, and API functionality working together.

---

 2) Architecture

 High-Level Architecture Diagram (Conceptual)

```
Client (Browser / curl)
        |
        v
     NGINX (Port 8080)
        |
        v
   Flask API (Docker Container, Port 5000)
        |
        v
   In-Memory Notes Store
```
 Architecture Components

* **Compute**

  * Docker containers
  * Flask application (simulates ECS container workload)

* **Networking**

  * NGINX reverse proxy
  * Port mapping: `8080 → 5000`
  * Docker bridge network (local equivalent of VPC networking)

* **IAM & Secrets**

  * No hard-coded secrets
  * Environment-based configuration (AWS equivalent: IAM Task Roles + Secrets Manager)

---

 3) API Usage

 Create a Note (WRITE)

```bash
curl -X POST http://localhost:8080/notes \
-H "Content-Type: application/json" \
-d '{"text":"My first cloud note"}'
```

**Response:**

```json
{"message":"Note added"}
```

---

### Read Notes (READ)

```bash
curl http://localhost:8080/notes
```

**Response:**

```json
[
  {"text":"My first cloud note"}
]
```

---

 4) SLO & Monitoring Plan (Design-Level)

**Service Level Objectives (SLOs):**

* 95% of API requests respond within **400 ms**
* Error rate less than **2% over a 5-minute window**

**Monitoring Plan (Planned):**

* Request count
* Error count
* Response latency

**AWS Equivalent Tools:**

* Amazon CloudWatch Metrics
* CloudWatch Alarms

---

 5) How to Run / Deploy

### Prerequisites

* Docker
* Docker Compose

### Run the Application

```bash
docker-compose up --build
```

### Access the App

* API Base URL: `http://localhost:8080`
* Notes endpoint: `http://localhost:8080/notes`

---

## 6) Team & Roles

* **Trikky** — Architecture design, Docker setup, Flask API, documentation

(Individual project)

---

## 7) AI Usage Disclosure

GenAI tools (ChatGPT) were used to:

* Scaffold Flask API structure
* Explain Docker, NGINX, and cloud architecture concepts
* Assist with documentation formatting

**Human Review & Modifications:**

* All generated code was reviewed, corrected, and tested
* Security practices were validated (no secrets committed)
* Application logic and error handling were manually fixed and verified

---

## 8) Real-World Cloud Mapping (AWS)

| Local Component  | AWS Equivalent            |
| ---------------- | ------------------------- |
| Docker container | ECS Task                  |
| Docker Compose   | ECS Service               |
| NGINX            | Application Load Balancer |
| Local ports      | Security Groups           |
| Flask API        | Microservice              |

---

## 9) Summary

This project demonstrates:

* Containerized application deployment
* Reverse proxy networking
* REST API design (write + read)
* Cloud-ready architecture aligned with AWS best practices

