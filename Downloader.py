#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Khamdihi Dev
# Open Jasa Bikin Script WhatsApp: +6283853140469

import requests, re, sys, os

class TikTok:

   def __init__(self, curl, file):
       self.ulul = curl
       self.file = file
       self.GetLinkVid()

   def GetLinkVid(self):
       with requests.Session() as self.r:
          try:
              self.cookies = {
                  'perf_feed_cache': '{%22expireTimestamp%22:1718632800000%2C%22itemIds%22:[%227379653241388240161%22%2C%227374213452182719749%22%2C%227352243264180849925%22]}',
                  'tt_chain_token': 'zcCEGW55CjWsgf6gIV9gHA==',
                  'msToken': 'k7t6WJduYGTivXgUPmh8At63JOlpNYUWt7egDaQ5_qiPSMRirWRcvGpO0bA7Jdnfwimq0caYvfhVN7P4zD29HpQntz6ue6nlwdCzQBhaItZTt3VN_ckou3IZgIsn',
                  'msToken': '1a8hsWMj2hqo1X5XeCKqspQzbH6PiG3hLfvUHP1vxK95mxrVhjOOxX53L4mCiJIdgj7EQ7u4MYNl5tlKBiizyUOVG6NMYZX8n_6XzTpLkkvHnMgSxR6fTXdWjchKLWTxGrwMPmHgSTrRDeZXknAKnES8',
                  'tt_csrf_token': 'F4h33dkH-Wee1KfLOU-0sLLke14J7ze5j5Lw',
                  'tiktok_webapp_theme': 'light',
                  'odin_tt': '1ef1485ae5eb6c9e79c9a0fc0700f8b891c91bd3621cc35044e6513de1e1b91979871b84bc93b8fe0681ae6158aae532f8ff60b3c16a60338a332d5021a1f567930d1e71b703e391979e814f6f13f51e',
                  's_v_web_id': 'verify_lxg8mwuv_1o3cv7zC_79mq_4UW7_8cg0_MIzj78s0HFfN',
                  'ak_bmsc': '977FC6BD96558B7D2601E82C6F0F1B32~000000000000000000000000000000~YAAQJw81F9StQBaQAQAAZotkHBjuZOKhBFSIU9NMhaUUpOWuK65SR5jlHRDKjDBUxiPHKWCP1Fc74zg6jTnpn7iyT9qc/n7BJNrWKabMPwIMnIP+jlZ7OUt1S4buTa9ITYqOWWyy0ohX/a9s7saWgHA1oU44/F789vGAbYEd10/QhUwGJOSGI3aIZqKih0pIxO+s/XdPrIjQb2Z0c+xrBQBWc9B/AIdnUscEWUCWeZOuM2NrtmdveIQhvgSdcrh2kUfhrRFFgJTAQoGU999tgFmey0MHUXGZxAka0iz/7ezNzwSknKFWfeHh0X02HDsseuLkyfUnqzECY6Q+wa6ddnh0mAWRS2KcU812K7r6nuEubjUUxLagS23YgrU81+b+6wLm+moL3w6tp7wa/sZFmnLcD+KuCdT6IPM=',
                  'bm_sv': '6B5B02E39BB24F60AF190ED9A1693720~YAAQJw81FzOvQBaQAQAALxVlHBg8W3Zgcj7NBZuoWopxY9vlmBshUFZc42gftAQp2Hp6cHX8ypjlpI6SHZs3jTP3VB2vkKrod6tLxUtXhIJCkaz0eFQv6VOC+JihMqKOmjbJXYzu7Dwh64q7xXD6uETJT2zix7Cb7FhmFnUVA5xsnAIiP21xDSkJ4xbHnsivGbQCTieW6xaPmAXDev4wNTXLIrNKTzq+7aVMrQJXWGyYoqO8T4FtPebJZ1g0KcGW~1',
                  'ttwid': '1%7Cag-HVdjDKIjq4KjjbxG7m6wva6CMARWQ98gbS2Nkj7s%7C1718463308%7C2816eeede5259dadb2d3da39c54d1779afdf7d24fe90537121c104df5816c377',
              }

              self.headers = {
                  'accept': '*/*',
                  'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                  'priority': 'u=1, i',
                  'referer': self.ulul,
                  'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
                  'sec-ch-ua-mobile': '?1',
                  'sec-ch-ua-platform': '"Android"',
                  'sec-fetch-dest': 'empty',
                  'sec-fetch-mode': 'cors',
                  'sec-fetch-site': 'same-origin',
                  'user-agent': 'Mozilla/5.0 (Linux; Android 12; Pixel 6 Build/SQ3A.220705.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/125.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.0.65;] Edg/125.0.0.0',
              }
              if 'video' not in str(self.ulul):
                  self.z = self.r.get(self.ulul, cookies=self.cookies, headers=self.headers).text
                  self.user = re.search('"share_item_id":"(\d+)"', str(self.z)).group(1)
              else:
                  self.user = re.search('video/(\d+)',str(self.ulul)).group(1)
              self.response = self.r.get(f'https://www.tiktok.com/api/item/detail/?aid=1988&app_id=1180&app_language=id-ID&app_name=tiktok_web&browser_language=id&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Linux%3B%20Android%2012%3B%20Pixel%206%20Build%2FSQ3A.220705.004%3B%20wv%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Version%2F4.0%20Chrome%2F125.0.0.0%20Mobile%20Safari%2F537.36%20%5BFB_IAB%2FFB4A%3BFBAV%2F407.0.0.0.65%3B%5D%20Edg%2F125.0.0.0&channel=tiktok_web&clientABVersions=70508271&clientABVersions=72139453&clientABVersions=72224360&clientABVersions=72313476&clientABVersions=72350765&clientABVersions=72372940&clientABVersions=72373487&clientABVersions=72375446&clientABVersions=72394777&clientABVersions=72402045&client_ab_versions=70508271&client_ab_versions=72139453&client_ab_versions=72224360&client_ab_versions=72313476&client_ab_versions=72350765&client_ab_versions=72372940&client_ab_versions=72373487&client_ab_versions=72375446&client_ab_versions=72394777&client_ab_versions=72402045&cookie_enabled=true&coverFormat=0&device_id=7380743124052411921&device_platform=web_mobile&focus_state=true&from_page=video&history_len=5&is_fullscreen=false&is_page_visible=true&itemId={self.user}&item_id={self.user}&language=id-ID&os=android&priority_region=&referer=&region=ID&screen_height=892&screen_width=412&sourceType=33&traffic_type=0&tz_name=Asia%2FJakarta&uCode=&u_code=&user_info_type=1&verifyFp=verify_lxg8mwuv_1o3cv7zC_79mq_4UW7_8cg0_MIzj78s0HFfN&web_id=7380743124052411921&webcast_language=id-ID', cookies=self.cookies, headers=self.headers).json()['itemInfo']['itemStruct']['video']['playAddr']
              self.download = requests.get(self.response,headers=self.headers, cookies=self.cookies)
              with open(self.file,'wb') as self.save:
                self.save.write(self.download.content)
              print('\nVidio di simpan di : %s'%(self.file))
          except Exception as Error:
              exit(f'\nTerjadi Kesalahan Saat Download vidio! {Error}')

