from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infra.configs.base import Base


class Registration(Base):
    """registrations table definition."""

    __tablename__ = "registrations"

    id_student: Mapped[int] = mapped_column(
        ForeignKey("students.id_student"), primary_key=True
    )
    id_course: Mapped[int] = mapped_column(
        ForeignKey("courses.id_course"), primary_key=True
    )

    course = relationship("Course", back_populates="registration", lazy="subquery")
    student = relationship(
        "Student", uselist=False, back_populates="registration", lazy="subquery"
    )

    def __repr__(self) -> str:
        return (
            f"Registration (id_student={self.id_student}, id_course={self.id_course})"
        )
