from typing import List, Dict, Optional


class StructureInfo:
    def __init__(
            self,
            root_name: str,
            root_channels: List[str],
            joint_channels: List[str],
            index_to_name_map: Dict[int, str],
            name_to_children_map: Dict[str, List[str]],
            root_rotation_standard_joint_name: str,
            rotation_order: str,
            scale: float,
    ):
        self.root_name = root_name
        self.root_channels = root_channels
        self.joint_channels = joint_channels
        self.index_to_name_map = index_to_name_map
        self.name_to_children_map = name_to_children_map
        self.root_rotation_standard_joint_name = root_rotation_standard_joint_name
        self.rotation_order = rotation_order
        self.scale = scale

        # Build name to index map
        self.name_to_index_map = {name: index for index, name in self.index_to_name_map.items()}
        # Find root index
        self.root_index = self.name_to_index_map[root_name]
        # Find root rotation standard joint index
        self.root_rotation_standard_joint_index = self.name_to_index_map[root_rotation_standard_joint_name]
        # Build children index to parent index map
        self.index_to_parent_index_map = {}
        for parent_name, children in self.name_to_children_map.items():
            parent_index = self.name_to_index_map[parent_name]
            for child_name in children:
                child_index = self.name_to_index_map[child_name]
                self.index_to_parent_index_map[child_index] = parent_index


def default_structure_info() -> StructureInfo:
    return StructureInfo(
        root_name="Hips",
        root_channels=["Xposition", "Yposition", "Zposition", "Zrotation", "Xrotation", "Yrotation"],
        joint_channels=["Zrotation", "Xrotation", "Yrotation"],
        index_to_name_map={
            0: "Hips",
            1: "LeftUpperLeg",
            2: "RightUpperLeg",
            3: "Spine",
            4: "LeftLowerLeg",
            5: "RightLowerLeg",
            6: "Chest",
            7: "LeftFoot",
            8: "RightFoot",
            9: "UpperChest",
            10: "LeftToe",
            11: "RightToe",
            12: "Neck",
            13: "LeftShoulder",
            14: "RightShoulder",
            15: "Head",
            16: "LeftUpperArm",
            17: "RightUpperArm",
            18: "LeftLowerArm",
            19: "RightLowerArm",
            20: "LeftHand",
            21: "RightHand",
        },
        name_to_children_map={
            "Hips": ["Spine", "LeftUpperLeg", "RightUpperLeg"],
            "Spine": ["Chest"],
            "Chest": ["UpperChest"],
            "UpperChest": ["Neck", "LeftShoulder", "RightShoulder"],
            "Neck": ["Head"],
            "Head": [],
            "LeftShoulder": ["LeftUpperArm"],
            "LeftUpperArm": ["LeftLowerArm"],
            "LeftLowerArm": ["LeftHand"],
            "LeftHand": [],
            "RightShoulder": ["RightUpperArm"],
            "RightUpperArm": ["RightLowerArm"],
            "RightLowerArm": ["RightHand"],
            "RightHand": [],
            "LeftUpperLeg": ["LeftLowerLeg"],
            "LeftLowerLeg": ["LeftFoot"],
            "LeftFoot": ["LeftToe"],
            "LeftToe": [],
            "RightUpperLeg": ["RightLowerLeg"],
            "RightLowerLeg": ["RightFoot"],
            "RightFoot": ["RightToe"],
            "RightToe": [],
        },
        root_rotation_standard_joint_name="Spine",
        rotation_order="ZXY",
        scale=100.0,
    )
