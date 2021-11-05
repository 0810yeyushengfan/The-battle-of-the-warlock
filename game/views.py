from django.http import HttpResponse

def index(request):
    line1='<h1 style="text-align:center">术士之战</h1>'
    line3='<hr/>'
    line4='<a href="/play/">进入游戏页面</a>'
    line2='<img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201709%2F17%2F20170917233141_NCPrc.thumb.700_0.jpeg&refer=http%3A%2F%2Fb-ssl.duitang.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1638678230&t=7b2045d5c4d3f2e6d346305470616073" width=2000>'

    return HttpResponse(line1+line4+line3+line2)


def play(request):
    line1='<h1 style="text-align:center">游戏页面</h1>'
    line2='<img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fi.gtimg.cn%2Fqqlive%2Fimg%2Fjpgcache%2Ffiles%2Fqqvideo%2Fy%2Fyerxhe0fg1ygnex.jpg&refer=http%3A%2F%2Fi.gtimg.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1638678230&t=ef2d2142fc3b26d0f596415c4f629806" width=800>'

    return HttpResponse(line1+line2)
