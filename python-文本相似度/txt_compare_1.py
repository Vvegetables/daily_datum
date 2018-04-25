# -*- coding: utf-8 -*-

import jieba
from gensim import corpora, models, similarities
from collections import defaultdict

定义文件目录
work_dir = "D:/workspace/PythonSdy/data"
f1 = work_dir + "/t1.txt"
f2 = work_dir + "/t2.txt"
# 读取文件内容
c1 = open(f1, encoding='utf-8').read()
c2 = open(f2, encoding='utf-8').read()

# c1 = '<p style="margin-top: 20px; margin-bottom: 20px; line-height: 3em;"><span style="font-size: 16px; font-family: 微软雅黑, &#39;Microsoft YaHei&#39;;">近日，“2014年中国野生动植物保护十件大事评选”结果由国家林业局网站公布，西北大学的金丝猴研究团队2014年10月在《Nature Communications》上发表的研究成果入选。</span></p><p style="margin-top: 20px; margin-bottom: 20px; line-height: 3em;"><span style="font-size: 16px; font-family: 微软雅黑, &#39;Microsoft YaHei&#39;;">《Nature Communications》发表了我校李保国教授研究团队的学术发现，该研究揭示了我国特有动物川金丝猴社群独特的重层社会结构模式，其观点打破了西方学者50年来有关灵长类重层社会进化的一贯认识。该成果与兰花全基因组测序等其他研究工作标志着我国濒危物种保护取得重大研究突破，也是此次入选十件大事中唯一一项来自高校的研究成果。</span></p><p style="margin-top: 20px; margin-bottom: 20px; line-height: 3em;"><span style="font-size: 16px; font-family: 微软雅黑, &#39;Microsoft YaHei&#39;;">“2014年中国野生动植物保护十件大事”由国家林业局野生动植物保护与自然保护区管理司和中国绿色时报社共同主办。评选活动采取网上推选投票和评委推荐评审的办法进行。“十件大事”评委会由国家林业局保护司、宣传办、绿色时报社、濒管办、中动协、专家代表及人民日报、新华社等新闻媒体代表组成。</span></p><p><br/></p>'
# c2 = '<p style="margin-top: 20px; margin-bottom: 20px; line-height: 3em;"><span style="font-family: 微软雅黑, &#39;Microsoft YaHei&#39;;">2015年3月20日，第五届“纳通国际儒学奖”颁奖典礼在四川大学举行。西北大学名誉校长、著名历史学家张岂之教授荣获“优秀导师奖”。</span></p><p style="margin-top: 20px; margin-bottom: 20px; line-height: 3em;"><span style="font-family: 微软雅黑, &#39;Microsoft YaHei&#39;;">四川大学党委常务副书记、国际儒学研究院常务副理事长、纳通儒学奖学•奖教金评审委员会主任罗中枢，国际儒学联合会副会长、北京纳通医疗集团董事长赵毅武，中国工程院院士、美国工程院外籍院士、美国医学与生物工程院会士张兴栋，四川省社科联党组副书记、副主席唐永进，原西南政法大学副校长、重庆社科院院长俞荣根，陕西师范大学教授、四川大学国际儒学研究院学术委员刘学智，台湾元智大学、四川大学特聘教授詹海云，四川巨人文化有限公司董事长、四川大学国际儒学研究院理事李彗生，成都融信智慧地产公司总经理、四川大学国际儒学院理事叶青等出席典礼。典礼由四川大学国际儒学研究院院长舒大刚主持。</span></p><p style="margin-top: 20px; margin-bottom: 20px; line-height: 3em;"><span style="font-family: 微软雅黑, &#39;Microsoft YaHei&#39;;">西北大学张岂之教授出席颁奖典礼，并作了发言，并应邀<span style="font-family: 微软雅黑, &#39;Microsoft YaHei&#39;; line-height: 48px;">应邀在四川大学为师生做了《中华经典滋养我的心灵》的学术演讲。</span></span></p><p style="margin-top: 20px; margin-bottom: 20px; line-height: 3em;"><strong><span style="font-family: 微软雅黑, &#39;Microsoft YaHei&#39;;">青塔小贴士：</span></strong></p><p style="margin-top: 20px; margin-bottom: 20px; line-height: 3em;"><span style="font-family: 微软雅黑, &#39;Microsoft YaHei&#39;;">“纳通国际儒学奖”是由国际儒学联合会、北京纳通医疗集团在四川大学国际儒学研究院设立的儒学专门奖项，旨在推动儒学研究，弘扬儒学精神，培养儒学人才，促进西部文化建设。“优秀导师奖”是“优秀成果及贡献奖”的专项奖，重在奖励从事儒学研究，弘扬和实践儒学精神的先进个人和单位。按照程序，评委会经过网评、专家匿名通讯评、会评等多个环节，最后产生了1名获奖者。张岂之教授获此殊荣，实属实至名归。</span></p><p style="margin-top: 20px; margin-bottom: 20px; line-height: 3em;"><span style="font-family: 微软雅黑, &#39;Microsoft YaHei&#39;;">“纳通国际儒学奖”是目前国内学术界在人文社会科学方面影响较大、奖金额度最高的奖项。</span></p>'

# jieba 进行分词
data1 = jieba.cut(c1)
data2 = jieba.cut(c2)

data11 = ""
# 获取分词内容
for i in data1:
    data11 += i + " "
data21 = ""
# 获取分词内容
for i in data2:
    data21 += i + " "

doc1 = [data11, data21]
# print(doc1)

t1 = [[word for word in doc.split()]
      for doc in doc1]
# print(t1)

# # frequence频率
freq = defaultdict(int)
for i in t1:
    for j in i:
        freq[j] += 1
# print(freq)

# 限制词频
t2 = [[token for token in k if freq[j] >= 3]
      for k in t1]
print(t2)

# corpora语料库建立字典
dic1 = corpora.Dictionary(t2)
dic1.save(work_dir + "/yuliaoku.txt")

# 对比文件
f3 = work_dir + "/t3.txt"
c3 = open(f3, encoding='utf-8').read()
# jieba 进行分词
data3 = jieba.cut(c3)
data31 = ""
for i in data3:
    data31 += i + " "
new_doc = data31
print(new_doc)

# doc2bow把文件变成一个稀疏向量
new_vec = dic1.doc2bow(new_doc.split())
# 对字典进行doc2bow处理，得到新语料库
new_corpor = [dic1.doc2bow(t3) for t3 in t2]
tfidf = models.TfidfModel(new_corpor)

# 特征数
featurenum = len(dic1.token2id.keys())

# similarities 相似之处
# SparseMatrixSimilarity 稀疏矩阵相似度
idx = similarities.SparseMatrixSimilarity(tfidf[new_corpor], num_features=featurenum)
sims = idx[tfidf[new_vec]]
print(sims)