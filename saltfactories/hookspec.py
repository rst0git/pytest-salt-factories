# -*- coding: utf-8 -*-
'''
saltfactories.hookspec
~~~~~~~~~~~~~~~~~~~~~~

Salt Factories Hooks
'''
# Import Python libs
from __future__ import absolute_import, print_function, unicode_literals

# Import 3rd-party libs
import pytest


@pytest.hookspec(firstresult=True)
def pytest_saltfactories_generate_default_minion_configuration(
    request, factories_manager, minion_id, master_port
):
    '''
    Hook which should return a dictionary tailored for the provided minion_id

    Stops at the first non None result
    '''


@pytest.hookspec(firstresult=True)
def pytest_saltfactories_minion_configuration_overrides(
    request, factories_manager, default_options, minion_id
):
    '''
    Hook which should return a dictionary tailored for the provided minion_id.
    This dictionary will override the default_options dictionary.

    Stops at the first non None result
    '''


def pytest_saltfactories_verify_minion_configuration(request, minion_config, username):
    '''
    This hook is called to vefiry the provided minion configuration
    '''


@pytest.hookspec(firstresult=True)
def pytest_saltfactories_write_minion_configuration(request, minion_config):
    '''
    This hook is called to write the provided minion configuration
    '''


@pytest.hookspec(firstresult=True)
def pytest_saltfactories_generate_default_master_configuration(
    request, factories_manager, master_id
):
    '''
    Hook which should return a dictionary tailored for the provided master_id

    Stops at the first non None result
    '''


@pytest.hookspec(firstresult=True)
def pytest_saltfactories_master_configuration_overrides(
    request, factories_manager, default_options, master_id
):
    '''
    Hook which should return a dictionary tailored for the provided master_id.
    This dictionary will override the default_options dictionary.

    Stops at the first non None result
    '''


def pytest_saltfactories_verify_master_configuration(request, master_config, username):
    '''
    This hook is called to vefiry the provided master configuration
    '''


@pytest.hookspec(firstresult=True)
def pytest_saltfactories_write_master_configuration(request, master_config):
    '''
    This hook is called to write the provided master configuration
    '''


@pytest.hookspec(firstresult=True)
def pytest_saltfactories_generate_default_syndic_configuration(
    request, factories_manager, syndic_id, master_port
):
    '''
    Hook which should return a dictionary tailored for the provided syndic_id

    Stops at the first non None result
    '''


@pytest.hookspec(firstresult=True)
def pytest_saltfactories_syndic_configuration_overrides(
    request, factories_manager, default_options, syndic_id
):
    '''
    Hook which should return a dictionary tailored for the provided syndic_id.
    This dictionary will override the default_options dictionary.

    Stops at the first non None result
    '''


def pytest_saltfactories_verify_syndic_configuration(request, syndic_config, username):
    '''
    This hook is called to vefiry the provided syndic configuration
    '''


@pytest.hookspec(firstresult=True)
def pytest_saltfactories_write_syndic_configuration(request, syndic_config):
    '''
    This hook is called to write the provided syndic configuration
    '''