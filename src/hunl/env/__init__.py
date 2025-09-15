try:
    import pyspiel  # real OpenSpiel
except ImportError:
    from . import pyspiel_stub as pyspiel  # fallback stub

__all__ = ["pyspiel"]