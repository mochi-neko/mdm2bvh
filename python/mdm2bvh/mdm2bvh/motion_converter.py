from typing import List
import numpy as np
from scipy.spatial.transform import Rotation as R

from mdm2bvh.bone import Bone


def calculate_root_offset(
        npy_motion: List[List[List[float]]],
        root_index: int,
        scale: float,
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
        scale: float,
) -> List[float]:
    joint = npy_motion[joint_index]
    parent = npy_motion[parent_index]
    return [
        (joint[0][0] - parent[0][0]) * scale,  # Local X position of joint at 0 frame
        (joint[1][0] - parent[1][0]) * scale,  # Local Y position of joint at 0 frame
        (joint[2][0] - parent[2][0]) * scale,  # Local Z position of joint at 0 frame
    ]


def calculate_root_motion(
        root: Bone,
        root_position: List[float],
        root_direction: List[float],
        rotation_order: str,
) -> List[float]:
    # Calculate root rotation
    euler_angles = from_to_rotation_euler_angles(
        from_direction=[0, 1, 0],  # World up direction
        to_direction=root_direction,
        rotation_order=rotation_order
    )

    # Write motion frame
    root.motion_data.append([
        root_position[0],
        root_position[1],
        root_position[2],
        euler_angles[0],
        euler_angles[1],
        euler_angles[2],
    ])

    return root_direction


def calculate_joint_motion(
        joint: Bone,
        joint_position: List[float],
        parent_position: List[float],
        parent_direction: List[float],
        rotation_order: str,
) -> List[float]:
    # Calculate joint direction
    joint_direction = [
        joint_position[0] - parent_position[0],
        joint_position[1] - parent_position[1],
        joint_position[2] - parent_position[2],
    ]

    # Calculate joint rotation from parent direction
    euler_angles = from_to_rotation_euler_angles(
        from_direction=parent_direction,
        to_direction=joint_direction,
        rotation_order=rotation_order
    )

    # Write motion frame
    joint.motion_data.append([
        euler_angles[0],
        euler_angles[1],
        euler_angles[2],
    ])

    return joint_direction


def from_to_rotation_euler_angles(
        from_direction: List[float],
        to_direction: List[float],
        rotation_order: str,
) -> List[float]:
    # Calculate normalized directions
    from_vec = np.array(from_direction)
    from_vec = from_vec / np.linalg.norm(from_vec)
    to_vec = np.array(to_direction)
    to_vec = to_vec / np.linalg.norm(to_vec)

    # Calculate angles from direction vectors
    rotation_axis = np.cross(from_vec, to_vec)
    rotation_angle = np.arccos(np.dot(from_vec, to_vec))  # dot = cos -> arccos(dot) = arccos(cos) = angle

    # Calculate rotation matrix
    rotation = R.from_rotvec(rotation_axis * rotation_angle)

    # Convert to euler angles with rotation order
    euler_angles = rotation.as_euler(rotation_order, degrees=True)

    return [
        euler_angles[0],
        euler_angles[1],
        euler_angles[2],
    ]
