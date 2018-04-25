#encoding=utf-8
import jieba
import jieba.analyse

def words2vec(words1=None, words2=None):
    v1 = []
    v2 = []
    tag1 = jieba.analyse.extract_tags(words1, withWeight=True)
    tag2 = jieba.analyse.extract_tags(words2, withWeight=True)
    tag_dict1 = {i[0]: i[1] for i in tag1}
    tag_dict2 = {i[0]: i[1] for i in tag2}
    merged_tag = set(tag_dict1.keys()) | set(tag_dict2.keys())
    for i in merged_tag:
        if i in tag_dict1:
            v1.append(tag_dict1[i])
        else:
            v1.append(0)
        if i in tag_dict2:
            v2.append(tag_dict2[i])
        else:
            v2.append(0)
    return v1, v2


def cosine_similarity(vector1, vector2):
    dot_product = 0.0
    normA = 0.0
    normB = 0.0
    for a, b in zip(vector1, vector2):
        dot_product += a * b
        normA += a ** 2
        normB += b ** 2
    if normA == 0.0 or normB == 0.0:
        return 0
    else:
        return round(dot_product / ((normA**0.5)*(normB**0.5)) * 100, 2)
	
def cosine(str1, str2):
    vec1, vec2 = words2vec(str1, str2)
    return cosine_similarity(vec1, vec2)

