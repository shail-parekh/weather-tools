# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from .clients import FakeClient, CdsClient, MarsClient


class MaxWorkersTest(unittest.TestCase):
    def test_cdsclient_internal(self):
        self.assertEqual(CdsClient.num_requests_per_key("reanalysis-era5-some-data"), 5)

    def test_cdsclient_mars_hosted(self):
        self.assertEqual(CdsClient.num_requests_per_key("reanalysis-carra-height-levels"), 2)

    def test_marsclient(self):
        self.assertEqual(MarsClient.num_requests_per_key("reanalysis-era5-some-data"), 2)

    def test_fakeclient(self):
        self.assertEqual(FakeClient.num_requests_per_key("reanalysis-era5-some-data"), 1)


if __name__ == '__main__':
    unittest.main()
