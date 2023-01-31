## First Module plan

1)
2) 
3) 
4) 
5) 

## The task

PIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PICPIC PIC PIC PIC
**M1_1**

**The task: Load the Data from an external source  everyday and provide a revenue statistics in available sections. The report must come to the whole team mail at 10 am. Data should be saved in a local Data Base.**

## The Python solution

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

### Everything works, but there are some problems

  * We can't see at what step our script broke
  * Is idempotence saved?
  * How to inform us that script broke down?
  * All steps in sequence

These are problems that are solved with tools such as Airflow.

## DAG

Directed Acyclic Graph:
  * Doesn't have cycles
  * Every node has an direction
  * Parallel steps possibility
  * Finiteness of the system

**M1_6**
**M1_7**

## Idempotency

This is a property of a system or procedure that means that its results are independent of external factors and do not change when called again with the same input.

For example, this function returns the figure square:

  def square(x):
    return x * x

If we'll call square(5) now and one month later, the result will be the same. This is idempotency.
In the Data case - it is important to not duplicate Data.