str1 = '2016年以来，哪些高校发表过CNS顶尖论文？2015年10月24日，国务院印发《统筹推进世界一流大学和一流学科建设总体方案》，方案提出了分阶段推进世界一流大学和一流学科建设的总体方案。方案出台后，众多专家撰文指出，缺乏原创性重大理论和创新性科技成果是我国一流大学和一流学科与世界一流的主要差距。而目前学术界普遍认为原创性重大理论和创新性科技成果的重要载体和重要的产出途径就是在顶级学术期刊上发表高水平的学术论文，包括著名的Nature、Science、Cell等学术期刊期刊。本期青塔小编统计了2016年以来中国内地高校和科研院所在Nature、Science和Cell三大顶尖期刊上发表论文情况，供大家参考。享誉世界的三大顶尖学术期刊Nature：《自然》是英国自然出版集团出版的科技期刊，同时也是世界上最早的国际性科技期刊。创刊于1869年，Nature致力于报道和评论全球科技领域里最重要的突破。Science: 《科学》是美国科学促进会出版的一份学术期刊，为全世界最权威的学术期刊之一。《科学》是发表最好的原始研究论文、以及综述和分析当前研究和科学政策的同行评议的期刊之一。该杂志于1880年由爱迪生投资1万美元创办，于1894年成为美国最大的科学团体“美国科学促进会”的官方刊物。Cell: 《细胞》是由美国爱思维尔(Elsevier)出版公司旗下的细胞出版社(Cell Press)发行的关于生命科学领域中最新研究发现的的杂志。Cell创刊于1974年，现已成为世界自然科学研究领域最著名的期刊之一，并陆续发行了十几种姊妹刊，在各自专业领域里均占据着举足轻重的地位。Cell以发表具有重要意义的原创性科研报告为主，许多生命科学领域最重要的发现都发表在Cell上。中国内地2016年以来共发表47篇本期青塔小编统计了2016年以来中国内地高校和科研院所在Nature、Science和Cell三大顶尖期刊上发表论文情况，统计时间节点为2016年1月1日—2016年8月2日，其中高校共发表33篇，中科院等科研院所发表14篇。从发表文章的学科领域来看，绝大部分都是生命科学与医学领域，此外发表文章的学科领域还包括物理学、化学、化工、天文、环境科学、机械等。从发表文章的通讯作者来看（通讯作者一般是研究的实际负责人），大都是各个研究领域的顶尖科学家，其中包括多位两院院士、长江学者、国家杰青以及青年千人等顶尖科学家。从发表文章的高校上看，2016年以来共有19所高校以第一作者+第一单位发表三大顶尖期刊，其中清华大发表了4篇Nature、4篇Science和2篇Cell总计10篇顶尖期刊，遥遥领先其他高校与科研院所，显示了清华大学在基础科学研究特别是生命科学与医学领域的强大实力。特别值得一提的是，清华大学施一公院士2016年以来以通讯作者已发表三篇Science。北京大学已经发表了3篇Science和2篇Nature总计5篇，仅次于清华大学。此外，中国科学技术大学发表两篇Nature。浙江大学、西安交通大学、厦门大学、四川大学、中山大学等其他16所高校各发表一篇顶尖论文。科研院所方面，共发表14篇顶尖期刊，其中中科院上海生命科学研究院共发表3篇，中科院生物物理所、中科院古脊椎动物与古人类研究所各发表2篇，中科院大连化学物理研究所、中科院生态环境研究中心等其他科研院所各发表1篇。下面来看看各大高校以及科研院所的具体发表情况（统计时间节点为2016年1月1日—2016年8月2日，以文章在线发表时间为准；统计文章类型为 Article和 Review两类；统计时以第一完成单位为准，且第一作者所在单位须为第一单位，不考虑文章的参与单位；通讯作者仅统计第一工作单位在中国内地的科学家；高校附属医院发表文章纳入所在高校；数据来源于 Nature、Science 和 Cell 期刊官网）：'
str2 = '重磅：2016年国家杰青正式出炉！部分高校进步明显！今天上午（8月4日），中国科技网—科技日报正式公布了国家自然科学基金委员会关于公布2016年度国家杰出青年科学基金建议资助项目申请人名单的通告，2016年国家杰青正式出炉。今年建议资助的国家杰青共有200人。作为和长江学者一样备受关注的高端人才，每年的杰青牵动着无数人的心，而今年的结果也必然又是几家欢乐几家愁。入选国家杰青难度到底有多大？国家杰出青年科学基金项目支持在基础研究方面已取得突出成绩的青年学者自主选择研究方向开展创新研究，促进青年科学技术人才的成长，吸引海外人才，培养造就一批进入世界科技前沿的优秀学术带头人。1994年，鉴于当时的人才断层情况，刚从海外归国不久的年轻学者陈章良向时任国务院总理李鹏建议设立支持科学家自主选题、自由探索的“总理基金”，后正式命名为“国家杰出青年科学基金”。1994年首批入选49人，每人资助额度为60万元。经过22年的发展，一大批国家杰青获得者当选为两院院士，同时国家杰青已经成为我国风向标式的高端科技人才资助项目，几乎成为每一个中青年学者的奋斗目标，也是每一个科研院校所必争的人才项目。国家杰青一年的名额仅为200左右，因此国家杰青竞争非常激烈。根据国家自然科学基金委员会提供的数据，2015年度国家杰出青年科学基金项目接收申请2148项，资助198项，资助率仅为9.22%，由此可见当选杰青的难度有多大了。部分高校进步明显青塔对2016年国家杰青的当选情况进行了统计，本年度共有200位申请人入选建议资助名单。其中北京大学入选13人排名第一，清华大学和中国科学技术大学入选11人并列第二，浙江大学入选10人排名第四，以上四所高校入选人数都超过了10人。此外，复旦大学也入选7人，上海交通大学入选6人，华中科技大学入选5人，南京大学、南开大学、四川大学、同济大学、中科院上海生命科学研究院等单位都入选4人。相比2015年，很多高校入选数量明显增加。下面来看看今年的杰青获得者名单和机构数量排名吧：'

