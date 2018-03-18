"""mocks live here."""

LOGIN_RESPONSE = '''
        {
            "d": {
                "__type": "MyTagList.ethClient+TagManagerSettings",
                "postbackInterval": 600,
                "temp_unit": 0,
                "tzo": -120,
                "serverTime": 131650977888314263,
                "rev": 7,
                "limited": false,
                "rxFilter": 64,
                "optimizeForV2Tag": true,
                "freqTols": [
                    2000,
                    3000,
                    4000,
                    12000,
                    16000
                ],
                "phoneID": "121212121212",
                "loginEmail": null,
                "wsRoot": "https://my.wirelesstag.net/",
                "noWemoSearch": false
            }
        }
        '''


TAGS_LIST_RESPONSE = '''
        {
        "d": [
            {
                "__type": "MyTagList.Tag",
                "notificationJS": null,
                "name": "Kitchen",
                "uuid": "fake-1111-2222-3333-111111111111",
                "comment": "",
                "slaveId": 4,
                "tagType": 13,
                "lastComm": 131649791032183860,
                "alive": true,
                "signaldBm": -73,
                "batteryVolt": 3.056917542381937,
                "beeping": false,
                "lit": false,
                "migrationPending": false,
                "beepDurationDefault": 5,
                "eventState": 0,
                "tempEventState": 0,
                "OutOfRange": false,
                "lux": 0,
                "temperature": 19.849382400512695,
                "tempCalOffset": 0,
                "capCalOffset": 0,
                "image_md5": null,
                "cap": 45.9866943359375,
                "capRaw": 0,
                "az2": 0,
                "capEventState": 0,
                "lightEventState": 0,
                "shorted": false,
                "thermostat": null,
                "playback": null,
                "postBackInterval": 600,
                "rev": 111,
                "version1": 3,
                "freqOffset": 1,
                "freqCalApplied": 6527,
                "reviveEvery": 4,
                "oorGrace": 2,
                "LBTh": 2.55,
                "enLBN": true,
                "txpwr": 16,
                "rssiMode": false,
                "ds18": false,
                "v2flag": 26,
                "batteryRemaining": 0.97
            },
            {
                "__type": "MyTagList.Tag",
                "notificationJS": null,
                "name": "Hall",
                "uuid": "fake-1111-2222-4444-111111111111",
                "comment": "",
                "slaveId": 0,
                "tagType": 13,
                "lastComm": 131649788589728506,
                "alive": true,
                "signaldBm": -71,
                "batteryVolt": 3.05576890659684,
                "beeping": false,
                "lit": false,
                "migrationPending": false,
                "beepDurationDefault": 1001,
                "eventState": 0,
                "tempEventState": 0,
                "OutOfRange": false,
                "lux": 0,
                "temperature": 22.3912296295166,
                "tempCalOffset": 0,
                "capCalOffset": 0,
                "image_md5": null,
                "cap": 36.27447509765625,
                "capRaw": 0,
                "az2": 0,
                "capEventState": 0,
                "lightEventState": 0,
                "shorted": false,
                "thermostat": null,
                "playback": null,
                "postBackInterval": 600,
                "rev": 111,
                "version1": 3,
                "freqOffset": -357,
                "freqCalApplied": 7541,
                "reviveEvery": 4,
                "oorGrace": 2,
                "LBTh": 2.55,
                "enLBN": true,
                "txpwr": 16,
                "rssiMode": false,
                "ds18": false,
                "v2flag": 26,
                "batteryRemaining": 0.96
            }
        ]
    }
    '''

ARM_MOTION_RESPONSE = '''
    {
        "d": {
            "name": "Living room",
            "uuid": "fake-1111-2222-4444-111111111111",
            "slaveId": 1,
            "tagType": 13,
            "eventState": 1,
            "tempEventState": 0,
            "capEventState": 0,
            "lightEventState": 0,
            "temperature": 22.3912296295166,
            "lux": 0,
            "cap": 36.27447509765625
        }
    }
    '''

DISARM_MOTION_RESPONSE = '''
    {
        "d": {
            "name": "Living room",
            "uuid": "fake-1111-2222-4444-111111111111",
            "slaveId": 1,
            "tagType": 13,
            "eventState": 0,
            "tempEventState": 0,
            "capEventState": 0,
            "lightEventState": 0,
            "temperature": 22.3912296295166,
            "lux": 0,
            "cap": 36.27447509765625
        }
    }
    '''

ARM_TEMP_RESPONSE = '''
    {
        "d": {
            "name": "Living room",
            "uuid": "fake-1111-2222-4444-111111111111",
            "slaveId": 1,
            "tagType": 13,
            "eventState": 0,
            "tempEventState": 1,
            "capEventState": 0,
            "lightEventState": 0,
            "temperature": 22.3912296295166,
            "lux": 0,
            "cap": 36.27447509765625
        }
    }
    '''

DISARM_TEMP_RESPONSE = '''
    {
        "d": {
            "name": "Living room",
            "uuid": "fake-1111-2222-4444-111111111111",
            "slaveId": 1,
            "tagType": 13,
            "eventState": 0,
            "tempEventState": 0,
            "capEventState": 0,
            "lightEventState": 0,
            "temperature": 22.3912296295166,
            "lux": 0,
            "cap": 36.27447509765625
        }
    }
    '''

ARM_HUMIDITY_RESPONSE = '''
    {
        "d": {
            "name": "Living room",
            "uuid": "fake-1111-2222-4444-111111111111",
            "slaveId": 1,
            "tagType": 13,
            "eventState": 0,
            "tempEventState": 0,
            "capEventState": 2,
            "lightEventState": 0,
            "temperature": 22.3912296295166,
            "lux": 0,
            "cap": 36.27447509765625
        }
    }
    '''

DISARM_HUMIDITY_RESPONSE = '''
    {
        "d": {
            "name": "Living room",
            "uuid": "fake-1111-2222-4444-111111111111",
            "slaveId": 1,
            "tagType": 13,
            "eventState": 0,
            "tempEventState": 0,
            "capEventState": 0,
            "lightEventState": 0,
            "temperature": 22.3912296295166,
            "lux": 0,
            "cap": 36.27447509765625
        }
    }
    '''

ARM_LIGHT_RESPONSE = '''
    {
        "d": {
            "name": "Living room",
            "uuid": "fake-1111-2222-4444-111111111111",
            "slaveId": 1,
            "tagType": 13,
            "eventState": 0,
            "tempEventState": 0,
            "capEventState": 0,
            "lightEventState": 2,
            "temperature": 22.3912296295166,
            "lux": 0,
            "cap": 36.27447509765625
        }
    }
    '''

DISARM_LIGHT_RESPONSE = '''
    {
        "d": {
            "name": "Living room",
            "uuid": "fake-1111-2222-4444-111111111111",
            "slaveId": 1,
            "tagType": 13,
            "eventState": 0,
            "tempEventState": 0,
            "capEventState": 0,
            "lightEventState": 0,
            "temperature": 22.3912296295166,
            "lux": 0,
            "cap": 36.27447509765625
        }
    }
    '''
