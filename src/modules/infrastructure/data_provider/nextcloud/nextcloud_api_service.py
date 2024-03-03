from nc_py_api import Nextcloud, FsNode
from nc_py_api.files import Share

from src.modules.entities.document import Document
from src.modules.infrastructure.data_provider.nextcloud.a_nextcloud_api_service import ANextcloudService

class NextcloudApiService(ANextcloudService) :


  def __init__(self, nextcloudApi : Nextcloud, root_path : str) -> None:
    self.__api : Nextcloud = nextcloudApi
    self.__root_path : str = root_path

  def get_document(self, file_name : str) -> Document | None : 
    return self.__find_document(file_name)

  def get_last_report(self, path_name : str = "CR-Alvéole", file_name : str ="%reunion_alveole.pdf") -> Document | None :
    files = self.__api.files.find(["like", "name", file_name], f"{self.__root_path}/{path_name}")
    # Works because names are formatted : YYMMDD-reunion_alveole.pdf
    files = sorted(files, key=lambda f: f.name, reverse=True)
    
    if len(files) > 0 :
      return self.__convert_file_to_document(files[0])
    return None

  async def get_documents(self, path : str) -> list[Document] | None : pass

  def __find_document(self, file_name: str) -> Document | None : 
    shared_files = self.__api.files.sharing.get_list()
    files = list(filter(lambda f : str(f.label).lower() ==  file_name.lower(), shared_files))

    if len(files) == 0 :
      files = self.__api.files.find(["like", "name", file_name], self.__root_path)
      if len(files) > 0 :
        return self.__convert_file_to_document(files[0])
    else :
      return self.__convert_shared_file_to_document(files[0])
    
    return None


  def __convert_shared_file_to_document(self, file : Share) -> Document : 
    return Document(file.label, None, file.url)

  def __convert_file_to_document(self, file : FsNode) -> Document : 
    return Document(file.name, file.full_path, None)

