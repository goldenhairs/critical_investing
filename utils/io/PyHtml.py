# *_*coding:utf-8 *_*
"""
Descri：
"""
import datetime

from pigeomail import Mailer, Message

from chinese_calendar import is_workday


def table_blue(cols: list, data, name="Test Table"):
    r"""This is a beatuiful blue table written by html, you can put into your own data

    example:
    >>> cols = ["Band", "Year formed", "No. of Albums", "Most famous song"]
    >>> data = [
            ["The Clash", "1976", 6, "Ever fallen in love (with someone you shouldn't've)"],
            ["The Clashs", "1964", 5, "Bending Calling"],
            ["The Csflash", "1986", 36, "China Calling"],
        ]
    >>> body = html4table(cols=cols, data=data, name="测试表")
    >>> print(body)
        :param name: 表名
        :param cols: 列名
        :param data: 数据
        :return:
    """
    if not isinstance(data, list):
        raise Exception("The type must be list, please check it...")

    head = """
<!DOCTYPE html>
<html lang="en" >
<head>
  <meta charset="UTF-8">
  <title>CodePen - Responsive Table</title>

    <style>
       body {
      background-color: #91ced4;
    }
    body * {
      box-sizing: border-box;
    }
    
    .header {
      background-color: #327a81;
      color: white;
      font-size: 1.5em;
      padding: 1rem;
      text-align: center;
      text-transform: uppercase;
    }
    
    img {
      border-radius: 50%;
      height: 60px;
      width: 60px;
    }
    
    .table-users {
      border: 1px solid #327a81;
      border-radius: 10px;
      box-shadow: 3px 3px 0 rgba(0, 0, 0, 0.1);
      max-width: calc(100% - 2em);
      margin: 1em auto;
      overflow: hidden;
      width: 800px;
    }
    
    table {
      width: 100%;
    }
    table td, table th {
      color: #2b686e;
      padding: 10px;
    }
    table td {
      text-align: center;
      vertical-align: middle;
    }
    table td:last-child {
      font-size: 0.95em;
      line-height: 1.4;
      text-align: left;
    }
    table th {
      background-color: #daeff1;
      font-weight: 300;
    }
    table tr:nth-child(2n) {
      background-color: white;
    }
    table tr:nth-child(2n+1) {
      background-color: #edf7f8;
    }
    
    @media screen and (max-width: 700px) {
      table, tr, td {
        display: block;
      }
    
      td:first-child {
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        width: 100px;
      }
      td:not(:first-child) {
        clear: both;
        margin-left: 100px;
        padding: 4px 20px 4px 90px;
        position: relative;
        text-align: left;
      }
      td:not(:first-child):before {
        color: #91ced4;
        content: "";
        display: block;
        left: 0;
        position: absolute;
      }
      td:nth-child(2):before {
        content: "Name:";
      }
      td:nth-child(3):before {
        content: "Email:";
      }
      td:nth-child(4):before {
        content: "Phone:";
      }
      td:nth-child(5):before {
        content: "Comments:";
      }
    
      tr {
        padding: 10px 0;
        position: relative;
      }
      tr:first-child {
        display: none;
      }
    }
    @media screen and (max-width: 500px) {
      .header {
        background-color: transparent;
        color: white;
        font-size: 2em;
        font-weight: 700;
        padding: 0;
        text-shadow: 2px 2px 0 rgba(0, 0, 0, 0.1);
      }
    
      img {
        border: 3px solid;
        border-color: #daeff1;
        height: 100px;
        margin: 0.5rem 0;
        width: 100px;
      }
    
      td:first-child {
        background-color: #c8e7ea;
        border-bottom: 1px solid #91ced4;
        border-radius: 10px 10px 0 0;
        position: relative;
        top: 0;
        transform: translateY(0);
        width: 100%;
      }
      td:not(:first-child) {
        margin: 0;
        padding: 5px 1em;
        width: 100%;
      }
      td:not(:first-child):before {
        font-size: 0.8em;
        padding-top: 0.3em;
        position: relative;
      }
      td:last-child {
        padding-bottom: 1rem !important;
      }
    
      tr {
        background-color: white !important;
        border: 1px solid #6cbec6;
        border-radius: 10px;
        box-shadow: 2px 2px 0 rgba(0, 0, 0, 0.1);
        margin: 0.5rem 0;
        padding: 0;
      }
    
      .table-users {
        border: none;
        box-shadow: none;
        overflow: visible;
      }
    }
</style>
</head>
"""
    body1 = """
        <body>
    <!-- partial:index.partial.html -->
    <div class="table-users">
       <div class="header">%(name)s</div>
          <table cellspacing="0">
          <tr>
              """ % {
        "name": name
    }
    head = head + body1
    # 添加cols标签
    for col in cols:
        head += f"<th>{col}</th>\n"

    body = """
      </tr>
        """
    rowlist = []
    for row in data:
        ins = "<tr>\n"
        for i, rowi in enumerate(row):
            ins += f"\t<td>{rowi}</td>\n"
        ins += "</tr>\n"
        rowlist.extend(ins)
    body += "".join(rowlist)
    last = """
   </table>
</div>
<!-- partial -->
  
</body>
</html>

        """

    return head + body + last


