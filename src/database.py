from sqlalchemy import create_engine
import pandas as pd

class DatabaseManager:

    def __init__(self):

        self.engine = create_engine(
            "sqlite:///data/diesel.db"
        )

    def salvar(self, dataframe):

        dataframe.to_sql(
            "tb_preco_diesel",
            self.engine,
            if_exists="replace",
            index=False
        )