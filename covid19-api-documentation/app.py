from chalice import Chalice,Response

app = Chalice(app_name='covid19-api-documentation')


@app.route("/")
def index():
    return Response(body="""
    
<h1>
COVID 19 APIS
</h1>

<pre>
The following APIs feed off a database designed to help the fight against covid 19
The database is a centralized source of publicly available data 
The sources for each data set are listed in the below documentation
</pre>



<h2>Database ERD</h2>

<pre>
Each table can be accessed using the following base API Call followed by the table name
https://9gnht4xyvf.execute-api.eu-west-1.amazonaws.com/api/get_table/
</pre>

<img src="https://erd2corona.s3-eu-west-1.amazonaws.com/erd.PNG">

<h2>
How to get the API output into Python
</h2>


<pre>
<code>
import pandas as pd 
import numpy as np
import requests

r = requests.get('https://9gnht4xyvf.execute-api.eu-west-1.amazonaws.com/api/get_table/CasesGlobal')
x = r.json()
df = pd.DataFrame(x)
</code>
</pre>



<h2>
Database views available as APIs
</h2>

<h3>
1. Global Cases API
</h3>

<a href="https://9gnht4xyvf.execute-api.eu-west-1.amazonaws.com/api/get_table/CasesGlobalView">https://9gnht4xyvf.execute-api.eu-west-1.amazonaws.com/api/get_table/CasesGlobalView</a>


<h5>

<pre> <h3>Source:</h3> 
2019 Novel Coronavirus COVID-19 (2019-nCoV) Data Repository by Johns Hopkins CSSE. 
https://github.com/CSSEGISandData/COVID-19
</pre>

</h5>


<h4>
Example Output
</h4>


<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>date</th>\n      <th>country</th>\n      <th>lat</th>\n      <th>long</th>\n      <th>confirmed</th>\n      <th>deaths</th>\n      <th>recovered</th>\n      <th>active</th>\n      <th>confirmed_daily</th>\n      <th>deaths_daily</th>\n      <th>recovered_daily</th>\n      <th>daily_change_in_active_cases</th>\n      <th>active_dailiy_growth_rate</th>\n      <th>active_rolling_3_day_growth_rate</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>2020-02-24</td>\n      <td>Afghanistan</td>\n      <td>33.0</td>\n      <td>65.0</td>\n      <td>1</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>2020-02-25</td>\n      <td>Afghanistan</td>\n      <td>33.0</td>\n      <td>65.0</td>\n      <td>1</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.000000</td>\n      <td>NaN</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>2020-02-26</td>\n      <td>Afghanistan</td>\n      <td>33.0</td>\n      <td>65.0</td>\n      <td>1</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.000000</td>\n      <td>NaN</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>2020-02-27</td>\n      <td>Afghanistan</td>\n      <td>33.0</td>\n      <td>65.0</td>\n      <td>1</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>2020-02-28</td>\n      <td>Afghanistan</td>\n      <td>33.0</td>\n      <td>65.0</td>\n      <td>1</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>2020-02-29</td>\n      <td>Afghanistan</td>\n      <td>33.0</td>\n      <td>65.0</td>\n      <td>1</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>2020-03-01</td>\n      <td>Afghanistan</td>\n      <td>33.0</td>\n      <td>65.0</td>\n      <td>1</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>2020-03-02</td>\n      <td>Afghanistan</td>\n      <td>33.0</td>\n      <td>65.0</td>\n      <td>1</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>2020-03-03</td>\n      <td>Afghanistan</td>\n      <td>33.0</td>\n      <td>65.0</td>\n      <td>1</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>9</th>\n      <td>2020-03-04</td>\n      <td>Afghanistan</td>\n      <td>33.0</td>\n      <td>65.0</td>\n      <td>1</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>10</th>\n      <td>2020-03-05</td>\n      <td>Afghanistan</td>\n      <td>33.0</td>\n      <td>65.0</td>\n      <td>1</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>11</th>\n      <td>2020-03-06</td>\n      <td>Afghanistan</td>\n      <td>33.0</td>\n      <td>65.0</td>\n      <td>1</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>12</th>\n      <td>2020-03-07</td>\n      <td>Afghanistan</td>\n      <td>33.0</td>\n      <td>65.0</td>\n      <td>1</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>13</th>\n      <td>2020-03-08</td>\n      <td>Afghanistan</td>\n      <td>33.0</td>\n      <td>65.0</td>\n      <td>4</td>\n      <td>0</td>\n      <td>0</td>\n      <td>4</td>\n      <td>3.0</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>3.0</td>\n      <td>3.000000</td>\n      <td>0.587400</td>\n    </tr>\n    <tr>\n      <th>14</th>\n      <td>2020-03-09</td>\n      <td>Afghanistan</td>\n      <td>33.0</td>\n      <td>65.0</td>\n      <td>4</td>\n      <td>0</td>\n      <td>0</td>\n      <td>4</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.000000</td>\n      <td>0.587400</td>\n    </tr>\n    <tr>\n      <th>15</th>\n      <td>2020-03-10</td>\n      <td>Afghanistan</td>\n      <td>33.0</td>\n      <td>65.0</td>\n      <td>5</td>\n      <td>0</td>\n      <td>0</td>\n      <td>5</td>\n      <td>1.0</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>1.0</td>\n      <td>0.250000</td>\n      <td>0.709975</td>\n    </tr>\n    <tr>\n      <th>16</th>\n      <td>2020-03-11</td>\n      <td>Afghanistan</td>\n      <td>33.0</td>\n      <td>65.0</td>\n      <td>7</td>\n      <td>0</td>\n      <td>0</td>\n      <td>7</td>\n      <td>2.0</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>2.0</td>\n      <td>0.400000</td>\n      <td>0.205071</td>\n    </tr>\n    <tr>\n      <th>17</th>\n      <td>2020-03-12</td>\n      <td>Afghanistan</td>\n      <td>33.0</td>\n      <td>65.0</td>\n      <td>7</td>\n      <td>0</td>\n      <td>0</td>\n      <td>7</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.000000</td>\n      <td>0.205071</td>\n    </tr>\n    <tr>\n      <th>18</th>\n      <td>2020-03-13</td>\n      <td>Afghanistan</td>\n      <td>33.0</td>\n      <td>65.0</td>\n      <td>7</td>\n      <td>0</td>\n      <td>0</td>\n      <td>7</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>0.000000</td>\n      <td>0.118689</td>\n    </tr>\n    <tr>\n      <th>19</th>\n      <td>2020-03-14</td>\n      <td>Afghanistan</td>\n      <td>33.0</td>\n      <td>65.0</td>\n      <td>11</td>\n      <td>0</td>\n      <td>0</td>\n      <td>11</td>\n      <td>4.0</td>\n      <td>0.0</td>\n      <td>0.0</td>\n      <td>4.0</td>\n      <td>0.571429</td>\n      <td>0.162603</td>\n    </tr>\n  </tbody>\n</table>



<h3>
2. Local Cases API
</h3>

<a href="https://9gnht4xyvf.execute-api.eu-west-1.amazonaws.com/api/get_table/CasesLocalView">https://9gnht4xyvf.execute-api.eu-west-1.amazonaws.com/api/get_table/CasesLocalView</a>

<h5>

<pre> <h3>Source:</h3> 
COVID 19 Data and Dashboard for South Africa  by DataScience for Social Impact 
https://github.com/dsfsi/covid19za
</pre>

</h5>




<h4>
Example Output
</h4>



'<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>id</th>\n      <th>country_id</th>\n      <th>location</th>\n      <th>location_level</th>\n      <th>date</th>\n      <th>confirmed</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>1</td>\n      <td>153</td>\n      <td>EC</td>\n      <td>Provincial</td>\n      <td>2020-03-05</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>1</td>\n      <td>153</td>\n      <td>EC</td>\n      <td>Provincial</td>\n      <td>2020-03-07</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>1</td>\n      <td>153</td>\n      <td>EC</td>\n      <td>Provincial</td>\n      <td>2020-03-08</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>1</td>\n      <td>153</td>\n      <td>EC</td>\n      <td>Provincial</td>\n      <td>2020-03-09</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>1</td>\n      <td>153</td>\n      <td>EC</td>\n      <td>Provincial</td>\n      <td>2020-03-11</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>1</td>\n      <td>153</td>\n      <td>EC</td>\n      <td>Provincial</td>\n      <td>2020-03-12</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>1</td>\n      <td>153</td>\n      <td>EC</td>\n      <td>Provincial</td>\n      <td>2020-03-13</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>1</td>\n      <td>153</td>\n      <td>EC</td>\n      <td>Provincial</td>\n      <td>2020-03-14</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>1</td>\n      <td>153</td>\n      <td>EC</td>\n      <td>Provincial</td>\n      <td>2020-03-15</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>9</th>\n      <td>1</td>\n      <td>153</td>\n      <td>EC</td>\n      <td>Provincial</td>\n      <td>2020-03-16</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>10</th>\n      <td>1</td>\n      <td>153</td>\n      <td>EC</td>\n      <td>Provincial</td>\n      <td>2020-03-17</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>11</th>\n      <td>1</td>\n      <td>153</td>\n      <td>EC</td>\n      <td>Provincial</td>\n      <td>2020-03-18</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>12</th>\n      <td>1</td>\n      <td>153</td>\n      <td>EC</td>\n      <td>Provincial</td>\n      <td>2020-03-19</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>13</th>\n      <td>1</td>\n      <td>153</td>\n      <td>EC</td>\n      <td>Provincial</td>\n      <td>2020-03-20</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>14</th>\n      <td>1</td>\n      <td>153</td>\n      <td>EC</td>\n      <td>Provincial</td>\n      <td>2020-03-21</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>15</th>\n      <td>1</td>\n      <td>153</td>\n      <td>EC</td>\n      <td>Provincial</td>\n      <td>2020-03-22</td>\n      <td>2</td>\n    </tr>\n    <tr>\n      <th>16</th>\n      <td>1</td>\n      <td>153</td>\n      <td>EC</td>\n      <td>Provincial</td>\n      <td>2020-03-23</td>\n      <td>2</td>\n    </tr>\n    <tr>\n      <th>17</th>\n      <td>1</td>\n      <td>153</td>\n      <td>EC</td>\n      <td>Provincial</td>\n      <td>2020-03-24</td>\n      <td>2</td>\n    </tr>\n    <tr>\n      <th>18</th>\n      <td>1</td>\n      <td>153</td>\n      <td>EC</td>\n      <td>Provincial</td>\n      <td>2020-03-25</td>\n      <td>2</td>\n    </tr>\n    <tr>\n      <th>19</th>\n      <td>1</td>\n      <td>153</td>\n      <td>EC</td>\n      <td>Provincial</td>\n      <td>2020-03-26</td>\n      <td>5</td>\n    </tr>\n  </tbody>\n</table>'


<h3>
3. Local Tests Done API 
</h3>

<a href="https://9gnht4xyvf.execute-api.eu-west-1.amazonaws.com/api/get_table/CasesLocalView">https://9gnht4xyvf.execute-api.eu-west-1.amazonaws.com/api/get_table/Testing</a>

<h5>

<pre> <h3>Source:</h3> 
COVID 19 Data and Dashboard for South Africa  by DataScience for Social Impact 
https://github.com/dsfsi/covid19za
</pre>

</h5>

<h4>
Example Output
</h4>


'<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>date</th>\n      <th>cumulative_tests</th>\n      <th>country</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>2020-02-11</td>\n      <td>61</td>\n      <td>South Africa</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>2020-02-13</td>\n      <td>67</td>\n      <td>South Africa</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>2020-02-14</td>\n      <td>71</td>\n      <td>South Africa</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>2020-02-19</td>\n      <td>95</td>\n      <td>South Africa</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>2020-02-20</td>\n      <td>106</td>\n      <td>South Africa</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>2020-02-24</td>\n      <td>116</td>\n      <td>South Africa</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>2020-02-26</td>\n      <td>121</td>\n      <td>South Africa</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>2020-03-02</td>\n      <td>160</td>\n      <td>South Africa</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>2020-03-03</td>\n      <td>164</td>\n      <td>South Africa</td>\n    </tr>\n    <tr>\n      <th>9</th>\n      <td>2020-03-06</td>\n      <td>200</td>\n      <td>South Africa</td>\n    </tr>\n    <tr>\n      <th>10</th>\n      <td>2020-03-07</td>\n      <td>241</td>\n      <td>South Africa</td>\n    </tr>\n    <tr>\n      <th>11</th>\n      <td>2020-03-11</td>\n      <td>645</td>\n      <td>South Africa</td>\n    </tr>\n    <tr>\n      <th>12</th>\n      <td>2020-03-12</td>\n      <td>848</td>\n      <td>South Africa</td>\n    </tr>\n    <tr>\n      <th>13</th>\n      <td>2020-03-13</td>\n      <td>924</td>\n      <td>South Africa</td>\n    </tr>\n    <tr>\n      <th>14</th>\n      <td>2020-03-14</td>\n      <td>1017</td>\n      <td>South Africa</td>\n    </tr>\n    <tr>\n      <th>15</th>\n      <td>2020-03-15</td>\n      <td>1476</td>\n      <td>South Africa</td>\n    </tr>\n    <tr>\n      <th>16</th>\n      <td>2020-03-16</td>\n      <td>2405</td>\n      <td>South Africa</td>\n    </tr>\n    <tr>\n      <th>17</th>\n      <td>2020-03-17</td>\n      <td>2911</td>\n      <td>South Africa</td>\n    </tr>\n    <tr>\n      <th>18</th>\n      <td>2020-03-18</td>\n      <td>3070</td>\n      <td>South Africa</td>\n    </tr>\n    <tr>\n      <th>19</th>\n      <td>2020-03-19</td>\n      <td>4832</td>\n      <td>South Africa</td>\n    </tr>\n  </tbody>\n</table>'

""",
                    status_code=200,
                    headers={'Content-Type': 'text/html'})