def table_red(cols: list, data, name="Test Table"):
    r"""This is a beatuiful blue table written by html, you can put into your own data

    example:
    >>> cols = ["Band", "Year formed", "No. of Albums", "Most famous song"]
    >>> data = [
            ["The Clash", "1976", 6, "Ever fallen in love (with someone you shouldn't've)"],
            ["The Clashs", "1964", 5, "Bending Calling"],
            ["The Csflash", "1986", 36, "China Calling"],
        ]
    >>> body = html4table(cols=cols, data=data, name="测试表")
    >>> print(body)
        :param name: 表名
        :param cols: 列名
        :param data: 数据
        :return:
    """
    if not isinstance(data, list):
        raise Exception("The type must be list, please check it...")

    head = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CodePen - Responsive Table</title>
    <!--  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css">-->
    <!--<link rel="stylesheet" href="./style.css">-->
    <style>
        body {
            background-color: #91ced4;
        }

        body * {
            box-sizing: border-box;
        }

        .header {
            background-color: #ea6153;
            color: white;
            font-size: 1.5em;
            padding: 1rem;
            text-align: center;
            text-transform: uppercase;
        }

        img {
            border-radius: 50%;
            height: 60px;
            width: 60px;
        }

        .table-users {
            border: 1px solid #327a81;
            border-radius: 10px;
            box-shadow: 3px 3px 0 rgba(0, 0, 0, 0.1);
            max-width: calc(100% - 2em);
            margin: 1em auto;
            overflow: hidden;
            width: 800px;
        }

        table {
            width: 100%;
        }

        table td, table th {
            color: #ea6153;
            padding: 10px;
        }

        table td {
            text-align: center;
            vertical-align: middle;
        }

        table td:last-child {
            font-size: 0.95em;
            line-height: 1.4;
            text-align: left;
        }

        table th {
            background-color: #daeff1;
            font-weight: 300;
        }

        table tr:nth-child(2n) {
            background-color: white;
        }

        table tr:nth-child(2n+1) {
            background-color: #edf7f8;
        }

        @media screen and (max-width: 700px) {
            table, tr, td {
                display: block;
            }

            td:first-child {
                position: absolute;
                top: 50%;
                transform: translateY(-50%);
                width: 100px;
            }

            td:not(:first-child) {
                clear: both;
                margin-left: 100px;
                padding: 4px 20px 4px 90px;
                position: relative;
                text-align: left;
            }

            td:not(:first-child):before {
                color: #969696;
                content: "";
                display: block;
                left: 0;
                position: absolute;
            }

            td:nth-child(2):before {
                content: "Name:";
            }

            td:nth-child(3):before {
                content: "Email:";
            }

            td:nth-child(4):before {
                content: "Phone:";
            }

            td:nth-child(5):before {
                content: "Comments:";
            }

            tr {
                padding: 10px 0;
                position: relative;
            }

            tr:first-child {
                display: none;
            }
        }

        @media screen and (max-width: 500px) {
            .header {
                background-color: transparent;
                color: white;
                font-size: 2em;
                font-weight: 700;
                padding: 0;
                text-shadow: 2px 2px 0 rgba(0, 0, 0, 0.1);
            }

            img {
                border: 3px solid;
                border-color: #daeff1;
                height: 100px;
                margin: 0.5rem 0;
                width: 100px;
            }

            td:first-child {
                background-color: #c8e7ea;
                border-bottom: 1px solid #91ced4;
                border-radius: 10px 10px 0 0;
                position: relative;
                top: 0;
                transform: translateY(0);
                width: 100%;
            }

            td:not(:first-child) {
                margin: 0;
                padding: 5px 1em;
                width: 100%;
            }

            td:not(:first-child):before {
                font-size: 0.8em;
                padding-top: 0.3em;
                position: relative;
            }

            td:last-child {
                padding-bottom: 1rem !important;
            }

            tr {
                background-color: white !important;
                border: 1px solid #6cbec6;
                border-radius: 10px;
                box-shadow: 2px 2px 0 rgba(0, 0, 0, 0.1);
                margin: 0.5rem 0;
                padding: 0;
            }

            .table-users {
                border: none;
                box-shadow: none;
                overflow: visible;
            }
        }
    </style>
