from django.core.files.storage import FileSystemStorage
from django.utils.deconstruct import deconstructible

@deconstructible
class PreserveNameStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        """
        Overrides the default method to keep the original file name.
        """
        if self.exists(name):
            # Do nothing; keep the original name and handle duplicates as needed.
            return name
        return super().get_available_name(name, max_length=max_length)
