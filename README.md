# 📝 To-Do List App (Client)

**Developer:** *Udita Maji*

A simple, clean, and fast **Streamlit-based client application** for managing tasks through a dedicated REST API.
The goal? Make task management stupidly easy while keeping the UI lightweight, responsive, and deployable anywhere (Render, Docker, local, whatever you want).

---

## 🚀 Problem Statement

People just *forget stuff* (like… all the time).
Sticky notes fall off, phone reminders get ignored, and not everyone wants a full-blown productivity suite with a 10-step onboarding ritual.

**The problem:**

> There’s no lightweight, distraction-free environment where users can simply add, update, delete, and view tasks without unnecessary features or logins.

So this app solves it by providing:
✔ Fast UI
✔ Zero learning curve
✔ API-powered structure (clean separation of concerns)
✔ Easy integration with any backend

---

## 🎯 Purpose of the Application

This client app is meant to be the **front-end** for a modular To-Do List ecosystem.
It uses **Streamlit** to give a smooth, reactive UI where users can:

* Add a new task
* View all tasks
* Update task status
* Delete tasks
* Talk to a backend server via clean REST endpoints

Basically:
It’s a cute but efficient wrapper that turns raw API routes into a usable interface.

---

## 🧠 Tech Stack

### **Frontend / Client**

* **Python 3.10+**
* **Streamlit** — for building the UI
* **Requests** — to communicate with the backend API
* **Docker** — for containerizing the client
* **Render** (optional) — for deployment

### **Environment + Build**

* `requirements.txt`
* `Dockerfile` (for setting up the container)

---

## 🧱 Code Structure (Typical)

```
client/
│── main.py           # Streamlit UI
│── api.py            # Helper functions to call backend endpoints
│── requirements.txt
│── Dockerfile
│── README.md
```

---

## ⚙️ How It Works

### 1. **Streamlit UI (`main.py`)**

The front-end interface is powered entirely by Streamlit widgets:

* Text input for new tasks
* Buttons for CRUD actions
* Auto-refresh UI after every API call

Streamlit reruns the script on each interaction, which keeps everything reactive and snappy.

---

### 2. **Backend Interaction**

The app communicates with your backend using `requests`:

* `POST /tasks` → Add a task
* `GET /tasks` → Retrieve all tasks
* `PUT /tasks/<id>` → Update a task
* `DELETE /tasks/<id>` → Delete a task

The client doesn't store anything itself — everything lives in the backend.
That makes the app scalable and easy to upgrade later.

---

## 🐳 Running with Docker

### **1. Build the Docker image**

```bash
docker build -t todo-client .
```

### **2. Run the container**

```bash
docker run -p 8501:8501 todo-client
```

### Streamlit will be live at:

```
http://localhost:8501
```

---

## 🛠️ Local Development Setup

### Clone the repo:

```bash
git clone <repo-url>
cd client
```

### Create a virtual environment:

```bash
python -m venv venv
```

### Activate it:

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install dependencies:

```bash
pip install -r requirements.txt
```

### Run the client:

```bash
streamlit run main.py
```

---

## 📦 Deployment (Render)

Just push your Dockerfile-based project — Render builds it automatically.
Make sure your Dockerfile ends with:

```
CMD ["streamlit", "run", "main.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
```

---

## 💡 Future Upgrades

* User authentication
* Dark mode UI
* Database-side pagination
* Notifications
* Multi-device syncing
* Categories / tags for tasks

---

## 👩‍💻 Developer

**Udita Maji**
Python developer, full-stack explorer, and the brain behind this to-do app.

---

