import streamlit as st
import plotly.graph_objects as go

def gauge_chart(value, title):
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = value,
        title = {'text': title},
        gauge = {
            'axis': {'range': [None, 100]},
            'bar': {'color': "blue"},
            'bgcolor': "white",
            'borderwidth': 3,
            'bordercolor': "black",
            'steps': [
                {'range': [0, 40], 'color': 'white'},
                {'range': [40, 60], 'color': 'white'},
                {'range': [60, 100], 'color': 'white'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 3},
                'thickness': 0.75,
                'value': 50
            }
        }
    ))

    return fig

# Streamlit uygulama başlatma
st.title("General Model Control")


# Rastgele bir değer oluşturma
value = 50

# Gauge grafiğini oluşturma ve gösterme
fig = gauge_chart(value, "QUALITY")
st.plotly_chart(fig)