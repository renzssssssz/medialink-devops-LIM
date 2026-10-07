import os
import unittest
from unittest.mock import patch

import config


class ConfigTests(unittest.TestCase):
    def test_get_api_key_uses_default_when_unset(self):
        with patch.dict(os.environ, {}, clear=False):
            os.environ.pop("MEDILINK_API_KEY", None)
            self.assertEqual(config.get_api_key(), "local-demo-key")

    def test_get_api_key_uses_environment_value(self):
        with patch.dict(os.environ, {"MEDILINK_API_KEY": "demo-secret"}, clear=False):
            self.assertEqual(config.get_api_key(), "demo-secret")

    def test_get_request_timeout_uses_default_value(self):
        with patch.dict(os.environ, {}, clear=False):
            os.environ.pop("REQUEST_TIMEOUT", None)
            self.assertEqual(config.get_request_timeout(), 5)

    def test_get_request_timeout_rejects_non_positive_value(self):
        with patch.dict(os.environ, {"REQUEST_TIMEOUT": "0"}, clear=False):
            with self.assertRaises(ValueError):
                config.get_request_timeout()


if __name__ == "__main__":
    unittest.main()
