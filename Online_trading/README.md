# online-trading


**Bài tập thu thập sản thông tin sản phẩm – collecting products &#39;s detail from online trading webs**

1. **Nguồn Websosanh – Websosanh source (**[**https://websosanh.vn/**](https://websosanh.vn/)**)**
  1.1. **Thông tin thu thập – collecting data items**

&#39;\_url&#39;: link sản phẩm – link to the product

&#39;\_name&#39;: tên sản phẩm – name of the product

&#39;\_id&#39;: mã sản phẩm – ID of th product

&#39;\_image&#39;: hình ảnh sản phẩm – image of the product

&#39;\_store&#39;: link tới cửa hàng bán sản phấm – link to the store selling the product

&#39;\_price&#39;: biểu giá sản phẩm – prices of the product

- Định dạng file – file type: json
- Mẫu- example:
- {&quot;\_url&quot;: &quot;https://websosanh.vn/dien-thoai-samsung-galaxy-a71-8gb128gb/1222490345/so-sanh.htm&quot;, &quot;\_name&quot;: &quot;Điện thoại Samsung Galaxy A71 - 8GB RAM,128GB,6.7 inch&quot;, &quot;\_id&quot;: &quot;1222490345&quot;, &quot;\_image&quot;: &quot;http://img.websosanh.vn/v2/users/root\_product/images/dien-thoai-samsung-galaxy-a71/xvybrlcyllnt1.jpg&quot;, &quot;\_store&quot;: [&quot;http://websosanh.vn/dien-thoai-samsung-galaxy-a71/6675308389480790391/343220106741734172/direct.htm&quot;, &quot;http://websosanh.vn/samsung-galaxy-a71/4525829744254709444/1862900947526397052/direct.htm&quot;, &quot;http://websosanh.vn/dien-thoai-samsung-galaxy-a71/7646933063506649512/6615345395640391072/direct.htm&quot;, &quot;http://websosanh.vn/dien-thoai-samsung-galaxy-a71-rom-128gb-ram-8gb-hang-nguyen-seal-moi-100-bao-hanh-12-thang/1446820900460458181/3502170206813664485/direct.htm&quot;, &quot;http://websosanh.vn/dien-thoai-samsung-galaxy-a71-xanh/854886585965751940/3624201225223465067/direct.htm&quot;, &quot;http://websosanh.vn/samsung-galaxy-a71-8gb128gb-chinh-hang-4-camera-snapdragon-730-gia-re/5683505324071954449/3314395516257662903/direct.htm&quot;, &quot;http://websosanh.vn/samsung-galaxy-a71-a715-new-100-actived-/7803898830289431583/656749824287169829/direct.htm&quot;, &quot;http://websosanh.vn/dien-thoai-samsung-galaxy-a71-128gb8gb-hang-chinh-hang-bac/1945105550968298160/2642071820174507179/direct.htm&quot;, &quot;http://websosanh.vn/samsung-galaxy-a71-troi-bao-hanh-den-128gb/752375102299544679/6992345092433090958/direct.htm&quot;, &quot;http://websosanh.vn/dien-thoai-samsung-galaxy-a71/1061428996109350767/8923813711556934424/direct.htm&quot;], &quot;\_price&quot;: [&quot;6990000&quot;, &quot;7390000&quot;, &quot;7450000&quot;, &quot;7490000&quot;, &quot;7600000&quot;, &quot;7890000&quot;, &quot;8099000&quot;, &quot;8290000&quot;, &quot;7590000&quot;, &quot;8390000&quot;]}

  1.2. **Trạng thái thu thập – collecting status**

Đã xong – done

Số lượng sản phẩm thu thập- number of collected product: 25184

Thời gian thu thập – collecting time: 1 tiếng - 1 hour

[**ảnh chụp màn hình – screen caption**](https://drive.google.com/file/d/1pBOcAiRVkhBaauGfkHpKTi_5mgaTsW9U/view?usp=sharing)

[**tệp kết quả - output file**](https://drive.google.com/file/d/1pBOcAiRVkhBaauGfkHpKTi_5mgaTsW9U/view?usp=sharing)

  1.3. **Phương pháp thu thập – collecting method**

lan bài theo đường dẫn có sẵn trong bài viết - using the available links in curent page to get the next article.

  1.4. **Đánh giá, vướng mắc – comments, problems**

Tốc độ chậm, cần thời gian nghỉ giữa các request – speed is low, need waiting between requesting times (0.1s)

2. **Nguồn Amazon – Amazon source(**[**https://www.amazon.com/**](https://www.amazon.com/)**)**
  2.1. **Thông tin thu thập – collecting data items**

&#39;\_url&#39;: link sản phẩm – link to the product

&#39;\_name&#39;: tên sản phẩm – name of the product

&#39;\_price&#39;: biểu giá sản phẩm – prices of the product

&#39;\_image&#39;: hình ảnh sản phẩm – image of the product

&#39;\_rate: đánh giá – rating

- Định dạng file – file type: json
- Mẫu- example:
- {&quot;\_url&quot;: &quot;https://www.amazon.com/Samsung-QVO-Disco-duro-Gris/dp/B07L3D19MY/ref=sr\_1\_17?dchild=1&amp;qid=1596357401&amp;s=computers-intl-ship&amp;sr=1-17&quot;, &quot;\_name&quot;: &quot;Samsung 860 QVO 1TB Solid State Drive (MZ-76Q1T0) V-NAND, SATA 6Gb/s, Quality and Value Optimized SSD&quot;, &quot;\_price&quot;: &quot;109.99&quot;, &quot;\_image&quot;: &quot;https://m.media-amazon.com/images/I/91KgeW3UJeL.\_AC\_UY218\_.jpg&quot;, &quot;\_rate&quot;: &quot;4.8 out of 5 stars&quot;}

  2.2. **Trạng thái thu thập – collecting status**

Đã xong – done

Số lượng sản phẩm thu thập- number of collected product: 25184

Thời gian thu thập – collecting time: 20 phút – 20 minutes

[ảnh chụp màn hình – screen caption](https://drive.google.com/file/d/1IfIc0CRZEyCdeRQ6zYB-wwkQEzWQOcR8/view?usp=sharing)

[tệp kết quả - output file](https://drive.google.com/file/d/1l2uTRP_5LMHe-1g1ExIJswIRcTTtvyEj/view?usp=sharing)

  2.3. **Phương pháp thu thập – collecting method**

lan bài theo đường dẫn có sẵn trong bài viết - using the available links in curent page to get the next article.

  2.4. **Đánh giá, vướng mắc – comments, problems**

Sử dụng user agent – using use agent

DOWNLOADER\_MIDDLEWARES = {
&#39;scrapy.downloadermiddlewares.useragent.UserAgentMiddleware&#39;: None,
&#39;scrapy\_user\_agents.middlewares.RandomUserAgentMiddleware&#39;: 400,
}
