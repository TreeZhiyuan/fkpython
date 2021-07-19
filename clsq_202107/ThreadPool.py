from concurrent.futures import ThreadPoolExecutor
import htmlUtil
import time


def print_name(i_path, i_url):
    htmlUtil.download_image(i_path, i_url)


pool = ThreadPoolExecutor(10, 'thread_name_prefix_')
task = pool.submit(htmlUtil.download_image, 'D:\\atp_workspace\\pyfkclsq\\[朝花夕拾]302期，老婆希望我有雷神的身材，我其实已经有了\\BbsImg_1564415795_s_1939993_o_w_186_h_332_59268.gif',
                   'https://i1.hoopchina.com.cn/blogfile/201907/29/BbsImg_1564415795_s_1939993_o_w_186_h_332_59268.gif')

time.sleep(5)
print(task.done())
