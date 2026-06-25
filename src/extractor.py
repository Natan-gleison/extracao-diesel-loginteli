import re
import requests

from tenacity import retry
from tenacity import stop_after_attempt
from tenacity import wait_fixed

from datetime import datetime

class LoginteliExtractor:

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_fixed(5)
    )
    def buscar_diesel(
        self,
        estado,
        dt_ini,
        dt_fim,
        produto
    ):

        url = (
            "https://www.loginteli.com.br/"
            f"?abrangencia=estado"
            f"&local={estado}"
            f"&data_inicio={dt_ini}"
            f"&data_fim={dt_fim}"
            f"&produto={produto}"
        )

        response = requests.get(
            url,
            timeout=30
        )

        response.raise_for_status()

        html = response.text

        match = re.search(
            r'class="valor">\s*R\$\s*([\d,.]+)',
            html
        )

        valor = None

        if match:

            valor = float(
                match.group(1)
                .replace(".", "")
                .replace(",", ".")
            )

        semana = datetime.strptime(
            dt_ini,
            "%Y-%m-%d"
        ).isocalendar().week

        return {
            "ESTADO": estado,
            "PERIODO": f"{dt_ini} a {dt_fim}",
            "SEMANA": semana,
            "VALOR_MEDIA": valor,
            "DATA_INICIO": dt_ini,
            "DATA_FIM": dt_fim
        }