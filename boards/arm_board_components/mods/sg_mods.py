from .update_path import update_path

update_path()


from components.cmn import (
    CMNL1CacheConfigModifier,
    CMNL2CacheConfigModifier,
    CMNSystemCacheConfigModifier,
    CMNDMARequestorModifier,
    CMNDataSeqTypeModifier,
    CMNInstSeqTypeModifier,
    CMNDMASeqTypeModifier,
    CMNSysSeqTypeModifier,
)

from components.modifier import ModifierBundle


def get_bundle_from_version(version: int) -> ModifierBundle:
    return bundle_version[version]


bundle_version = {
    0: ModifierBundle(
        [
            CMNL1CacheConfigModifier(
                alloc_for_ind_index=False,
                alloc_for_ind_value=True,
            ),
            CMNL2CacheConfigModifier(
                alloc_for_ind_index=False,
                alloc_for_ind_value=True,
            ),
            CMNSystemCacheConfigModifier(
                alloc_for_ind_index=True,
                alloc_for_ind_value=False,
            ),
            CMNDMARequestorModifier(
                alloc_for_ind_index=False, alloc_for_ind_value=False
            ),
            CMNDataSeqTypeModifier(),
            CMNInstSeqTypeModifier(),
            CMNDMASeqTypeModifier(),
            CMNSysSeqTypeModifier(),
        ]
    ),
}
