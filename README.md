# courseGet-BUPT  
**北邮新版本科教务抢课脚本，基于python3的selenium框架**
---------------------------
**使用说明**  

请确保在校园网或vpn环境下使用，若选课成功，请及时关闭脚本，不要给教务系统以及其他同学的选课带来麻烦

---------------------------
**具体使用方法：**

打开脚本编辑页面，更改以下参数：

_student_ID_：输入学号，如2022210666  
_password_：输入密码  
_course_name_：此处输入自己要抢的课程的名称（尽量输入全称，否则有可能无法正确定位课程；若无法输入全称，请保证输入的名称可以少字但无错字，请保证字符串不为""），如"社会创新与社会创业（双创）",或"社会创新与"  
_teacher_name_:此处输入课程的授课教师名（有些课程会有不同教师授课，因此为了准确性，可以在此处输入教师名称，若不清楚教师名称，请保证字符串为""），如"刘丹,张佳鑫"或"刘丹,"  
_course_type_:此处输入抢课的课程类型，必修选课请将标号改为2，选修选课请改为3，公选课请改为4，留级选课请改为5  

输入上述参数后，在python3环境下运行脚本
