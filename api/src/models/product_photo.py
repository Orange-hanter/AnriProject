import os

from libcloud.storage.drivers.local import LocalStorageDriver
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy_file import ImageField
from sqlalchemy_file.storage import StorageManager

from src.database import Base
from src.models.core_model import CoreModel


class ProductPhoto(Base, CoreModel):
    __tablename__ = "product_photos"

    photo: Mapped[any] = mapped_column(ImageField)


os.makedirs("src/media/attachment", 0o777, exist_ok=True)  # Make sure the directory exist
container = LocalStorageDriver("src/media").get_container("attachment")
StorageManager.add_storage("default", container)
