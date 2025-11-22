#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script để thêm Q&A mới vào dataset
"""
import json
import re

# Đọc file hiện tại
with open('qa_dataset.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

existing_questions = {qa['question'].lower().strip() for qa in data['questions']}

# Danh sách Q&A mới từ tài liệu
new_qa_list = [
    # PHONG TRÀO THƠ MỚI
    {
        "question": "Phong trào Thơ mới diễn ra trong giai đoạn nào?",
        "answer": "Phong trào Thơ mới diễn ra trong giai đoạn từ năm 1932 đến năm 1945.",
        "keywords": ["phong trào thơ mới", "giai đoạn", "1932", "1945"]
    },
    {
        "question": "Thơ mới đánh dấu sự chấm dứt điều gì trong thơ ca Việt Nam?",
        "answer": "Thơ mới đánh dấu sự chấm dứt của thơ cũ với hệ thống niêm luật chặt chẽ đã chi phối suốt nhiều thế kỉ của thơ ca trung đại Việt Nam.",
        "keywords": ["thơ mới", "chấm dứt", "niêm luật", "thơ ca trung đại"]
    },
    {
        "question": "Về nội dung, Thơ mới chủ yếu bộc lộ điều gì?",
        "answer": "Về nội dung, Thơ mới bộc lộ những tình cảm, cảm xúc và cái \"tôi\" cá nhân của con người với nhiều biểu hiện đa dạng, độc đáo.",
        "keywords": ["nội dung", "thơ mới", "tình cảm", "cảm xúc", "cái tôi"]
    },
    {
        "question": "Về hình thức, Thơ mới có điểm gì đột phá?",
        "answer": "Về hình thức, Thơ mới là sự đột phá khỏi những quy tắc niêm luật cứng nhắc, chủ yếu dùng thơ 7 chữ, 8 chữ, thơ tự do, chú trọng nhạc điệu, hình ảnh và cảm xúc cá nhân.",
        "keywords": ["hình thức", "thơ mới", "đột phá", "niêm luật", "thơ tự do"]
    },
    {
        "question": "Vì sao nói Thơ mới đưa thơ Việt Nam vào quỹ đạo hiện đại?",
        "answer": "Vì Thơ mới đặt trọng tâm vào cái \"tôi\" cá nhân, cảm xúc chủ quan, đổi mới hình thức, mở đường cho thơ Việt Nam tiếp cận tinh thần hiện đại của thơ ca thế giới.",
        "keywords": ["thơ mới", "hiện đại", "cái tôi", "cảm xúc chủ quan"]
    },
    # TÁC GIẢ HÀN MẶC TỬ
    {
        "question": "Hàn Mặc Tử là hiện tượng như thế nào trong phong trào Thơ mới?",
        "answer": "Hàn Mặc Tử là một hiện tượng thơ kì lạ vào bậc nhất của phong trào Thơ mới, với phong cách rất riêng, khó trộn lẫn.",
        "keywords": ["hàn mặc tử", "hiện tượng", "thơ mới", "phong cách"]
    },
    {
        "question": "Phong cách thơ của Hàn Mặc Tử có đặc điểm gì nổi bật?",
        "answer": "Thơ Hàn Mặc Tử vừa có vẻ đẹp trinh bạch, trong trẻo, vừa dữ dội, ám ảnh, nhiều hình ảnh huyền ảo, kì lạ, thể hiện nỗi đau và khát vọng sống mãnh liệt.",
        "keywords": ["phong cách", "hàn mặc tử", "trinh bạch", "dữ dội", "huyền ảo"]
    },
    {
        "question": "Bệnh tật đã ảnh hưởng thế nào tới thơ Hàn Mặc Tử?",
        "answer": "Bệnh tật khiến nỗi đau thể xác và tinh thần của Hàn Mặc Tử dâng cao, nhưng đồng thời cũng làm thơ ông bùng nổ cảm xúc, khao khát sống, yêu đời đến cực điểm, từ đó tạo nên những thi phẩm rất đặc biệt.",
        "keywords": ["bệnh tật", "hàn mặc tử", "nỗi đau", "khao khát sống"]
    },
    # BÀI THƠ MÙA XUÂN CHÍN - CHUNG
    {
        "question": "Nhan đề \"Mùa xuân chín\" có cấu tạo kiểu gì?",
        "answer": "Nhan đề \"Mùa xuân chín\" có cấu tạo kiểu Danh từ + Tính từ (mùa xuân + chín).",
        "keywords": ["nhan đề", "mùa xuân chín", "cấu tạo", "danh từ", "tính từ"]
    },
    {
        "question": "Từ \"chín\" trong \"Mùa xuân chín\" gợi ra ý nghĩa gì?",
        "answer": "Từ \"chín\" gợi cảm giác mùa xuân đã vào độ rực rỡ, tròn đầy, căng mọng nhất, nhưng cũng là lúc giáp ranh với sự phai tàn, gợi cảm xúc bâng khuâng, man mác buồn.",
        "keywords": ["chín", "mùa xuân chín", "ý nghĩa", "rực rỡ", "phai tàn"]
    },
    {
        "question": "Phương thức biểu đạt chính của bài thơ là gì?",
        "answer": "Phương thức biểu đạt chính của bài thơ là biểu cảm, thông qua miêu tả cảnh để bộc lộ tình cảm.",
        "keywords": ["phương thức biểu đạt", "biểu cảm", "miêu tả"]
    },
    {
        "question": "Bố cục bài thơ \"Mùa xuân chín\" có mấy phần, là những phần nào?",
        "answer": "Bài thơ có 4 đoạn:\n\nĐoạn 1: Cảnh mùa xuân trong con mắt thi sĩ yêu đời.\n\nĐoạn 2: Bước đi của mùa xuân.\n\nĐoạn 3: Tiếng hát yêu đời, tràn đầy khao khát cuộc sống.\n\nĐoạn 4: Lời hỏi thăm cùng sự tiếc nuối của nhân vật trữ tình.",
        "keywords": ["bố cục", "4 đoạn", "mùa xuân chín"]
    },
    # KHỔ 1
    {
        "question": "Những hình ảnh nào báo hiệu mùa xuân trong khổ thơ 1?",
        "answer": "Những hình ảnh báo hiệu mùa xuân là: làn nắng ửng, khói mơ tan, mái nhà tranh lấm tấm vàng, tà áo biếc trên giàn thiên lý, \"bóng xuân sang\".",
        "keywords": ["khổ 1", "hình ảnh", "báo hiệu", "mùa xuân", "nắng ửng", "khói mơ"]
    },
    {
        "question": "Màu sắc chủ đạo trong khổ thơ 1 là gì và mang ý nghĩa gì?",
        "answer": "Màu sắc chủ đạo là sắc vàng của nắng, của mái nhà tranh, và sắc biếc của tà áo, tạo nên không khí tươi sáng, ấm áp, nhẹ nhàng của một làng quê vào xuân.",
        "keywords": ["khổ 1", "màu sắc", "vàng", "biếc", "ý nghĩa"]
    },
    {
        "question": "Tác giả đã nhân hóa gió như thế nào trong khổ thơ 1?",
        "answer": "Tác giả nhân hóa gió qua hình ảnh \"gió trêu tà áo biếc\", khiến gió như một đứa trẻ tinh nghịch đang trêu đùa, làm cảnh xuân trở nên sinh động.",
        "keywords": ["khổ 1", "nhân hóa", "gió", "trêu", "tinh nghịch"]
    },
    {
        "question": "Dấu chấm giữa câu trong câu \"Trên giàn thiên lý. Bóng xuân sang\" có tác dụng gì?",
        "answer": "Dấu chấm tạo một khoảng ngắt nhịp bất thường, như một cái dừng lại để cảm nhận, làm nổi bật cảm xúc ngập ngừng, bâng khuâng, như khoảnh khắc thi nhân chợt nhận ra \"bóng xuân\" đã sang.",
        "keywords": ["khổ 1", "dấu chấm", "ngắt nhịp", "bâng khuâng", "bóng xuân sang"]
    },
    {
        "question": "Khổ thơ 1 gợi lên bức tranh mùa xuân thôn quê như thế nào?",
        "answer": "Khổ thơ 1 gợi lên bức tranh mùa xuân nơi thôn quê thanh bình, duyên dáng, đằm thắm với mái nhà tranh, giàn thiên lý, tà áo biếc, ánh nắng vàng, tất cả hòa quyện trong không khí tươi vui mà vẫn nhẹ nhàng.",
        "keywords": ["khổ 1", "bức tranh", "mùa xuân", "thôn quê", "thanh bình"]
    },
    # KHỔ 2
    {
        "question": "Hình ảnh \"sóng cỏ xanh tươi gợn tới trời\" là hình ảnh gì, gợi cảm giác thế nào?",
        "answer": "Đó là hình ảnh ẩn dụ, gợi cỏ non mơn mởn như sóng, trải dài bất tận, làm nổi bật sức sống tươi trẻ, tràn đầy của mùa xuân trên cánh đồng.",
        "keywords": ["khổ 2", "sóng cỏ", "ẩn dụ", "sức sống", "mùa xuân"]
    },
    {
        "question": "Không gian trong khổ thơ 2 được mở rộng như thế nào?",
        "answer": "Không gian được mở rộng từ mặt đất lên tới bầu trời, từ cỏ đến đồi, tạo cảm giác thoáng đãng, khoáng đạt của mùa xuân.",
        "keywords": ["khổ 2", "không gian", "mở rộng", "thoáng đãng"]
    },
    {
        "question": "Hình ảnh \"bao cô thôn nữ hát trên đồi\" gợi ra không khí gì?",
        "answer": "Hình ảnh đó gợi nên không khí vui tươi, rộn ràng, trẻ trung, tràn đầy sức sống, như bản hòa ca của tuổi xuân nơi thôn quê.",
        "keywords": ["khổ 2", "cô thôn nữ", "hát", "vui tươi", "rộn ràng"]
    },
    {
        "question": "Qua khổ 2, tâm trạng của nhà thơ có gì vừa vui vừa buồn?",
        "answer": "Nhà thơ vui trước cảnh xuân tràn trề sức sống, tiếng hát rộn ràng, nhưng cũng buồn, xót xa trước quy luật đời người, khi tuổi xuân và những niềm vui hồn nhiên chẳng thể giữ mãi.",
        "keywords": ["khổ 2", "tâm trạng", "vui", "buồn", "quy luật đời người"]
    },
    # KHỔ 3
    {
        "question": "Cụm từ \"tiếng ca vắt vẻo lưng chừng núi\" sử dụng thủ pháp nghệ thuật gì?",
        "answer": "Cụm từ này dùng nghệ thuật ẩn dụ chuyển đổi cảm giác, khiến tiếng ca như có hình khối, có đường nét, \"vắt vẻo\" giữa không trung, rất độc đáo.",
        "keywords": ["khổ 3", "tiếng ca vắt vẻo", "ẩn dụ", "chuyển đổi cảm giác"]
    },
    {
        "question": "Từ láy \"hổn hển\" gợi cảm giác gì về tiếng hát?",
        "answer": "Từ \"hổn hển\" gợi tiếng hát dồn dập, nồng nàn, như đầy cảm xúc, vừa mệt nhưng lại rất say mê, thể hiện cường độ cảm xúc mạnh mẽ của người hát.",
        "keywords": ["khổ 3", "hổn hển", "tiếng hát", "dồn dập", "nồng nàn"]
    },
    {
        "question": "Tiếng ca được so sánh với điều gì trong câu \"Hổn hển như lời của nước mây\"?",
        "answer": "Tiếng ca được so sánh với \"lời của nước mây\", vừa gần gũi, mềm mại, vừa bồng bềnh, xa xăm, gợi vẻ đẹp mơ hồ, huyền ảo.",
        "keywords": ["khổ 3", "so sánh", "lời của nước mây", "huyền ảo"]
    },
    {
        "question": "Tiếng hát trong khổ 3 có ý nghĩa gì đối với việc thể hiện độ \"chín\" của mùa xuân?",
        "answer": "Tiếng hát yêu đời, tràn đầy khát vọng sống chính là biểu hiện độ \"chín\" nhất của mùa xuân trong lòng người: cảm xúc dâng trào, tình yêu cuộc sống mãnh liệt.",
        "keywords": ["khổ 3", "tiếng hát", "chín", "mùa xuân", "khát vọng"]
    },
    {
        "question": "Cụm từ \"nghe ra ý vị và thơ ngây\" nói lên điều gì?",
        "answer": "Cụm từ đó cho thấy trong tiếng hát có cả chiều sâu ý vị lẫn nét hồn nhiên, ngây thơ, khiến lòng người nghe bâng khuâng, xao xuyến.",
        "keywords": ["khổ 3", "ý vị", "thơ ngây", "bâng khuâng"]
    },
    # KHỔ 4
    {
        "question": "Nhân vật trữ tình \"sực nhớ làng\" trong hoàn cảnh nào?",
        "answer": "Giữa không gian xuân chín nơi đất khách, nhân vật trữ tình đột ngột \"sực nhớ làng\", nhớ quê hương, nhớ con người thân thuộc nơi chôn rau cắt rốn.",
        "keywords": ["khổ 4", "sực nhớ", "làng", "quê hương"]
    },
    {
        "question": "Hình ảnh \"chị ấy năm nay còn gánh thóc dọc bờ sông trắng nắng chang chang?\" gợi điều gì?",
        "answer": "Hình ảnh đó gợi cuộc đời nhọc nhằn, lam lũ của người phụ nữ thôn quê, gánh thóc dưới nắng chang chang, đồng thời gợi nỗi nhớ thương, xót xa rất chân thành của nhân vật trữ tình.",
        "keywords": ["khổ 4", "chị ấy", "gánh thóc", "nhọc nhằn", "xót xa"]
    },
    {
        "question": "Vì sao có thể nói khổ 4 mang âm hưởng buồn man mác?",
        "answer": "Vì khổ thơ đan xen giữa cảnh xuân đẹp với nỗi nhớ làng, nhớ người, nhớ thân phận người phụ nữ, tất cả đều nhuốm màu tiếc nuối, bâng khuâng, buồn nhẹ nhàng mà sâu thẳm.",
        "keywords": ["khổ 4", "âm hưởng", "buồn", "man mác", "tiếc nuối"]
    },
    # TỔNG KẾT
    {
        "question": "Về nội dung, bài \"Mùa xuân chín\" thể hiện những phương diện nào của mùa xuân?",
        "answer": "Bài thơ thể hiện vẻ đẹp thiên nhiên mùa xuân nơi thôn quê, niềm vui rộn ràng của tuổi trẻ, tiếng hát yêu đời, đồng thời bộc lộ nỗi buồn, nỗi nhớ quê hương và sự xót xa trước thân phận con người, nhất là người phụ nữ.",
        "keywords": ["nội dung", "mùa xuân chín", "thiên nhiên", "nỗi buồn", "thân phận"]
    },
    {
        "question": "Bức tranh làng quê Việt Nam trong bài thơ hiện lên với những hình ảnh tiêu biểu nào?",
        "answer": "Bức tranh làng quê hiện lên với mái nhà tranh, giàn thiên lý, sóng cỏ xanh, đồi, sông, người gánh thóc, cô thôn nữ hát trên đồi… rất đậm hồn quê Việt Nam.",
        "keywords": ["bức tranh", "làng quê", "việt nam", "hình ảnh"]
    },
    {
        "question": "Vì sao có thể nói \"Mùa xuân chín\" mang phong vị ca dao?",
        "answer": "Vì bài thơ có hình ảnh làng quê, người nông dân, người phụ nữ gánh gồng, tiếng hát thôn nữ, cách diễn đạt gần gũi, mộc mạc mà sâu lắng, rất giống chất dân ca, ca dao Việt Nam.",
        "keywords": ["phong vị", "ca dao", "làng quê", "dân ca"]
    },
    {
        "question": "Tâm trạng chủ đạo của nhân vật trữ tình trong bài thơ là gì?",
        "answer": "Tâm trạng chủ đạo là vừa yêu mến, say đắm cảnh xuân, vừa bâng khuâng, buồn man mác, nhớ quê, thương người, tiếc nuối những gì đẹp đẽ mà mong manh trong cuộc đời.",
        "keywords": ["tâm trạng", "nhân vật trữ tình", "bâng khuâng", "tiếc nuối"]
    },
    {
        "question": "Qua bài thơ, Hàn Mặc Tử gửi gắm suy nghĩ gì về thời gian và tuổi trẻ?",
        "answer": "Ông gợi lên cảm thức rằng mùa xuân và tuổi trẻ đều có lúc \"chín\" đẹp nhất, nhưng cũng là lúc gần kề phôi pha; vì thế con người vừa say mê tận hưởng, vừa xót xa trước sự trôi đi không níu giữ được của thời gian.",
        "keywords": ["thời gian", "tuổi trẻ", "chín", "phôi pha"]
    },
    # TÓM TẮT
    {
        "question": "Hãy tóm tắt ngắn gọn bài thơ \"Mùa xuân chín\".",
        "answer": "\"Mùa xuân chín\" miêu tả một bức tranh mùa xuân thôn quê rực rỡ, tràn đầy sức sống với nắng ấm, khói mơ, sóng cỏ xanh, tiếng hát thôn nữ. Đằng sau vẻ đẹp đó là nỗi buồn man mác, sự tiếc nuối tuổi xuân và nỗi nhớ quê da diết của nhân vật trữ tình.",
        "keywords": ["tóm tắt", "ngắn gọn", "mùa xuân chín"]
    },
    {
        "question": "Hãy tóm tắt nội dung 4 đoạn của bài thơ theo đúng bố cục tài liệu.",
        "answer": "Đoạn 1: Miêu tả cảnh mùa xuân nơi thôn quê với nắng ửng, khói mơ tan, mái nhà tranh vàng và tà áo biếc trên giàn thiên lý.\n\nĐoạn 2: Mùa xuân lan tỏa trên đồng cỏ xanh, tiếng hát của các cô thôn nữ vang lên rộn ràng nhưng pha chút tiếc nuối khi \"có kẻ theo chồng bỏ cuộc chơi\".\n\nĐoạn 3: Tiếng hát thôn nữ được miêu tả sống động, huyền ảo, \"vắt vẻo lưng chừng núi\", \"hổn hển như lời của nước mây\", gợi sức sống mãnh liệt.\n\nĐoạn 4: Nhân vật trữ tình là người \"khách xa\", chợt nhớ về làng quê và xót xa cho người chị gánh thóc dưới nắng chang chang.",
        "keywords": ["tóm tắt", "4 đoạn", "bố cục", "mùa xuân chín"]
    },
    # NỘI DUNG TỪNG KHỔ
    {
        "question": "Nội dung chính của khổ thơ 1 là gì?",
        "answer": "Khổ thơ 1 vẽ bức tranh mùa xuân thôn quê thanh bình với ánh nắng ửng, làn khói mơ tan, mái nhà tranh lấm tấm vàng, gió đùa tà áo biếc trên giàn thiên lý. Cảnh sắc gợi lên vẻ đẹp trong trẻo, dịu dàng và tinh khôi của mùa xuân.",
        "keywords": ["khổ 1", "nội dung", "bức tranh", "mùa xuân"]
    },
    {
        "question": "Các hình ảnh \"nắng ửng\", \"khói mơ tan\", \"mái nhà tranh lấm tấm vàng\" trong khổ 1 có ý nghĩa gì?",
        "answer": "Những hình ảnh này tạo nên không khí xuân dịu nhẹ và ấm áp, gợi cảm giác làng quê thanh bình, gần gũi. \"Khói mơ tan\" là hình ảnh đặc trưng của buổi sáng mùa xuân, mềm mại và bảng lảng, làm tăng vẻ mơ hồ thơ mộng của cảnh xuân.",
        "keywords": ["khổ 1", "nắng ửng", "khói mơ", "mái nhà tranh", "ý nghĩa"]
    },
    {
        "question": "Nội dung chính của khổ thơ 2 là gì?",
        "answer": "Khổ thơ 2 miêu tả cánh đồng xuân rộng lớn với \"sóng cỏ xanh tươi gợn tới trời\", cùng tiếng hát của các cô thôn nữ trên đồi. Cảnh xuân rộn ràng ấy lại nhuốm chút buồn man mác khi \"có kẻ theo chồng bỏ cuộc chơi\", gợi sự tiếc nuối tuổi xuân.",
        "keywords": ["khổ 2", "nội dung", "sóng cỏ", "cô thôn nữ"]
    },
    {
        "question": "Hình ảnh \"sóng cỏ xanh tươi gợn tới trời\" mang ý nghĩa gì trong khổ thơ 2?",
        "answer": "Đây là hình ảnh ẩn dụ chỉ cánh đồng cỏ mênh mông, gợn theo gió như sóng biển, thể hiện sức sống bất tận của mùa xuân.",
        "keywords": ["khổ 2", "sóng cỏ", "ẩn dụ", "sức sống"]
    },
    {
        "question": "Nội dung của khổ thơ 3 là gì?",
        "answer": "Khổ thơ 3 tập trung khắc họa tiếng hát thôn nữ. Tiếng hát được miêu tả bằng những hình ảnh đầy sáng tạo: \"vắt vẻo lưng chừng núi\", \"hổn hển như lời của nước mây\", vừa mạnh mẽ, vừa mềm mại, chứa đựng khát vọng sống và cảm xúc dâng trào của tuổi trẻ.",
        "keywords": ["khổ 3", "nội dung", "tiếng hát", "thôn nữ"]
    },
    {
        "question": "Vì sao tiếng hát trong khổ 3 được xem là linh hồn của mùa xuân?",
        "answer": "Vì tiếng hát thể hiện sức sống, niềm vui, sự khao khát của con người, hòa vào không gian xuân, tạo nên độ \"chín\" trọn vẹn của mùa xuân trong lòng người.",
        "keywords": ["khổ 3", "tiếng hát", "linh hồn", "mùa xuân"]
    },
    {
        "question": "Nội dung chính của khổ thơ 4 là gì?",
        "answer": "Khổ thơ 4 chuyển sang nỗi niềm của nhân vật trữ tình – một \"khách xa\" đang thưởng xuân nhưng chợt nhớ làng quê. Hình ảnh \"chị ấy gánh thóc dọc bờ sông trắng nắng chang chang\" gợi sự lam lũ, nhọc nhằn và nỗi xót xa về thân phận người phụ nữ.",
        "keywords": ["khổ 4", "nội dung", "khách xa", "nhớ làng"]
    },
    # TỔNG HỢP ĐẶC BIỆT
    {
        "question": "Hãy nêu đầy đủ nội dung khổ thơ 1 theo đúng trình tự hình ảnh.",
        "answer": "Khổ thơ 1 gồm các hình ảnh:\n\nNắng ửng trên mái nhà tranh\n\nKhói mơ tan buổi sớm\n\nMái nhà tranh lấm tấm vàng\n\nGió trêu tà áo biếc\n\nGiàn thiên lý\n\n\"Bóng xuân sang\" – dấu hiệu mùa xuân đã tới",
        "keywords": ["khổ 1", "đầy đủ", "trình tự", "hình ảnh"]
    },
    {
        "question": "Tóm tắt khổ thơ 2 theo đúng ý thơ.",
        "answer": "Khổ thơ 2 miêu tả:\n\nSóng cỏ xanh mơn mởn gợn tới bầu trời\n\nNhiều cô thôn nữ hát trên đồi\n\nCả không gian tràn đầy sức sống mùa xuân\n\nXen vào đó là sự tiếc nuối nhẹ nhàng khi \"có kẻ theo chồng bỏ cuộc chơi\"",
        "keywords": ["khổ 2", "tóm tắt", "ý thơ"]
    },
    {
        "question": "Tóm tắt khổ thơ 3 theo đúng cảm xúc và hình ảnh thơ.",
        "answer": "Khổ thơ 3 tập trung vào tiếng hát thôn nữ:\n\nTiếng hát \"vắt vẻo lưng chừng núi\"\n\nTiếng hát \"hổn hển như lời của nước mây\"\n\nLời ca chứa đựng cảm xúc mạnh mẽ\n\nVừa ý vị vừa thơ ngây\n\nBiểu hiện sức sống và niềm vui của mùa xuân",
        "keywords": ["khổ 3", "tóm tắt", "cảm xúc", "hình ảnh"]
    },
    {
        "question": "Tóm tắt khổ thơ 4 theo đúng mạch thơ.",
        "answer": "Khổ thơ 4 nói về:\n\nNgười khách xa gặp lúc mùa xuân đang \"chín\"\n\nBỗng nhiên nhớ về làng quê\n\nNhớ hình ảnh người chị gánh thóc dọc bờ sông\n\nGợi sự lam lũ và nỗi xót thương thân phận\n\nTạo dư âm buồn man mác ở cuối bài",
        "keywords": ["khổ 4", "tóm tắt", "mạch thơ"]
    }
]

# Thêm các Q&A mới (tránh trùng lặp)
added_count = 0
for qa in new_qa_list:
    if qa['question'].lower().strip() not in existing_questions:
        data['questions'].append(qa)
        existing_questions.add(qa['question'].lower().strip())
        added_count += 1

# Lưu file
with open('qa_dataset.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Đã thêm {added_count} Q&A mới vào dataset!")
print(f"Tổng số Q&A hiện tại: {len(data['questions'])}")

