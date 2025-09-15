try:
    from sklearn.cluster import KMeans  # real sklearn
except ImportError:
    from sklearn.cluster import KMeans  # fallback stub

__all__ = ["KMeans"]