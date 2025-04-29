import pandas as pd
import yfinance as yf
import altair as alt
import streamlit as st
import math

st.title('米国株価可視化アプリ')

st.sidebar.write("""
# GAFA株価
こちらは株価可視化ツールです。以下のオプションから表示日数を指定してください。               
""")

st.sidebar.write("""
## 表示日数選択
""")
days=st.sidebar.slider('日数',1,50,20)

#st.sidebar.write("""
### 株価の範囲指定
#""")
#smin=0.0
#smax=3500.0
#ymin, ymax=st.sidebar.slider(
#    '範囲を指定してください。',
#    smin,smax,(smin,smax)
#)

st.write(f"""
### 過去 **{days}日間**のGAFA株価
""")
@st.cache_data
def get_data(days, tickers):
      df=pd.DataFrame()
      for company in tickers.keys():
          #get value
          tkr = yf.Ticker(tickers[company]) #get ticker

          hist = tkr.history(period=f'{days}d') 


          hist.index = hist.index.strftime('%d %B %Y') #format
          hist=hist[['Close']]
          hist.columns = [company]

          hist = hist.T #pivot
          hist.index.name='Name' #rename

          df = pd.concat([df,hist]) #add to pandas dataframe
      return df
try:


    tickers={
        'apple':'AAPL',
        'meta':'META',
        'microsoft':'MSFT',
        'google':'GOOGL',
        'netflix':'NFLX',
        'amazon':'AMZN',
        'tesla':'TSLA'
    }

    df=get_data(days,tickers)



    companies=st.multiselect(
        '会社名を選択してください',
        list(df.index),
        ['google','amazon','meta','apple']
    )

    if not companies:
        st.error('少なくとも１社は選んでください。')
    else:
        data = df.loc[companies]
        st.write('### 株価 (USD)',data.sort_index())
        data=data.T.reset_index()
        data=pd.melt(data, id_vars=['Date']).rename(
            columns={'value':'Stock Prices(USD)'}
        )
        smax=data['Stock Prices(USD)'].max()
        smax=math.ceil(smax/100) * 100

        smin=data['Stock Prices(USD)'].min()
        smin=math.floor(smin/100) * 100

        st.sidebar.write("""
        ## 株価の範囲指定
        """)
        
        ymin, ymax=st.sidebar.slider(
            '範囲を指定してください。',
            smin,smax,(smin,smax)
        )


        chart=(
            alt.Chart(data)
            .mark_line(opacity=0.8, clip=True) #Trim 
            .encode(
                x="Date:T",
                y=alt.Y("Stock Prices(USD):Q", stack=None, scale=alt.Scale(domain=[ymin,ymax])),
                color="Name:N"
            )
        )
        st.altair_chart(chart, use_container_width=True)
except:
    st.error(
        "おっと！なにか問題が起きているようです。"
    )
