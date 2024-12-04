from core.database import SessionDependency, SQLModel
from sqlmodel import select

class CRUD:
    def __init__(self, session: SessionDependency):
        self.session = session
        
    def read(self, base_model: SQLModel, id: int):
        statement = select(base_model).where(base_model.id == id)
        return self.session.exec(statement).first()
    
    def read_all(self, base_model: SQLModel):
        statement = select(base_model)
        return self.session.exec(statement).all()
        
    def create(self, base_model: SQLModel, model_in: SQLModel):
        resource = base_model(**model_in.model_dump())
        self.session.add(resource)
        self.session.commit()
        self.session.refresh(resource)
        return resource
    
    def update(self, id: int, base_model: SQLModel, model_in: SQLModel):
        resource = self.session.get(base_model, id)
        resource_data = model_in.model_dump(exclude_unset=True)
        resource.sqlmodel_update(resource_data)
        self.session.add(resource)
        self.session.commit()
        self.session.refresh(resource)
        return resource
