from core.database import SessionDependency, SQLModel

class CRUD:
    def __init__(self, session: SessionDependency):
        self.session = session
        
    def create(self, base_model: SQLModel, model_in: SQLModel):
        resource = base_model(**model_in.model_dump())
        self.session.add(resource)
        self.session.commit()
        self.session.refresh(resource)
        return resource
