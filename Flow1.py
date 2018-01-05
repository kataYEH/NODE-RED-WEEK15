[
    {
        "id": "72a890cd.4ba68",
        "type": "tab",
        "label": "Flow 1",
        "disabled": false
    },
    {
        "id": "55b52757.cc9418",
        "type": "rpi-gpio in",
        "z": "72a890cd.4ba68",
        "name": "Button",
        "pin": "7",
        "intype": "up",
        "debounce": "25",
        "read": true,
        "x": 90,
        "y": 180,
        "wires": [
            [
                "dbde833b.8d91b",
                "82deed1.1643b1"
            ]
        ]
    },
    {
        "id": "dbde833b.8d91b",
        "type": "debug",
        "z": "72a890cd.4ba68",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "false",
        "x": 490,
        "y": 80,
        "wires": []
    },
    {
        "id": "fd5c788b.27fa78",
        "type": "rpi-gpio out",
        "z": "72a890cd.4ba68",
        "name": "LED",
        "pin": "12",
        "set": true,
        "level": "0",
        "freq": "",
        "out": "out",
        "x": 710,
        "y": 200,
        "wires": []
    },
    {
        "id": "82deed1.1643b1",
        "type": "switch",
        "z": "72a890cd.4ba68",
        "name": "",
        "property": "payload",
        "propertyType": "msg",
        "rules": [
            {
                "t": "eq",
                "v": "1",
                "vt": "str"
            },
            {
                "t": "else"
            }
        ],
        "checkall": "true",
        "outputs": 2,
        "x": 230,
        "y": 220,
        "wires": [
            [
                "95774852.b42f18"
            ],
            [
                "71d64e86.e34e3"
            ]
        ]
    },
    {
        "id": "95774852.b42f18",
        "type": "change",
        "z": "72a890cd.4ba68",
        "name": "0",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "0",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 450,
        "y": 220,
        "wires": [
            [
                "fd5c788b.27fa78"
            ]
        ]
    },
    {
        "id": "71d64e86.e34e3",
        "type": "change",
        "z": "72a890cd.4ba68",
        "name": "1",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "1",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 470,
        "y": 300,
        "wires": [
            [
                "fd5c788b.27fa78"
            ]
        ]
    }
]
