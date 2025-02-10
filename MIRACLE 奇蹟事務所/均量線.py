#https://www.youtube.com/watch?v=VmGMxgCiTRE&ab_channel=MIRACLE%E5%A5%87%E8%B9%9F%E4%BA%8B%E5%8B%99%E6%89%80
#黃金交叉 短期均線向上穿越長期均線 買進
#死亡交叉 短期均線向下穿越長期均線 賣出

import twstock as t 
import pandas as p 
import plotly.graph_objects as g 

#在('')裡面打 股票代碼
stock = t.Stock('3374')
date = stock.date 

#收盤價
price = stock.price 
data_price = p.DataFrame({'日期':date, '收盤價':price})

#成交量
amount = stock.capacity 
data_amount = p.DataFrame({'日期':date, '成交量':amount})

#5MA
five = date[4:]
average = stock.moving_average(amount, 5)
ma5 = p.DataFrame({'日期':five, '5日平均成交量':average})

#10MA
ten = date[9:]
average = stock.moving_average(amount, 10)
ma10 = p.DataFrame({'日期':ten, '10日平均成交量':average})

#20MA
twenty = date[19:]
average = stock.moving_average(amount, 20)
ma20 = p.DataFrame({'日期':twenty, '20日平均成交量':average})

result = g.Figure() 

#收盤價的圖
result.add_trace(
    g.Scatter(
        x=data_price['日期'],
        y=data_price['收盤價'],
        name='收盤價'
    )
)

#成交量的圖
result.add_trace(
    g.Scatter(
        x=data_amount['日期'],
        y=data_amount['成交量'],
        yaxis='y2',
        name='成交量'
    )
)

#5MA的圖
result.add_trace(
    g.Scatter(
        x=ma5['日期'],
        y=ma5['5日平均成交量'],
        yaxis='y3',
        name='5日均量線'
    )
)

#10MA的圖
result.add_trace(
    g.Scatter(
        x=ma10['日期'],
        y=ma10['10日平均成交量'],
        yaxis='y4',
        name='10日均量線'
    )
)

#20MA的圖
result.add_trace(
    g.Scatter(
        x=ma20['日期'],
        y=ma20['20日平均成交量'],
        yaxis='y5',
        name='20日均量線'
    )
)

result.update_layout(
    title_text='1215卜蜂',
    hovermode='x unified', #滑鼠停在上面會有資訊卡
    
    #調x軸座標的間距
    xaxis=dict(
        domain=[0.27, 1]
    ),

    #收盤價 的 y軸座標
    yaxis=dict(
        title='收盤價'
    ),
    
    #成交量 的 y軸座標
    yaxis2=dict(
        title='成交量', 
        anchor='free',
        overlaying='y',
        position=0.1899
    ),
    
    #5MA 的 y軸座標
    yaxis3=dict(
        title='MA均量線', 
        anchor='free',
        overlaying='y',
        position=0.098
    ),
    
    #10MA 的 y軸座標
    yaxis4=dict(
        overlaying='y',
        visible=False   #不顯示這個y軸座標 因為5MA、10MA、20MA單位一樣 所以只要顯示其中一個就好了
    ),
    
    #20MA 的 y軸座標
    yaxis5=dict(
        overlaying='y',
        visible=False  #不顯示這個y軸座標
    )
)
result.show()