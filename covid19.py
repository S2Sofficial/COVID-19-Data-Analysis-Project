# COVID-19 Data Analysis Project

import pandas as pd
covid_data= pd.read_csv('covid.csv')
print(covid_data)
print("\nDataset information:")
print(covid_data.info())
print("\nMissing data information:")
print(covid_data.isna().sum())
print()
print('---------------------------------------------------------------------------------------------------')
print('To Get the latest number of confirmed, deaths, recovered and active cases of Novel Coronavirus Country wise')
covid_data= pd.read_csv('https://raw.githubusercontent.com/S2Sofficial/COVID-19-Data-Analysis-Project/main/covid.csv')
covid_data['Active'] = covid_data['Confirmed'] - covid_data['Deaths'] - covid_data['Recovered']
result = covid_data.groupby('Country/Region')['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()
print(result) 

print()
print('-------------------------------------------------------------------------------------------------------')
print('To Get Latest number of confirmed deaths and recovered people of Novel Coronavirus cases Country wise')
covid_data= pd.read_csv('ttps://raw.githubusercontent.com/S2Sofficial/COVID-19-Data-Analysis-Project/main/covid.csv')
data = covid_data.groupby(['Country/Region', 'Province/State'])['Confirmed', 'Deaths', 'Recovered'].max()
pd.set_option('display.max_rows', None)
print(data)

print()
print('-------------------------------------------------------------------------------------------------------')
print('To Get the Chinese province wise cases of confirmed, deaths and recovered cases of Novel Coronavirus')
covid_data= pd.read_csv('https://raw.githubusercontent.com/S2Sofficial/COVID-19-Data-Analysis-Project/main/covid.csv')
c_data = covid_data[covid_data['Country/Region']=='China']
c_data = c_data[['Province/State', 'Confirmed', 'Deaths', 'Recovered']]
result = c_data.sort_values(by='Confirmed', ascending=False)
result = result.reset_index(drop=True)
print(result)


print()
print('-------------------------------------------------------------------------------------------------------')
print('To Get the latest country wise deaths cases of Novel Coronavirus')
covid_data= pd.read_csv('https://raw.githubusercontent.com/S2Sofficial/COVID-19-Data-Analysis-Project/main/covid.csv')
data = covid_data.groupby('Country/Region')['Confirmed', 'Deaths', 'Recovered'].sum().reset_index()
result = data[data['Deaths']>0][['Country/Region', 'Deaths']]
print(result)

print()
print('-------------------------------------------------------------------------------------------------------')
print('to get the List  of countries with no cases of Novel Coronavirus recovered')
covid_data= pd.read_csv('https://raw.githubusercontent.com/S2Sofficial/COVID-19-Data-Analysis-Project/main/covid.csv')
data = covid_data.groupby('Country/Region')['Confirmed', 'Deaths', 'Recovered'].sum().reset_index()
result = data[data['Recovered']==0][['Country/Region', 'Confirmed', 'Deaths', 'Recovered']]
print(result)

print()
print('List of countries with all cases of Novel Coronavirus died')
print('----------------------------------------------------------------------------------------------------')
covid_data= pd.read_csv('https://raw.githubusercontent.com/S2Sofficial/COVID-19-Data-Analysis-Project/main/covid.csv')
data = covid_data.groupby('Country/Region')['Confirmed', 'Deaths', 'Recovered'].sum().reset_index()
result = data[data['Confirmed']==data['Deaths']]
result = result[['Country/Region', 'Confirmed', 'Deaths']]
result = result.sort_values('Confirmed', ascending=False)
result = result[result['Confirmed']>0]
result = result.reset_index(drop=True)
print(result)


print()
print('------------------------------------------------------------------------------------------------')
print('List of countries with all cases of Novel Coronavirus recovered')
covid_data= pd.read_csv('https://raw.githubusercontent.com/S2Sofficial/COVID-19-Data-Analysis-Project/main/covid.csv')
data = covid_data.groupby('Country/Region')['Confirmed', 'Deaths', 'Recovered'].sum().reset_index()
result = data[data['Confirmed']==data['Recovered']]
result = result[['Country/Region', 'Confirmed', 'Recovered']]
result = result.sort_values('Confirmed', ascending=False)
result = result[result['Confirmed']>0]
result = result.reset_index(drop=True)
print(result)


print()
print('----------------------------------------------------------------------------------------------')
print(' To Get the top 10 countries data of Novel Coronavirus')
covid_data= pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-18-2020.csv', usecols = ['Last Update', 'Country/Region', 'Confirmed', 'Deaths', 'Recovered'])
result = covid_data.groupby('Country/Region').max().sort_values(by='Confirmed', ascending=False)[:10]
pd.set_option('display.max_column', None)
print(result)

'''
Output:
            Province/State                    Country/Region  \
0                           Hubei                             China   
1                             NaN                             Italy   
2                             NaN                              Iran   
3                             NaN                             Spain   
4                             NaN                           Germany   
5                             NaN                      Korea, South   
6                          France                            France   
7                             NaN                       Switzerland   
8                  United Kingdom                    United Kingdom   
9                        New York                                US   
10                    Netherlands                       Netherlands   
11                            NaN                            Norway   
12                      Guangdong                             China   
13                            NaN                           Austria   
14                          Henan                             China   
15                            NaN                           Belgium   
16                       Zhejiang                             China   
17                            NaN                            Sweden   
18                     Washington                                US   
19                          Hunan                             China   
20                          Anhui                             China   
21                        Denmark                           Denmark   
22                        Jiangxi                             China   
23                            NaN                             Japan   
24                       Shandong                             China   
25                     California                                US   
26               Diamond Princess                       Cruise Ship   
27                            NaN                          Malaysia   
28                        Jiangsu                             China   
29                      Chongqing                             China   
30                        Sichuan                             China   
31                   Heilongjiang                             China   
32                        Beijing                             China   
33                            NaN                          Portugal   
34                            NaN                             Qatar   
35                            NaN                           Czechia   
36                            NaN                            Greece   
37                       Shanghai                             China   
38                            NaN                            Israel   
39                            NaN                            Brazil   
40                            NaN                           Finland   
41                          Hebei                             China   
42                         Fujian                             China   
43                            NaN                          Slovenia   
44                     New Jersey                                US   
45                            NaN                         Singapore   
46                        Guangxi                             China   
47                        Shaanxi                             China   
48                            NaN                            Poland   
49                            NaN                          Pakistan   
50                            NaN                           Bahrain   
51                            NaN                           Estonia   
52                            NaN                           Ireland   
53                            NaN                           Iceland   
54                  Massachusetts                                US   
55                        Florida                                US   
56                New South Wales                         Australia   
57                            NaN                             Chile   
58                            NaN                             Egypt   
59                      Louisiana                                US   
60                            NaN                       Philippines   
61                        Ontario                            Canada   
62                            NaN                           Romania   
63                            NaN                          Thailand   
64                         Yunnan                             China   
65                            NaN                         Indonesia   
66                            NaN                      Saudi Arabia   
67                         Hainan                             China   
68                      Hong Kong                             China   
69                       Illinois                                US   
70                       Colorado                                US   
71                            NaN                              Iraq   
72                        Guizhou                             China   
73                        Georgia                                US   
74                            NaN                             India   
75                            NaN                        Luxembourg   
76                        Tianjin                             China   
77                          Gansu                             China   
78                         Shanxi                             China   
79                            NaN                            Kuwait   
80                       Liaoning                             China   
81                            NaN                           Lebanon   
82                            NaN                              Peru   
83                            NaN                            Russia   
84                   Pennsylvania                                US   
85                          Texas                                US   
86                            NaN                        San Marino   
87               British Columbia                            Canada   
88                            NaN              United Arab Emirates   
89                       Victoria                         Australia   
90                          Jilin                             China   
91                            NaN                            Mexico   
92                            NaN                           Armenia   
93                     Queensland                         Australia   
94                            NaN                           Taiwan*   
95                       Xinjiang                             China   
96                 Inner Mongolia                             China   
97                        Ningxia                             China   
98                        Alberta                            Canada   
99                         Quebec                            Canada   
100                     Tennessee                                US   
101                           NaN                          Slovakia   
102                     Wisconsin                                US   
103                           NaN                            Panama   
104                           NaN                         Argentina   
105                   Connecticut                                US   
106                           NaN                          Bulgaria   
107                          Ohio                                US   
108                      Virginia                                US   
109                        Oregon                                US   
110                           NaN                           Vietnam   
111                           NaN                          Colombia   
112                           NaN                           Croatia   
113                           NaN                            Serbia   
114                      Michigan                                US   
115                North Carolina                                US   
116                           NaN                      South Africa   
117                           NaN                           Algeria   
118                      Maryland                                US   
119                     Minnesota                                US   
120                           NaN                           Ecuador   
121                           NaN                            Brunei   
122                        Nevada                                US   
123                           NaN                           Albania   
124                          Utah                                US   
125                           NaN                           Hungary   
126                           NaN                            Latvia   
127                 Faroe Islands                           Denmark   
128                           NaN                            Turkey   
129              Diamond Princess                                US   
130                South Carolina                                US   
131                           NaN                            Cyprus   
132                           NaN                         Sri Lanka   
133                           NaN                        Costa Rica   
134                           NaN                           Andorra   
135                       Alabama                                US   
136                           NaN                             Malta   
137                           NaN                           Morocco   
138                           NaN                           Belarus   
139                           NaN                           Georgia   
140                           NaN                            Jordan   
141                           NaN                          Cambodia   
142                           NaN                        Kazakhstan   
143                           NaN                         Venezuela   
144                         Maine                                US   
145             Western Australia                         Australia   
146                           NaN                           Moldova   
147                       Indiana                                US   
148               South Australia                         Australia   
149                           NaN                           Uruguay   
150                           NaN                        Azerbaijan   
151                           NaN            Bosnia and Herzegovina   
152                           NaN                   North Macedonia   
153                           NaN                           Senegal   
154                      Kentucky                                US   
155                 New Hampshire                                US   
156                           NaN                         Lithuania   
157                           NaN                              Oman   
158                           NaN                           Tunisia   
159                          Iowa                                US   
160                    New Mexico                                US   
161                  Rhode Island                                US   
162                           NaN                       Afghanistan   
163                      Arkansas                                US   
164          District of Columbia                                US   
165                           NaN                Dominican Republic   
166                Grand Princess                                US   
167                   Mississippi                                US   
168                      Nebraska                                US   
169                       Arizona                                US   
170                      Oklahoma                                US   
171                       Qinghai                             China   
172                           NaN                        Guadeloupe   
173                        Kansas                                US   
174                           NaN                        Martinique   
175                      Delaware                                US   
176                           NaN                      Burkina Faso   
177                           NaN                           Ukraine   
178                           NaN                          Maldives   
179                         Macau                             China   
180                           NaN                           Jamaica   
181                           NaN                       New Zealand   
182                       Vermont                                US   
183                           NaN                           Bolivia   
184                           NaN                     French Guiana   
185                      Missouri                                US   
186                  South Dakota                                US   
187                       Wyoming                                US   
188                           NaN                        Bangladesh   
189                           NaN                          Cameroon   
190                        Hawaii                                US   
191                           NaN                        Uzbekistan   
192                       Reunion                            France   
193                           NaN                          Paraguay   
194                           NaN                           Reunion   
195                       Montana                                US   
196                Grand Princess                            Canada   
197                      Manitoba                            Canada   
198                 New Brunswick                            Canada   
199                           NaN                          Honduras   
200                         Idaho                                US   
201                      Tasmania                         Australia   
202                   Nova Scotia                            Canada   
203                  Saskatchewan                            Canada   
204                 French Guiana                            France   
205                           NaN                             Ghana   
206                           NaN                            Guyana   
207                           NaN                     Liechtenstein   
208                           NaN                            Monaco   
209                           NaN                            Rwanda   
210                    Guadeloupe                            France   
211                           NaN                         Guatemala   
212               Channel Islands                    United Kingdom   
213                           NaN                     Cote d'Ivoire   
214                           NaN                              Cuba   
215                           NaN                          Ethiopia   
216                           NaN                          Mongolia   
217                           NaN               Trinidad and Tobago   
218                   Puerto Rico                                US   
219                           NaN                        Seychelles   
220                           NaN                             Aruba   
221     Newfoundland and Labrador                            Canada   
222                           NaN                  Congo (Kinshasa)   
223              French Polynesia                            France   
224              Saint Barthelemy                            France   
225                           NaN                              Guam   
226                           NaN                             Kenya   
227                       Curacao                       Netherlands   
228                           NaN                           Nigeria   
229                        Alaska                                US   
230                          Guam                                US   
231                  North Dakota                                US   
232                     Gibraltar                    United Kingdom   
233  Australian Capital Territory                         Australia   
234                           NaN                          Barbados   
235                     St Martin                            France   
236                           NaN                            Kosovo   
237                           NaN                        Montenegro   
238                           NaN                           Namibia   
239                           NaN                       Saint Lucia   
240                Virgin Islands                                US   
241                           NaN               Antigua and Barbuda   
242            Northern Territory                         Australia   
243                           NaN                             Benin   
244                           NaN                            Bhutan   
245          Prince Edward Island                            Canada   
246                           NaN          Central African Republic   
247                         Tibet                             China   
248                           NaN               Congo (Brazzaville)   
249                           NaN                 Equatorial Guinea   
250                           NaN                          Eswatini   
251                       Mayotte                            France   
252                           NaN                             Gabon   
253                           NaN                         Greenland   
254                           NaN                            Guinea   
255                           NaN                          Holy See   
256                           NaN                           Liberia   
257                           NaN                        Mauritania   
258                           NaN                           Mayotte   
259                           NaN                             Nepal   
260                           NaN  Saint Vincent and the Grenadines   
261                           NaN                           Somalia   
262                           NaN                             Sudan   
263                           NaN                          Suriname   
264                           NaN                          Tanzania   
265                           NaN                       The Bahamas   
266                           NaN                        The Gambia   
267                           NaN                              Togo   
268                 West Virginia                                US   
269                Cayman Islands                    United Kingdom   
270         From Diamond Princess                         Australia   
271                           NaN                          Guernsey   
272                           NaN                            Jersey   
273                           NaN                       Puerto Rico   
274                           NaN             Republic of the Congo   
275                           NaN    occupied Palestinian territory   

             Last Update  Confirmed  Deaths  Recovered  Latitude  Longitude  
0    2020-03-17T11:53:10      67799    3111      56003   30.9756   112.2707  
1    2020-03-17T18:33:02      31506    2503       2941   41.8719    12.5674  
2    2020-03-17T15:13:09      16169     988       5389   32.4279    53.6880  
3    2020-03-17T20:53:02      11748     533       1028   40.4637    -3.7492  
4    2020-03-17T18:53:02       9257      24         67   51.1657    10.4515  
5    2020-03-17T10:33:03       8320      81       1407   35.9078   127.7669  
6    2020-03-17T19:13:08       7652     148         12   46.2276     2.2137  
7    2020-03-17T16:33:04       2700      27          4   46.8182     8.2275  
8    2020-03-17T15:13:09       1950      55         52   55.3781    -3.4360  
9    2020-03-17T22:53:03       1706      13          0   42.1657   -74.9481  
10   2020-03-17T15:13:11       1705      43          2   52.1326     5.2913  
11   2020-03-17T19:53:02       1463       3          1   60.4720     8.4689  
12   2020-03-17T01:53:03       1364       8       1307   23.3417   113.4244  
13   2020-03-17T15:33:06       1332       3          1   47.5162    14.5501  
14   2020-03-14T09:53:08       1273      22       1250   33.8820   113.6140  
15   2020-03-17T15:33:06       1243      10          1   50.5039     4.4699  
16   2020-03-17T02:13:21       1232       1       1216   29.1832   120.0934  
17   2020-03-17T15:33:06       1190       7          1   60.1282    18.6435  
18   2020-03-17T23:33:03       1076      55          1   47.4009  -121.4905  
19   2020-03-14T08:33:03       1018       4       1014   27.6104   111.7088  
20   2020-03-11T02:18:14        990       6        984   31.8257   117.2264  
21   2020-03-17T16:33:04        977       4          1   56.2639     9.5018  
22   2020-03-12T02:13:04        935       1        934   27.6140   115.7221  
23   2020-03-17T16:53:04        878      29        144   36.2048   138.2529  
24   2020-03-17T00:33:02        761       7        746   36.3427   118.1498  
25   2020-03-17T22:53:03        698      12          6   36.1162  -119.6816  
26   2020-03-13T14:13:25        696       7        325   35.4498   139.6649  
27   2020-03-17T15:33:06        673       2         49    4.2105   101.9758  
28   2020-03-15T01:53:02        631       0        631   32.9711   119.4550  
29   2020-03-15T03:53:04        576       6        570   30.0572   107.8740  
30   2020-03-17T08:33:02        540       3        520   30.6171   102.7103  
31   2020-03-17T01:33:02        482      13        456   47.8620   127.7615  
32   2020-03-17T10:53:03        456       8        369   40.1824   116.4142  
33   2020-03-17T15:33:06        448       1          3   39.3999    -8.2245  
34   2020-03-16T15:13:09        439       0          4   25.3548    51.1839  
35   2020-03-17T15:33:06        396       0          3   49.8175    15.4730  
36   2020-03-17T16:33:04        387       5          8   39.0742    21.8243  
37   2020-03-17T02:13:20        358       3        325   31.2020   121.4491  
38   2020-03-17T20:53:02        337       0         11   31.0461    34.8516  
39   2020-03-17T15:33:06        321       1          2  -14.2350   -51.9253  
40   2020-03-17T12:33:06        321       0         10   61.9241    25.7482  
41   2020-03-13T11:09:03        318       6        310   38.0428   114.5149  
42   2020-03-11T02:18:14        296       1        295   26.0789   117.9874  
43   2020-03-17T16:53:04        275       1          0   46.1512    14.9955  
44   2020-03-17T20:13:22        267       3          1   40.2989   -74.5210  
45   2020-03-17T15:33:06        266       0        114    1.3521   103.8198  
46   2020-03-17T00:33:02        253       2        248   23.8298   108.7881  
47   2020-03-17T10:53:03        246       3        236   35.1917   108.8701  
48   2020-03-17T20:53:02        238       5         13   51.9194    19.1451  
49   2020-03-17T15:33:06        236       0          2   30.3753    69.3451  
50   2020-03-17T03:13:15        228       1         81   26.0667    50.5577  
51   2020-03-17T10:33:03        225       0          1   58.5953    25.0136  
52   2020-03-17T02:53:03        223       2          5   53.1424    -7.6921  
53   2020-03-17T15:33:06        220       1          0   64.9631   -19.0208  
54   2020-03-17T22:53:02        218       0          1   42.2302   -71.5301  
55   2020-03-17T23:33:02        216       6          0   27.7663   -81.6868  
56   2020-03-17T12:33:07        210       4          4  -33.8688   151.2093  
57   2020-03-17T15:33:06        201       0          0  -35.6751   -71.5430  
58   2020-03-17T18:13:10        196       4         32   26.8206    30.8025  
59   2020-03-17T22:53:03        196       4          0   31.1695   -91.8678  
60   2020-03-17T10:33:03        187      12          5   12.8797   121.7740  
61   2020-03-17T16:53:04        185       1          5   51.2538   -85.3232  
62   2020-03-17T10:33:03        184       0         16   45.9432    24.9668  
63   2020-03-17T10:33:03        177       1         41   15.8700   100.9925  
64   2020-03-16T23:53:02        176       2        172   24.9740   101.4870  
65   2020-03-17T10:33:03        172       5          8   -0.7893   113.9213  
66   2020-03-17T17:53:03        171       0          6   23.8859    45.0792  
67   2020-03-16T14:38:45        168       6        161   19.1959   109.7453  
68   2020-03-17T10:13:11        162       4         88   22.3000   114.2000  
69   2020-03-17T22:53:03        161       1          2   40.3495   -88.9861  
70   2020-03-17T22:53:03        160       2          0   39.0598  -105.3111  
71   2020-03-17T15:33:06        154      11         32   33.2232    43.6793  
72   2020-03-17T07:33:03        147       2        144   26.8154   106.8748  
73   2020-03-17T20:13:22        146       1          0   33.0406   -83.6431  
74   2020-03-17T15:33:06        142       3         14   20.5937    78.9629  
75   2020-03-17T15:33:06        140       1          0   49.8153     6.1296  
76   2020-03-15T18:20:18        136       3        133   39.3054   117.3230  
77   2020-03-15T18:20:18        133       2         91   36.0611   103.8343  
78   2020-03-13T11:09:03        133       0        133   37.5777   112.2922  
79   2020-03-17T10:53:03        130       0          9   29.3117    47.4818  
80   2020-03-17T12:13:13        125       1        120   41.2956   122.6085  
81   2020-03-17T10:53:03        120       3          3   33.8547    35.8623  
82   2020-03-17T15:53:12        117       0          1   -9.1900   -75.0152  
83   2020-03-17T15:53:12        114       0          8   61.5240   105.3188  
84   2020-03-17T23:13:10        112       0          0   40.5908   -77.2098  
85   2020-03-17T20:13:22        110       1          0   31.0545   -97.5635  
86   2020-03-16T01:33:03        109       7          4   43.9424    12.4578  
87   2020-03-16T19:13:13        103       4          4   53.7267  -127.6476  
88   2020-03-16T00:22:11         98       0         23   23.4241    53.8478  
89   2020-03-17T12:53:09         94       0          8  -37.8136   144.9631  
90   2020-03-16T00:22:10         93       1         92   43.6661   126.1923  
91   2020-03-17T10:53:03         82       0          4   23.6345  -102.5528  
92   2020-03-17T19:33:02         78       0          1   40.0691    45.0382  
93   2020-03-17T12:33:07         78       0          8  -28.0167   153.4000  
94   2020-03-17T08:13:11         77       1         22   23.7000   121.0000  
95   2020-03-11T02:18:14         76       3         73   41.1129    85.2401  
96   2020-03-16T14:38:45         75       1         73   44.0935   113.9448  
97   2020-03-16T14:38:45         75       0         75   37.2692   106.1655  
98   2020-03-17T03:13:18         74       0          0   53.9333  -116.5765  
99   2020-03-17T19:33:03         74       0          0   52.9399   -73.5491  
100  2020-03-17T23:13:10         74       0          0   35.7478   -86.6923  
101  2020-03-17T02:13:34         72       0          0   48.6690    19.6990  
102  2020-03-17T20:13:22         72       0          1   44.2685   -89.6165  
103  2020-03-17T10:53:03         69       1          0    8.5380   -80.7821  
104  2020-03-17T15:53:12         68       2          3  -38.4161   -63.6167  
105  2020-03-17T23:13:10         68       0          0   41.5978   -72.7554  
106  2020-03-17T10:53:03         67       2          0   42.7339    25.4858  
107  2020-03-17T20:53:02         67       0          0   40.3888   -82.7649  
108  2020-03-17T20:13:22         67       2          0   37.7693   -78.1700  
109  2020-03-17T23:13:10         66       1          0   44.5720  -122.0709  
110  2020-03-17T15:53:12         66       0         16   14.0583   108.2772  
111  2020-03-17T15:53:12         65       0          1    4.5709   -74.2973  
112  2020-03-17T10:53:03         65       0          4   45.1000    15.2000  
113  2020-03-17T11:13:18         65       0          1   44.0165    21.0059  
114  2020-03-17T20:53:02         65       0          0   43.3266   -84.5361  
115  2020-03-17T23:13:10         64       0          0   35.6301   -79.8064  
116  2020-03-16T14:38:45         62       0          0  -30.5595    22.9375  
117  2020-03-17T03:13:15         60       4         12   28.0339     1.6596  
118  2020-03-17T16:13:14         60       0          3   39.0639   -76.8021  
119  2020-03-17T17:53:03         60       0          0   45.6945   -93.9002  
120  2020-03-17T03:13:15         58       2          0   -1.8312   -78.1834  
121  2020-03-17T15:53:12         56       0          0    4.5353   114.7277  
122  2020-03-17T23:33:02         56       1          0   38.3135  -117.0554  
123  2020-03-17T15:53:12         55       1          0   41.1533    20.1683  
124  2020-03-17T20:53:02         51       0          0   40.1500  -111.8624  
125  2020-03-17T11:13:29         50       1          2   47.1625    19.5033  
126  2020-03-17T11:13:29         49       0          1   56.8796    24.6032  
127  2020-03-17T10:13:13         47       0          0   61.8926    -6.9118  
128  2020-03-17T22:13:16         47       1          0   38.9637    35.2433  
129  2020-03-16T16:53:06         47       0          0   35.4437   139.6380  
130  2020-03-17T23:13:10         47       1          0   33.8569   -80.9450  
131  2020-03-17T03:13:15         46       0          0   35.1264    33.4299  
132  2020-03-17T15:53:12         44       0          1    7.8731    80.7718  
133  2020-03-17T03:13:15         41       0          0    9.7489   -83.7534  
134  2020-03-17T20:53:02         39       0          1   42.5063     1.5218  
135  2020-03-17T23:13:10         39       0          0   32.3182   -86.9023  
136  2020-03-17T15:53:12         38       0          2   35.9375    14.3754  
137  2020-03-17T15:53:12         38       2          1   31.7917    -7.0926  
138  2020-03-16T14:38:45         36       0          3   53.7098    27.9534  
139  2020-03-17T11:13:29         34       0          1   42.3154    43.3569  
140  2020-03-17T11:13:29         34       0          1   30.5852    36.2384  
141  2020-03-17T15:53:13         33       0          1   12.5657   104.9910  
142  2020-03-17T15:53:12         33       0          0   48.0196    66.9237  
143  2020-03-17T11:33:05         33       0          0    6.4238   -66.5897  
144  2020-03-17T17:53:03         32       0          0   44.6939   -69.3819  
145  2020-03-17T12:53:09         31       1          0  -31.9505   115.8605  
146  2020-03-17T15:53:12         30       0          1   47.4116    28.3699  
147  2020-03-17T23:13:10         30       2          0   39.8494   -86.2583  
148  2020-03-16T14:38:46         29       0          3  -34.9285   138.6007  
149  2020-03-17T02:13:54         29       0          0  -32.5228   -55.7658  
150  2020-03-17T11:53:10         28       1          6   40.1431    47.5769  
151  2020-03-17T15:53:12         26       0          2   43.9159    17.6791  
152  2020-03-17T11:53:10         26       0          1   41.6086    21.7453  
153  2020-03-17T12:33:06         26       0          2   14.4974   -14.4524  
154  2020-03-17T23:33:02         26       1          1   37.6681   -84.6701  
155  2020-03-17T23:13:10         26       0          0   43.4525   -71.5639  
156  2020-03-17T18:53:02         25       0          1   55.1694    23.8813  
157  2020-03-17T11:53:10         24       0          9   21.4735    55.9754  
158  2020-03-17T11:53:10         24       0          0   33.8869     9.5375  
159  2020-03-16T23:53:03         23       0          0   42.0115   -93.2105  
160  2020-03-17T23:13:10         23       0          0   34.8405  -106.2485  
161  2020-03-17T20:53:02         23       0          0   41.6809   -71.5118  
162  2020-03-17T11:53:10         22       0          1   33.9391    67.7100  
163  2020-03-16T17:13:23         22       0          0   34.9697   -92.3731  
164  2020-03-16T23:53:03         22       0          0   38.8974   -77.0268  
165  2020-03-17T08:13:22         21       1          0   18.7357   -70.1627  
166  2020-03-17T20:53:02         21       0          0   37.6489  -122.6655  
167  2020-03-17T17:53:03         21       0          0   32.7416   -89.6787  
168  2020-03-17T17:53:03         21       0          0   41.1254   -98.2681  
169  2020-03-17T23:13:10         20       0          1   33.7298  -111.4312  
170  2020-03-17T17:53:03         19       0          0   35.5653   -96.9289  
171  2020-03-11T02:18:14         18       0         18   35.7452    95.9956  
172  2020-03-17T10:53:03         18       0          0   16.2650   -61.5510  
173  2020-03-17T23:13:10         18       1          0   38.5266   -96.7265  
174  2020-03-17T10:53:03         16       1          0   14.6415   -61.0242  
175  2020-03-17T23:33:02         16       0          0   39.3185   -75.5071  
176  2020-03-16T14:38:45         15       0          0   12.2383    -1.5616  
177  2020-03-17T19:33:02         14       2          0   48.3794    31.1656  
178  2020-03-15T18:20:18         13       0          0    3.2028    73.2207  
179  2020-03-17T04:32:18         12       0         10   22.1667   113.5500  
180  2020-03-17T12:13:16         12       0          2   18.1096   -77.2975  
181  2020-03-17T11:53:10         12       0          0  -40.9006   174.8860  
182  2020-03-16T17:13:23         12       0          0   44.0459   -72.7107  
183  2020-03-16T14:38:45         11       0          0  -16.2902   -63.5887  
184  2020-03-16T14:38:46         11       0          0    3.9339   -53.1258  
185  2020-03-17T23:33:02         11       0          0   38.4561   -92.2884  
186  2020-03-17T23:33:02         11       1          0   44.2998   -99.4388  
187  2020-03-17T23:53:03         11       0          0   42.7560  -107.3025  
188  2020-03-17T12:13:16         10       0          3   23.6850    90.3563  
189  2020-03-17T15:53:13         10       0          0    3.8480    11.5021  
190  2020-03-17T17:33:03         10       0          0   21.0943  -157.4983  
191  2020-03-17T12:13:16         10       0          0   41.3775    64.5853  
192  2020-03-17T11:13:29          9       0          0  -21.1351    55.2471  
193  2020-03-17T12:13:16          9       0          0  -23.4425   -58.4438  
194  2020-03-17T07:15:25          9       0          0  -21.1151    55.5364  
195  2020-03-17T17:33:03          9       0          0   46.9219  -110.4544  
196  2020-03-17T03:13:18          8       0          0   37.6489  -122.6655  
197  2020-03-17T19:33:03          8       0          0   53.7609   -98.8139  
198  2020-03-17T19:33:03          8       0          0   46.5653   -66.4619  
199  2020-03-17T12:13:16          8       0          0   15.2000   -86.2419  
200  2020-03-17T23:33:02          8       0          0   44.2405  -114.4788  
201  2020-03-16T14:38:46          7       0          0  -41.4545   145.9707  
202  2020-03-17T19:33:03          7       0          0   44.6820   -63.7443  
203  2020-03-16T20:13:20          7       0          0   52.9399  -106.4509  
204  2020-03-17T07:33:03          7       0          0    4.0000   -53.0000  
205  2020-03-17T19:33:02          7       0          0    7.9465    -1.0232  
206  2020-03-17T10:53:03          7       1          0    4.8604   -58.9302  
207  2020-03-17T12:13:16          7       0          0   47.1660     9.5554  
208  2020-03-16T14:38:45          7       0          0   43.7384     7.4246  
209  2020-03-17T02:33:10          7       0          0   -1.9403    29.8739  
210  2020-03-17T07:33:03          6       0          0   16.2500   -61.5833  
211  2020-03-17T12:13:16          6       1          0   15.7835   -90.2308  
212  2020-03-16T14:38:45          6       0          0   49.3723    -2.3644  
213  2020-03-17T14:33:05          5       0          1    7.5400    -5.5471  
214  2020-03-17T15:53:13          5       0          0   21.5218   -77.7812  
215  2020-03-16T14:38:45          5       0          0    9.1450    40.4897  
216  2020-03-17T15:53:13          5       0          0   46.8625   103.8467  
217  2020-03-17T15:53:13          5       0          0   10.6918   -61.2225  
218  2020-03-16T00:22:11          5       0          0   18.2208   -66.5901  
219  2020-03-17T12:33:06          4       0          0   -4.6796    55.4920  
220  2020-03-17T12:33:07          3       0          0   12.5211   -69.9683  
221  2020-03-17T17:53:03          3       0          0   53.1355   -57.6604  
222  2020-03-17T12:33:06          3       0          0   -4.0383    21.7587  
223  2020-03-15T18:20:19          3       0          0  -17.6797  -149.4068  
224  2020-03-16T14:38:45          3       0          0   17.9000   -62.8333  
225  2020-03-16T02:13:16          3       0          0   13.4443   144.7937  
226  2020-03-16T00:22:11          3       0          0   -0.0236    37.9062  
227  2020-03-17T12:33:07          3       0          0   12.1696   -68.9900  
228  2020-03-17T12:33:06          3       0          0    9.0820     8.6753  
229  2020-03-17T17:33:03          3       0          0   61.3707  -152.4044  
230  2020-03-15T18:20:19          3       0          0   13.4443   144.7937  
231  2020-03-17T23:33:02          3       0          0   47.5289   -99.7840  
232  2020-03-17T02:53:03          3       0          1   36.1408    -5.3536  
233  2020-03-16T14:38:46          2       0          0  -35.4735   149.0124  
234  2020-03-17T16:13:14          2       0          0   13.1939   -59.5432  
235  2020-03-14T16:33:03          2       0          0   18.0708   -63.0501  
236  2020-03-15T18:20:19          2       0          0   42.6026    20.9030  
237  2020-03-17T21:33:02          2       0          0   42.5000    19.3000  
238  2020-03-14T16:33:03          2       0          0  -22.9576    18.4904  
239  2020-03-17T04:32:19          2       0          0   13.9094   -60.9789  
240  2020-03-17T20:53:02          2       0          0   18.3358   -64.8963  
241  2020-03-15T18:20:19          1       0          0   17.0608   -61.7964  
242  2020-03-14T01:53:03          1       0          0  -12.4634   130.8456  
243  2020-03-16T14:38:46          1       0          0    9.3077     2.3158  
244  2020-03-13T22:22:02          1       0          0   27.5142    90.4336  
245  2020-03-15T02:13:21          1       0          0   46.5107   -63.4168  
246  2020-03-16T03:33:03          1       0          0    6.6111    20.9394  
247  2020-03-11T02:18:14          1       0          1   31.6927    88.0924  
248  2020-03-16T14:38:45          1       0          0   -0.2280    15.8277  
249  2020-03-15T06:41:54          1       0          0    1.5000    10.0000  
250  2020-03-15T06:41:54          1       0          0  -26.5225    31.4659  
251  2020-03-16T14:38:45          1       0          0  -12.8431    45.1383  
252  2020-03-14T13:33:04          1       0          0   -0.8037    11.6094  
253  2020-03-16T16:53:06          1       0          0   71.7069   -42.6043  
254  2020-03-15T06:41:54          1       0          0    9.9456    -9.6966  
255  2020-03-13T22:22:02          1       0          0   41.9029    12.4534  
256  2020-03-17T12:13:16          1       0          0    6.4281    -9.4295  
257  2020-03-15T18:20:19          1       0          0   21.0079   -10.9408  
258  2020-03-16T14:38:45          1       0          0  -12.8275    45.1662  
259  2020-03-13T22:22:03          1       0          1   28.3949    84.1240  
260  2020-03-14T16:33:03          1       0          0   12.9843   -61.2872  
261  2020-03-16T14:38:46          1       0          0    5.1521    46.1996  
262  2020-03-14T01:13:32          1       1          0   12.8628    30.2176  
263  2020-03-14T16:33:03          1       0          0    3.9193   -56.0278  
264  2020-03-17T01:33:03          1       0          0   -6.3690    34.8888  
265  2020-03-16T03:33:03          1       0          0   24.2500   -76.0000  
266  2020-03-17T23:33:02          1       0          0   13.4667   -16.6000  
267  2020-03-13T22:22:02          1       0          0    8.6195     0.8248  
268  2020-03-17T23:33:02          1       0          0   38.4912   -80.9545  
269  2020-03-16T14:53:04          1       1          0   19.3133   -81.2546  
270  2020-03-14T02:33:04          0       0          0   35.4437   139.6380  
271  2020-03-17T18:33:03          0       0          0   49.4500    -2.5800  
272  2020-03-17T18:33:03          0       0          0   49.1900    -2.1100  
273  2020-03-17T16:13:14          0       0          0   18.2000   -66.5000  
274  2020-03-17T21:33:03          0       0          0   -1.4400    15.5560  
275  2020-03-11T20:53:02          0       0          0   31.9522    35.2332  

Dataset information:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 276 entries, 0 to 275
Data columns (total 8 columns):
 #   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   Province/State  126 non-null    object 
 1   Country/Region  276 non-null    object 
 2   Last Update     276 non-null    object 
 3   Confirmed       276 non-null    int64  
 4   Deaths          276 non-null    int64  
 5   Recovered       276 non-null    int64  
 6   Latitude        276 non-null    float64
 7   Longitude       276 non-null    float64
dtypes: float64(2), int64(3), object(3)
memory usage: 14.1+ KB
None

Missing data information:
Province/State    150
Country/Region      0
Last Update         0
Confirmed           0
Deaths              0
Recovered           0
Latitude            0
Longitude           0
dtype: int64

---------------------------------------------------------------------------------------------------
To Get the latest number of confirmed, deaths, recovered and active cases of Novel Coronavirus Country wise
C:\Users\sachin\Anaconda3\lib\site-packages\ipykernel_launcher.py:15: FutureWarning: Indexing with multiple keys (implicitly converted to a tuple of keys) will be deprecated, use a list instead.
  from ipykernel import kernelapp as app
                       Country/Region  Confirmed  Deaths  Recovered  Active
0                         Afghanistan         22       0          1      21
1                             Albania         55       1          0      54
2                             Algeria         60       4         12      44
3                             Andorra         39       0          1      38
4                 Antigua and Barbuda          1       0          0       1
5                           Argentina         68       2          3      63
6                             Armenia         78       0          1      77
7                               Aruba          3       0          0       3
8                           Australia        452       5         23     424
9                             Austria       1332       3          1    1328
10                         Azerbaijan         28       1          6      21
11                            Bahrain        228       1         81     146
12                         Bangladesh         10       0          3       7
13                           Barbados          2       0          0       2
14                            Belarus         36       0          3      33
15                            Belgium       1243      10          1    1232
16                              Benin          1       0          0       1
17                             Bhutan          1       0          0       1
18                            Bolivia         11       0          0      11
19             Bosnia and Herzegovina         26       0          2      24
20                             Brazil        321       1          2     318
21                             Brunei         56       0          0      56
22                           Bulgaria         67       2          0      65
23                       Burkina Faso         15       0          0      15
24                           Cambodia         33       0          1      32
25                           Cameroon         10       0          0      10
26                             Canada        478       5          9     464
27           Central African Republic          1       0          0       1
28                              Chile        201       0          0     201
29                              China      81058    3230      68798    9030
30                           Colombia         65       0          1      64
31                Congo (Brazzaville)          1       0          0       1
32                   Congo (Kinshasa)          3       0          0       3
33                         Costa Rica         41       0          0      41
34                      Cote d'Ivoire          5       0          1       4
35                            Croatia         65       0          4      61
36                        Cruise Ship        696       7        325     364
37                               Cuba          5       0          0       5
38                             Cyprus         46       0          0      46
39                            Czechia        396       0          3     393
40                            Denmark       1024       4          1    1019
41                 Dominican Republic         21       1          0      20
42                            Ecuador         58       2          0      56
43                              Egypt        196       4         32     160
44                  Equatorial Guinea          1       0          0       1
45                            Estonia        225       0          1     224
46                           Eswatini          1       0          0       1
47                           Ethiopia          5       0          0       5
48                            Finland        321       0         10     311
49                             France       7683     148         12    7523
50                      French Guiana         11       0          0      11
51                              Gabon          1       0          0       1
52                            Georgia         34       0          1      33
53                            Germany       9257      24         67    9166
54                              Ghana          7       0          0       7
55                             Greece        387       5          8     374
56                          Greenland          1       0          0       1
57                         Guadeloupe         18       0          0      18
58                               Guam          3       0          0       3
59                          Guatemala          6       1          0       5
60                           Guernsey          0       0          0       0
61                             Guinea          1       0          0       1
62                             Guyana          7       1          0       6
63                           Holy See          1       0          0       1
64                           Honduras          8       0          0       8
65                            Hungary         50       1          2      47
66                            Iceland        220       1          0     219
67                              India        142       3         14     125
68                          Indonesia        172       5          8     159
69                               Iran      16169     988       5389    9792
70                               Iraq        154      11         32     111
71                            Ireland        223       2          5     216
72                             Israel        337       0         11     326
73                              Italy      31506    2503       2941   26062
74                            Jamaica         12       0          2      10
75                              Japan        878      29        144     705
76                             Jersey          0       0          0       0
77                             Jordan         34       0          1      33
78                         Kazakhstan         33       0          0      33
79                              Kenya          3       0          0       3
80                       Korea, South       8320      81       1407    6832
81                             Kosovo          2       0          0       2
82                             Kuwait        130       0          9     121
83                             Latvia         49       0          1      48
84                            Lebanon        120       3          3     114
85                            Liberia          1       0          0       1
86                      Liechtenstein          7       0          0       7
87                          Lithuania         25       0          1      24
88                         Luxembourg        140       1          0     139
89                           Malaysia        673       2         49     622
90                           Maldives         13       0          0      13
91                              Malta         38       0          2      36
92                         Martinique         16       1          0      15
93                         Mauritania          1       0          0       1
94                            Mayotte          1       0          0       1
95                             Mexico         82       0          4      78
96                            Moldova         30       0          1      29
97                             Monaco          7       0          0       7
98                           Mongolia          5       0          0       5
99                         Montenegro          2       0          0       2
100                           Morocco         38       2          1      35
101                           Namibia          2       0          0       2
102                             Nepal          1       0          1       0
103                       Netherlands       1708      43          2    1663
104                       New Zealand         12       0          0      12
105                           Nigeria          3       0          0       3
106                   North Macedonia         26       0          1      25
107                            Norway       1463       3          1    1459
108                              Oman         24       0          9      15
109                          Pakistan        236       0          2     234
110                            Panama         69       1          0      68
111                          Paraguay          9       0          0       9
112                              Peru        117       0          1     116
113                       Philippines        187      12          5     170
114                            Poland        238       5         13     220
115                          Portugal        448       1          3     444
116                       Puerto Rico          0       0          0       0
117                             Qatar        439       0          4     435
118             Republic of the Congo          0       0          0       0
119                           Reunion          9       0          0       9
120                           Romania        184       0         16     168
121                            Russia        114       0          8     106
122                            Rwanda          7       0          0       7
123                       Saint Lucia          2       0          0       2
124  Saint Vincent and the Grenadines          1       0          0       1
125                        San Marino        109       7          4      98
126                      Saudi Arabia        171       0          6     165
127                           Senegal         26       0          2      24
128                            Serbia         65       0          1      64
129                        Seychelles          4       0          0       4
130                         Singapore        266       0        114     152
131                          Slovakia         72       0          0      72
132                          Slovenia        275       1          0     274
133                           Somalia          1       0          0       1
134                      South Africa         62       0          0      62
135                             Spain      11748     533       1028   10187
136                         Sri Lanka         44       0          1      43
137                             Sudan          1       1          0       0
138                          Suriname          1       0          0       1
139                            Sweden       1190       7          1    1182
140                       Switzerland       2700      27          4    2669
141                           Taiwan*         77       1         22      54
142                          Tanzania          1       0          0       1
143                          Thailand        177       1         41     135
144                       The Bahamas          1       0          0       1
145                        The Gambia          1       0          0       1
146                              Togo          1       0          0       1
147               Trinidad and Tobago          5       0          0       5
148                           Tunisia         24       0          0      24
149                            Turkey         47       1          0      46
150                                US       6421     108         17    6296
151                           Ukraine         14       2          0      12
152              United Arab Emirates         98       0         23      75
153                    United Kingdom       1960      56         53    1851
154                           Uruguay         29       0          0      29
155                        Uzbekistan         10       0          0      10
156                         Venezuela         33       0          0      33
157                           Vietnam         66       0         16      50
158    occupied Palestinian territory          0       0          0       0

-------------------------------------------------------------------------------------------------------
To Get Latest number of confirmed deaths and recovered people of Novel Coronavirus cases Country wise
C:\Users\sachin\Anaconda3\lib\site-packages\ipykernel_launcher.py:22: FutureWarning: Indexing with multiple keys (implicitly converted to a tuple of keys) will be deprecated, use a list instead.
                                             Confirmed  Deaths  Recovered
Country/Region Province/State                                            
Australia      Australian Capital Territory          2       0          0
               From Diamond Princess                 0       0          0
               New South Wales                     171       2          4
               Northern Territory                    1       0          0
               Queensland                           68       0          8
               South Australia                      29       0          3
               Tasmania                              7       0          0
               Victoria                             71       0          8
               Western Australia                    28       1          0
Canada         Alberta                              56       0          0
               British Columbia                    103       4          4
               Grand Princess                        2       0          0
               Manitoba                              7       0          0
               New Brunswick                         6       0          0
               Newfoundland and Labrador             1       0          0
               Nova Scotia                           5       0          0
               Ontario                             177       0          5
               Prince Edward Island                  1       0          0
               Quebec                               50       0          0
               Saskatchewan                          7       0          0
China          Anhui                               990       6        984
               Beijing                             452       8        360
               Chongqing                           576       6        570
               Fujian                              296       1        295
               Gansu                               133       2         91
               Guangdong                          1361       8       1306
               Guangxi                             252       2        248
               Guizhou                             146       2        144
               Hainan                              168       6        161
               Hebei                               318       6        310
               Heilongjiang                        482      13        455
               Henan                              1273      22       1250
               Hong Kong                           155       4         84
               Hubei                             67798    3099      55142
               Hunan                              1018       4       1014
               Inner Mongolia                       75       1         73
               Jiangsu                             631       0        631
               Jiangxi                             935       1        934
               Jilin                                93       1         92
               Liaoning                            125       1        115
               Macau                                11       0         10
               Ningxia                              75       0         75
               Qinghai                              18       0         18
               Shaanxi                             245       2        233
               Shandong                            760       7        746
               Shanghai                            355       3        325
               Shanxi                              133       0        133
               Sichuan                             539       3        516
               Tianjin                             136       3        133
               Tibet                                 1       0          1
               Xinjiang                             76       3         73
               Yunnan                              176       2        172
               Zhejiang                           1231       1       1216
Cruise Ship    Diamond Princess                    696       7        325
Denmark        Denmark                             914       3          1
               Faroe Islands                        18       0          0
France         France                             6633     148         12
               French Guiana                         5       0          0
               French Polynesia                      3       0          0
               Guadeloupe                            3       0          0
               Mayotte                               1       0          0
               Saint Barthelemy                      3       0          0
               St Martin                             2       0          0
Netherlands    Curacao                               1       0          0
               Netherlands                        1413      24          2
US             Alabama                              29       0          0
               Alaska                                1       0          0
               Arizona                              18       0          1
               Arkansas                             22       0          0
               California                          557       7          6
               Colorado                            160       1          0
               Connecticut                          30       0          0
               Delaware                              8       0          0
               Diamond Princess                     47       0          0
               District of Columbia                 22       0          0
               Florida                             155       5          0
               Georgia                             121       1          0
               Grand Princess                       20       0          0
               Guam                                  3       0          0
               Hawaii                                7       0          0
               Idaho                                 5       0          0
               Illinois                            105       0          2
               Indiana                              25       1          0
               Iowa                                 23       0          0
               Kansas                               11       1          0
               Kentucky                             21       1          1
               Louisiana                           136       3          0
               Maine                                17       0          0
               Maryland                             41       0          3
               Massachusetts                       197       0          1
               Michigan                             53       0          0
               Minnesota                            54       0          0
               Mississippi                          13       0          0
               Missouri                              6       0          0
               Montana                               7       0          0
               Nebraska                             18       0          0
               Nevada                               45       1          0
               New Hampshire                        17       0          0
               New Jersey                          178       2          1
               New Mexico                           17       0          0
               New York                            967      10          0
               North Carolina                       38       0          0
               North Dakota                          1       0          0
               Ohio                                 50       0          0
               Oklahoma                             10       0          0
               Oregon                               39       1          0
               Pennsylvania                         77       0          0
               Puerto Rico                           5       0          0
               Rhode Island                         21       0          0
               South Carolina                       33       1          0
               South Dakota                         10       1          0
               Tennessee                            52       0          0
               Texas                                85       0          0
               Utah                                 39       0          0
               Vermont                              12       0          0
               Virgin Islands                        1       0          0
               Virginia                             49       1          0
               Washington                          904      48          1
               West Virginia                         0       0          0
               Wisconsin                            47       0          1
               Wyoming                               3       0          0
United Kingdom Cayman Islands                        1       1          0
               Channel Islands                       6       0          0
               Gibraltar                             1       0          1
               United Kingdom                     1543      55         20

-------------------------------------------------------------------------------------------------------
To Get the Chinese province wise cases of confirmed, deaths and recovered cases of Novel Coronavirus
    Province/State  Confirmed  Deaths  Recovered
0            Hubei      67799    3111      56003
1        Guangdong       1364       8       1307
2            Henan       1273      22       1250
3         Zhejiang       1232       1       1216
4            Hunan       1018       4       1014
5            Anhui        990       6        984
6          Jiangxi        935       1        934
7         Shandong        761       7        746
8          Jiangsu        631       0        631
9        Chongqing        576       6        570
10         Sichuan        540       3        520
11    Heilongjiang        482      13        456
12         Beijing        456       8        369
13        Shanghai        358       3        325
14           Hebei        318       6        310
15          Fujian        296       1        295
16         Guangxi        253       2        248
17         Shaanxi        246       3        236
18          Yunnan        176       2        172
19          Hainan        168       6        161
20       Hong Kong        162       4         88
21         Guizhou        147       2        144
22         Tianjin        136       3        133
23           Gansu        133       2         91
24          Shanxi        133       0        133
25        Liaoning        125       1        120
26           Jilin         93       1         92
27        Xinjiang         76       3         73
28  Inner Mongolia         75       1         73
29         Ningxia         75       0         75
30         Qinghai         18       0         18
31           Macau         12       0         10
32           Tibet          1       0          1

-------------------------------------------------------------------------------------------------------
To Get the latest country wise deaths cases of Novel Coronavirus
C:\Users\sachin\Anaconda3\lib\site-packages\ipykernel_launcher.py:41: FutureWarning: Indexing with multiple keys (implicitly converted to a tuple of keys) will be deprecated, use a list instead.
         Country/Region  Deaths
1               Albania       1
2               Algeria       4
5             Argentina       2
8             Australia       5
9               Austria       3
10           Azerbaijan       1
11              Bahrain       1
15              Belgium      10
20               Brazil       1
22             Bulgaria       2
26               Canada       5
29                China    3230
36          Cruise Ship       7
40              Denmark       4
41   Dominican Republic       1
42              Ecuador       2
43                Egypt       4
49               France     148
53              Germany      24
55               Greece       5
59            Guatemala       1
62               Guyana       1
65              Hungary       1
66              Iceland       1
67                India       3
68            Indonesia       5
69                 Iran     988
70                 Iraq      11
71              Ireland       2
73                Italy    2503
75                Japan      29
80         Korea, South      81
84              Lebanon       3
88           Luxembourg       1
89             Malaysia       2
92           Martinique       1
100             Morocco       2
103         Netherlands      43
107              Norway       3
110              Panama       1
113         Philippines      12
114              Poland       5
115            Portugal       1
125          San Marino       7
132            Slovenia       1
135               Spain     533
137               Sudan       1
139              Sweden       7
140         Switzerland      27
141             Taiwan*       1
143            Thailand       1
149              Turkey       1
150                  US     108
151             Ukraine       2
153      United Kingdom      56

-------------------------------------------------------------------------------------------------------
to get the List  of countries with no cases of Novel Coronavirus recovered
C:\Users\sachin\Anaconda3\lib\site-packages\ipykernel_launcher.py:49: FutureWarning: Indexing with multiple keys (implicitly converted to a tuple of keys) will be deprecated, use a list instead.
                       Country/Region  Confirmed  Deaths  Recovered
1                             Albania         55       1          0
4                 Antigua and Barbuda          1       0          0
7                               Aruba          3       0          0
13                           Barbados          2       0          0
16                              Benin          1       0          0
17                             Bhutan          1       0          0
18                            Bolivia         11       0          0
21                             Brunei         56       0          0
22                           Bulgaria         67       2          0
23                       Burkina Faso         15       0          0
25                           Cameroon         10       0          0
27           Central African Republic          1       0          0
28                              Chile        201       0          0
31                Congo (Brazzaville)          1       0          0
32                   Congo (Kinshasa)          3       0          0
33                         Costa Rica         41       0          0
37                               Cuba          5       0          0
38                             Cyprus         46       0          0
41                 Dominican Republic         21       1          0
42                            Ecuador         58       2          0
44                  Equatorial Guinea          1       0          0
46                           Eswatini          1       0          0
47                           Ethiopia          5       0          0
50                      French Guiana         11       0          0
51                              Gabon          1       0          0
54                              Ghana          7       0          0
56                          Greenland          1       0          0
57                         Guadeloupe         18       0          0
58                               Guam          3       0          0
59                          Guatemala          6       1          0
60                           Guernsey          0       0          0
61                             Guinea          1       0          0
62                             Guyana          7       1          0
63                           Holy See          1       0          0
64                           Honduras          8       0          0
66                            Iceland        220       1          0
76                             Jersey          0       0          0
78                         Kazakhstan         33       0          0
79                              Kenya          3       0          0
81                             Kosovo          2       0          0
85                            Liberia          1       0          0
86                      Liechtenstein          7       0          0
88                         Luxembourg        140       1          0
90                           Maldives         13       0          0
92                         Martinique         16       1          0
93                         Mauritania          1       0          0
94                            Mayotte          1       0          0
97                             Monaco          7       0          0
98                           Mongolia          5       0          0
99                         Montenegro          2       0          0
101                           Namibia          2       0          0
104                       New Zealand         12       0          0
105                           Nigeria          3       0          0
110                            Panama         69       1          0
111                          Paraguay          9       0          0
116                       Puerto Rico          0       0          0
118             Republic of the Congo          0       0          0
119                           Reunion          9       0          0
122                            Rwanda          7       0          0
123                       Saint Lucia          2       0          0
124  Saint Vincent and the Grenadines          1       0          0
129                        Seychelles          4       0          0
131                          Slovakia         72       0          0
132                          Slovenia        275       1          0
133                           Somalia          1       0          0
134                      South Africa         62       0          0
137                             Sudan          1       1          0
138                          Suriname          1       0          0
142                          Tanzania          1       0          0
144                       The Bahamas          1       0          0
145                        The Gambia          1       0          0
146                              Togo          1       0          0
147               Trinidad and Tobago          5       0          0
148                           Tunisia         24       0          0
149                            Turkey         47       1          0
151                           Ukraine         14       2          0
154                           Uruguay         29       0          0
155                        Uzbekistan         10       0          0
156                         Venezuela         33       0          0
158    occupied Palestinian territory          0       0          0

List of countries with all cases of Novel Coronavirus died
----------------------------------------------------------------------------------------------------
C:\Users\sachin\Anaconda3\lib\site-packages\ipykernel_launcher.py:57: FutureWarning: Indexing with multiple keys (implicitly converted to a tuple of keys) will be deprecated, use a list instead.
  Country/Region  Confirmed  Deaths
0          Sudan          1       1

------------------------------------------------------------------------------------------------
List of countries with all cases of Novel Coronavirus recovered
C:\Users\sachin\Anaconda3\lib\site-packages\ipykernel_launcher.py:70: FutureWarning: Indexing with multiple keys (implicitly converted to a tuple of keys) will be deprecated, use a list instead.
  Country/Region  Confirmed  Recovered
0          Nepal          1          1

----------------------------------------------------------------------------------------------
 To Get the top 10 countries data of Novel Coronavirus
                        Last Update  Confirmed  Deaths  Recovered
Country/Region                                                   
China           2020-03-18T12:13:09      67800    3122      56927
Italy           2020-03-18T17:33:05      35713    2978       4025
Iran            2020-03-18T12:33:02      17361    1135       5389
Spain           2020-03-18T13:13:13      13910     623       1081
Germany         2020-03-18T19:33:02      12327      28        105
France          2020-03-18T18:33:02       9043     148         12
Korea, South    2020-03-18T02:53:03       8413      84       1540
Switzerland     2020-03-18T14:53:05       3028      28         15
United Kingdom  2020-03-18T14:53:05       2626      71         65
US              2020-03-18T19:53:03       2495      55        106

'''
