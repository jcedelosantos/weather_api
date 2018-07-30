# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.medicion import Medicion  # noqa: E501
from swagger_server.test import BaseTestCase


class TestClimaController(BaseTestCase):
    """ClimaController integration test stubs"""

    def test_clima_id_estacion_get(self):
        """Test case for clima_id_estacion_get

        Devuelve los valores medidos mas reciente, de una estación.
        """
        query_string = [('inicio', '2013-10-20T19:20:30+01:00'),
                        ('fin', '2013-10-20T19:20:30+01:00'),
                        ('sensor', 'sensor_example')]
        response = self.client.open(
            '/api/clima/{idEstacion}'.format(idEstacion='idEstacion_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
