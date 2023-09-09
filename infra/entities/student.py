from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

import infra.entities
from infra.configs.base import Base


class Student(Base):
    """students table definition."""

    __tablename__ = "students"

    id_student: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    fullname: Mapped[Optional[str]]
    cpf: Mapped[str] = mapped_column(String(11), nullable=False)

    registration: Mapped["infra.entities.Registration()"] = relationship(
        uselist=False, back_populates="courses"
    )

    def __repr__(self) -> str:
        return f"Student (id={self.id_student}, name={self.name}, registration={self.registration})"
