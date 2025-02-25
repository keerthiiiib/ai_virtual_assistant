# 🔦 AI Virtual Assistant (FastAPI)  

Hey there! 👋 This is a simple AI Virtual Assistant backend built with **FastAPI**. It takes text input (simulating voice), processes it using basic **NLP intent recognition**, and responds accordingly.  

## 🚀 Features  
✅ **FastAPI-powered API** – Super fast & lightweight  
✅ **Basic NLP Processing** – Keyword-based intent recognition  
✅ **Docker Support** – Easy to containerize & deploy  
✅ **MongoDB Integration**  

---

## 🛠️ Setup Instructions  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/keerthiiiib/ai_virtual_assistant.git
cd ai_virtual_assistant
```

### 2️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Server  
```bash
uvicorn main:app --reload
```
🔗 API will be live at: **http://127.0.0.1:8000**  
📝 Explore endpoints in **Swagger UI**: **http://127.0.0.1:8000/docs**  

---

## 🐫 Docker Deployment 

If you want to run this inside a **Docker container**, follow these steps:  

### 1️⃣ Build the Docker Image  
```bash
docker build -t ai_virtual_assistant .
```

### 2️⃣ Run the Container  
```bash
docker run -p 8000:8000 ai_virtual_assistant
```
Now, visit **http://localhost:8000/docs** to test the API inside Docker! 🎉  

---

## 📹 Demo Video (Required for Submission)  
🎥 **Watch a quick demo here:** [Demo Video](https://youtu.be/example) *(replace with your actual link)*  

---

