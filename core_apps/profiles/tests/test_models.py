import pytest

from core_apps.profiles.models import Profile


def test_profile_str(profile):
    assert profile.__str__() == f"{profile.user.username}'s profile"


def test_profile_gender(profile):
    assert profile.gender in ['male', 'female', 'other']


def test_profile_twitter_handle_length(profile):
    assert len(profile.twitter_handle) <= 20
