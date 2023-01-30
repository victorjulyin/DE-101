## The task

PIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PIC
**M1_1**

**The task: Load the Data from an external source  everyday and provide a revenue statistics in available sections. The report must come to the whole team mail at 10 am. Data should be saved in a local Data Base.**

## The solution

### We can use some programming language to make pipelines, Python in this case.

I had to install pandas package first:

    pip3 install pandas 

**M1_2**

Then I used [this script](ССЫЛЬ НА ФАЙЛ КОТОРЫЙ В ПАПКЕ) to send go through that pipeline (I didn't write it).

**M1_3**

#### I had a problem

When I tried to start the command via Terminal I received this error:

    urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:997)>


Then I found this file => clicked on it => the problem was solved:

    /Applications/Python 3.10/Install Certificates.command



### CRON setup

**M1_4**


To edit or create a crontab file:

    $ export EDITOR=nano
    $ crontab -e



I'll use this script:

    $ 0 10 * * * python3 *full_path*


To quit and save push **ctrl + X** => **Y**.

Finally:

    0 10 * * * /usr/local/bin/python3 "/Users/a1/Documents/GitHub/DE-101/Apache Airflow/M1 ETL introduction - Write the pipeline/try_m1.py"

**M1_5**

#### Some Bash notes

    # delete all symbols in a row
    $ ctrl + K 

    # go to the row end 
    $ ctrl + e

    # go to the row start
    $ ctrl + a