str3 = '<p style="margin-top: 20px; margin-bottom: 20px; line-height: 3em;"><span style="color: rgb(108, 108, 108); line-height: 35px; white-space: pre-wrap; font-size: 16px; font-family: 微软雅黑, &quot;Microsoft YaHei&quot;;">2015年10月24日，国务院印发《统筹推进世界一流大学和一流学科建设总体方案》，方案提出了分阶段推进世界一流大学和一流学科建设的总体方案。方案出台后，众多专家撰文指出，缺乏原创性重大理论和创新性科技成果是我国一流大学和一流学科与世界一流的主要差距。而目前学术界普遍认为原创性重大理论和创新性科技成果的重要载体和重要的产出途径就是在顶级学术期刊上发表高水平的学术论文，包括著名的Nature、Science、Cell等学术期刊期刊。本期青塔小编统计了2016年以来中国内地高校和科研院所在Nature、Science和Cell三大顶尖期刊上发表论文情况，供大家参考。<br/></span></p><p style="padding: 0px; clear: both; white-space: pre-wrap; font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; text-align: center; margin-top: 20px; margin-bottom: 20px; line-height: 3em;"><span style="font-size: 16px; font-family: 微软雅黑, &quot;Microsoft YaHei&quot;;"><strong style="margin: 0px; padding: 0px;"><span style="font-size: 16px; margin: 0px; padding: 0px; max-width: 100%; color: rgb(108, 108, 108); font-family: 微软雅黑, sans-serif; line-height: 35px; box-sizing: border-box !important; word-wrap: break-word !important;">享誉世界的三大顶尖学术期刊</span></strong><strong style="margin: 0px; padding: 0px;"><span style="font-size: 16px; margin: 0px; padding: 0px; max-width: 100%; color: rgb(108, 108, 108); font-family: 微软雅黑, sans-serif; line-height: 35px; box-sizing: border-box !important; word-wrap: break-word !important;"></span></strong><strong style="margin: 0px; padding: 0px;"></strong></span></p><p style="padding: 0px; clear: both; white-space: pre-wrap; font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; margin-top: 20px; margin-bottom: 20px; line-height: 3em;"><span style="font-size: 16px; font-family: 微软雅黑, &quot;Microsoft YaHei&quot;;"><strong style="margin: 0px; padding: 0px; line-height: 2em;"><span style="font-size: 16px; margin: 0px; padding: 0px; max-width: 100%; color: rgb(108, 108, 108); font-family: 微软雅黑, sans-serif; line-height: 35px; box-sizing: border-box !important; word-wrap: break-word !important;">Nature：</span></strong><span style="font-size: 16px; margin: 0px; padding: 0px; max-width: 100%; color: rgb(108, 108, 108); font-family: 微软雅黑, sans-serif; line-height: 35px; box-sizing: border-box !important; word-wrap: break-word !important;">《自然》是英国自然出版集团出版的科技期刊，同时也是世界上最早的国际性科技期刊。创刊于1869年，Nature致力于报道和评论全球科技领域里最重要的突破。</span><br style="margin: 0px; padding: 0px;"/></span></p><p style="padding: 0px; clear: both; white-space: pre-wrap; font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; margin-top: 20px; margin-bottom: 20px; line-height: 3em;"><span style="font-size: 16px; font-family: 微软雅黑, &quot;Microsoft YaHei&quot;;"><strong style="margin: 0px; padding: 0px;"><span style="font-size: 16px; margin: 0px; padding: 0px; max-width: 100%; color: rgb(108, 108, 108); font-family: 微软雅黑, sans-serif; line-height: 35px; box-sizing: border-box !important; word-wrap: break-word !important;">Science:</span></strong><span style="font-size: 16px; margin: 0px; padding: 0px; max-width: 100%; color: rgb(108, 108, 108); font-family: 微软雅黑, sans-serif; line-height: 35px; box-sizing: border-box !important; word-wrap: break-word !important;"> 《科学》是美国科学促进会出版的一份学术期刊，为全世界最权威的学术期刊之一。《科学》是发表最好的原始研究论文、以及综述和分析当前研究和科学政策的同行评议的期刊之一。该杂志于1880年由爱迪生投资1万美元创办，于1894年成为美国最大的科学团体“美国科学促进会”的官方刊物。</span></span></p><p style="padding: 0px; clear: both; white-space: pre-wrap; font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; margin-top: 20px; margin-bottom: 20px; line-height: 3em;"><span style="font-size: 16px; font-family: 微软雅黑, &quot;Microsoft YaHei&quot;;"><strong style="margin: 0px; padding: 0px;"><span style="font-size: 16px; margin: 0px; padding: 0px; max-width: 100%; color: rgb(108, 108, 108); font-family: 微软雅黑, sans-serif; line-height: 35px; box-sizing: border-box !important; word-wrap: break-word !important;">Cell: </span></strong><span style="font-size: 16px; margin: 0px; padding: 0px; max-width: 100%; color: rgb(108, 108, 108); font-family: 微软雅黑, sans-serif; line-height: 35px; box-sizing: border-box !important; word-wrap: break-word !important;">《细胞》是由美国爱思维尔(Elsevier)出版公司旗下的细胞出版社(Cell Press)发行的关于生命科学领域中最新研究发现的的杂志。&nbsp;Cell创刊于1974年，现已成为世界自然科学研究领域最著名的期刊之一，并陆续发行了十几种姊妹刊，在各自专业领域里均占据着举足轻重的地位。Cell以发表具有重要意义的原创性科研报告为主，许多生命科学领域最重要的发现都发表在Cell上。</span></span></p><p style="padding: 0px; clear: both; white-space: pre-wrap; font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; text-align: center; margin-top: 20px; margin-bottom: 20px; line-height: 3em;"><span style="font-size: 16px; font-family: 微软雅黑, &quot;Microsoft YaHei&quot;;"><strong style="margin: 0px; padding: 0px;"><span style="font-size: 16px; margin: 0px; padding: 0px; color: rgb(108, 108, 108); font-family: 微软雅黑, sans-serif; line-height: 35px;">中国内地2016年以来共发表47篇</span><br style="margin: 0px; padding: 0px;"/></strong><strong style="margin: 0px; padding: 0px;"></strong></span></p><p style="padding: 0px; clear: both; white-space: pre-wrap; font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; margin-top: 20px; margin-bottom: 20px; line-height: 3em;"><span style="margin: 0px; padding: 0px; max-width: 100%; color: rgb(108, 108, 108); line-height: 35px; font-size: 16px; font-family: 微软雅黑, &quot;Microsoft YaHei&quot;; box-sizing: border-box !important; word-wrap: break-word !important;">本期青塔小编统计了2016年以来中国内地高校和科研院所在Nature、Science和Cell三大顶尖期刊上发表论文情况，统计时间节点为2016年1月1日—2016年8月2日，其中高校共发表33篇，中科院等科研院所发表14篇。</span></p><p style="padding: 0px; clear: both; white-space: pre-wrap; font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; margin-top: 20px; margin-bottom: 20px; line-height: 3em;"><span style="margin: 0px; padding: 0px; max-width: 100%; color: rgb(108, 108, 108); line-height: 35px; font-size: 16px; font-family: 微软雅黑, &quot;Microsoft YaHei&quot;; box-sizing: border-box !important; word-wrap: break-word !important;">从发表文章的学科领域来看，绝大部分都是生命科学与医学领域，此外发表文章的学科领域还包括物理学、化学、化工、天文、环境科学、机械等。</span></p><p style="padding: 0px; clear: both; white-space: pre-wrap; font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; margin-top: 20px; margin-bottom: 20px; line-height: 3em;"><span style="margin: 0px; padding: 0px; max-width: 100%; color: rgb(108, 108, 108); line-height: 35px; font-size: 16px; font-family: 微软雅黑, &quot;Microsoft YaHei&quot;; box-sizing: border-box !important; word-wrap: break-word !important;">从发表文章的通讯作者来看（通讯作者一般是研究的实际负责人），大都是各个研究领域的顶尖科学家，其中包括多位两院院士、长江学者、国家杰青以及青年千人等顶尖科学家。</span></p><p style="padding: 0px; clear: both; white-space: pre-wrap; font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; margin-top: 20px; margin-bottom: 20px; line-height: 3em;"><span style="margin: 0px; padding: 0px; max-width: 100%; color: rgb(108, 108, 108); line-height: 35px; font-size: 16px; font-family: 微软雅黑, &quot;Microsoft YaHei&quot;; box-sizing: border-box !important; word-wrap: break-word !important;">从发表文章的高校上看，2016年以来共有19所高校以第一作者+第一单位发表三大顶尖期刊，其中清华大发表了4篇Nature、4篇Science和2篇Cell总计10篇顶尖期刊，遥遥领先其他高校与科研院所，显示了清华大学在基础科学研究特别是生命科学与医学领域的强大实力。特别值得一提的是，清华大学施一公院士2016年以来以通讯作者已发表三篇Science。北京大学已经发表了3篇Science和2篇Nature总计5篇，仅次于清华大学。此外，中国科学技术大学发表两篇Nature。浙江大学、西安交通大学、厦门大学、四川大学、中山大学等其他16所高校各发表一篇顶尖论文。</span></p><p style="padding: 0px; clear: both; white-space: pre-wrap; font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; margin-top: 20px; margin-bottom: 20px; line-height: 3em;"><span style="margin: 0px; padding: 0px; max-width: 100%; color: rgb(108, 108, 108); line-height: 35px; font-size: 16px; font-family: 微软雅黑, &quot;Microsoft YaHei&quot;; box-sizing: border-box !important; word-wrap: break-word !important;">科研院所方面，共发表14篇顶尖期刊，其中中科院上海生命科学研究院共发表3篇，中科院生物物理所、中科院古脊椎动物与古人类研究所各发表2篇，中科院大连化学物理研究所、中科院生态环境研究中心等其他科研院所各发表1篇。</span></p><p style="padding: 0px; clear: both; white-space: pre-wrap; font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; margin-top: 20px; margin-bottom: 20px; line-height: 3em;"><span style="font-size: 16px; font-family: 微软雅黑, &quot;Microsoft YaHei&quot;;"><span style="font-size: 16px; margin: 0px; padding: 0px; max-width: 100%; color: rgb(108, 108, 108); font-family: 微软雅黑, sans-serif; line-height: 35px; box-sizing: border-box !important; word-wrap: break-word !important;">下面来看看各大高校以及科研院所的具体发表情况</span><strong style="margin: 0px; padding: 0px;"><span style="font-size: 16px; margin: 0px; padding: 0px; max-width: 100%; color: rgb(108, 108, 108); font-family: 微软雅黑, sans-serif; line-height: 35px; box-sizing: border-box !important; word-wrap: break-word !important;">（统计时间节点为2016年1月1日—2016年8月2日，以文章在线发表时间为准；</span></strong><strong style="margin: 0px; padding: 0px; line-height: 2em;"><span style="font-size: 16px; margin: 0px; padding: 0px; max-width: 100%; color: rgb(108, 108, 108); font-family: 微软雅黑, sans-serif; line-height: 35px; box-sizing: border-box !important; word-wrap: break-word !important;">统计文章类型为 A</span></strong><strong style="margin: 0px; padding: 0px; line-height: 2em;"><span style="font-size: 16px; margin: 0px; padding: 0px; max-width: 100%; color: rgb(108, 108, 108); font-family: 微软雅黑, sans-serif; line-height: 35px; box-sizing: border-box !important; word-wrap: break-word !important;">rticle</span></strong><strong style="margin: 0px; padding: 0px; line-height: 2em;"><span style="font-size: 16px; margin: 0px; padding: 0px; max-width: 100%; color: rgb(108, 108, 108); font-family: 微软雅黑, sans-serif; line-height: 35px; box-sizing: border-box !important; word-wrap: break-word !important;">和 Review两类；</span></strong><strong style="margin: 0px; padding: 0px; line-height: 2em;"><span style="font-size: 16px; margin: 0px; padding: 0px; max-width: 100%; color: rgb(108, 108, 108); font-family: 微软雅黑, sans-serif; line-height: 35px; box-sizing: border-box !important; word-wrap: break-word !important;">统计时以</span><span style="font-size: 16px; margin: 0px; padding: 0px; color: rgb(108, 108, 108); font-family: 微软雅黑, sans-serif; line-height: 35px;">第一完成单位为准，且第一作者所在单位须为第一单位，</span></strong><strong style="margin: 0px; padding: 0px; line-height: 2em;"><span style="font-size: 16px; margin: 0px; padding: 0px; color: rgb(108, 108, 108); font-family: 微软雅黑, sans-serif; line-height: 35px;">不考虑文章的参与单位；通讯作者仅统计第一工作单位在中国内地的科学家；高校附属医院发表文章纳入所在高校；</span></strong><strong style="margin: 0px; padding: 0px; line-height: 2em;"><span style="font-size: 16px; margin: 0px; padding: 0px; color: rgb(108, 108, 108); font-family: 微软雅黑, sans-serif; line-height: 35px;">数据来源于 Nature、Science 和 Cell 期刊官网）</span></strong><span style="font-size: 16px; margin: 0px; padding: 0px; color: rgb(108, 108, 108); font-family: 微软雅黑, sans-serif; line-height: 35px;">：</span></span></p><p style="padding: 0px; clear: both; white-space: pre-wrap; font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; text-align: center; margin-top: 20px; margin-bottom: 20px; line-height: 3em;"><span style="margin: 0px; padding: 0px; color: rgb(108, 108, 108); line-height: 35px; font-size: 16px; font-family: 微软雅黑, &quot;Microsoft YaHei&quot;;"><img src="static/image/20160803/1470226091293649.png" title="1470226091293649.png" alt="中国高校CNS—5.png"/><img src="static/image/20160803/1470226182912948.png" title="1470226182912948.png" alt="中国CNS—科研院所.png"/></span></p><p style="padding: 0px; clear: both; white-space: pre-wrap; font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; text-align: center; margin-top: 20px; margin-bottom: 20px; line-height: 3em;"><span style="margin: 0px; padding: 0px; color: rgb(108, 108, 108); line-height: 35px; font-size: 16px; font-family: 微软雅黑, &quot;Microsoft YaHei&quot;;"><img src="http://admin.cingta.comstatic/image/20160618/1466233898826438.jpg"/></span></p>'
str4 = '<p style="margin-top: 20px; margin-bottom: 20px; line-height: 3em;"><span style="font-size: 16px;"><span style="white-space: pre-wrap; margin: 0px; padding: 0px; max-width: 100%; color: rgb(108, 108, 108); font-family: 微软雅黑, sans-serif; line-height: 35px; box-sizing: border-box !important; word-wrap: break-word !important;">今天上午（8月4日），中国科技网—科技日报正式公布了国家自然科学基金委员会关于公布2016年度国家杰出青年科学基金建议资助项目申请人名单的通告，2016年国家杰青正式出炉。</span><span style="white-space: pre-wrap; margin: 0px; padding: 0px; color: rgb(108, 108, 108); font-family: 微软雅黑, sans-serif; line-height: 35px;">今年建议资助的国家杰青共有200人。作为和长江学者一样备受关注的高端人才，每年的杰青牵动着无数人的心，而今年的结果也必然又是几家欢乐几家愁。</span></span></p><p style="padding: 0px; clear: both; white-space: pre-wrap; font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; text-align: center; margin-top: 20px; margin-bottom: 20px; line-height: 3em;"><span style="font-size: 16px;"><strong style="margin: 0px; padding: 0px; line-height: 2em;"><span style="font-size: 16px; margin: 0px; padding: 0px; max-width: 100%; color: rgb(108, 108, 108); font-family: 微软雅黑, sans-serif; line-height: 35px; box-sizing: border-box !important; word-wrap: break-word !important;">入选国家杰青难度到底有多大？</span></strong><strong style="margin: 0px; padding: 0px; line-height: 2em;"><span style="font-size: 16px; margin: 0px; padding: 0px; max-width: 100%; color: rgb(108, 108, 108); font-family: 微软雅黑, sans-serif; line-height: 35px; box-sizing: border-box !important; word-wrap: break-word !important;"></span></strong><strong style="margin: 0px; padding: 0px; line-height: 2em;"></strong></span></p><p style="padding: 0px; clear: both; white-space: pre-wrap; font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; margin-top: 20px; margin-bottom: 20px; line-height: 3em;"><span style="margin: 0px; padding: 0px; max-width: 100%; color: rgb(108, 108, 108); font-family: 微软雅黑, sans-serif; line-height: 35px; font-size: 16px; box-sizing: border-box !important; word-wrap: break-word !important;">国家杰出青年科学基金项目支持在基础研究方面已取得突出成绩的青年学者自主选择研究方向开展创新研究，促进青年科学技术人才的成长，吸引海外人才，培养造就一批进入世界科技前沿的优秀学术带头人。1994年，鉴于当时的人才断层情况，刚从海外归国不久的年轻学者陈章良向时任国务院总理李鹏建议设立支持科学家自主选题、自由探索的“总理基金”，后正式命名为“国家杰出青年科学基金”。1994年首批入选49人，每人资助额度为60万元。经过22年的发展，一大批国家杰青获得者当选为两院院士，同时国家杰青已经成为我国风向标式的高端科技人才资助项目，几乎成为每一个中青年学者的奋斗目标，也是每一个科研院校所必争的人才项目。</span></p><p style="padding: 0px; clear: both; white-space: pre-wrap; font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; margin-top: 20px; margin-bottom: 20px; line-height: 3em;"><span style="margin: 0px; padding: 0px; max-width: 100%; color: rgb(108, 108, 108); font-family: 微软雅黑, sans-serif; line-height: 35px; font-size: 16px; box-sizing: border-box !important; word-wrap: break-word !important;">国家杰青一年的名额仅为200左右，因此国家杰青竞争非常激烈。根据国家自然科学基金委员会提供的数据，2015年度国家杰出青年科学基金项目接收申请2148项，资助198项，资助率仅为9.22%，由此可见当选杰青的难度有多大了。</span></p><p style="padding: 0px; clear: both; white-space: pre-wrap; font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; text-align: center; margin-top: 20px; margin-bottom: 20px; line-height: 3em;"><span style="font-size: 16px;"><strong style="margin: 0px; padding: 0px;"><span style="margin: 0px; padding: 0px; max-width: 100%; color: rgb(108, 108, 108); font-family: 微软雅黑, sans-serif; line-height: 35px; box-sizing: border-box !important; word-wrap: break-word !important;">部分高校进步明显</span></strong><strong style="margin: 0px; padding: 0px;"><span style="margin: 0px; padding: 0px; max-width: 100%; color: rgb(108, 108, 108); font-family: 微软雅黑, sans-serif; line-height: 35px; box-sizing: border-box !important; word-wrap: break-word !important;"></span></strong><strong style="margin: 0px; padding: 0px;"></strong></span></p><p style="padding: 0px; clear: both; white-space: pre-wrap; font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; margin-top: 20px; margin-bottom: 20px; line-height: 3em;"><span style="font-size: 16px;"><span style="margin: 0px; padding: 0px; max-width: 100%; color: rgb(108, 108, 108); font-family: 微软雅黑, sans-serif; line-height: 35px; box-sizing: border-box !important; word-wrap: break-word !important;">青塔对2016年国家杰青的当选情况进行了统计，本年度共有200位申请人入选建议资助名单。其中北京大学入选13人排名第一，清华大学和中国科学技术大学入选11人并列第二，浙江大学入选10人排名第四，以上四所高校入选人数都超过了10人。此外，复旦大学也入选7人，上海交通大学入选6人，华中科技大学入选5人，南京大学、南开大学、四川大学、同济大学、中科院上海生命科学研究院等单位都入选4人。相比2015年，很多高校入选数量明显增加。</span><span style="margin: 0px; padding: 0px; color: rgb(108, 108, 108); font-family: 微软雅黑, sans-serif; line-height: 35px;">下面来看看今年的杰青获得者名单和机构数量排名吧：</span></span></p><p style="padding: 0px; clear: both; white-space: pre-wrap; font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; text-align: center; margin-top: 20px; margin-bottom: 20px; line-height: 3em;"><span style="margin: 0px; padding: 0px; color: rgb(108, 108, 108); font-family: 微软雅黑, sans-serif; line-height: 35px; font-size: 16px;"><img src="static/image/20160804/1470275880101235.png" title="1470275880101235.png" alt="2016年杰青名单—1.png"/></span></p><p style="padding: 0px; clear: both; white-space: pre-wrap; font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; text-align: center; margin-top: 20px; margin-bottom: 20px; line-height: 3em;"><span style="margin: 0px; padding: 0px; color: rgb(108, 108, 108); font-family: 微软雅黑, sans-serif; line-height: 35px; font-size: 16px;"><img src="static/image/20160804/1470275940544940.png" title="1470275940544940.png" alt="2016年杰青名单—2.png"/></span></p><p style="padding: 0px; clear: both; white-space: pre-wrap; font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; text-align: center; margin-top: 20px; margin-bottom: 20px; line-height: 3em;"><span style="margin: 0px; padding: 0px; color: rgb(108, 108, 108); font-family: 微软雅黑, sans-serif; line-height: 35px; font-size: 16px;"><img src="static/image/20160804/1470275896297722.png" title="1470275896297722.png" alt="2016年杰青名单—3.png"/></span></p><p style="padding: 0px; clear: both; white-space: pre-wrap; font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; text-align: center; margin-top: 20px; margin-bottom: 20px; line-height: 3em;"><span style="margin: 0px; padding: 0px; color: rgb(108, 108, 108); font-family: 微软雅黑, sans-serif; line-height: 35px; font-size: 16px;"><img src="http://admin.cingta.comstatic/image/20160618/1466233898826438.jpg"/></span></p>'

print(cosine(str1, str2))
print(cosine(str3, str4))