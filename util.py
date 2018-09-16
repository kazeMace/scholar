from fake_useragent import UserAgent

BASE_PATH = "http://xueshu.baidu.com"
HEADERS = {
     'accept': 'image/webp,*/*;q=0.8',
    'accept-language': 'zh-CN,zh;q=0.8',
    'referer': 'http://xueshu.baidu.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36',
    # 'User-Agent': UserAgent().random

}
BASE_PATH_GOOGLE = "https://xs.bban.top/scholar?hl=zh-CN&scisbd=1"

HEADERS_GOOGLE = {
    # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    # "Accept-Encoding": "gzip, deflate, br",
    # "Accept-Language": "zh-CN,zh;q=0.9",
    # "Connection": "keep-alive",
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36',
}