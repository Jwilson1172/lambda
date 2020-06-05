from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    utc_time = db.Column(db.String(128))
    value = db.Column(db.Float)

    def __repr__(self):
        return f"TIME:{self.utc_time}\tAIR_QUALITY[PPM]:{self.value}"
