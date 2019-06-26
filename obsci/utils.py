# Copyright (c) 2019 SUSE Linux GmbH
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import io
import tarfile


def create_tarfile(directory):
    """Create a tarfile in memory"""

    tar_stream = io.BytesIO()
    with tarfile.open(mode='w', fileobj=tar_stream) as tarf:
        for f in os.listdir(directory):
            fullpath = os.path.join(directory, f)
            if os.path.isfile(fullpath):
                tarf.add(fullpath, arcname=f, recursive=False)
    tar_stream.seek(0)
    return tar_stream