</head>
    """
    body1 = """
        <body>
    <!-- partial:index.partial.html -->
    <div class="table-users">
       <div class="header">%(name)s</div>
          <table cellspacing="0">
          <tr>
              """ % {
        "name": name
    }
    head = head + body1
    # 添加cols标签
    for col in cols:
        head += f"<th>{col}</th>\n"

    body = """
      </tr>
        """
    rowlist = []
    for row in data:
        ins = "<tr>\n"
        for i, rowi in enumerate(row):
            ins += f"\t<td>{rowi}</td>\n"
        ins += "</tr>\n"
        rowlist.extend(ins)
    body += "".join(rowlist)
    last = """
   </table>
</div>
<!-- partial -->

</body>
</html>

        """
    return head + body + last

def table_green(cols: list, data, name="Test Table"):
    r"""This is a beatuiful blue table written by html, you can put into your own data

    example:
    >>> cols = ["Band", "Year formed", "No. of Albums", "Most famous song"]
    >>> data = [
            ["The Clash", "1976", 6, "Ever fallen in love (with someone you shouldn't've)"],
            ["The Clashs", "1964", 5, "Bending Calling"],
            ["The Csflash", "1986", 36, "China Calling"],
        ]
    >>> body = html4table(cols=cols, data=data, name="测试表")
    >>> print(body)
        :param name: 表名
        :param cols: 列名
        :param data: 数据
        :return:
    """
    if not isinstance(data, list):
        raise Exception("The type must be list, please check it...")

    head = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CodePen - Responsive Table</title>
    <!--  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css">-->
    <!--<link rel="stylesheet" href="./style.css">-->
    <style>
        body {
            background-color: #91ced4;
        }

        body * {
            box-sizing: border-box;
        }

        .header {
            background-color: #27ae60;
            color: white;
            font-size: 1.5em;
            padding: 1rem;
            text-align: center;
            text-transform: uppercase;
        }

        img {
            border-radius: 50%;
            height: 60px;
            width: 60px;
        }

        .table-users {
            border: 1px solid #327a81;
            border-radius: 10px;
            box-shadow: 3px 3px 0 rgba(0, 0, 0, 0.1);
            max-width: calc(100% - 2em);
            margin: 1em auto;
            overflow: hidden;
            width: 800px;
        }

        table {
            width: 100%;
        }

        table td, table th {
            color: #27ae60;
            padding: 10px;
        }

        table td {
            text-align: center;
            vertical-align: middle;
        }

        table td:last-child {
            font-size: 0.95em;
            line-height: 1.4;
            text-align: left;
        }

        table th {
            background-color: #daeff1;
            font-weight: 300;
        }

        table tr:nth-child(2n) {
            background-color: white;
        }

        table tr:nth-child(2n+1) {
            background-color: #edf7f8;
        }

        @media screen and (max-width: 700px) {
            table, tr, td {
                display: block;
            }

            td:first-child {
                position: absolute;
                top: 50%;
                transform: translateY(-50%);
                width: 100px;
            }

            td:not(:first-child) {
                clear: both;
                margin-left: 100px;
                padding: 4px 20px 4px 90px;
                position: relative;
                text-align: left;
            }

            td:not(:first-child):before {
                color: #969696;
                content: "";
                display: block;
                left: 0;
                position: absolute;
            }

            td:nth-child(2):before {
                content: "Name:";
            }

            td:nth-child(3):before {
                content: "Email:";
            }

            td:nth-child(4):before {
                content: "Phone:";
            }

            td:nth-child(5):before {
                content: "Comments:";
            }

            tr {
                padding: 10px 0;
                position: relative;
            }

            tr:first-child {
                display: none;
            }
        }

        @media screen and (max-width: 500px) {
            .header {
                background-color: transparent;
                color: white;
                font-size: 2em;
                font-weight: 700;
                padding: 0;
                text-shadow: 2px 2px 0 rgba(0, 0, 0, 0.1);
            }

            img {
                border: 3px solid;
                border-color: #daeff1;
                height: 100px;
                margin: 0.5rem 0;
                width: 100px;
            }

            td:first-child {
                background-color: #c8e7ea;
                border-bottom: 1px solid #91ced4;
                border-radius: 10px 10px 0 0;
                position: relative;
                top: 0;
                transform: translateY(0);
                width: 100%;
            }

            td:not(:first-child) {
                margin: 0;
                padding: 5px 1em;
                width: 100%;
            }

            td:not(:first-child):before {
                font-size: 0.8em;
                padding-top: 0.3em;
                position: relative;
            }

            td:last-child {
                padding-bottom: 1rem !important;
            }

            tr {
                background-color: white !important;
                border: 1px solid #6cbec6;
                border-radius: 10px;
                box-shadow: 2px 2px 0 rgba(0, 0, 0, 0.1);
                margin: 0.5rem 0;
                padding: 0;
            }

            .table-users {
                border: none;
                box-shadow: none;
                overflow: visible;
            }
        }
    </style>
</head>
    """
    body1 = """
        <body>
    <!-- partial:index.partial.html -->
    <div class="table-users">
       <div class="header">%(name)s</div>
          <table cellspacing="0">
          <tr>
              """ % {
        "name": name
    }
    head = head + body1
    # 添加cols标签
    for col in cols:
        head += f"<th>{col}</th>\n"

    body = """
      </tr>
        """
    rowlist = []
    for row in data:
        ins = "<tr>\n"
        for i, rowi in enumerate(row):
            ins += f"\t<td>{rowi}</td>\n"
        ins += "</tr>\n"
        rowlist.extend(ins)
    body += "".join(rowlist)
    last = """
   </table>
</div>
<!-- partial -->

</body>
</html>

        """
    return head + body + last

