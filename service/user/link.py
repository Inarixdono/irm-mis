from sqlmodel import SQLModel, Field


class UserRoleLink(SQLModel, table=True):
    __tablename__ = "user_role"

    user_id: int = Field(foreign_key="user.id", primary_key=True)
    role_id: int = Field(foreign_key="role.id", primary_key=True)


class UserDepartmentLink(SQLModel, table=True):
    __tablename__ = "user_department"

    user_id: int = Field(foreign_key="user.id", primary_key=True, unique=True)
    department_id: int = Field(foreign_key="department.id", primary_key=True)
