import json
import pytest
from handler import detect_language, translate_message, handler


@pytest.mark.skip
@pytest.mark.parametrize("test_input, expected", [
    ('This text is written in English', 'en'),
    ('Этот текст написан mostly по-русски', 'ru'),
    ('Ten tekst jest napisany w jezyku polskim, ale bez znakow diakrytycznych', 'pl'),
    ('Текст написаний українською', 'uk')
])
def test_detect_language(test_input, expected):
    assert detect_language(test_input) == expected


@pytest.mark.skip
@pytest.mark.parametrize("test_input, source_lang, target_lang, expected", [
    ('day', 'en', 'ru', 'день'),
    ('słońce', 'pl', 'en', 'sun')
])
def test_translate_message(test_input, source_lang, target_lang, expected):
    assert translate_message(test_input, source_lang, target_lang) == expected


@pytest.mark.skip
@pytest.mark.parametrize("event, expected", [
    ({'body': {'message': 'day', 'target_language': 'ru'}}, 'день'),
    ({'body': {'message': 'słońce', 'target_language': 'en'}}, 'sun'),
])
def test_handler(event, expected):
    response = handler(event, 'context')
    assert response['statusCode'] == 200
    result = json.loads(response['body'])
    assert result['translated_message'] == expected
