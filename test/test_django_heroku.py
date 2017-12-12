import sys
import os
import imp

import pytest

import testproject.settings as config

def test_databases():
    imp.reload(config)

def test_test_runner():
    imp.reload(config)
    
def test_staticfiles():
    imp.reload(config)

def test_allowed_hosts():
    imp.reload(config)
    
    assert config.ALLOWED_HOSTS == ['*']
    
    
def test_logging():
    imp.reload(config)
    
def test_secret_key():
    os.environ['SECRET_KEY'] = 'SECRET'

    imp.reload(config)
    assert config.SECRET_KEY == 'SECRET'
