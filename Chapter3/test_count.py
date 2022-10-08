import pytest
import cards

from pathlib import Path
from tempfile import TemporaryDirectory


@pytest.fixture()
def cards_db():
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)

        yield db
        db.close()


def test_empty(cards_db):
    assert cards_db.count() == 0
