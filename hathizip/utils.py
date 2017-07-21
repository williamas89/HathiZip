import os


def has_subdirs(path: str)->bool:
    """
    Validate path. Make sure it has folders in it

    Args:
        path: Location to validated

    Returns:

    """
    for _ in filter(lambda x: x.is_dir(), os.scandir(path)):
        return True
    return False
