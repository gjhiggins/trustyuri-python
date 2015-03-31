from trustyuri.TrustyUriModule import TrustyUriModule
from trustyuri.file import FileHasher

class FileModule(TrustyUriModule):
    def module_id(self):
        return "FA"
    def has_correct_hash(self, resource):
        h = FileHasher.make_hash(resource.get_content())
        return resource.get_hashstr() == h
