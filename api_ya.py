import requests
import pytest


def put_folder(url, token):
    headers = {'Authorization': f'OAuth {token}'}
    params = {'path': 'test_folder'}


    response = requests.put(url, headers=headers, params=params)
    return response.status_code

class TestYandexDisk:


    @pytest.mark.parametrize('token,url', [('y0_AgAAAABWbMqRAADLWwAAAAECUNgeAAAPNEjO985NEpabjg5U3PMdLsaBMw', 'https://cloud-api.yandex.net/v1/disk/resources')])
    def test_put_201(self,token,url):
        response = put_folder(url=url, token=token)
        assert response == 201

    @pytest.mark.parametrize('token,url', [('y0_AgAAAABWbMqRAADLWwAAAAECUNgeAAAPNEjO985NEpabjg5U3PMdLsaBMw',
                                            'https://cloud-api.yandex.net/v1/disk/resources')])
    @pytest.mark.xfail
    def test_put_409(self,token,url):
        response = put_folder(url='https://cloud-api.yandex.net/v1/disk/resources', token='y0_AgAAAABWbMqRAADLWwAAAAECUNgeAAAPNEjO985NEpabjg5U3PMdLsaBMw')
        assert response == 409

    @pytest.mark.parametrize('token,url', [('y0_AgAAAABWbMqRAADLWwAAAAECUNgeAAAPNEjO985NEpabjg5U3PMdLsaBMw',
                                                'https://cloud-api.yandex.net/v1/disk/resources')])
    @pytest.mark.xfail
    def test_put_401(self,token,url):
        response = put_folder(url='https://cloud-api.yandex.net/v1/disk/resources', token='y0_AgAAAABWbMqRAADLWwAAAAECUNgeAAAPNEjO985NEpabjg5U3PMdLsaBMx')
        assert response == 401





