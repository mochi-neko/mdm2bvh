from typing import List, Dict, Optional
import numpy as np

from src.mdm2bvh.bone import Bone
from src.mdm2bvh.bvh_writer import write_bvh
from src.mdm2bvh.motion_converter import calculate_root_offset, calculate_joint_offset, calculate_joint_motions, \
    calculate_root_motions
from src.mdm2bvh.structure_info import StructureInfo, default_structure_info


def find_parent_name(
        name_to_children_map: Dict[str, List[str]],
        name: str,
) -> Optional[str]:
    for parent_name, children in name_to_children_map.items():
        if name in children:
            return parent_name
    return None


def find_parent_index(
        index_to_name_map: Dict[int, str],
        name_to_children_map: Dict[str, List[str]],
        index: int,
) -> Optional[int]:
    name = index_to_name_map[index]
    parent_name = find_parent_name(name_to_children_map, name)
    if parent_name is None:
        return None
    for parent_index, parent_name in index_to_name_map.items():
        if parent_name == parent_name:
            return parent_index
    return None


def create_skeleton(
        npy: Dict,
        info: StructureInfo
) -> List[Bone]:
    npy_motion = npy["motion"][0]
    bones = []
    for joint_index in range(len(npy_motion)):
        name = info.index_to_name_map[joint_index]
        if name == info.root_name:
            bones.append(Bone(
                name=name,
                is_root=True,
                offset=calculate_root_offset(npy_motion, joint_index),
                channels=info.root_channels,
                children=info.name_to_children_map[name],
                motion_data=calculate_root_motions(
                    npy_motion,
                    joint_index,
                    info.rotation_order),
            ))
        else:
            parent_index = find_parent_index(info.index_to_name_map, info.name_to_children_map, joint_index)
            bones.append(Bone(
                name=name,
                is_root=False,
                offset=calculate_joint_offset(npy_motion, joint_index, parent_index),
                channels=info.joint_channels,
                children=info.name_to_children_map[name],
                motion_data=calculate_joint_motions(
                    npy_motion,
                    joint_index,
                    parent_index,
                    info.rotation_order),
            ))

    return bones


def mdm2bvh(
        npy_file: str,
        output_file: str,
        seconds_per_frame: float,
        info: StructureInfo = default_structure_info(),
):
    data = np.load(npy_file, allow_pickle=True)
    data_dictionary = dict(enumerate(data.flatten()))[0]
    data_dictionary["motion"] = data_dictionary["motion"].tolist()
    skeleton = create_skeleton(data_dictionary, info)
    write_bvh(
        output_file=output_file,
        skeleton=skeleton,
        number_of_frames=len(data_dictionary["motion"][0][0][0]),
        seconds_per_frame=seconds_per_frame,
    )


if __name__ == '__main__':
    source_npy_file = 'results.npy'
    output_bvh_file = 'results.bvh'
    seconds_per_frame = 1 / 30
    mdm2bvh(source_npy_file, output_bvh_file, seconds_per_frame)
