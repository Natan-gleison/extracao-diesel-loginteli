import pandas as pd

from config import (
    UNIDADES,
    SEMANAS,
    PRODUTO
)

from extractor import LoginteliExtractor
from database import DatabaseManager
from logger import logger


def main():

    logger.info(
        "Iniciando processo"
    )

    extractor = LoginteliExtractor()

    df_unidades = pd.DataFrame(
        UNIDADES
    )

    estados = (
        df_unidades["ESTADO"]
        .drop_duplicates()
        .tolist()
    )

    registros = []

    for dt_ini, dt_fim in SEMANAS:

        for estado in estados:

            try:

                logger.info(
                    f"Consultando {estado}"
                )

                registro = (
                    extractor.buscar_diesel(
                        estado,
                        dt_ini,
                        dt_fim,
                        PRODUTO
                    )
                )

                registros.append(
                    registro
                )

            except Exception as e:

                logger.error(
                    f"Erro {estado}: {e}"
                )

    df_preco = pd.DataFrame(
        registros
    )

    df_final = df_preco.merge(
        df_unidades,
        on="ESTADO",
        how="inner"
    )

    db = DatabaseManager()

    db.salvar(
        df_final
    )

    logger.info(
        f"{len(df_final)} registros gravados"
    )

    print(
        "Carga concluída."
    )


if __name__ == "__main__":
    main()