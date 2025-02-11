from brainzutils import cache
from brainzutils.musicbrainz_db import work as db

from critiquebrainz.frontend.external.musicbrainz_db import DEFAULT_CACHE_EXPIRATION


def get_work_by_id(mbid):
    """Get work with MusicBrainz ID.

    Args:
        mbid (uuid): MBID(gid) of the work.
    Returns:
        Dictionary containing the work information
    """
    key = cache.gen_key('work', mbid)
    work = cache.get(key)
    if not work:
        work = db.get_work_by_id(
            mbid,
            includes=['artist-rels', 'recording-rels'],
        )
        cache.set(key=key, val=work, time=DEFAULT_CACHE_EXPIRATION)
    return work
