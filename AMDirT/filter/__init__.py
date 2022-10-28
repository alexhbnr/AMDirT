# from AMDirT import logger
import sys
from streamlit import cli as stcli
from pathlib import Path
from AMDirT.core import get_json_path, logger


def run_app(tables=None):
    """
    Run the AMDirT interactive filtering application

    Args:
        tables (str): path to JSON file listing AncientMetagenomeDir tables
    """
    directory = Path(__file__).parent.resolve()
    app = "streamlit.py"
    if tables is None:
        config_path = get_json_path()
    else:
        config_path = tables
    app_path = f"{directory}/{app}"

    sys.argv = ["streamlit", "run", app_path, "--", "--config", config_path]
    logger.info("\n[AMDirT] To close app, press on your keyboard: ctrl+c\n")
    sys.exit(stcli.main())
