import json
import requests


class CSDNhot:
    def __init__(self):
        self.url = 'https://blog.csdn.net/phoenix/web/blog/hot-rank?page=0&pageSize=25&type=blog'
        self.headers = {
            # "Cookie": "uuid_tt_dd=10_30602795580-1693290690746-768136; loginbox_strategy=%7B%22taskId%22%3A270%2C%22abCheckTime%22%3A1693290693432%2C%22version%22%3A%22notInDomain%22%7D; hide_login=1; Hm_up_6bcd52f51e9b3dce32bec4a3997715ac=%7B%22islogin%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%7D; creative_btn_mp=3; write_guide_show=3; SidecHatdocDescBoxNum=true; Hm_lvt_e5ef47b9f471504959267fd614d579cd=1693291914; ssxmod_itna=Yq+OPjx0OWY5GHD8Yi4RxIOBYZQ0=YqFD0D8x05xi=iDpxBKidDaxQPnjmboniExj3EDWfhOj03q+W3iYOcRIGzIfnaYoxCPGn+6244YD44GTDt4DTD34DYDihQGIDieDFCTXUkDbxYQDYMPDzdIBDGfgDYPyiqDg/qDBDD6UD7QDIu6SSS2HUeDSRAt4Y0=DjdTD/+pad2=oOccbRLtb=12Wiwi4xBQD7MPyDYE7UeDH+kXPVofxmD4s8D4FFoq4zi+b738GF+x+YS5F7hGb7Evtji89dxDAtX4sYiD; ssxmod_itna2=Yq+OPjx0OWY5GHD8Yi4RxIOBYZQ0=YqFD0D4nK3hbK4DsDcmrDj4476vydrEzK13SOuGt7KoeT5AzYtRlcGszngi3aoDpIwp0HOnFZ4BpeStQTi4+r8L=983+SAIO7VKl1Z2zcnTFrrOuNkl4asOu8=h7K2CAtSlY+vxoGBZyHW+oGN7Etel4D6lFsmFw7QKOpP9Hz8IEbsRRjC/HKi8uDfFnDK/febmk=Hpc=qaAFf=fzTPW7GWRAuoSKrZwAbjBAxo8QD9nEzHeQ+LZccWZCOBiB9CSPpXmAc=uAXHmfvKw47S=fPd1DbkwSozd52YC1kD0rWKnHrE84nWBd+aQqvBzcG3qiwWgr+TH4dmeuwG8m4fb+4iplWWr8v8kUWtti7XTdbi8ajbSfKfObO8OZmQ8gomEOAds/h37RKskmg7pVOYnd1=mD1wDmkWuuAWPLEw=rlD4lbQTNLWEm3fH0Wr1tfe6RWd+fd3Q1chQbmW14bbmaFab/rW01YA6dNfkgaxADDwo=DjKDeLe4D=; dc_session_id=10_1693312547398.392277; c_first_ref=default; c_segment=8; dc_sid=376fc1f2c402ad70ebbd25710386dbce; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1693290694,1693312549; https_waf_cookie=f1b7dfd1-f708-40ad65600fa1d75d08b1cfe81ea5cca85348; c_utm_term=python; c_first_page=https%3A//edu.csdn.net/skill/python%3Fops_request_misc%3D%26request_id%3D%26biz_id%3D%26utm_medium%3Ddistribute.pc_search_result.none-task-skillTree-2%7Eall%7Etop_card%7Edefault-1-python-null-null.142%5Ev93%5EchatgptT3_2%26utm_term%3Dpython; c_dsid=11_1693313185927.694640; c_utm_relevant_index=2; relevant_index=2; c_utm_medium=distribute.pc_search_result.none-task-blog-2%7Eall%7Etop_positive%7Edefault-2-102807071-null-null.142%5Ev93%5EchatgptT3_2; c_page_id=default; log_Id_pv=29; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1693313223; firstDie=1; referrer_search=1693313224329; __gads=ID=b4ecb99d36d99946-22cd5b1429e300d9",
            # "Host": "so.csdn.net",
            # "Referer": "https",
            # "Sec-Ch-Ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
            # "Sec-Ch-Ua-Mobile": "?0",
            # "Sec-Ch-Ua-Platform": "\"Windows\"",
            # "Sec-Fetch-Dest": "empty",
            # "Sec-Fetch-Mode": "cors",
            # "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
        }

    def send_request(self, url):
        try:
            res = requests.get(url, headers=self.headers, timeout=10)
            if res.status_code == 200:
                html = res.text
            else:
                html = None
            return html
        except requests.RequestException:
            print("请求网页失败")

    @staticmethod
    def get_data(html):
        data_list = json.loads(html)
        data = data_list['data']
        for obj in data:
            author = obj['nickName']
            title = obj['articleTitle']
            url = obj['articleDetailUrl']
            create_time_str = obj['period']
            yield {
                "作者": author,
                "标题": title,
                "链接": url,
                "发布时间": create_time_str,
            }

    def main(self):
        print("正在获取热门博客...")
        html = self.send_request(self.url)
        result = []
        for data in self.get_data(html):
            print(data)
            result.append(data)
            # self.insert_data(db, list(data.values()))
        return result


if __name__ == '__main__':
    CSDNhot().main()
