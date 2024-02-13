from unittest.mock import Mock

import pytest

from app import resources


def mock_base_storage_get(value_type: str):
    value = {"json": '{"value": "dummy json"}', "txt": "dummy txt"}
    return value[value_type]


@pytest.fixture
def MockBaseStorage():
    def _MockBaseStorage(bucket_name: str):
        mock_base_storage = Mock()
        get_return_value = mock_base_storage_get(bucket_name)
        mock_base_storage.get = Mock(return_value=get_return_value)
        return mock_base_storage

    return _MockBaseStorage


@pytest.mark.parametrize(
    "resource, restaurant, version, bucket_name, expected_base_name",
    [
        (
            resources.TxtResource,
            "mock_restaurant",
            "mock_version",
            "txt",
            "txt_resource",
        ),
        (
            resources.Menu,
            "mock_restaurant",
            "mock_version",
            "json",
            "menu",
        ),
        (
            resources.OrderPromptTemplate,
            "mock_restaurant",
            "mock_version",
            "txt",
            "order_prompt_template",
        ),
        (
            resources.OrderPrefixPrompt,
            "mock_restaurant",
            "mock_version",
            "txt",
            "order_prefix_prompt",
        ),
        (
            resources.OrderSuffixPrompt,
            "mock_restaurant",
            "mock_version",
            "txt",
            "order_suffix_prompt",
        ),
        (
            resources.GreetingsMessage,
            "mock_restaurant",
            "mock_version",
            "txt",
            "greetings_message",
        ),
        (
            resources.FarewellMessage,
            "mock_restaurant",
            "mock_version",
            "txt",
            "farewell_message",
        ),
        (
            resources.ValidationPrompt,
            "mock_restaurant",
            "mock_version",
            "txt",
            "validation_prompt",
        ),
        (
            resources.ValidationPromptTemplate,
            "mock_restaurant",
            "mock_version",
            "txt",
            "validation_prompt_template",
        ),
        (
            resources.SummaryPromptTemplate,
            "mock_restaurant",
            "mock_version",
            "txt",
            "summary_prompt_template",
        ),
        (
            resources.SummaryPrompt,
            "mock_restaurant",
            "mock_version",
            "txt",
            "summary_prompt",
        ),
        (
            resources.ConfigPromptTemplate,
            "mock_restaurant",
            "mock_version",
            "txt",
            "config_prompt_template",
        ),
        (
            resources.ConfigPrompt,
            "mock_restaurant",
            "mock_version",
            "txt",
            "config_prompt",
        ),
        (
            resources.ConfigEntitiesExtractorPrompt,
            "mock_restaurant",
            "mock_version",
            "txt",
            "config_entities_extractor_prompt",
        ),
        (
            resources.ConfigEntitiesExtractorPromptTemplate,
            "mock_restaurant",
            "mock_version",
            "txt",
            "config_entities_extractor_prompt_template",
        ),
        (
            resources.ConfigFillerPrompt,
            "mock_restaurant",
            "mock_version",
            "txt",
            "config_filler_prompt",
        ),
        (
            resources.ConfigFillerPromptTemplate,
            "mock_restaurant",
            "mock_version",
            "txt",
            "config_filler_prompt_template",
        ),
        (
            resources.StoreConfig,
            "mock_restaurant",
            "mock_version",
            "json",
            "store_config",
        ),
        (
            resources.Store,
            "mock_restaurant",
            "mock_version",
            "json",
            "store",
        ),
    ],
)
def test_resources_base_name(
    MockBaseStorage, resource, restaurant, version, bucket_name, expected_base_name
):
    storage = MockBaseStorage(bucket_name)
    resource2test = resource(restaurant, version, storage)
    assert resource2test.BASE_NAME == expected_base_name
