import json


class KincoVar:
    name: str = None
    address: str = None
    type: str = None
    comment: str = ""

    def __init__(self, name: str=None,
                 address: str=None,
                 type: str=None,
                 comment: str=""
    ) -> None:
        self.name = name
        self.address = address
        self.type = type
        self.comment = comment

    def to_dict(self) -> dict:
        if self.name is None or self.address is None or self.type is None:
            raise Exception("Called to_dict on a non defined KincoVar")
        return {
            "name": self.name,
            "address": self.address,
            "type": self.type,
            "comment": self.comment
        }
    
    def __str__(self) -> str:
        return json.dumps(self.to_dict(), indent=2)
    