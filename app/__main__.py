#archivo que permite su ejecucion
import logging
from app import unreleased

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    print(unreleased())
    logging.debug("Comenzando el debug")
    logging.warning("Mensaje de warning")