[
    {
        "id": "85321044.951f9",
        "type": "tab",
        "label": "Flow 3"
    },
    {
        "id": "e083a35b.2b4c1",
        "type": "inject",
        "z": "85321044.951f9",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": true,
        "x": 150,
        "y": 80,
        "wires": [
            [
                "2a1f5d52.6e9422"
            ]
        ]
    },
    {
        "id": "2a1f5d52.6e9422",
        "type": "function",
        "z": "85321044.951f9",
        "name": "payload",
        "func": "msg.headers={\n    deviceKey: \"aEt17PHFXNbXAtsR\"\n};\nmsg.payload= \"Temperature,,25.5\"\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 354,
        "y": 100,
        "wires": [
            [
                "6fad5412.694e2c"
            ]
        ]
    },
    {
        "id": "6fad5412.694e2c",
        "type": "http request",
        "z": "85321044.951f9",
        "name": "",
        "method": "POST",
        "ret": "txt",
        "url": "https://api.mediatek.com/mcs/v2/devices/D0XKGXpv/datapoints.csv",
        "tls": "",
        "x": 530,
        "y": 100,
        "wires": [
            [
                "396815de.fe3ffa",
                "27acad39.8f2242"
            ]
        ]
    },
    {
        "id": "396815de.fe3ffa",
        "type": "http response",
        "z": "85321044.951f9",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 723,
        "y": 115,
        "wires": []
    },
    {
        "id": "27acad39.8f2242",
        "type": "debug",
        "z": "85321044.951f9",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "false",
        "x": 614,
        "y": 242,
        "wires": []
    }
]
