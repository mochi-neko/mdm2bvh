from typing import List

from src.mdm2bvh.humanoid_skeleton import Bone


def template() -> List[Bone]:
    return [
        Bone(
            name="Hips",
            is_root=True,
            offset=[0.0, 0.0, 0.0],
            channels=["Xposition", "Yposition", "Zposition", "Zrotation", "Yrotation", "Xrotation"],
            children=["Spine", "LeftUpperLeg", "RightUpperLeg"],
            motion_data=[
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            ],
        ),
        Bone(
            name="Spine",
            is_root=False,
            offset=[0.0, 0.0, 0.0],
            channels=["Zrotation", "Yrotation", "Xrotation"],
            children=["Chest"],
            motion_data=[
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0],
            ],
        ),
        Bone(
            name="Chest",
            is_root=False,
            offset=[0.0, 0.0, 0.0],
            channels=["Zrotation", "Yrotation", "Xrotation"],
            children=["UpperChest"],
            motion_data=[
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0],
            ],
        ),
        Bone(
            name="UpperChest",
            is_root=False,
            offset=[0.0, 0.0, 0.0],
            channels=["Zrotation", "Yrotation", "Xrotation"],
            children=["Neck", "RightShoulder", "LeftShoulder"],
            motion_data=[
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0],
            ],
        ),
        Bone(
            name="Neck",
            is_root=False,
            offset=[0.0, 0.0, 0.0],
            channels=["Zrotation", "Yrotation", "Xrotation"],
            children=["Head"],
            motion_data=[
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0],
            ],
        ),
        Bone(
            name="Head",
            is_root=False,
            offset=[0.0, 0.0, 0.0],
            channels=["Zrotation", "Yrotation", "Xrotation"],
            children=[],
            motion_data=[
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0],
            ],
        ),
        Bone(
            name="LeftShoulder",
            is_root=False,
            offset=[0.0, 0.0, 0.0],
            channels=["Zrotation", "Yrotation", "Xrotation"],
            children=["LeftUpperArm"],
            motion_data=[
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0],
            ],
        ),
        Bone(
            name="LeftUpperArm",
            is_root=False,
            offset=[0.0, 0.0, 0.0],
            channels=["Zrotation", "Yrotation", "Xrotation"],
            children=["LeftLowerArm"],
            motion_data=[
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0],
            ],
        ),
        Bone(
            name="LeftLowerArm",
            is_root=False,
            offset=[0.0, 0.0, 0.0],
            channels=["Zrotation", "Yrotation", "Xrotation"],
            children=["LeftHand"],
            motion_data=[
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0],
            ],
        ),
        Bone(
            name="LeftHand",
            is_root=False,
            offset=[0.0, 0.0, 0.0],
            channels=["Zrotation", "Yrotation", "Xrotation"],
            children=[],
            motion_data=[
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0],
            ],
        ),
        Bone(
            name="RightShoulder",
            is_root=False,
            offset=[0.0, 0.0, 0.0],
            channels=["Zrotation", "Yrotation", "Xrotation"],
            children=["RightUpperArm"],
            motion_data=[
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0],
            ],
        ),
        Bone(
            name="RightUpperArm",
            is_root=False,
            offset=[0.0, 0.0, 0.0],
            channels=["Zrotation", "Yrotation", "Xrotation"],
            children=["RightLowerArm"],
            motion_data=[
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0],
            ],
        ),
        Bone(
            name="RightLowerArm",
            is_root=False,
            offset=[0.0, 0.0, 0.0],
            channels=["Zrotation", "Yrotation", "Xrotation"],
            children=["RightHand"],
            motion_data=[
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0],
            ],
        ),
        Bone(
            name="RightHand",
            is_root=False,
            offset=[0.0, 0.0, 0.0],
            channels=["Zrotation", "Yrotation", "Xrotation"],
            children=[],
            motion_data=[
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0],
            ],
        ),
        Bone(
            name="LeftUpperLeg",
            is_root=False,
            offset=[0.0, 0.0, 0.0],
            channels=["Zrotation", "Yrotation", "Xrotation"],
            children=["LeftLowerLeg"],
            motion_data=[
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0],
            ],
        ),
        Bone(
            name="LeftLowerLeg",
            is_root=False,
            offset=[0.0, 0.0, 0.0],
            channels=["Zrotation", "Yrotation", "Xrotation"],
            children=["LeftFoot"],
            motion_data=[
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0],
            ],
        ),
        Bone(
            name="LeftFoot",
            is_root=False,
            offset=[0.0, 0.0, 0.0],
            channels=["Zrotation", "Yrotation", "Xrotation"],
            children=["LeftToe"],
            motion_data=[
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0],
            ],
        ),
        Bone(
            name="LeftToe",
            is_root=False,
            offset=[0.0, 0.0, 0.0],
            channels=["Zrotation", "Yrotation", "Xrotation"],
            children=[],
            motion_data=[
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0],
            ],
        ),
        Bone(
            name="RightUpperLeg",
            is_root=False,
            offset=[0.0, 0.0, 0.0],
            channels=["Zrotation", "Yrotation", "Xrotation"],
            children=["RightLowerLeg"],
            motion_data=[
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0],
            ],
        ),
        Bone(
            name="RightLowerLeg",
            is_root=False,
            offset=[0.0, 0.0, 0.0],
            channels=["Zrotation", "Yrotation", "Xrotation"],
            children=["RightFoot"],
            motion_data=[
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0],
            ],
        ),
        Bone(
            name="RightFoot",
            is_root=False,
            offset=[0.0, 0.0, 0.0],
            channels=["Zrotation", "Yrotation", "Xrotation"],
            children=["RightToe"],
            motion_data=[
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0],
            ],
        ),
        Bone(
            name="RightToe",
            is_root=False,
            offset=[0.0, 0.0, 0.0],
            channels=["Zrotation", "Yrotation", "Xrotation"],
            children=[],
            motion_data=[
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0],
            ],
        ),
    ]
