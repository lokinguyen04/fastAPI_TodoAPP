from database import engine
from models import Todos  # This is important to import so SQLAlchemy knows about the model
from database import Base

# Create tables
Base.metadata.create_all(bind=engine)

print("Todos table created successfully.")