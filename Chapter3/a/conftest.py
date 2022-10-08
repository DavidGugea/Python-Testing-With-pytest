import pytest
import cards

from pathlib import Path
from tempfile import TemporaryDirectory


@pytest.fixture(scope="session")
def cards_db():
    """CardDB object connected to a temporary database"""
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db
        db.close()