def color_table(cols: list, data, style='red'):
    if not isinstance(data, list):
        raise Exception("The type must be list, please check it...")

    head = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CodePen - CSS Responsive Table Layout</title>
    <!--  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css">-->
    <style>
                body {
            background-color: #91ced4;
        }


        @media screen and (max-width: 580px) {
            body {
                font-size: 16px;
                line-height: 22px;
            }
        }

        .wrapper {
            margin: 0 auto;
            padding: 40px;
            max-width: 900px;
        }

        .table {
            /*border: 1px solid #327a81;*/
            border-radius: 10px;
            box-shadow: 3px 3px 0 rgba(0, 0, 0, 0.1);
            margin: 1em auto;
            overflow: hidden;
            display: table;
            width: 100%;
        }

        @media screen and (max-width: 580px) {
            .table {
                display: block;
            }
        }

        .row {
            display: table-row;
            background: #f6f6f6;
        }

        .row:nth-of-type(odd) {
            background: #e9e9e9;
        }

        .row.header {
            font-weight: 900;
            color: #ffffff;
            background: #ea6153;
        }

        .row.green {
            background: #27ae60;
        }

        .row.blue {
            background: #2980b9;
        }

        @media screen and (max-width: 580px) {
            .row {
                padding: 14px 0 7px;
                display: block;
            }

            .row.header {
                padding: 0;
                height: 6px;
            }

            .row.header .cell {
                display: none;
            }

            .row .cell {
                margin-bottom: 10px;
            }

            .row .cell:before {
                margin-bottom: 3px;
                content: attr(data-title);
                min-width: 98px;
                font-size: 10px;
                line-height: 10px;
                font-weight: bold;
                text-transform: uppercase;
                color: #969696;
                display: block;
            }
        }

        .cell {
            padding: 6px 12px;
            display: table-cell;
        }

        @media screen and (max-width: 580px) {
            .cell {
                padding: 2px 16px;
                display: block;
            }
        }
    </style>

</head>
<body>
<!-- partial:index.partial.html -->
<div class="wrapper">

    <div class="table">
    """
    head = head + f'\n        <div class="row header {style}">'
    # 添加cols标签
    for col in cols:
        head += f'<div class="cell">{col}</div>\n'

    body = """
      </div>
        """
    rowlist = []
    for row in data:
        ins = '<div class="row">'
        for i, rowi in enumerate(row):
            ins += f'\t<div class="cell" >{rowi}</div>\n'
        ins += '</div>'
        rowlist.extend(ins)
    body += "".join(rowlist)
    last = """
    </div>

