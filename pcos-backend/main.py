from fastapi import FastAPI, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from datetime import date
from models import Base, SymptomLog

# FastAPI app
app = FastAPI()

# Database setup
DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- API Routes ---
@app.post("/logs/")
def create_log(cycle_length: int, acne: str, mood: str, weight: float, db: Session = Depends(get_db)):
    log = SymptomLog(
        date=str(date.today()),
        cycle_length=cycle_length,
        acne=acne,
        mood=mood,
        weight=weight
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return {"message": "✅ Log saved!", "id": log.id}

@app.get("/logs/")
def get_logs(db: Session = Depends(get_db)):
    logs = db.query(SymptomLog).all()
    return logs
