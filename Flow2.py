[
    {
        "id": "d21e97f8.af0f78",
        "type": "tab",
        "label": "Flow 2"
    },
    {
        "id": "eee35452.d143c8",
        "type": "inject",
        "z": "d21e97f8.af0f78",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": true,
        "x": 129,
        "y": 57,
        "wires": [
            [
                "6dc087b3.3ea0f8"
            ]
        ]
    },
    {
        "id": "6dc087b3.3ea0f8",
        "type": "function",
        "z": "d21e97f8.af0f78",
        "name": "payload",
        "func": "msg.headers={\n    deviceKey: \"aEt17PHFXNbXAtsR\"\n};\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 333,
        "y": 77,
        "wires": [
            [
                "913ac62e.3d9858"
            ]
        ]
    },
    {
        "id": "913ac62e.3d9858",
        "type": "http request",
        "z": "d21e97f8.af0f78",
        "name": "",
        "method": "GET",
        "ret": "txt",
        "url": "https://api.mediatek.com/mcs/v2/devices/D0XKGXpv/datachannels/Humidity/datapoints.csv",
        "tls": "",
        "x": 510,
        "y": 91,
        "wires": [
            [
                "a6a8410d.02181",
                "5dc39af0.3d1c54"
            ]
        ]
    },
    {
        "id": "a6a8410d.02181",
        "type": "http response",
        "z": "d21e97f8.af0f78",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 702,
        "y": 92,
        "wires": []
    },
    {
        "id": "5dc39af0.3d1c54",
        "type": "debug",
        "z": "d21e97f8.af0f78",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "false",
        "x": 593,
        "y": 219,
        "wires": []
    }
]
