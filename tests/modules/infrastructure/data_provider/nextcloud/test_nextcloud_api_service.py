import sys

from src.modules.entities.document import Document

sys.path.append('../')
import unittest
from unittest.mock import Mock

from nc_py_api import Nextcloud, FsNode
from nc_py_api.files import Share
from nc_py_api.files.files import FilesAPI, _FilesSharingAPI

from src.modules.infrastructure.data_provider.nextcloud.nextcloud_api_service import NextcloudApiService

class TestNextcloudApiService(unittest.TestCase):
  def setUp(self):
    self.mockedNextcloudAPI = Mock(Nextcloud)
    self.mockedNextcloudFilesAPI = Mock(FilesAPI)
    self.mockedNextcloudFilesSharingAPI = Mock(_FilesSharingAPI)
    self.mockedNextcloudAPI.files = self.mockedNextcloudFilesAPI
    self.mockedNextcloudAPI.files.sharing = self.mockedNextcloudFilesSharingAPI

    self.api = NextcloudApiService(self.mockedNextcloudAPI, "")
  
  def test_when_unknown_document_is_searched_then_none_is_returned(self):
    expectedDocument =  None

    self.mockedNextcloudAPI.files.find.return_value = []
    self.mockedNextcloudAPI.files.sharing.get_list.return_value = []

    api = NextcloudApiService(self.mockedNextcloudAPI, "")
    document = api.get_document("unknown_document.txt")
    self.assertEqual(expectedDocument, document)
    

  def test_when_document_in_files_system_repository_is_searched_then_document_is_returned(self):
    expectedDocument =  Document("document.txt", 'repository/document.txt', None)

    self.mockedNextcloudAPI.files.find.return_value = [
      FsNode(full_path='repository/document.txt', name="document.txt"),
    ]
    self.mockedNextcloudAPI.files.sharing.get_list.return_value = []
    
    document = self.api.get_document("document.txt")
    self.assertEqual(expectedDocument.name, document.name)
    self.assertEqual(expectedDocument.path, document.path)
    self.assertEqual(expectedDocument.link, document.link)

  def test_when_document_in_files_sharing_repository_is_searched_then_document_is_returned(self):
    expectedDocument =  Document("document.txt", None, 'http://localhost/sharedFiles/Sftuni8123')

    self.mockedNextcloudAPI.files.find.return_value = []
    self.mockedNextcloudAPI.files.sharing.get_list.return_value = [
      Share({
        "label": "document.txt",
        "url": "http://localhost/sharedFiles/Sftuni8123",
      })
    ]
    
    document = self.api.get_document("document.txt")
    self.assertEqual(expectedDocument.name, document.name)
    self.assertEqual(expectedDocument.path, document.path)
    self.assertEqual(expectedDocument.link, document.link)

  def test_when_document_in_files_sharing_and_in_files_system_repositories_is_searched_then_document_in_files_sharing_repository_is_returned(self):
    expectedDocument =  Document("document.txt", None, 'http://localhost/sharedFiles/Sftuni8123')

    self.mockedNextcloudAPI.files.find.return_value = [
      FsNode(full_path='repository/document.txt'),
    ]
    self.mockedNextcloudAPI.files.sharing.get_list.return_value = [
      Share({
        "label": "document.txt",
        "url": "http://localhost/sharedFiles/Sftuni8123",
      })
    ]
    
    document = self.api.get_document("document.txt")
    self.assertEqual(expectedDocument.name, document.name)
    self.assertEqual(expectedDocument.path, document.path)
    self.assertEqual(expectedDocument.link, document.link)

  def test_when_document_in_files_sharing_and_in_files_system_repositories_is_searched_then_document_in_files_sharing_repository_is_returned(self):
    expectedDocument =  Document("030303-reunion_alveole.pdf", 'repository/030303-reunion_alveole.pdf', None)

    self.mockedNextcloudAPI.files.find.return_value = [
      FsNode(full_path='repository/020202-reunion_alveole.pdf'),
      FsNode(full_path='repository/030303-reunion_alveole.pdf'),
      FsNode(full_path='repository/010101-reunion_alveole.pdf'),      
    ]
    
    document = self.api.get_last_report()
    self.assertEqual(expectedDocument.name, document.name)
    self.assertEqual(expectedDocument.path, document.path)
    self.assertEqual(expectedDocument.link, document.link)

  

if __name__ == '__main__':
  unittest.main()