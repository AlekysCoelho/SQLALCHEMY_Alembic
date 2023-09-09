from typing import Optional, Set

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infra.configs.base import Base
from infra.entities import Course as tb_course


class Teacher(Base):
    """teachers table definition"""

    __tablename__ = "teachers"

    id_teacher: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    fullname: Mapped[Optional[str]]
    cpf: Mapped[str] = mapped_column(String(11), nullable=False)

    courses: Mapped[Set["tb_course"]] = relationship(back_populates="teacher")

    def __repr__(self) -> str:
        return f"Teacher (id={self.id_teacher}, name={self.name})"
