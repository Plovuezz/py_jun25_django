import os

from django.core.exceptions import SuspiciousFileOperation
from storages.backends.dropbox import DropboxStorage
from storages.utils import safe_join


class WindowsCompatibleDropboxStorage(DropboxStorage):
    def _full_path(self, name):
        if name == "/":
            name = ""

        # If the machine is windows do not append the drive letter to file path
        if os.name == "nt":
            return os.path.join("/", self.root_path, name).replace("\\", "/")
        else:
            return safe_join(self.root_path, name).replace("\\", "/")
