from typing import Any

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infra.configs.base import Base


class Course(Base):
    """courses table definition."""

    __tablename__ = "courses"

    id_course: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    codigo: Mapped[str] = mapped_column(String(3), nullable=False)
    id_teacher: Mapped[int] = mapped_column(ForeignKey("teachers.id_teacher"))

    teacher = relationship("Teacher", uselist=False, back_populates="courses", lazy="subquery")

    def __repr__(self) -> str:
        return f"Course (id={self.id_course}, course={self.name})"
