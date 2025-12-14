

## 1) What this project does (User Flow)

This project is a **minimal Notes API** designed to demonstrate core cloud architecture concepts rather than UI polish.

**User Flow:**

1. A client (browser or curl) sends a request to the application.
2. NGINX acts as a reverse proxy and forwards traffic to the Flask API.
3. The Flask API handles requests:

   * **POST /notes** → creates a note (write path)
   * **GET /notes** → retrieves all notes (read path)
4. Notes are stored in application memory (used to validate end-to-end cloud flow).

This proves compute, networking, containerization, and API functionality working together.

---

## 2) Architecture

### High-Level Architecture Diagram (Conceptual)

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

### Architecture Components

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

## 3) API Usage

### Create a Note (WRITE)

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
