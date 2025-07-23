import pytest
from pytests.support.log_service import LogService

LOG = LogService


@pytest.fixture(scope="session", autouse=True)
def before_all():
    LOG.log_info("Teste log before all")


@pytest.fixture(autouse=True)
def before_after():
    LOG.log_info("Teste log before")
    yield
    LOG.log_info("Teste log after")
