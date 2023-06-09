import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from tasks import DBT_0, Script_1, Script_2
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "test_abhisheks_e2etests_SQL_BigqueryMain_AirflowGCP_BQ", 
    schedule_interval = "0 0 * * *", 
    default_args = {"owner" : "Prophecy", "ignore_first_depends_on_past" : True, "do_xcom_push" : True}, 
    start_date = pendulum.today('UTC'), 
    catchup = True
) as dag:
    DBT_0_op = DBT_0()
    Script_1_op = Script_1()
    Script_2_op = Script_2()
    DBT_0_op >> Script_1_op
    Script_1_op >> Script_2_op
