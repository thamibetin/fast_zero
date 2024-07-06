from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_return_ok_hellow():
    client = TestClient(app)  # Arrange (organização do teste)

    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert (garanta que)
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert
