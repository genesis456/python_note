import re
res = """
<dd class="job_bt">
        <h3 class="description">职位描述：</h3>
        <div class="job-detail">
        <p>职位描述<br>
        1. 负责游戏后台相关开发工作<br>
        2. 主导游戏运营相关数据库设计，接口、web后台编写<br>
        3. 海量用户行为数据分析、处理，并生成后台报表<br><br>
        岗位要求<br>
        1. 至少精通一门web框架（如：flask、django等），熟悉flask为佳<br>
        2. 3年及以上服务端开发经验为佳<br>
        3. 能熟练地在Linux/Unix上进行维护和开发工作，熟悉Bash等脚本语言为佳<br>
        4. 熟悉html/css/js，会前端开发框架vuejs/reactjs更佳<br>
        5. 熟悉Postgres/Mysql/Redis/Mongodb/Kafka为佳<br>
        6. 善于沟通，具备良好合作态度及团队精神，富有工作激情、创造力和责任感<br>
        7. 游戏研发相关行业从业者优先</p>
        </div>
    </dd>"""

st = re.sub(r'<[\w\s]+="[\w-]*">|</?\w*>',' ',res)
print(st)