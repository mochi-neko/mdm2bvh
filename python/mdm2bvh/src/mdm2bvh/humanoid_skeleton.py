from typing import List, Optional


class Bone:
    def __init__(
            self,
            name: str,
            is_root: bool,
            offset: List[float],
            channels: List[str],
            children: List[str],
            motion_data: List[List[float]],
    ):
        self.name = name
        self.is_root = is_root
        self.offset = offset
        self.channels = channels
        self.children = children
        self.motion_data = motion_data


def find_bone(skeleton: List[Bone], name: str) -> Optional[int]:
    for index, bone in enumerate(skeleton):
        if bone.name == name:
            return index
    return None
