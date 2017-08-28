# _*_ coding:utf-8 _*_
import glob
from JsonUtil import get_json_from_file, write_js_2_file


def get_file_list():
    path = '../scrape_yy/config/*'
    # print glob.glob(path)
    return glob.glob(path)


def generate_json_file():
    js_data = {"shxwcb": ["新闻晨报", "newspaper"], "sina_hotnews": ["新浪", "news"],
               "sina_society": ["新浪", "news"], "sina_pic": ["新浪", "news"],
               "news173": ["news173", "news"],
               "sina_tech": ["新浪", "news"], "china_social": ["中华新闻网", "news"],
               "huanqiu_society": ["环球网", "news"],
               "tencentgame": ["腾讯网", "news"],
               "jun_jie": ["俊杰网", "news"], "neteasy": ["网易", "news"],
               "sohush": ["搜狐", "news"],
               "east_society": ["东方网", "news"], "taiwan_sh": ["中国台湾网", "news"],
               "myzaker": ["myzaker","forum"], "southcn_it": ["搜狐", "news"],
               "china_z": ["站长之家","forum"],"ali_hotnews": ["游侠网","forum"],
               "cac_gov": ["中国网信网", "gov"],
               "ccm_gov": ["中国文化市场网", "gov"],"shdf": ["中国扫黄扫非网", "gov"]}

    lst_file = get_file_list()

    for file in lst_file:
        js = get_json_from_file(file)
        name = js["name"]
        if js_data.has_key(name) and len(js_data.get(name)) == 2:
            js_data[name].append(js["url"])
        else:
            None

    file = '../config/web_src_name.json'
    write_js_2_file(js_data, file)


if __name__ == '__main__':
    generate_json_file()
    # get_file_list()
    pass