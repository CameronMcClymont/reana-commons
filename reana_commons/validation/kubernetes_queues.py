# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2025 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""REANA-Commons kubernetes queues validation."""

from reana_commons.errors import REANAValidationError


def validate_kubernetes_queues(
    reana_yaml: dict, kueue_enabled: bool, supported_queues: list[str]
) -> None:
    """Validate Kubernetes queues in REANA specification file.

    :param reana_yaml: dictionary which represents REANA specification file.

    :raises REANAValidationError: Given Kubernetes queue specified in REANA spec file does not validate against
        supported Kubernetes queues.
    """
    workflow: dict = reana_yaml["workflow"]
    workflow_steps: list[dict] = workflow["specification"]["steps"]

    for step in workflow_steps:
        queue = step.get("kubernetes_queue")
        if queue:
            if not kueue_enabled:
                raise REANAValidationError(
                    f'Kubernetes queue "{queue}" found in step "{step.get("name")}" but Kueue is not enabled.'
                )
            if queue not in supported_queues:
                raise REANAValidationError(
                    f'Kubernetes queue "{queue}" in step "{step.get("name")}" is not in list of supported queues: {", ".join(supported_queues)}'
                )
