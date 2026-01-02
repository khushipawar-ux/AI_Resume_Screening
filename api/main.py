from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import jd_routes, resume_routes, ranking_routes

app = FastAPI(title="AI Resume Screening API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(jd_routes.router)
app.include_router(resume_routes.router)
app.include_router(ranking_routes.router)

@app.get("/")
def read_root():
    return {"message": "AI Resume Screening API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
