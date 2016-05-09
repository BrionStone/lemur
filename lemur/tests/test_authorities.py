
import pytest
from lemur.authorities.views import *  # noqa

from .vectors import VALID_ADMIN_HEADER_TOKEN, VALID_USER_HEADER_TOKEN


def test_authority_input_schema(client, role):
    from lemur.authorities.schemas import AuthorityInputSchema

    input_data = {
        'name': 'Example Authority',
        'owner': 'jim@example.com',
        'description': 'An example authority.',
        'commonName': 'AnExampleAuthority',
        'pluginName': {'slug': 'verisign-issuer'},
        'type': 'root',
        'signingAlgorithm': 'sha256WithRSA',
        'keyType': 'RSA2048',
        'sensitivity': 'medium'
    }

    data, errors = AuthorityInputSchema().load(input_data)

    assert not errors


@pytest.mark.parametrize("token,status", [
    (VALID_USER_HEADER_TOKEN, 404),
    (VALID_ADMIN_HEADER_TOKEN, 404),
    ('', 401)
])
def test_authority_get(client, token, status):
    assert client.get(api.url_for(Authorities, authority_id=1), headers=token).status_code == status


@pytest.mark.parametrize("token,status", [
    (VALID_USER_HEADER_TOKEN, 405),
    (VALID_ADMIN_HEADER_TOKEN, 405),
    ('', 405)
])
def test_authority_post(client, token, status):
    assert client.post(api.url_for(Authorities, authority_id=1), data={}, headers=token).status_code == status


@pytest.mark.parametrize("token,status", [
    (VALID_USER_HEADER_TOKEN, 400),
    (VALID_ADMIN_HEADER_TOKEN, 400),
    ('', 401)
])
def test_authority_put(client, token, status):
    assert client.put(api.url_for(Authorities, authority_id=1), data={}, headers=token).status_code == status


@pytest.mark.parametrize("token,status", [
    (VALID_USER_HEADER_TOKEN, 405),
    (VALID_ADMIN_HEADER_TOKEN, 405),
    ('', 405)
])
def test_authority_delete(client, token, status):
    assert client.delete(api.url_for(Authorities, authority_id=1), headers=token).status_code == status


@pytest.mark.parametrize("token,status", [
    (VALID_USER_HEADER_TOKEN, 405),
    (VALID_ADMIN_HEADER_TOKEN, 405),
    ('', 405)
])
def test_authority_patch(client, token, status):
    assert client.patch(api.url_for(Authorities, authority_id=1), data={}, headers=token).status_code == status


@pytest.mark.parametrize("token,status", [
    (VALID_USER_HEADER_TOKEN, 200),
    (VALID_ADMIN_HEADER_TOKEN, 200),
    ('', 401)
])
def test_authorities_get(client, token, status):
    assert client.get(api.url_for(AuthoritiesList), headers=token).status_code == status


@pytest.mark.parametrize("token,status", [
    (VALID_USER_HEADER_TOKEN, 400),
    (VALID_ADMIN_HEADER_TOKEN, 400),
    ('', 401)
])
def test_authorities_post(client, token, status):
    assert client.post(api.url_for(AuthoritiesList), data={}, headers=token).status_code == status


@pytest.mark.parametrize("token,status", [
    (VALID_USER_HEADER_TOKEN, 405),
    (VALID_ADMIN_HEADER_TOKEN, 405),
    ('', 405)
])
def test_authorities_put(client, token, status):
    assert client.put(api.url_for(AuthoritiesList), data={}, headers=token).status_code == status


@pytest.mark.parametrize("token,status", [
    (VALID_USER_HEADER_TOKEN, 405),
    (VALID_ADMIN_HEADER_TOKEN, 405),
    ('', 405)
])
def test_authorities_delete(client, token, status):
    assert client.delete(api.url_for(AuthoritiesList), headers=token).status_code == status


@pytest.mark.parametrize("token,status", [
    (VALID_USER_HEADER_TOKEN, 405),
    (VALID_ADMIN_HEADER_TOKEN, 405),
    ('', 405)
])
def test_authorities_patch(client, token, status):
    assert client.patch(api.url_for(AuthoritiesList), data={}, headers=token).status_code == status


@pytest.mark.parametrize("token,status", [
    (VALID_USER_HEADER_TOKEN, 200),
    (VALID_ADMIN_HEADER_TOKEN, 200),
    ('', 401)
])
def test_certificate_authorities_get(client, token, status):
    assert client.get(api.url_for(AuthoritiesList), headers=token).status_code == status


@pytest.mark.parametrize("token,status", [
    (VALID_USER_HEADER_TOKEN, 400),
    (VALID_ADMIN_HEADER_TOKEN, 400),
    ('', 401)
])
def test_certificate_authorities_post(client, token, status):
    assert client.post(api.url_for(AuthoritiesList), data={}, headers=token).status_code == status


@pytest.mark.parametrize("token,status", [
    (VALID_USER_HEADER_TOKEN, 405),
    (VALID_ADMIN_HEADER_TOKEN, 405),
    ('', 405)
])
def test_certificate_authorities_put(client, token, status):
    assert client.put(api.url_for(AuthoritiesList), data={}, headers=token).status_code == status


@pytest.mark.parametrize("token,status", [
    (VALID_USER_HEADER_TOKEN, 405),
    (VALID_ADMIN_HEADER_TOKEN, 405),
    ('', 405)
])
def test_certificate_authorities_delete(client, token, status):
    assert client.delete(api.url_for(AuthoritiesList), headers=token).status_code == status


@pytest.mark.parametrize("token,status", [
    (VALID_USER_HEADER_TOKEN, 405),
    (VALID_ADMIN_HEADER_TOKEN, 405),
    ('', 405)
])
def test_certificate_authorities_patch(client, token, status):
    assert client.patch(api.url_for(AuthoritiesList), data={}, headers=token).status_code == status
