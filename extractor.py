import tempfile
import os

from assemblyline_v4_service.common.base import ServiceBase
from assemblyline_v4_service.common.request import ServiceRequest
from assemblyline_v4_service.common.result import Result, ResultSection


from library import calculate_sha256, extract_defender


class Dequarantine(ServiceBase):

    def __init__(self, config=None):
        super(Dequarantine, self).__init__(config)

    def start(self):
        self.log.info(f'start() from {self.service_attributes.name} service called')

    def execute(self, request: ServiceRequest) -> None:

        result = Result()

        if request.file_type.startswith('quarantine/windowsdefender'):

            fd, temp_path = tempfile.mkstemp(dir=self.working_directory)

            with os.fdopen(fd, 'wb') as temp_file:
                extracted = extract_defender(request.file_path)
                temp_file.write(extracted)

            file_name = calculate_sha256(temp_path)

            request.add_extracted(temp_path, file_name, 'Extracted quarantine file.')

        request.result = result
