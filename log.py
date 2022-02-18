"""
Logs servem para rastrear eventos que ocorreram em um programa executado.
Além disso, possuem importância e gravidade.

Níveis de log:
1) debug: informações detalhadas,quando ocorre problemas
2) info: confirmar coisas funcionando como esperado
3) warning: algo inesperado ocorreu,mas funciona corretamente (EXCEPT)
4) error: programa não conseguiu executar
5) critical: o sistema é impedido de executar
"""

import logging
from typing import Any


class LogGenerator:
    def __init__(self, filename: str = "logGenerator.log", level: str = "info") -> None:
        """Gera log,para o arquivo especificado e no nível definido.
        Os níveis são: debug, info, warning, error, critical"""
        assert level == "info".lower() or level == "debug".lower() or level == "error".lower() \
               or level == "warning".lower() or level == "critical".lower()

        self.__filename = filename
        self.__level = level

    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, new_level) -> None:
        self.__level = new_level

    def config(self) -> Any:
        """Configura o arquivo que receberá informações de log
        [*]Importante: não acentue as palavras"""
        if self.__level == 'info'.lower():
            logging.basicConfig(filename=self.__filename, filemode='a', level=logging.INFO, format="%(asctime)s : %(filename)s: %(levelname)s : %(message)s")
            self.division_by_zero()  # método de exemplo de aplicação
            return self.info('[*]Registrando que tudo esta ok')[0]

        elif self.__level == 'debug'.lower():
            logging.basicConfig(filename=self.__filename, filemode='a', level=logging.DEBUG, format="%(asctime)s : %(filename)s: %(levelname)s : %(message)s")
            self.debug('[*]Debugando...')

        elif self.__level == 'warning'.lower():
            logging.basicConfig(filename=self.__filename, filemode='a',level=logging.WARNING, format="%(asctime)s : %(filename)s: %(levelname)s : %(message)s")
            self.warning('[*]Ops...ocorreu uma excessao')

        elif self.__level == 'error'.lower():
            logging.basicConfig(filename=self.__filename, filemode='a',level=logging.ERROR, format="%(asctime)s : %(filename)s: %(levelname)s : %(message)s")
            self.error('[*]Ops...ocorreu um erro')

        elif self.__level == 'critical'.lower():
            logging.basicConfig(filename=self.__filename, filemode='a',level=logging.CRITICAL, format="%(asctime)s : %(filename)s: %(levelname)s : %(message)s")
            self.critical('[*]Ops...o programa deixou de funcionar..')

    def format(self, *args) -> str:
        """
        Permite personalizar as mensagens:
        asctime: hora no log
        filename: arquivo em q foi feito a chamada
        levelname: nivel do log
        message: mensagem do log
        :return: str com os itens de format
        """
        return ', '.join(str(item) for item in args)

    def info(self, text: str = "info") -> str or Any:
        """Define a mensagem a ser registrada no log"""
        return logging.info(text), self.format("%(asctime)s:%(filename)s:")

    def debug(self, text: str) -> Any:
        """Define a mensagem a ser registrada no log"""
        return logging.debug(text)

    def warning(self, text: str) -> Any:
        """Define a mensagem a ser registrada no log"""
        return logging.warning(text)

    def error(self, text: str) -> Any:
        """Define a mensagem a ser registrada no log"""
        return logging.error(text)

    def critical(self, text: str) -> Any:
        """Define a mensagem a ser registrada no log"""
        return logging.critical(text)

    def division_by_zero(self) -> None:
        """Método para fim de DEMONSTRAÇÃO DE USO"""
        try:
            7 / 0
        except Exception as e:
            self.warning(f"Erro ao dividir: {e}")

    def handler(self, level: str = logging.DEBUG) -> None:
        """
        Configura handlers
        :param level: ex: loggin.DEBUG
        :return: None
        """
        """O metodo handler da instancia logger permite manipular o log, definindo onde será usado, sua rotatividade , etc
        Além disso, ele conta com o construtor formater que permite formatar msgs"""
        logger = logging.getLogger() # padrão é root
        logger.setLevel(level) # define o level
        formato = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s") # define o formato e pode personalizar

        # configura o handler
        screen = logging.StreamHandler() # escreve no console
        screen.setFormatter(formato)
        screen.setLevel(level)

        logger.addHandler(screen)  # adiciona o handler criado
        # definindo a mensagem e o tipo de level:
        logger.debug("Debug do handler no console")

        file = logging.FileHandler(self.__filename)  # escreve em arquivo
        file.setFormatter(formato)
        file.setLevel(level)

        logger.addHandler(file)  # adiciona o handler criado
        # definindo a mensagem e o tipo de level:
        logger.debug("Debug do handler em arquivo")


if __name__ == '__main__':
    LogGenerator().config()

    # com handler
    LogGenerator().handler()
