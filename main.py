#Trần Văn Tuấn Phong

#Các thư viện cần dùng
import  luu_url,quet_url

def start():
    url_list = ["https://vietnamnet.vn/"]
    url_list_const=5
    history=[]
    max_page = 5
    count=0
    luu_url.kiem_tra("C:\\")
    thu_muc_luu_du_lieu = 'C:\\crawl'

    #kịch bản các đường dẫn
    while (count < max_page) and (len(url_list) > 0):
        url_new = []
        url = url_list.pop(0)
        page = quet_url.doc_noi_dung(url)
        links = quet_url.lay_cac_duong_link(page)
        for item in links:
            if quet_url.kiem_tra_link(item)==False:
                item = quet_url.chinh_sua_link(url,item)
            if (item not in url_list) and (item not in history) and (item not in url_new) and (item != url):
                url_new.append(item)
        if (len(url_list) + len(url_new) <= url_list_const):
            url_list = url_list + url_new
        else:
            check = int(url_list_const - len(url_list))
            array =url_new[:check]
            url_list = url_list + array
        count += 1
        history.append(url)
        ten_thu_muc = luu_url.tao_ten_thu_muc_tu_dong(thu_muc_luu_du_lieu,url)
        luu_url.luu_file(page, ten_thu_muc)
        luu_url.luu_lich_su_cac_url(url)
        print("Đã duyệt " + str(count) + " url")

if __name__ == '__main__':
    start()