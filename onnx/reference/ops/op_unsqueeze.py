# SPDX-License-Identifier: Apache-2.0
# pylint: disable=E0203,W0221

import numpy as np

from onnx.defs import onnx_opset_version
from onnx.reference.op_run import OpRun


class Unsqueeze_1(OpRun):
    def _run(self, data, axes=None):  # type: ignore
        if isinstance(axes, np.ndarray):
            axes = tuple(axes)
        elif axes in [[], tuple()]:
            axes = None
        elif isinstance(axes, list):
            axes = tuple(axes)
        if isinstance(axes, (tuple, list)):
            sq = data
            for a in axes:
                sq = np.expand_dims(sq, axis=a)
        else:
            raise RuntimeError(
                "axes cannot be None for operator Unsqueeze (Unsqueeze_1)."
            )
        return (sq,)


class Unsqueeze_11(Unsqueeze_1):
    pass


class Unsqueeze_13(OpRun):
    def _run(self, data, axes=None):  # type: ignore
        if axes is not None:
            if hasattr(axes, "__iter__") and len(axes.shape) > 0:
                sq = np.expand_dims(data, axis=tuple(axes))
            else:
                sq = np.expand_dims(data, axis=axes)
        else:
            raise RuntimeError(
                "axes cannot be None for operator Unsqueeze (Unsqueeze_13)."
            )
        return (sq,)


if onnx_opset_version() >= 13:
    Unsqueeze = Unsqueeze_13
elif onnx_opset_version() >= 11:
    Unsqueeze = Unsqueeze_11  # type: ignore
else:
    Unsqueeze = Unsqueeze_1  # type: ignore
