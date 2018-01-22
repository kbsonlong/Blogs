#!/usr/bin/python
# -*- coding: UTF-8 -*-

#发送带附件邮件
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from block_api import get_info
import traceback


def sendmail(Smtp_Server,Smtp_user,Smtp_password,Subject,TO=[],files=[]):
    # 实例
    msg = MIMEMultipart('alternative')
    msg['To'] = ';'.join(TO)
    msg['From'] = Smtp_user
    msg['Subject'] = Subject

    data = get_info('https://block.cc/api/v1/coin/list?size=18')

    html_context = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>数字货币交易数据</title>
</head>
<body>
    <script src="http://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.2.1.js">
    </script>

    <script type="text/javascript">
    //放大图片
    $(function () {
        var x = 0;
        var y = 5;
        $("button#showimage2").mouseover(
        function (e) {
            this.myTitle = this.title;
            this.title = "";
            var imgtip = "<div id='imgtip' style='position:absolute;'><img src='https://www.along.party/wp-content/themes/Cui2.0/img/weixin.bng' width='300' alt='预览图'/><\/div>"; //创建 div 元素
            $("body").append(imgtip); //把它追加到文档中
            $("#imgtip")
                .css({
                    "top": (e.pageY + y) + "px",
                    "left": (e.pageX + x) + "px"
                }).show("fast");   //设置x坐标和y坐标，并且显示
        }
        )
        .mouseout(function ()
        {
            this.title = this.myTitle;
            $("#imgtip").remove();  //移除
        }
        )
        ;
    });
</script>


    <script>
        $(document).ready(function(){
        var packJson = "{
    "code": 0,
    "message": "success",
    "data": {
        "list": [
            {
                "id": "bitcoin",
                "name": "Bitcoin",
                "symbol": "BTC",
                "change1d": -6.59,
                "available_supply": "16819075.0",
                "price": 11286.16076131,
                "volume_ex": 6277883154.741826,
                "marketCap": 189822784306,
                "change1h": -1.29,
                "change7d": -20.8,
                "suggest_ex": [
                    {
                        "display_name": "Coincheck",
                        "zh_name": "Coincheck",
                        "link": "https://coincheck.com/",
                        "name": "coincheck"
                    },
                    {
                        "display_name": "Huobi.pro",
                        "zh_name": "火币",
                        "link": "https://www.huobi.pro/ko-kr/btc_usdt/exchange/",
                        "name": "huobipro"
                    }
                ],
                "listingTime": null,
                "zhName": "比特币"
            }
        ],
        "page": 0,
        "size": 1,
        "pageCount": 1822
    }
}";
        var l = typeof(packJson);
        $("p#wods").append("<b>l</b>");
        var lists = packJson.data.list;
        for(var i = 0,j=1; i <= lists.length; i++,j++){
           {#alert(lists[0].name + " " + lists[0].change1d);#}
            //将数据追加到id为hq的p标签
            if (lists[i].zhName==""){
                $("tbody#btc").append("<tr>" +
               "<td>" + j +"</td>" +
               "<td>" + lists[i].symbol + "-" + lists[i].name + "</td>" +
               "<td>" + lists[i].price +"</td>" +
               "<td>" + lists[i].change1h +"</td>" +
               "<td>" + lists[i].change1d +"</td>" +
               "<td>" + lists[i].volume_ex +"</td>" +
               "<td>" + lists[i].marketCap +"</td>" +
               "<td>" + lists[i].change7d +"</td>" +
               "</tr>");}
            else {
               $("tbody#btc").append("<tr>" +
                   "<td>" + j +"</td>" +
                   "<td>" + lists[i].symbol + "-" + lists[i].zhName + "</td>" +
                   "<td>" + lists[i].price +"</td>" +
                   "<td>" + lists[i].change1h +"</td>" +
                   "<td>" + lists[i].change1d +"</td>" +
                   "<td>" + lists[i].volume_ex +"</td>" +
                   "<td>" + lists[i].marketCap +"</td>" +
                   "<td>" + lists[i].change7d +"</td>" +
                   "</tr>");}
        }
        });
    </script>



    <button id="showimage2" type="button" >查看二维码</button>
    <p><b>数据来源于<a href="https://block.cc/" target="_blank">block.cc</a> </b></p>
    <p id="wods"></p>
    <table border="1">
        <thead>
            <tr bgcolor="#696969">
                <td><b>排名</b></td>
                <td><b>名称</b></td>
                <td><b>价格($)</b></td>
                <td><b>涨幅(1h)</b></td>
                <td><b>涨幅(24h)</b></td>
                <td><b>交易量($)</b></td>
                <td><b>市值($)</b></td>
                <td><b>涨幅(7d)</b></td>
            </tr>
        </thead>

        <tbody id="btc">

        </tbody>

    </table>
</body>
</html>"""
    print html_context
    content = MIMEText(html_context, 'html', 'utf-8')
    msg.attach(content)

    # 构造附件，当多个为附件是用for读取构造
    # for file in files:
    #     part = MIMEBase('application', 'octet-stream')  # 'octet-stream': binary data
    #     part.set_payload(open(file, 'rb').read())
    #     encoders.encode_base64(part)
    #     part.add_header('Content-Disposition', 'attachment; filename="%s"' % file)
    #     msg.attach(part)

    try:
        server = smtplib.SMTP_SSL(Smtp_Server, 465)
        server.login(Smtp_user, Smtp_password)
        server.sendmail(Smtp_user, TO, msg.as_string())
        server.quit()
        message = 'Sendmail Success'
    except Exception, e:
        print str(e)
        message = traceback.format_exc()
    return message

if __name__ == '__main__':

    smtp_server = 'smtp.qq.com'
    smtp_user = 'kbsonlong@qq.com'
    smtp_pass = 'puvvwmufacopbbcg'
    subject = '数字货币行情预览'
    sendto = ['kbsonlong@qq.com']
    sendmail(smtp_server,smtp_user, smtp_pass,subject,sendto,files=[])
