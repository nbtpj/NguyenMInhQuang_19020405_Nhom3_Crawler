# News
 bài tập thu thập báo - collecting news assignment
 
I. nguồn Vietnamnet- Vietnamnet source (https://vietnamnet.vn/)
 1. thông tin thu thập - collecting data items
    'url': link bài viết - link of the article,
    'id': id bài viết - ID of the article,
    'cate': danh mục - category,
    'title': tiêu đề - title,
    'lead': mô tả bài viết - description,
    'content_text': nội dung - content,
    'time': thời gian - time,
    'image': link ảnh xuất hiện trong bài - links of images appeared in the article,
    'tag': từ khóa - keywords/tags
  *đinh dạng file: file .json - file type: json file.
  *mấu - example: {"url": "https://vietnamnet.vn/vn/thoi...-724-664561.html", "id": "664561", "cate": "Thời sự", "title": "Lịch trình .. BN 724", "lead": "Tối 8/7, BCĐ... được công bố ngày 6/8.", "content_text": ["Đáng.... điều trị tại Trung tâm Y tế huyện Hòa Vang."], "time": "07/08/2020 23:13 GMT+7", "image": ["https://...v=2.0&cj=1", "https://...-d2.svg", "https://..-gif.gif", "https://vnn..400-nguoi.jpg"], "tag": ["virus corona", "dịch Covid-19", "COVID-19", "Đà Nẵng"]}
 2. tình trạng thu thập - collecting status
  đã xong - done.
  số lượng bài viết - collected articles : 23445. 
  thời gian thu thập (đã bị giới hạn) - collecting time (limited by me): 1 tiếng - one hour.
  mẫu thu thập - collected example: giống mẫu phần thông tin thu thập - same as the collecting data itmes 's one.
  ảnh chụp màn hình - sceen caption: https://drive.google.com/file/d/17yHcNh4lkwsEs1TY3_IPQECd-FhM9J7F/view?usp=sharing
  kết quả - output file : https://drive.google.com/file/d/1ycz9VzojO-QAaKoByI-gG_fzRsxooqgz/view?usp=sharing
 3. phương pháp thu thập - collecting method
  lan bài theo đường dẫn có sẵn trong bài viết - using the available links in curent page to get the next article.
 4. đánh giá, vướng mắc - comments, problems
  vướng mắc: không có - problems: none
  đánh giá - comments:
   link bị lặp lại sẽ tốn thời gian xử lí - repeated links take more time to processed
   khó kiểm soát - hard to take control
   tốc độ chậm và giảm dần do gặp lại các link bị trùng lặp - collecing speed is low and decreased by the time because repeated links
  
  
II. nguồn Vnexpress- VNexpress source (https://vnexpress.vn/)
 1. thông tin thu thập - collecting data items
    'url': link bài viết - link of the article,
    'id': id bài viết - ID of the article,
    'cate': danh mục - category,
    'title': tiêu đề - title,
    'lead': mô tả bài viết - description,
    'content_text': nội dung - content,
    'time': thời gian - time,
    'image': link ảnh xuất hiện trong bài - links of images appeared in the article,
    'tag': từ khóa - keywords/tags
  *đinh dạng file: file .json - file type: json file.
  *mấu - example: "url": "https://vnexpress.net/tp-hcm-lam-viec-voi-ca-si-duy-manh-4142549.html", "id": "4142549", "cate": "Thá»i sá»±", "title": "TP HCM lÃ m viá»‡c vá»›i ca sÄ© Duy Máº¡nh", "lead": "Ca ...c.", "content_text": ["\"Sá..ng,", "..."], "time": Thứ Năm, 6/8/2020, 20:54 (GMT+7)", "image": [], "tag": ["ca s..c", " TP HCM ..nh", " ca ..nh", " V..a", " l..", " Tin n..g", " Tin"]}.
 2. tình trạng thu thập - collecting status
  đã xong - done.
  số lượng bài viết - collected articles : 29148. 
  thời gian thu thập (đã bị giới hạn) - collecting time (limited by me): 1 tiếng - one hour.
  mẫu thu thập - collected example: giống mẫu phần thông tin thu thập - same as the collecting data itmes 's one.
  ảnh chụp màn hình - sceen caption: https://drive.google.com/file/d/15kci40rxJcNJK1-N_oJn7gX_JTaVCAhU/view?usp=sharing
  kết quả - output file : https://drive.google.com/file/d/1SqePngXYBBF7ei69EjPQv-w8cWIAqg5Q/view?usp=sharing
 3. phương pháp thu thập - collecting method
  lan bài theo đường dẫn có sẵn trong bài viết - using the available links in curent page to get the next article.
 4. đánh giá, vướng mắc - comments, problems
  vướng mắc: không có - problems: none
  đánh giá - comments:
   link bị lặp lại sẽ tốn thời gian xử lí - repeated links take more time to processed
   khó kiểm soát - hard to take control
   tốc độ chậm và giảm dần do gặp lại các link bị trùng lặp - collecing speed is low and decreased by the time because repeated links
  
  
III`. nguồn Baomoi- Baomoi source (https://baomoi.com/)
 1. thông tin thu thập - collecting data items
    'url': link bài viết - link of the article,
    'id': id bài viết - ID of the article,
    'cate': danh mục - category,
    'title': tiêu đề - title,
    'lead': mô tả bài viết - description,
    'content_text': nội dung - content,
    'tag': từ khóa - keywords/tags
    'soure': nguồn bài viết - the source of the article
  *đinh dạng file: file .json - file type: json file.
  *mấu - example: {"url": "https://baomoi.com/tphc...860.epi", "id": "3..60", "cate": "Lao động - Việc làm", "title": "TPHCM: Nhiều t..c đích", "content": ["Lao đ.. này./."], "tag": ["H..kết", "Qu..g", "Tôn chỉ", "", "Sáp nhập", "Hội viên", "Thà..HCM", "Bộ ch.. trị", "S.. vụ", "Tư..đồng", "Trùng lắp", "Năm 2014", "Trưởng", "Giống nhau", "Kết luận"], "source": "https://vov.vn/chi...ich-935987.vov"}
 2. tình trạng thu thập - collecting status
  đã xong - done.
  số lượng bài viết - collected articles : 2. 
  thời gian thu thập (đã bị giới hạn) - collecting time (limited by me): 1 tiếng - one hour.
  mẫu thu thập - collected example: giống mẫu phần thông tin thu thập - same as the collecting data itmes 's one.
  ảnh chụp màn hình - sceen caption: https://drive.google.com/file/d/1ennDMU13yBeis1nxFfwT75IA32Z0iurc/view?usp=sharing
  kết quả - output file :https://drive.google.com/file/d/1RYcscIINe8Uesdf3Pq8sML_byfsKYrkQ/view?usp=sharing
 3. phương pháp thu thập - collecting method
  lấy url theo id bài viết - using the id article in a while loop to get the valid next links.
 4. đánh giá, vướng mắc - comments, problems
  vướng mắc - problems: 
    kết quả thu thập quá thấp - result is not as good as respected
    link hỏng nhiều - too many useless links   
  đánh giá - comments:
   thời gian xử lý rất nhanh - collecting speed is extremely fast
   dễ kiểm soát - easy to take control
   tiềm năng - potential to apply
   em chưa quen với phương pháp này, nên các bài sau em đều sử dụng phương pháp lan link - I have not get used to this method yet, so in other assignments, I do not use this method.
   
   
IV. nguồn Foxnews- Foxnews source (https://foxnews.com/)
 1. thông tin thu thập - collecting data items
    'url': link bài viết - link of the article,
    'cate': danh mục - category,
    'title': tiêu đề - title,
    'lead': mô tả bài viết - description,
    'content_text': nội dung - content,
    'time': thời gian - time,
    'image': link ảnh xuất hiện trong bài - links of images appeared in the article,
    'tag': từ khóa - keywords/tags
  *đinh dạng file: file .json - file type: json file.
  *mấu - example: {"url": "https://www.foxnew...-repo", "cate": "world", "title": "Beirut...ng bomb'", "lead": "Investig..rned was “a floating bomb.”", "content_text": ["This material may not.. 20 minutes."], "time": "2020-08-06", "image": ["http..033.jpg?ve=1&tl=1"], "tag": ["lebanon", "mideast", "russia"]}
 2. tình trạng thu thập - collecting status
  đã xong - done.
  số lượng bài viết - collected articles : 17448. 
  thời gian thu thập (không bị giới hạn) - collecting time (unlimited by me): 20 phút - 20 minutes.
  mẫu thu thập - collected example: giống mẫu phần thông tin thu thập - same as the collecting data itmes 's one.
  ảnh chụp màn hình - sceen caption: https://drive.google.com/file/d/1fVg3Z0aG8vSlXS6mh2_McD9t4N3D4ZLL/view?usp=sharing
  kết quả - output file : https://drive.google.com/file/d/1hEFicPaGnqUtK9BDi0Zcu9-ZutRGBqKV/view?usp=sharing
 3. phương pháp thu thập - collecting method
  lan bài theo đường dẫn có sẵn trong bài viết - using the available links in curent page to get the next article.
 4. đánh giá, vướng mắc - comments, problems
  vướng mắc: không có - problems: none
  đánh giá - comments:
   khó kiểm soát - hard to take control
   tốc độ chậm và giảm dần do gặp lại các link bị trùng lặp - collecing speed is low and decreased by the time because repeated links
   không có khả năng lấy toàn bộ bài viết - unable to collect all articles from server
  
  
 
