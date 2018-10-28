"""Version tests."""
from __future__ import unicode_literals
import unittest
from pep562.__meta__ import Pep440Version, parse_version


class TestVersion(unittest.TestCase):
    """Test versions."""

    def test_version_output(self):
        """Test that versions generate proper strings."""

        assert Pep440Version(1, 0, 0, "final")._get_canonical() == "1.0"
        assert Pep440Version(1, 2, 0, "final")._get_canonical() == "1.2"
        assert Pep440Version(1, 2, 3, "final")._get_canonical() == "1.2.3"
        assert Pep440Version(1, 2, 0, "alpha", pre=4)._get_canonical() == "1.2a4"
        assert Pep440Version(1, 2, 0, "beta", pre=4)._get_canonical() == "1.2b4"
        assert Pep440Version(1, 2, 0, "candidate", pre=4)._get_canonical() == "1.2rc4"
        assert Pep440Version(1, 2, 0, "final", post=1)._get_canonical() == "1.2.post1"
        assert Pep440Version(1, 2, 3, ".dev-alpha", pre=1)._get_canonical() == "1.2.3a1.dev0"
        assert Pep440Version(1, 2, 3, ".dev")._get_canonical() == "1.2.3.dev0"
        assert Pep440Version(1, 2, 3, ".dev", dev=1)._get_canonical() == "1.2.3.dev1"

    def test_version_comparison(self):
        """Test that versions compare proper."""

        assert Pep440Version(1, 0, 0, "final") < Pep440Version(1, 2, 0, "final")
        assert Pep440Version(1, 2, 0, "alpha", pre=4) < Pep440Version(1, 2, 0, "final")
        assert Pep440Version(1, 2, 0, "final") < Pep440Version(1, 2, 0, "final", post=1)
        assert Pep440Version(1, 2, 3, ".dev-beta", pre=2) < Pep440Version(1, 2, 3, "beta", pre=2)
        assert Pep440Version(1, 2, 3, ".dev") < Pep440Version(1, 2, 3, ".dev-beta", pre=2)
        assert Pep440Version(1, 2, 3, ".dev") < Pep440Version(1, 2, 3, ".dev", dev=1)

    def test_version_parsing(self):
        """Test version parsing."""

        assert parse_version(
            Pep440Version(1, 0, 0, "final")._get_canonical()
        ) == Pep440Version(1, 0, 0, "final")
        assert parse_version(
            Pep440Version(1, 2, 0, "final")._get_canonical()
        ) == Pep440Version(1, 2, 0, "final")
        assert parse_version(
            Pep440Version(1, 2, 3, "final")._get_canonical()
        ) == Pep440Version(1, 2, 3, "final")
        assert parse_version(
            Pep440Version(1, 2, 0, "alpha", pre=4)._get_canonical()
        ) == Pep440Version(1, 2, 0, "alpha", pre=4)
        assert parse_version(
            Pep440Version(1, 2, 0, "beta", pre=4)._get_canonical()
        ) == Pep440Version(1, 2, 0, "beta", pre=4)
        assert parse_version(
            Pep440Version(1, 2, 0, "candidate", pre=4)._get_canonical()
        ) == Pep440Version(1, 2, 0, "candidate", pre=4)
        assert parse_version(
            Pep440Version(1, 2, 0, "final", post=1)._get_canonical()
        ) == Pep440Version(1, 2, 0, "final", post=1)
        assert parse_version(
            Pep440Version(1, 2, 3, ".dev-alpha", pre=1)._get_canonical()
        ) == Pep440Version(1, 2, 3, ".dev-alpha", pre=1)
        assert parse_version(
            Pep440Version(1, 2, 3, ".dev")._get_canonical()
        ) == Pep440Version(1, 2, 3, ".dev")
        assert parse_version(
            Pep440Version(1, 2, 3, ".dev", dev=1)._get_canonical()
        ) == Pep440Version(1, 2, 3, ".dev", dev=1)

    def test_asserts(self):
        """Test asserts."""

        with self.assertRaises(ValueError):
            Pep440Version("1", "2", "3")
        with self.assertRaises(ValueError):
            Pep440Version(1, 2, 3, 1)
        with self.assertRaises(ValueError):
            Pep440Version("1", "2", "3")
        with self.assertRaises(ValueError):
            Pep440Version(1, 2, 3, "bad")
        with self.assertRaises(ValueError):
            Pep440Version(1, 2, 3, "alpha")
        with self.assertRaises(ValueError):
            Pep440Version(1, 2, 3, "alpha", pre=1, dev=1)
        with self.assertRaises(ValueError):
            Pep440Version(1, 2, 3, "alpha", pre=1, post=1)
        with self.assertRaises(ValueError):
            Pep440Version(1, 2, 3, ".dev-alpha")
        with self.assertRaises(ValueError):
            Pep440Version(1, 2, 3, ".dev-alpha", pre=1, post=1)
        with self.assertRaises(ValueError):
            Pep440Version(1, 2, 3, pre=1)
        with self.assertRaises(ValueError):
            Pep440Version(1, 2, 3, dev=1)