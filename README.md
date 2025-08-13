# FastAPI JWT Auth Blog

A secure Blog API built with **FastAPI** and **JWT authentication**.  
Users can **register**, **log in**, and perform **CRUD operations** on blog posts, with JWT protecting private routes.

---

## Deployment
The apis app is deployed and can be accessed at:  
[https://fastapi-jwt-auth-blog.onrender.com](https://fastapi-jwt-auth-blog.onrender.com/docs)


## Features
- User registration & login with JWT authentication
- Create, read, update, delete blog posts
- Built with **FastAPI** for high performance

---

## Installation & Setup

#### Create a virtual environment
```
python -m venv venv
```
#### Activate the virtual environment
##### Windows
```
venv\Scripts\activate
```
##### Mac/Linux
```
source venv/bin/activate
```

#### Install dependencies
```
pip install -r requirements.txt
```
#### Run the FastAPI server
```
uvicorn main:app --reload
```
### Clone the Repository

```bash
git clone https://github.com/yourusername/fastapi-jwt-auth-blog.git

cd fastapi-jwt-auth-blog

```
## API Documentation
#### Once the server is running, visit:
```
Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc
```

### License
#### This project is licensed under the MIT License.
