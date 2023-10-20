import os


class AllDatas:
    playerTitles = ['video1', 'video2', 'video3', 'video4', 'video5', 'video6', 'video7', 'video8', 'video9',
                    'black1', 'black2', 'sinxra']
    player = ["player1", "player2", "player3", "player4", "player5", "player6", "player7", "player8", "player9"]
    playerTitleCIF = ['CIF']
    player_800_x_450 = ['video_eq']
    black = ["player10" "player11"]
    mosaics_with_count_participants = {"50": 1, "10": 2, "11": 3, "17": 3, "1": 4, "2": 9, "6": 16, "7": 25, "36": 36,
                                       "49": 49, "5": 6, "4": 8, "52": 10, "27": 12, "31": 7, "16": 10, "15": 10, "22": 11,
                                       "23": 14, "18": 13, "8": 13, "9": 13, "25": 13, "19": 17, "37": 17, "29": 21,
                                       "34": 22, "38": 6, "3": 7, "14": 10, "24": 10, "26": 10, "28": 20, "35": 19,
                                       "40": 26, "108": 10, "105": 10, "106": 10}
    mosaics = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "14", "15", "16", "17", "18", "19", "22", "23",
               "24", "25", "26", "27", "28", "29", "31", "34", "35", "36", "37", "38", "40", "49", "50", "52", "105",
               "106", "108"]

    title_mosaic = {'auto':'108', 'auto-equal': '105', 'one': '50',
                    '2p': '10' , '3p': '11', 'p3': '17',
                    '4p': '1', '9p': '2', '16p': '6',
                    '25p': '7', '36p': '36', '49p': '49',
                    'auto-focus': '106', '1v5': '5', '1v7': '4',
                    '1v9': '52', '1d7': '31', '1d9': '16',
                    '9on1': '15', '10on1': '22', '13on1': '23',
                    '12v1': '18', '1v4': '8', '4v1': '9',
                    '1v12': '25', '16v1': '19', '1v16': '37',
                    '1v20': '29', '1v21': '34', '2v4': '38',
                    '3v4': '3', '2p8': '14', '2ptop8': '24',
                    '8v2': '26', '2v18': '28', '2v17': '35',
                    '2v4v15v4v1': '40', '1v11': '27'}
    
    @staticmethod
    def set_env_variable(key: str, default_value: str) -> str:
        if not(os.environ.get(key) is None):
            return str(os.environ.get(key))
        else:
            return default_value 


ip_server = AllDatas.set_env_variable(key='SERVER_IP', default_value='10.1.0.11')
login = AllDatas.set_env_variable(key='LOGIN',default_value='admin')
password = AllDatas.set_env_variable(key='PASSWORD',default_value='123456')

second_ip = AllDatas.set_env_variable(key='SECOND_IP',default_value='10.1.0.13')
second_login = AllDatas.set_env_variable(key='SECOND_LOGIN',default_value='10.1.0.13')
second_password = AllDatas.set_env_variable(key='SECOND_PASSWORD', default_value='123456')

call_ip = AllDatas.set_env_variable(key='CALL_IP', default_value='10.1.0.117:4567')
ip_call_number = AllDatas.set_env_variable(key='IP_CALL_NUMBER', default_value='10.23.9.59')
sleep = 0.3 

screenshots = AllDatas.set_env_variable(key='SCREENSHOTS', default_value='new')
ui_browser = AllDatas.set_env_variable(key='UI_BROWSER', default_value='local')
