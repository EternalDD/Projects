import time
import vk_api
timeOfSusPostsInterval = 30

class VkScan(object):
    def __init__(self):
        self.vk_session = vk_api.VkApi('user', 'pass')
        self.vk_session.auth(token_only=True)

        self.vk = self.vk_session.get_api()
        self.tools = vk_api.VkTools(self.vk_session)
        self.user_info_list = []


    def scan_one_user(self, OneUserDict):
        #Формируем словарь с показателями
        print(OneUserDict['id'])
        info_dict = {}
        info_dict['id'] = OneUserDict['id']
        info_dict['occupation'] = 1 if OneUserDict.get('occupation','')!= '' else 0
        info_dict['about'] = 1 if OneUserDict.get('about','')!= '' else 0
        info_dict['activities'] = 1 if OneUserDict.get('activities','')!= '' else 0
        info_dict['bdate'] = 1 if OneUserDict.get('bdate','') != '' else 0
        info_dict['education'] = 1 if OneUserDict.get('education','') != '' else 0
        info_dict['exports'] = 1 if OneUserDict.get('exports','')!= '' else 0
        info_dict['has_photo'] = OneUserDict.get('has_photo','')
        info_dict['home_town'] = 1 if OneUserDict.get('home_town','')!= '' else 0
        info_dict['interests'] = 1 if OneUserDict.get('interests','')!= '' else 0
        info_dict['movies'] = 1 if OneUserDict.get('movies','')!= '' else 0
        info_dict['music'] = 1 if OneUserDict.get('music','')!= '' else 0
        info_dict['personal'] = 1 if OneUserDict.get('personal','')!= '' else 0
        info_dict['relation'] = 1 if OneUserDict.get('relation','')!= '' else 0
        info_dict['site'] = 1 if OneUserDict.get('site','')!= '' else 0
        info_dict['city'] = 1 if OneUserDict.get('city','')!= '' else 0
        if OneUserDict.get('counters', 0):
            info_dict['counter_videos'] = OneUserDict['counters'].get('videos',0) if OneUserDict['counters'].get('videos',0) else 0
            info_dict['counter_gifts'] = OneUserDict['counters'].get('gifts',0) if OneUserDict['counters'].get('gifts',0) else 0
            info_dict['counter_photos'] = OneUserDict['counters'].get('photos',0)if OneUserDict['counters'].get('photos',0) else 0
            info_dict['counter_notes'] = OneUserDict['counters'].get('notes',0) if OneUserDict['counters'].get('notes',0) else 0
            info_dict['counter_friends'] = OneUserDict['counters'].get('friends',0) if OneUserDict['counters'].get('friends',0) else 0
            info_dict['counter_groups'] = OneUserDict['counters'].get('groups',0) if OneUserDict['counters'].get('groups',0) else 0
            info_dict['counter_followers'] = OneUserDict['counters'].get('followers',0) if OneUserDict['counters'].get('followers',0) else 0
            info_dict['counter_pages'] = OneUserDict['counters'].get('pages',0) if OneUserDict['counters'].get('pages',0) else 0
        else:
            info_dict['counter_videos'] = -1
            info_dict['counter_gifts'] = -1
            info_dict['counter_photos'] = -1
            info_dict['counter_notes'] = -1
            info_dict['counter_friends'] = -1
            info_dict['counter_groups'] = -1
            info_dict['counter_followers'] = -1
            info_dict['counter_pages'] = -1

        #Сканируем количество подозрительных постов

        try:
            wall = self.tools.get_all('wall.get', 50, {'owner_id': OneUserDict['id']})
            info_dict['counter_WallPost'] = wall['count']
            numOfSusPosts = -1
            if wall['count']:
                prev_element = wall['items'][0]
                for element in wall['items']:
                    if prev_element['date'] - element['date'] < timeOfSusPostsInterval:
                        numOfSusPosts = numOfSusPosts + 1
                    prev_element = element
                info_dict['numOfSusPosts'] = numOfSusPosts
        except:
            info_dict['counter_WallPost'] = 0
            info_dict['numOfSusPosts'] = 0
        #Возвращаем слоарь
        return (info_dict)
    
        print(info_dict['numOfSusPosts'])
    def ScanUserList(self, UserIds):
        listOfScannedUsers = []
        for element in UserIds:
            time.sleep(0.5)
            user_info_list = self.vk.users.get(user_ids=element,
                                               fields="counters,occupation,about,activities,bdate,exports,has_photo,home_town,interests,movies,music,personal,relation,site,city")

            listOfScannedUsers.append(self.scan_one_user(user_info_list[0]))
        return(listOfScannedUsers)
    
