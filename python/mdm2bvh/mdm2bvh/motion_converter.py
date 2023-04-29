from typing import List

import numpy as np
from scipy.spatial.transform import Rotation as R


def calculate_root_offset(
        npy_motion: List[List[List[float]]],
        root_index: int,
        scale: float
) -> List[float]:
    root = npy_motion[root_index]
    return [
        root[0][0] * scale,  # World X position of root at 0 frame
        root[1][0] * scale,  # World Y position of root at 0 frame
        root[2][0] * scale,  # World Z position of root at 0 frame
    ]


def calculate_joint_offset(
        npy_motion: List[List[List[float]]],
        joint_index: int,
        parent_index: int,
        scale: float
) -> List[float]:
    joint = npy_motion[joint_index]
    parent = npy_motion[parent_index]
    return [
        (joint[0][0] - parent[0][0]) * scale,  # Local X position of joint at 0 frame
        (joint[1][0] - parent[1][0]) * scale,  # Local Y position of joint at 0 frame
        (joint[2][0] - parent[2][0]) * scale,  # Local Z position of joint at 0 frame
    ]


def calculate_root_motions(
        npy_motion: List[List[List[float]]],
        root_index: int,
        rotation_order: str
) -> List[List[float]]:
    motions = []
    root = npy_motion[root_index]
    number_of_frames = len(npy_motion[0][0])
    for frame in range(number_of_frames):
        root_position = [root[0][frame], root[1][frame], root[2][frame]]
        euler_angles = position_to_euler_angles(
            parent_position=[0, 0, 0],
            child_position=root_position,
            rotation_order=rotation_order
        )
        motions.append(
            [
                root_position[0],  # X position at frame
                root_position[1],  # Y position at frame
                root_position[2],  # Z position at frame
                euler_angles[0],  # first rotation at frame
                euler_angles[1],  # second rotation at frame
                euler_angles[2],  # third rotation at frame
            ]
        )
    return motions


def calculate_joint_motions(
        npy_motion: List[List[List[float]]],
        joint_index: int,
        parent_index: int,
        rotation_order='ZYX'
) -> List[List[float]]:
    motions = []
    joint = npy_motion[joint_index]
    parent = npy_motion[parent_index]
    number_of_frames = len(npy_motion[0][0])
    for frame in range(number_of_frames):
        motions.append(
            position_to_euler_angles(
                parent_position=[parent[0][frame], parent[1][frame], parent[2][frame]],
                child_position=[joint[0][frame], joint[1][frame], joint[2][frame]],
                rotation_order=rotation_order
            ))
    return motions


def position_to_euler_angles(
        parent_position: List[float],
        child_position: List[float],
        rotation_order="ZYX"
) -> List[float]:
    # Calculate direction vector from parent to child
    vec1 = np.array(parent_position)
    vec2 = np.array(child_position)
    vec = vec2 - vec1
    vec = vec / np.linalg.norm(vec)

    # Calculate angles from direction vector
    yaw = np.arctan2(vec[1], vec[0])
    pitch = np.arctan2(-vec[2], np.sqrt(vec[0] ** 2 + vec[1] ** 2))

    # Convert angles to euler angles with rotation order
    rotation = R.from_euler(rotation_order, [yaw, pitch, 0])
    euler_angles = rotation.as_euler(rotation_order)
    euler_angles_degrees = np.degrees(euler_angles)

    return [
        euler_angles_degrees[0],
        euler_angles_degrees[1],
        euler_angles_degrees[2]
    ]
