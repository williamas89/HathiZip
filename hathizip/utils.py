import os


def has_subdirs(path: str)->bool:
    """
    Validate path. Make sure it has folders in it

    Args:
        path: Location to validated

    Returns:

    """
    for _ in filter(os.path.isdir, os.scandir(path)):
        return True
    return False
