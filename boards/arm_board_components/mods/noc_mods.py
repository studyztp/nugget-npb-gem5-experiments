from .update_path import update_path

update_path()

from m5.params import NullSimObject
from m5.objects.Prefetcher import StridePrefetcher

from components.cmn import (
    CMNL1CacheConfigModifier,
    CMNL1DPrefetcherModifier,
    CMNL1IPrefetcherModifier,
    CMNL2PrefetcherModifier,
    CMNClusterLatModifier,
    CMNSystemLatModifier,
    CMNMemoryLatModifier,
    CMNDMALatModifier,
)

from components.modifier import ModifierBundle


def get_bundle_from_version(version: int) -> ModifierBundle:
    return bundle_version[version]


bundle_version = {
    0: ModifierBundle(
        [
            CMNL1DPrefetcherModifier(NullSimObject),
            CMNL1IPrefetcherModifier(NullSimObject),
            CMNL2PrefetcherModifier(NullSimObject),
            CMNClusterLatModifier(2, 1),
            CMNSystemLatModifier(2, 1),
            CMNMemoryLatModifier(10, 10),
            CMNDMALatModifier(10, 10),
        ]
    ),
    1: ModifierBundle(
        [
            CMNL1DPrefetcherModifier(StridePrefetcher, degree=4, latency=1),
            CMNL1IPrefetcherModifier(StridePrefetcher, degree=4, latency=1),
            CMNL2PrefetcherModifier(StridePrefetcher, degree=8, latency=1),
            CMNClusterLatModifier(2, 1),
            CMNSystemLatModifier(2, 1),
            CMNMemoryLatModifier(10, 10),
            CMNDMALatModifier(10, 10),
        ]
    ),
    2: ModifierBundle(
        [
            CMNL1CacheConfigModifier(alloc_on_seq_line_write=True),
            CMNL1DPrefetcherModifier(StridePrefetcher, degree=4, latency=1),
            CMNL1IPrefetcherModifier(StridePrefetcher, degree=4, latency=1),
            CMNL2PrefetcherModifier(StridePrefetcher, degree=8, latency=1),
            CMNClusterLatModifier(2, 1),
            CMNSystemLatModifier(2, 1),
            CMNMemoryLatModifier(10, 10),
            CMNDMALatModifier(10, 10),
        ]
    ),
}
