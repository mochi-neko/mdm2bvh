from typing import List
import numpy as np

from mdm2bvh.bone import Bone
from mdm2bvh.bvh_writer import write_bvh
from mdm2bvh.motion_converter import calculate_root_offset, calculate_joint_offset, calculate_root_motion, \
    calculate_joint_motion
from mdm2bvh.structure_info import StructureInfo, default_structure_info


def create_hierarchy(
        npy_motion: List[List[List[float]]],
        info: StructureInfo
) -> List[Bone]:
    bones = []
    for joint_index in range(len(npy_motion)):
        name = info.index_to_name_map[joint_index]
        if name == info.root_name:
            bones.append(Bone(
                name=name,
                is_root=True,
                offset=calculate_root_offset(npy_motion, joint_index, info.scale),
                channels=info.root_channels,
                children=info.name_to_children_map[name],
                motion_data=[],
            ))
        else:
            parent_index = info.index_to_parent_index_map[joint_index]
            bones.append(Bone(
                name=name,
                is_root=False,
                offset=calculate_joint_offset(npy_motion, joint_index, parent_index, info.scale),
                channels=info.joint_channels,
                children=info.name_to_children_map[name],
                motion_data=[],
            ))

    return bones


def calculate_motions(
        npy_motion: List[List[List[float]]],
        hierarchy: List[Bone],
        info: StructureInfo,
):
    root_index = info.root_index
    root = hierarchy[info.root_index]
    standard_index = info.root_rotation_standard_joint_index
    for frame_index in range(len(npy_motion[0][0])):
        root_position = [
            npy_motion[root_index][0][frame_index],
            npy_motion[root_index][1][frame_index],
            npy_motion[root_index][2][frame_index],
        ]
        # NOTE: Root direction is calculated as relative direction for standard joint
        # then standard joint cannot rotate for root
        root_direction = [
            npy_motion[standard_index][0][frame_index] - root_position[0],
            npy_motion[standard_index][1][frame_index] - root_position[1],
            npy_motion[standard_index][2][frame_index] - root_position[2],
        ]
        calculate_root_motion(
            root,
            root_position,
            root_direction,
            info.rotation_order,
        )
        for child in root.children:
            calculate_motion_recursively(
                npy_motion,
                hierarchy,
                info,
                joint_index=info.name_to_index_map[child],
                parent_position=root_position,
                parent_direction=root_direction,
                frame_index=frame_index,
            )


def calculate_motion_recursively(
        npy_motion: List[List[List[float]]],
        hierarchy: List[Bone],
        info: StructureInfo,
        joint_index: int,
        parent_position: List[float],
        parent_direction: List[float],
        frame_index: int,
):
    joint = hierarchy[joint_index]
    joint_motion = npy_motion[joint_index]
    joint_position = [
        joint_motion[0][frame_index],
        joint_motion[1][frame_index],
        joint_motion[2][frame_index],
    ]

    joint_direction = calculate_joint_motion(
        joint,
        joint_position,
        parent_position,
        parent_direction,
        info.rotation_order,
    )

    # Recursion into children
    for child in joint.children:
        calculate_motion_recursively(
            npy_motion,
            hierarchy,
            info,
            info.name_to_index_map[child],
            joint_position,
            joint_direction,
            frame_index,
        )


def convert_npy_to_bvh(
        npy_file: str,
        output_file: str,
        seconds_per_frame: float,
        repetition_index: int = 0,
        info: StructureInfo = default_structure_info(),
):
    data = np.load(npy_file, allow_pickle=True)
    data_dictionary = dict(enumerate(data.flatten()))[0]
    data_dictionary["motion"] = data_dictionary["motion"].tolist()
    npy_motion = data_dictionary["motion"][repetition_index]
    hierarchy = create_hierarchy(npy_motion, info)
    calculate_motions(npy_motion, hierarchy, info)
    write_bvh(
        output_file=output_file,
        hierarchy=hierarchy,
        number_of_frames=len(data_dictionary["motion"][0][0][0]),
        seconds_per_frame=seconds_per_frame,
    )
