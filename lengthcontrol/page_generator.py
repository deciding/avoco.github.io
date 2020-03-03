# coding=utf8
from glob import glob
import os

dst_file = "index_cn.html"
text_list = [
    "yu2 jian4 jun1 : wei4 mei3 ge4 you3 cai2 neng2 de ren2 ti2 gong1 ping2 tai2 .",
    "ta1 shi4 yin1 pin2 ling3 yu4 de tao2 bao3 tian1 mao1 , zai4 zhe4 ge4 ping2 tai2 shang4, ",
    "mei3 ge4 nei4 rong2 sheng1 chan3 zhe3 dou1 ke3 yi3 hen3 fang1 bian4 de shi1 xian4 zi4 wo3 jia4 zhi2 , "
    "geng4 duo1 de ren2 yong1 you3 wei1 chuang4 ye4 de ji1 hui4 .",
    "zui4 jin4 xi3 ma3 la1 ya3 de bao4 guang1 lv4 you3 dian3 gao1 , ren4 xing4 shai4 chu1 yi1 dian3 qi1 yi4 yuan2 de "
    "zhang4 hu4 yu2 e2 de jie2 tu2 ,",
    "rang4 ye4 nei4 ye4 wai4 dou1 hen3 jing1 tan4 : yi2 ge4 zuo4 yin1 pin2 de , ju1 ran2 you3 zhe4 me duo1 qian2 ?",
    "ji4 zhe3 cha2 dao4 , wang3 shang4 dui4 xi3 ma3 la1 ya3 de jie4 shao4 shi4 ,",
    "xun4 su4 cheng2 zhang3 wei4 zhong1 guo2 zui4 da4 de yin1 pin2 fen1 xiang3 ping2 tai2 , mu4 qian2 yi3 yong1 you3 "
    "liang3 yi4 yong4 hu4 , qi3 ye4 zong3 gu1 zhi2 chao1 guo4 san1 shi2 yi4 yuan2 ren2 min2 bi4 .",
    "jin4 ri4 , ji4 zhe3 zai4 shang4 hai3 zhang1 jiang1 gao1 ke1 ji4 yuan2 qu1 de xi3 ma3 la1 ya3 ji1 di4 zhuan1 "
    "fang3 le yu2 jian4 jun1 .",
    "ta1 men dou1 shi4 han3 ta1 lao3 yu2 de , bu4 guo4 hou4 lai2 ji4 zhe3 wen4 guo4 ta1 de nian2 ling2 , "
    "qi2 shi2 cai2 yi1 jiu3 qi1 qi1 nian2 de .",
    "ji4 zhe3 liao3 jie3 dao4 , xi3 ma3 la1 ya3 cai3 qu3 bu4 duo1 jian4 de lian2 xi2 mo2 shi4 , ling4 yi1 wei4 jiu4 "
    "shi4 chen2 xiao3 yu3 ,",
    "liang3 ren2 qi4 zhi4 hun4 da1 , you3 dian3 nan2 zhu3 wai4 nv3 zhu3 nei4 de yi4 si1 ,",
    "bu4 guo4 ta1 men zhi3 shi4 da1 dang4 , bu2 shi4 chang2 jian4 de fu1 qi1 dang4 mo2 shi4 . yong4 yu2 jian4 jun1 de "
    "hua4 lai2 shuo1 , zhe4 ge4 mo2 shi4 ye3 bu4 chang2 jian4 .",
    "从行业来看 , 服务业受冲击最大 . 数据显示 ，2月份 ，交通运输 , 住宿餐饮 , 旅游 , 居民服务等人员聚集性较强的消费行业需求骤减 , 商务活动指数均落至20%以下 . 不过 , "
    "与抗击疫情相关的医药制造业以及与生活需求相关的农副食品加工 , 食品及酒饮料精制茶等行业PMI回落幅度相对较小 . 得益于云办公 , 在线教育和远程医疗等新业态新技术的支撑 , 电信 , "
    "互联网软件行业PMI明显好于服务业总体水 .平此外 , 2月份 , 金融业PMI为50.1% , 继续保持在扩张区间 , 对疫情防控和经济社会发展发挥了重要作用 . 官方最新披露数据已经传递出制造业复苏的积极信号 . "
    "据统计局数据 , 截至2月25日 , 全国采购经理调查企业中 , 大中型企业复工率为78.9% , 其中大中型制造业企业达到85.6% . "]

text_template = """<br><br><b>(%d) %s<b>"""
audio_template = """<div>
    <br>%s倍速度<br>
    <audio controls="controls">
        <source type="audio/mp3" src="%s"></source>
        <p>Your browser does not support the audio element.</p>
    </audio>
</div>"""

wav_path_list = glob("audios/cn_speech_control_sample/*")
audio_file_list = [os.path.basename(audio_path)
                   for audio_path in glob(os.path.join(wav_path_list[0], "*.wav"))]
print(wav_path_list)

page_file = open("index_cn.html", mode="a")

for index, sentence in enumerate(text_list):
    print(text_template % (index, sentence), file=page_file)
    print("\n", file=page_file)
    for speed_path in wav_path_list:
        speed = speed_path.replace("wavs", "").split("\\")[-1]
        audio_file_path = audio_file_list[index]
        audio_content = audio_template % (speed, os.path.join(speed_path, audio_file_path))
        print(audio_content, file=page_file)
        print("\n", file=page_file)