</div>
<!-- partial -->
<!--<script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>-->
</body>
</html>
        """
    return head + body + last


def two_diff_color_table(cols1: list, data1,cols2: list, data2, style1='red', style2='red'):

    head = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CodePen - CSS Responsive Table Layout</title>
    <!--  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css">-->
    <style>
                body {
            background-color: #91ced4;
        }


        @media screen and (max-width: 580px) {
            body {
                font-size: 16px;
                line-height: 22px;
            }
        }

        .wrapper {
            margin: 0 auto;
            padding: 40px;
            max-width: 900px;
        }

        .table {
            /*border: 1px solid #327a81;*/
            border-radius: 10px;
            box-shadow: 3px 3px 0 rgba(0, 0, 0, 0.1);
            margin: 1em auto;
            overflow: hidden;
            display: table;
            width: 100%;
        }

        @media screen and (max-width: 580px) {
            .table {
                display: block;
            }
        }

        .row {
            display: table-row;
            background: #f6f6f6;
        }

        .row:nth-of-type(odd) {
            background: #e9e9e9;
        }

        .row.header {
            font-weight: 900;
            color: #ffffff;
            background: #ea6153;
        }

        .row.green {
            background: #27ae60;
        }

        .row.blue {
            background: #2980b9;
        }

        @media screen and (max-width: 580px) {
            .row {
                padding: 14px 0 7px;
                display: block;
            }

            .row.header {
                padding: 0;
                height: 6px;
            }

            .row.header .cell {
                display: none;
            }

            .row .cell {
                margin-bottom: 10px;
            }

            .row .cell:before {
                margin-bottom: 3px;
                content: attr(data-title);
                min-width: 98px;
                font-size: 10px;
                line-height: 10px;
                font-weight: bold;
                text-transform: uppercase;
                color: #969696;
                display: block;
            }
        }

        .cell {
            padding: 6px 12px;
            display: table-cell;
        }

        @media screen and (max-width: 580px) {
            .cell {
                padding: 2px 16px;
                display: block;
            }
        }
    </style>

</head>
<body>
<!-- partial:index.partial.html -->
<div class="wrapper">

    """
    # table one
    head = head + f'    <div class="table">\n        <div class="row header {style1}">'
    # 添加cols标签
    for col in cols1:
        head += f'<div class="cell">{col}</div>\n'
    head += '</div>'

    rowlist = []
    for row in data1:
        ins = '<div class="row">'
        for i, rowi in enumerate(row):
            ins += f'\t<div class="cell" >{rowi}</div>\n'
        ins += '</div>'
        rowlist.extend(ins)
    head += "".join(rowlist)
    head += '</div>'

    # table two
    head = head + f'    <div class="table">\n        <div class="row header {style2}">'
    # 添加cols标签
    for col in cols2:
        head += f'<div class="cell">{col}</div>\n'
    head += '</div>'

    rowlist = []
    for row in data2:
        ins = '<div class="row">'
        for i, rowi in enumerate(row):
            ins += f'\t<div class="cell" >{rowi}</div>\n'
        ins += '</div>'
        rowlist.extend(ins)
    head += "".join(rowlist)
    head += '</div>'

    last = """
    </div>

</div>
<!-- partial -->
<!--<script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>-->
</body>
</html>
        """
    return head + last

if __name__ == "__main__":
    cols = ["Band", "Year formed", "No. of Albums", "Most famous song"]
    data = [
        ["The Clash", "1976", 6, "Ever fallen in love (with someone you shouldn't've)"],
        ["The Clashs", "1964", 5, "Bending Calling"],
        ["The Csflash", "1986", 36, "China Calling"],
    ]
    body = two_diff_color_table(cols1=cols, data1=data,cols2=cols, data2=data, style1='green', style2='red')

    if is_workday(datetime.datetime.now()):
        mailer = Mailer(
            host="smtpdm.aliyun.com",
            port=80,
            user="elkmonitor@kaisasecurities.site",
            pwd="Sz0a3ncf2c2ZFbLj",
        )
        msg = Message()
        msg.From = "佳兆业金融科技舆情监控测试邮件"
        msg.To = ["songzhij@kaisagroup.com"]
        msg.Cc = []
        msg.Subject = "佳兆业金融科技舆情监控测试邮件"
        msg.Html = body
        mailer.send(msg)  # just send your message through the mailer

if __name__ == "__main__1":
    cols = ["Band", "Year formed", "No. of Albums", "Most famous song"]
    data = [
        ["The Clash", "1976", 6, "Ever fallen in love (with someone you shouldn't've)"],
        ["The Clashs", "1964", 5, "Bending Calling"],
        ["The Csflash", "1986", 36, "China Calling"],
    ]
    body = color_table(cols=cols, data=data, style='green')
    # print(body)
    # body = table_blue(cols=cols, data=data, name="测试表")
    if is_workday(datetime.datetime.now()):
        mailer = Mailer(
            host="smtpdm.aliyun.com",
            port=80,
            user="elkmonitor@kaisasecurities.site",
            pwd="Sz0a3ncf2c2ZFbLj",
        )
        msg = Message()
        msg.From = "佳兆业金融科技舆情监控测试邮件"
        msg.To = ["songzhij@kaisagroup.com"]
        msg.Cc = []
        msg.Subject = "佳兆业金融科技舆情监控测试邮件"
        msg.Html = body
        mailer.send(msg)  # just send your message through the mailer
