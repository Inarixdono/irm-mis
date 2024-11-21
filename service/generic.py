from core.database import SessionDependency, SQLModel

class Generic:
    def __init__(self, session: SessionDependency):
        self.session = session
        
    def create(self, BaseModel: SQLModel, model_in: SQLModel):
        resource = BaseModel(**model_in.model_dump())
        self.session.add(resource)
        self.session.commit()
        self.session.refresh(resource)
        return resource
