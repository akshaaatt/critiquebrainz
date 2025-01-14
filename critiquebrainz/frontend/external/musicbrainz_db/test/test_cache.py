# pylint: disable=no-self-use
from unittest import mock

from critiquebrainz.frontend.external.musicbrainz_db import DEFAULT_CACHE_EXPIRATION
from critiquebrainz.frontend.external.musicbrainz_db.artist import get_artist_by_id
from critiquebrainz.frontend.external.musicbrainz_db.event import get_event_by_id
from critiquebrainz.frontend.external.musicbrainz_db.label import get_label_by_id
from critiquebrainz.frontend.external.musicbrainz_db.place import get_place_by_id
from critiquebrainz.frontend.external.musicbrainz_db.recording import get_recording_by_id
from critiquebrainz.frontend.external.musicbrainz_db.release import get_release_by_id
from critiquebrainz.frontend.external.musicbrainz_db.release_group import get_release_group_by_id
from critiquebrainz.frontend.external.musicbrainz_db.work import get_work_by_id
from critiquebrainz.data.testing import DataTestCase


class CacheTestCase(DataTestCase):

    @mock.patch('brainzutils.cache.get')
    @mock.patch('brainzutils.cache.set')
    @mock.patch('brainzutils.musicbrainz_db.artist.get_artist_by_id')
    def test_artist_cache(self, artist_fetch, cache_set, cache_get):
        mbid = "f59c5520-5f46-4d2c-b2c4-822eabf53419"
        expected_key = b"artist_f59c5520-5f46-4d2c-b2c4-822eabf53419"
        artist = {
            "id": "f59c5520-5f46-4d2c-b2c4-822eabf53419",
            "name": "Linkin Park",
            "sort_name": "Linkin Park",
            "type": "Group"
        }
        artist_fetch.return_value = artist

        cache_get.return_value = None
        get_artist_by_id(mbid)

        # Test that first time data is fetched database is queried
        cache_get.assert_called_with(expected_key)
        artist_fetch.assert_called_with(mbid, includes=['artist-rels', 'url-rels'], unknown_entities_for_missing=True)
        cache_set.assert_called_with(key=expected_key, val=artist, time=DEFAULT_CACHE_EXPIRATION)

        cache_get.return_value = artist
        cache_set.reset_mock()
        artist_fetch.reset_mock()
        get_artist_by_id(mbid)

        # Test that second time data is fetched from cache
        cache_get.assert_called_with(expected_key)
        artist_fetch.assert_not_called()
        cache_set.assert_not_called()

    @mock.patch('brainzutils.cache.get')
    @mock.patch('brainzutils.cache.set')
    @mock.patch('brainzutils.musicbrainz_db.event.get_event_by_id')
    def test_event_cache(self, event_fetch, cache_set, cache_get):
        mbid = "ebe6ce0f-22c0-4fe7-bfd4-7a0397c9fe94"
        expected_key = b"event_ebe6ce0f-22c0-4fe7-bfd4-7a0397c9fe94"
        event = {
            'id': 'ebe6ce0f-22c0-4fe7-bfd4-7a0397c9fe94',
            'name': 'Taubertal-Festival 2004, Day 1',
        }
        event_fetch.return_value = event

        cache_get.return_value = None
        get_event_by_id(mbid)

        # Test that first time data is fetched database is queried
        cache_get.assert_called_with(expected_key)
        event_fetch.assert_called_with(mbid, includes=['artist-rels', 'place-rels',
                                                       'series-rels', 'url-rels', 'release-group-rels'],
                                       unknown_entities_for_missing=True)
        cache_set.assert_called_with(key=expected_key, val=event, time=DEFAULT_CACHE_EXPIRATION)

        cache_get.return_value = event
        cache_set.reset_mock()
        event_fetch.reset_mock()
        get_event_by_id(mbid)

        # Test that second time data is fetched from cache
        cache_get.assert_called_with(expected_key)
        event_fetch.assert_not_called()
        cache_set.assert_not_called()

    @mock.patch('brainzutils.cache.get')
    @mock.patch('brainzutils.cache.set')
    @mock.patch('brainzutils.musicbrainz_db.label.get_label_by_id')
    def test_label_cache(self, label_fetch, cache_set, cache_get):
        mbid = "1aed8c3b-8e1e-46f8-b558-06357ff5f298"
        expected_key = b"label_1aed8c3b-8e1e-46f8-b558-06357ff5f298"
        label = {
            "id": "1aed8c3b-8e1e-46f8-b558-06357ff5f298",
            "name": "Dreamville",
            "type": "Imprint",
            "area": "United States",
        }
        label_fetch.return_value = label

        cache_get.return_value = None
        get_label_by_id(mbid)

        # Test that first time data is fetched database is queried
        cache_get.assert_called_with(expected_key)
        label_fetch.assert_called_with(mbid, includes=['artist-rels', 'url-rels'], unknown_entities_for_missing=True)
        cache_set.assert_called_with(key=expected_key, val=label, time=DEFAULT_CACHE_EXPIRATION)

        cache_get.return_value = label
        cache_set.reset_mock()
        label_fetch.reset_mock()
        get_label_by_id(mbid)

        # Test that second time data is fetched from cache
        cache_get.assert_called_with(expected_key)
        label_fetch.assert_not_called()
        cache_set.assert_not_called()

    @mock.patch('brainzutils.cache.get')
    @mock.patch('brainzutils.cache.set')
    @mock.patch('brainzutils.musicbrainz_db.place.get_place_by_id')
    def test_place_cache(self, place_fetch, cache_set, cache_get):
        mbid = "d71ffe38-5eaf-426b-9a2e-e1f21bc84609"
        expected_key = b"place_d71ffe38-5eaf-426b-9a2e-e1f21bc84609"
        place = {
            "id": "d71ffe38-5eaf-426b-9a2e-e1f21bc84609",
            "name": "Suisto",
            "coordinates": {
                'latitude': 60.997758,
                'longitude': 24.477142
            },
            "area": {
                "id": "4479c385-74d8-4a2b-bdab-f48d1e6969ba",
                "name": "Hämeenlinna",
            }
        }
        place_fetch.return_value = place

        cache_get.return_value = None
        get_place_by_id(mbid)

        # Test that first time data is fetched database is queried
        cache_get.assert_called_with(expected_key)
        place_fetch.assert_called_with(mbid, includes=['artist-rels', 'place-rels',
                                                       'release-group-rels', 'url-rels'],
                                       unknown_entities_for_missing=True)
        cache_set.assert_called_with(key=expected_key, val=place, time=DEFAULT_CACHE_EXPIRATION)

        cache_get.return_value = place
        cache_set.reset_mock()
        place_fetch.reset_mock()
        get_place_by_id(mbid)

        # Test that second time data is fetched from cache
        cache_get.assert_called_with(expected_key)
        place_fetch.assert_not_called()
        cache_set.assert_not_called()

    @mock.patch('brainzutils.cache.get')
    @mock.patch('brainzutils.cache.set')
    @mock.patch('brainzutils.musicbrainz_db.recording.get_recording_by_mbid')
    def test_recording_cache(self, recording_fetch, cache_set, cache_get):
        mbid = "442ddce2-ffa1-4865-81d2-b42c40fec7c5"
        expected_key = b"recording_442ddce2-ffa1-4865-81d2-b42c40fec7c5"
        recording = {
            'id': '442ddce2-ffa1-4865-81d2-b42c40fec7c5',
            'name': 'Dream Come True',
            'length': 229.0,
            'artists': [
                {
                    'id': '164f0d73-1234-4e2c-8743-d77bf2191051',
                    'name': 'Kanye West',
                    'join_phrase': ' feat. '
                },
                {
                    'id': '75a72702-a5ef-4513-bca5-c5b944903546',
                    'name': 'John Legend'
                }
            ],
            'artist-credit-phrase': 'Kanye West feat. John Legend'
        }
        recording_fetch.return_value = recording

        cache_get.return_value = None
        get_recording_by_id(mbid)

        # Test that first time data is fetched database is queried
        cache_get.assert_called_with(expected_key)
        recording_fetch.assert_called_with(mbid, includes=['artists', 'work-rels', 'url-rels'])
        cache_set.assert_called_with(key=expected_key, val=recording, time=DEFAULT_CACHE_EXPIRATION)

        cache_get.return_value = recording
        cache_set.reset_mock()
        recording_fetch.reset_mock()
        get_recording_by_id(mbid)

        # Test that second time data is fetched from cache
        cache_get.assert_called_with(expected_key)
        recording_fetch.assert_not_called()
        cache_set.assert_not_called()

    @mock.patch('brainzutils.cache.get')
    @mock.patch('brainzutils.cache.set')
    @mock.patch('brainzutils.musicbrainz_db.release.get_release_by_id')
    def test_release_cache(self, release_fetch, cache_set, cache_get):
        mbid = "16bee711-d7ce-48b0-adf4-51f124bcc0df"
        expected_key = b"release_16bee711-d7ce-48b0-adf4-51f124bcc0df"
        release = {
            "id": "16bee711-d7ce-48b0-adf4-51f124bcc0df",
            "name": "Numb/Encore",
            "medium-list": [{
                "track_list": [{
                    "id": "dfe024b2-95b2-453f-b03e-3b9fa06f44e6",
                    "name": "Numb/Encore (explicit)",
                    "number": "1",
                    "position": 1,
                    "length": 207000,
                    "recording_id": "daccb724-8023-432a-854c-e0accb6c8678",
                    "recording_title": "Numb/Encore (explicit)"
                }]
            }]
        }
        release_fetch.return_value = release

        cache_get.return_value = None
        get_release_by_id(mbid)

        # Test that first time data is fetched database is queried
        cache_get.assert_called_with(expected_key)
        release_fetch.assert_called_with(mbid, includes=['media', 'release-groups'], unknown_entities_for_missing=True)
        cache_set.assert_called_with(key=expected_key, val=release, time=DEFAULT_CACHE_EXPIRATION)

        cache_get.return_value = release
        cache_set.reset_mock()
        release_fetch.reset_mock()
        get_release_by_id(mbid)

        # Test that second time data is fetched from cache
        cache_get.assert_called_with(expected_key)
        release_fetch.assert_not_called()
        cache_set.assert_not_called()

    @mock.patch('brainzutils.cache.get')
    @mock.patch('brainzutils.cache.set')
    @mock.patch('brainzutils.musicbrainz_db.release_group.get_release_group_by_id')
    def test_release_group_cache(self, release_group_fetch, cache_set, cache_get):
        mbid = "7c1014eb-454c-3867-8854-3c95d265f8de"
        expected_key = b"release-group_7c1014eb-454c-3867-8854-3c95d265f8de"
        release_group = {
            'id': '7c1014eb-454c-3867-8854-3c95d265f8de',
            'title': 'Numb/Encore',
            'artist-credit-phrase': 'Jay-Z/Linkin Park',
            'artist-credit': [{
                'name': 'Jay-Z',
                'artist': {
                    'id': 'f82bcf78-5b69-4622-a5ef-73800768d9ac',
                    'name': 'JAY Z',
                    'sort_name': 'JAY Z'
                },
                'join_phrase': '/',
            }]
        }
        release_group_fetch.return_value = release_group

        cache_get.return_value = None
        get_release_group_by_id(mbid)

        # Test that first time data is fetched database is queried
        cache_get.assert_called_with(expected_key)
        release_group_fetch.assert_called_with(mbid,
                                               includes=['artists', 'releases', 'release-group-rels', 'url-rels', 'tags'],
                                               unknown_entities_for_missing=True)
        cache_set.assert_called_with(key=expected_key, val=release_group, time=DEFAULT_CACHE_EXPIRATION)

        cache_get.return_value = release_group
        cache_set.reset_mock()
        release_group_fetch.reset_mock()
        get_release_group_by_id(mbid)

        # Test that second time data is fetched from cache
        cache_get.assert_called_with(expected_key)
        release_group_fetch.assert_not_called()
        cache_set.assert_not_called()

    @mock.patch('brainzutils.cache.get')
    @mock.patch('brainzutils.cache.set')
    @mock.patch('brainzutils.musicbrainz_db.work.get_work_by_id')
    def test_work_cache(self, work_fetch, cache_set, cache_get):
        mbid = "54ce5e07-2aca-4578-83d8-5a41a7b2f434"
        expected_key = b"work_54ce5e07-2aca-4578-83d8-5a41a7b2f434"
        work = {
            "id": "54ce5e07-2aca-4578-83d8-5a41a7b2f434",
            "name": "a lot",
            "type": "Song",
        }
        work_fetch.return_value = work

        cache_get.return_value = None
        get_work_by_id(mbid)

        # Test that first time data is fetched database is queried
        cache_get.assert_called_with(expected_key)
        work_fetch.assert_called_with(mbid, includes=['artist-rels', 'recording-rels'])
        cache_set.assert_called_with(key=expected_key, val=work, time=DEFAULT_CACHE_EXPIRATION)

        cache_get.return_value = work
        cache_set.reset_mock()
        work_fetch.reset_mock()
        get_work_by_id(mbid)

        # Test that second time data is fetched from cache
        cache_get.assert_called_with(expected_key)
        work_fetch.assert_not_called()
        cache_set.assert_not_called()
