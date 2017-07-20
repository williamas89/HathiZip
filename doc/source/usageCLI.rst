This is a command line script so you will need a terminal window open to use it.

Zip HathiTrust Packages
-----------------------
To create zip file packages for submitting to HathiTrust, type "hathizip" followed by path to the root of the packages.
If the path has spaces in it, you must surround the path by quotes.


    :command:`hathizip "Y:\\DCC Unprocessed Files\\20170523_CavagnaCollectionRBML_rj"`




The Help Screen
---------------
This documentation should be up to date. However, you can always type :command:`hathizip -h` or
:command:`hathizip --help` into a command prompt to display the script usage instructions along with any
additional the options.


:command:`hathizip -h`

.. code-block:: console


    C:\Users\hborcher\PycharmProjects\HathiZip>hathizip --help
    usage: hathizip [-h] [--version] [--save-report REPORT_NAME] [--debug]
                    [--log-debug LOG_DEBUG]
                    path

    Creates .zip file packages for HathiTrust. Replacement script for HathiTrust
    Zip and Submit.

    positional arguments:
      path                  Path to the HathiTrust folders to be zipped

    optional arguments:
      -h, --help            show this help message and exit
      --version             show program's version number and exit
      --save-report REPORT_NAME
                            Save report to a file

    Debug:
      --debug               Run script in debug mode
      --log-debug LOG_DEBUG
                            Save debug information to a file




It's that simple!