try:
    import torch
except ImportError:
    from . import torch_stub as torch

__all__ = ["torch"]