class Facebook:

   def __init__(self, curl, files):
       self.file = files
       self.curl = curl
       self.GetLinkVid()

   def GetLinkVid(self):
       with requests.Session() as self.r:
          try:
              self.r.headers.update({
                  'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
                  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                  'cache-control': "max-age=0",
                  'dpr': "2",
                  'viewport-width': "980",
                  'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
                  'sec-ch-ua-mobile': "?0",
                  'sec-ch-ua-platform': "\"Linux\"",
                  'sec-ch-ua-platform-version': "\"\"",
                  'sec-ch-ua-model': "\"\"",
                  'sec-ch-ua-full-version-list': "\"Not-A.Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"124.0.6327.4\"",
                  'sec-ch-prefers-color-scheme': "light",
                  'upgrade-insecure-requests': "1",
                  'sec-fetch-site': "none",
                  'sec-fetch-mode': "navigate",
                  'sec-fetch-user': "?1",
                  'sec-fetch-dest': "document",
                  'accept-language': "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                  'Cookie': "datr=NQBrZqK7kYSWffNlzIXJtFZf; sb=NQBrZrF5wdyaWhLGwdnuFAVI; locale=id_ID; vpd=v1%3B674x360x2; ps_n=1; ps_l=1; m_pixel_ratio=2; wd=360x674; fr=0ENyc05udwqygpXd2..BmawA1..AAA.0.0.BmbyJ7.AWXDhRUN3_M"
              })

              self.dlua = self.r.get(self.curl).text # Ya You
              self.link = re.search('"browser_native_sd_url":"(.*?)"', str(self.dlua)).group(1).replace('\\','')
              self.faul = self.r.get(self.link)
              with open(self.file,'wb') as self.save:
                 self.save.write(self.faul.content)
              print('\nVidio di simpan di : %s'%(self.file))
          except Exception as Error:
              exit(f'\nTerjadi Kesalahan Saat Download vidio! {Error}')

class Menu:

   def __init__(self):
       pass

   def Main(self):
       os.system('clear' if 'linux' in sys.platform.lower() else 'cls')
       print('1. Download Vidio Tiktok')
       print('2. Download Vidio Facebook\n')
       self.f4h = input('> Choose: ')
       if self.f4h   in ['1','01']:
           print('\nMasukan Link Vidio Tiktok')
           self.link = input('Link : ')
           self.file = input('Simpan ke : ').replace(' ','')
           TikTok(self.link, f'{self.file}.mp4')
       elif self.f4h in ['2','02']:
           print('\nMasukan Link Vidio Facebook')
           self.link = input('Link : ')
           self.file = input('Simpan ke : ').replace(' ','')
           Facebook(self.link, f'{self.file}.mp4')
       else:exit()

if __name__ == '__main__':
   Menu().Main()
