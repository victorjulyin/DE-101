import pandas as pd
import sqlite3

CON = sqlite3.connect('example.db')

# Выгрузка данных с сайта
def extract_data(url):
    """ Extract CSV
    """
    return pd.read_csv(url)

# Группировка данных
def transform_data(data, group, agreg):
    """ Group by data
    """
    return data.groupby(group).agg(agreg).reset_index()

# Загрузка в базу данных
# Для тех кто не работал с pandas+sqlite
# data_frame.to_sql(...) автоматически создаст sqlite базу данных
def load_data(data, table_name, conn=CON):
    """ Load to DB
    """
    data["insert_time"] = pd.to_datetime("now")
    data.to_sql(table_name, conn, if_exists='replace', index=False)

# Отправка данных на почту
def send_email(data, cred, host, port, to, From):
    """ Send to email
    """ 
    _send_email(data=data, cred=cred, host=host, to=to, From=From, port=port)




from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

HOST = "smtp.yandex.ru"
TO = "v.julyin@yandex.ru"
FROM = "v.julyin@yandex.ru"

def html_pretty(df):
    """ Pretty html dataframe
    """
    return """\
    <html>
      <head></head>
      <body>
        {0}
      </body>
    </html>
    """.format(df.to_html())

def _send_email(data, cred, host, port, to, From):
    """ Send DF to email
    """

    msg = MIMEMultipart()
    part = MIMEText(html_pretty(data), 'html')
    msg.attach(part)

    server = smtplib.SMTP(host, port)
    server.starttls()
    server.login(cred[0], cred[1])
    server.sendmail(From, to, msg.as_string())
    server.quit()


if __name__ == '__main__':

    # Extract
    data = extract_data(
        "https://raw.githubusercontent.com/dm-novikov/stepik_airflow_course/main/data/data.csv")

    # Transform
    data = transform_data(data,
                          group=['A', 'B', 'C'],
                          agreg={"D": sum})

    # Load to DB
    load_data(data, "table")

    # Send Email
    send_email(data, cred=("v.julyin@yandex.ru", "A01020304-"), host=HOST, port=587, to=TO, From=FROM)

    
