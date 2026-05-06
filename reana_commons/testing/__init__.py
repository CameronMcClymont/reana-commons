# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2026 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Pytest fixtures and test helpers for REANA-Commons.

This subpackage ships pytest fixtures and helpers that previously lived in
``pytest-reana``. It is registered as a pytest plugin via the ``pytest11``
entry point, so projects that install ``reana-commons[tests]`` get the
fixtures auto-loaded by pytest collection.
"""

from __future__ import absolute_import, print_function

import pathlib

from .api_client import make_mock_api_client
from .fixtures import (
    ConsumerBase,
    ConsumerBaseOnMessageMock,
    consume_queue,
    corev1_api_client_with_user_secrets,
    cwl_workflow_with_name,
    cwl_workflow_without_name,
    default_exchange,
    default_in_memory_producer,
    default_queue,
    empty_user_secrets,
    in_memory_queue_connection,
    kerberos_user_secrets,
    no_db_user,
    sample_workflow_workspace,
    serial_workflow,
    snakemake_workflow_spec_loaded,
    tmp_shared_volume_path,
    user_secrets,
    yadage_workflow_spec_loaded,
    yadage_workflow_with_name,
    yadage_workflow_without_name,
)

TEST_WORKSPACE_DIR = pathlib.Path(__file__).parent / "data" / "test_workspace"
"""Filesystem path to the bundled sample workflow workspace."""

__all__ = (
    "ConsumerBase",
    "ConsumerBaseOnMessageMock",
    "TEST_WORKSPACE_DIR",
    "consume_queue",
    "corev1_api_client_with_user_secrets",
    "cwl_workflow_with_name",
    "cwl_workflow_without_name",
    "default_exchange",
    "default_in_memory_producer",
    "default_queue",
    "empty_user_secrets",
    "in_memory_queue_connection",
    "kerberos_user_secrets",
    "make_mock_api_client",
    "no_db_user",
    "sample_workflow_workspace",
    "serial_workflow",
    "snakemake_workflow_spec_loaded",
    "tmp_shared_volume_path",
    "user_secrets",
    "yadage_workflow_spec_loaded",
    "yadage_workflow_with_name",
    "yadage_workflow_without_name",
)
