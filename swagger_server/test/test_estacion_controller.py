# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.medicion import Medicion  # noqa: E501
from swagger_server.test import BaseTestCase


class TestEstacionController(BaseTestCase):
    """EstacionController integration test stubs"""

    def test_estacion_post(self):
        """Test case for estacion_post

        Registra los valores de telemetría de una estación de medición del tiempo.
        """
        body = Medicion()
        response = self.client.open(
            '/api/estacion',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
