"""Defines the schema and relationships of the database objects.

For more information, see https://docs.sqlalchemy.org/en/20/tutorial/metadata.html
"""

import enum
from datetime import UTC, datetime
from uuid import uuid4

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    MetaData,
    String,
    Table,
    UniqueConstraint,
    Uuid,
)
from sqlalchemy import (
    Enum as SqlEnum,
)


class Tier(enum.Enum):
    """Tier of an organization."""

    Basic = enum.auto()
    Pro = enum.auto()
    Enterprise = enum.auto()


class Role(enum.Enum):
    """Role of a user's membership in an organization."""

    User = enum.auto()
    Admin = enum.auto()


_metadata_obj = MetaData(schema="main")

organization = Table(
    "organization",
    _metadata_obj,
    Column("id", Uuid, primary_key=True, default=uuid4),
    Column("tier", SqlEnum(Tier), nullable=False, default=Tier.Basic),
    Column(
        "created",
        DateTime(timezone=True),
        nullable=False,
        default=datetime.now(tz=UTC),
    ),
    Column("name", String(100), nullable=False),
    Column("prefix", String(4), nullable=False, unique=True),
)

user = Table(
    "user",
    _metadata_obj,
    Column("id", Uuid, primary_key=True, default=uuid4),
    Column(
        "created",
        DateTime(timezone=True),
        nullable=False,
        default=datetime.now(tz=UTC),
    ),
    Column("name", String(100), nullable=False),
    Column("email", String(100), nullable=False, unique=True),
    Column("active", Boolean, nullable=False, default=True),
)

membership = Table(
    "membership",
    _metadata_obj,
    Column("id", Uuid, primary_key=True, default=uuid4),
    Column(
        "created",
        DateTime(timezone=True),
        nullable=False,
        default=datetime.now(tz=UTC),
    ),
    Column("org_id", Uuid, ForeignKey("organization.id"), nullable=False),
    Column("user_id", Uuid, ForeignKey("user.id"), nullable=False),
    Column("role", SqlEnum(Role), nullable=False, default=Role.User),
    UniqueConstraint("org_id", "user_id", name="u_membership"),
)


def init_schema(binding):
    """Emits DDL statements to the given engine or connection to drop and re-create all database objects."""
    _metadata_obj.drop_all(binding)
    _metadata_obj.create_all(binding)
