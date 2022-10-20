import logging

log = logging.getLogger()
log.setLevel(logging.DEBUG)
formattter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
ch = logging.StreamHandler()
ch.setFormatter(formattter)
log.addHandler