from typing import Optional

from m5.util import inform

from m5.objects.ArmSystem import ArmDefaultRelease
from m5.objects.RealView import (
    VExpress_GEM5_V1,
    VExpress_GEM5_Foundation,
)

from gem5.utils.override import overrides
from gem5.components.boards.arm_board import ArmBoard

from ..modifiable import MetaModifiable


class FullSystemArmBoard(ArmBoard, metaclass=MetaModifiable):
    def __init__(
        self,
        clk_freq: str,
        processor,
        cache_hierarchy,
        memory,
        use_kvm: bool = False,
        boot_interactive: bool = False,
        no_systemd: bool = False,
    ):
        release = (
            ArmDefaultRelease().for_kvm() if use_kvm else ArmDefaultRelease()
        )
        platform = (
            VExpress_GEM5_V1() if use_kvm else VExpress_GEM5_Foundation()
        )
        super().__init__(
            clk_freq, processor, memory, cache_hierarchy, platform, release
        )
        self._boot_interactive = boot_interactive
        self._no_systemd = no_systemd

    @overrides(ArmBoard)
    def get_default_kernel_args(self):
        tail = ["interactive"] if self._boot_interactive else []
        tail += ["no_systemd"] if self._no_systemd else []
        return [
            "console=ttyAMA0",
            "lpj=19988480",
            "norandmaps",
            "root={root_value}",
            "rw",
            f"mem={self.get_memory().get_size()}",
        ] + tail
