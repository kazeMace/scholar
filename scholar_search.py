from util import BASE_PATH, HEADERS
from bs4 import BeautifulSoup
import requests
import multiprocessing
import json
import time
PARAMS = {

    "tn": "SE_baiduxueshu_c1gjeupa",
    "ie": "utf-8",
    "sc_f_para": "sc_tasktype={firstSimpleSearch}"

}
def test_url(url):
    try:
        req = requests.get(url, timeout=0.4)
    except:
        return 404
    print(req.status_code)
    return req.status_code
def search_scholar(wd, page):
    data = []
    session = requests.Session()
    session.get(url=BASE_PATH)
    end_point = '/s'
    search_url = "".join([BASE_PATH, end_point]) + "?wd={}&pn={}&tn={}&ie={}&sc_f_para={}".format(wd, str((int(page)-1)*10), PARAMS["tn"], PARAMS["ie"], PARAMS["sc_f_para"])
    req = session.get(url=search_url, headers=HEADERS)
    soup = BeautifulSoup(req.text, 'html5lib')
    result_list = soup.select("div.result")
    id = 1
    count = 1
    for index, item in enumerate(result_list):
        print(count)
        count+=1
        try:
            exp_type1 = item.select("i.c-icon-zhuanli-mark")
            print(exp_type1)
            exp_type2 = item.select("i.c-icon-tushu-mark ")
            print(exp_type2)
            download = item.select("a.sc_download")
            print(download)
            if len(exp_type1) == 0 and len(exp_type2) == 0 and len(download) != 0:
                print("beixuan")
                title = item.select("h3")[0].text.strip()
                print("title {}:".format(str(id)), title)
                brief_info = item.select("div.sc_info")[0]
                info_list = brief_info.select("span")
                author = info_list[0].select("a")
                author_list = [item.text.strip() for item in author]
                print("author:",author_list)
                source = info_list[1].select("a")[0].get("title").strip()
                print("source:",source)
                time = info_list[2].get("data-year").strip()
                print("time:",time)
                refer_count = info_list[3].select("a")[0].text.strip()
                print("refer count:", refer_count)
                abstract = item.select("div.c_abstract")[0].text.split("来源")[0].strip()
                # print(abstract)
                detail_url = "".join([BASE_PATH, item.select("h3")[0].select("a")[0].get("href")])
                print("detail url:", detail_url)
                detail_req = session.get(detail_url)
                soup1 = BeautifulSoup(detail_req.text, 'html5lib')
                # print(soup1)
                download_list = soup1.select("div#savelink_wr")[0].select("span.dl_item_span")
                download_url_list = []

                for item in download_list:
                    if "全网免费下载" in item.text:
                        print("全网免费下载" in item.text)
                        source_name = item.select("a.dl_item")[0].select("span.dl_source")[0].text
                        if  source_name == "ResearchGate" and source_name == "pdfs.semanticscholar.org":
                            continue
                        # if item.select()
                        url = item.select("a")[0].get("href").strip().replace("\n","")
                        if test_url(url) == 200:
                            download_url_list.append(url)
                            break
                        else:
                            continue
                    else:
                        continue


                print(download_url_list)
                data_item = {
                    "title":title,
                    "author_list":author_list,
                    "source":source,
                    "time":time,
                    "refer_count":refer_count,
                    "abstract":abstract,
                    "download_url_list":download_url_list
                }
                data.append(data_item)

                id += 1
            else:
                continue
        except:
            continue
        # print("type:", type)
    # print(data)
    return data

if __name__ == '__main__':
    search_scholar("faster rcnn",1)

