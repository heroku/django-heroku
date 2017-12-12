import sys
import os

def test_config():
    import testproject.settings as config
    
    assert config.ALLOWED_HOSTS == ['*']