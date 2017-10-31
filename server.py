# coding:utf-8

import web
import sys
import logging, logging.config
import os

storm_jars_path = "./submit_jars"
submit_build_path = './logs/submit_build.log'

# log
logging.config.fileConfig("./config/logger.cfg")
logger = logging.getLogger("logger01")

# sys
reload(sys)
sys.setdefaultencoding('utf-8')

render = web.template.render('templates')

urls = (
    '/', 'Index',
    '/upload_server_path', 'UpLoad2ServerPath',
    '/submit_jar_info', 'SubmitJarInfo',
    '/submit_jar_execute', 'SubmitJarExecute',
    '/while_query_submit', 'WhileQuerySubmit',
)

app = web.application(urls, globals())


class Index:
    def GET(self):
        return render.index()


# 文件上传到服务器路径
class UpLoad2ServerPath:
    def POST(self):
        storage = web.input()
        fileStram = storage['fileStream']
        fileName = storage['fileName']
        target_f_name = os.path.join(storm_jars_path, fileName)
        # 如果存在,先删除旧的
        if os.path.exists(target_f_name):
            os.remove(target_f_name)
        target_f = open(target_f_name, 'a')
        target_f.write(fileStram)
        target_f.close()
        logger.info("fileName:" + fileName + '----文件上传完毕!')
        return "ok"


# 主类、topo名字、jar包地址的form表单
class SubmitJarInfo:
    def GET(self):
        get_url = web.input()
        target_f_name = os.path.join(storm_jars_path, get_url.fileName)
        jar_path = str(os.path.abspath(target_f_name))
        return render.submit_jar_info(jar_path)


class WhileQuerySubmit:
    def GET(self):
        if os.path.exists(submit_build_path):
            submit_build_file = open(submit_build_path, 'r')
            return str(submit_build_file.read())
        else:
            raise Exception("没有build log 文件!")


class SubmitJarExecute:
    def POST(self):
        form = web.input()
        form_main_class = form.main_class
        form_topo_name = form.topo_name
        form_run_jar = form.run_jar
        pshell = 'storm jar %s %s %s > %s' % (
            form_run_jar, form_main_class, form_topo_name, os.path.abspath(submit_build_path),)
        logger.info("执行的storm命令:" + pshell)
        os.system(pshell)
        return "ok"


if __name__ == "__main__":
    logger.info('启动web服务器.')
    app.run()
    logger.info('关闭web服务器.')
