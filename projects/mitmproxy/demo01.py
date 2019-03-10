"""
    Created by 朝南而行 2018/12/5 16:36
"""
from mitmproxy import ctx


# 必须这么写
def request(flow):
    # print(flow.request.headers)
    # 日志输出
    # ctx.log.info(str(flow.request.headers))
    # ctx.log.warn(str(flow.request.url))
    ctx.log.error(str(flow.request.headers))
    ctx.log.error(str('='*20))
    ctx.log.error(str(flow.request.url))
    ctx.log.error(str('=' * 20))
    ctx.log.error(str(flow.request.host))
    ctx.log.error(str('=' * 20))
    ctx.log.error(str(flow.request.method))
    ctx.log.error(str('=' * 20))
    ctx.log.error(str(flow.request.path))
    ctx.log.error(str('=' * 20))


# 必须这么写
def response(flow):
    ctx.log.error(str(flow.response.status_code))

