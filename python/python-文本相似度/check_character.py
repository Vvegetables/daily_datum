#coding=utf-8
import Levenshtein as lst

str1 = '南京师范大学六个项目入选国家“优秀本科生国际交流”计划近日，国家留学基金委公布了2016年优秀本科生国际交流项目资助名单。我校申报的与日本北海道大学、美国马里兰大学等六所国际知名高校合作的共六项校际交流项目获批，为历年之最。同时，我校获得20个优秀在读本科生赴海外学习奖学金名额。　　此次我校获批的校际交流项目包括：与日本北海道大学法学学生交流项目、与韩国拿撒勒大学秘书学专业本科生交流项目、与美国马里兰大学地理信息科学专业学生交流项目、与日本明治大学法学学生交流项目、与日本桐荫横滨大学法学学生交流项目和与英国思克莱德大学教育学院学生交流项目。　　推进学生海外学习是培养国际化人才的重要举措。近年来，学校不断拓展与国外高校和机构的合作，加大向国家留学基金委申报项目工作的力度，努力为学生创造更多的赴国（境）外学习的机会。　　我校2016学年第一批国际交流学生的遴选工作将于3月底陆续开始。'
str2 = '南京师范大学六个项目入选国家“优秀本科生国际交流”计划近日，国家留学基金委公布了2016年优秀本科生国际交流项目资助名单。我校申报的与日本北海道大学、美国马里兰大学等六所国际知名高校合作的共六项校际交流项目获批，为历年之最。同时，我校获得20个优秀在读本科生赴海外学习奖学金名额。　　此次我校获批的校际交流项目包括：与日本北海道大学法学学生交流项目、与韩国拿撒勒大学秘书学专业本科生交流项目、与美国马里兰大学地理信息科学专业学生交流项目、与日本明治大学法学学生交流项目、与日本桐荫横滨大学法学学生交流项目和与英国思克莱德大学教育学院学生交流项目。　　推进学生海外学习是培养国际化人才的重要举措。近年来，学校不断拓展与国外高校和机构的合作，加大向国家留学基金委申报项目工作的力度，努力为学生创造更多的赴国（境）外学习的机会。　　我校2016学年第一批国际交流学生的遴选工作将于3月底陆续开始。'
hit_rate = lst.jaro(str1,str2)
print hit_rate