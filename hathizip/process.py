import zipfile
import tempfile
import os
import shutil
import logging

def get_files(path):
    # capture the folder it's in
    starting_point = os.path.sep.join(os.path.normcase(path).split(os.path.sep)[:-1])
    for root, dirs, files in os.walk(path):
        for _file in files:
            relative_root = os.path.relpath(root, starting_point)
            yield os.path.join(root, _file), os.path.join(relative_root, _file)


def compress_folder(path, dst):
    logger = logging.getLogger(__name__)
    logger.debug("Taking care of {}".format(path))

    last_path = os.path.normcase(path).split(os.path.sep)[-1]
    zipname = "{}.zip".format(last_path)

    with tempfile.TemporaryDirectory() as tf:
        tmp_zip = os.path.join(tf, zipname)
        logger.debug("Creating temp zip file {}".format(tmp_zip))
        with zipfile.ZipFile(tmp_zip, "w") as zipped_package:

            for file, archive_name in get_files(path):
                logger.debug("Writing {} as {} to {}".format(file, archive_name, tmp_zip))
                zipped_package.write(file, arcname=archive_name)
                logger.info("Zipped {}".format(file))
        final_zip = os.path.join(dst, zipname)
        shutil.move(tmp_zip, final_zip)
        logger.info("Generated {}".format(final_zip))


    pass
