from sqlalchemy import insert, create_engine, Engine
from .bot_templates.feedback.database.models import Task


class BotDataBase:
    def __init__(self, bot_token) -> None:
        self.engine: Engine = create_engine(
            url=f"sqlite:///bot/user_bots/{bot_token.split(':')[0]}/database/db.sqlite3",
            echo=False
        )

    def add_task(self, data):
        with self.engine.begin() as session:
            stmt = (
                insert(Task).
                values(
                    type=data['type'],
                    message=data['message'] if data.get('message') else None,
                    command=data['command'] if data.get('command') else None,
                    new_response=data['new_response'] if data.get('new_response') else None
                )
            )
            session.execute(stmt)
            session.commit()