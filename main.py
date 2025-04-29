import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit 超入門 メモ')
st.write('DataFrame')

df=pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})
st.write('st.write(df)')
st.write(df)

st.write('st.dataframe(df.style.highlight_max(axis=0),width=300,height=800) #interactive')
st.dataframe(df.style.highlight_max(axis=0),width=300,height=250)

st.write('st.table(df.style.highlight_max(axis=0)) #static')
st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項
```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

#Chart

df1=pd.DataFrame(
    np.random.rand(20,3),
   columns=['a','b','c']
)

st.dataframe(df1)

st.write('st.line_chart(df1)')
st.line_chart(df1)

st.write('st.area_chart(df1)')
st.area_chart(df1)

st.write('scatter_chart(df1)')
st.scatter_chart(df1)

st.write('bar_chart(df1)')
st.bar_chart(df1)

#map

df3=pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
   columns=['lat','lon']
)

df3
#st.dataframe(df3)
st.write('st.map(df3)')
st.map(df3)

#image

from PIL import Image

st.write('Interactive Widgets')
if st.checkbox('Show Image', value=True):

    img=Image.open('myicom2.jpg')
    st.image(img,caption='myicom',use_container_width=True)

option=st.selectbox(
    'Select Num',
    list(range(1,11))
)

if st.checkbox('Show Num'):
    st.write('Num:',option)

text_line=st.text_input('Free Space')
if text_line=="":
    pass
else:
    st.write(text_line)


condition=st.slider('Slider',0,100,50)
st.write(condition)

left_column,mid_column,right_column=st.columns(3)

button1=left_column.button('右カラムに文字を表示')
button2=mid_column.button('表示を消す')
if button1:
    right_column.write('True')
    if button2:
        right_column.write('')
expander_sample=st.expander('Q1')
expander_sample.write('Ans1')

#Progress bar

import time

st.write('Progress bar')
'Start!'

latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'Done!'

