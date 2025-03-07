from http import HTTPStatus

from fastapi.testclient import TestClient

from src.fast_zero.app import app


def test_read_root_deve_retornar_OK_e_ola_mundo():
    # Organize, Arrange
    client = TestClient(app)

    response = client.get('/')  # Act

    # Assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo'}
